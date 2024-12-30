from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
from static.utils import generate_unique_code as gen_room

# NOTE: understand the main process to sockets: initialize sockets, then you can send connection events after establishing this connection

# initialize Flask application
app = Flask(__name__)

# configure Flask application
app.config["SECRET_KEY"] = "djkshf7e3whf" # NOTE: in production environment, this would be encrypted and securely retrieved

# socketio integration (used later for actual socket connectivity)
socketio = SocketIO(app)

# this dictionary will house the chat rooms for the project
rooms = {} 

# create home route for website
@app.route("/", methods=["GET", "POST"])
def home():
    # always start off with a new session
    session.clear()

    # grab form data if POST request
    if request.method == "POST":
         # NOTE: the request object from flask is used to eventually get the value of the "name" property within the form dictionary. This is why having a "name" attribute in html for each unique input/button is necessary, as it identifies exactly where data/events are coming from
         # NOTE: since form is a Python dictionary, using the get method is the safest way to see if data exists without getting errors. Since it normally returns None if the key doesn't exist, we can set the buttons to False by default as they don't return values, but rather we just need to know if the button was clicked or not
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        # validate if user passed in a name
        if not name:
                # we can pass an error argument to the render_template object as it can be used dynamically in html files
                # we also want to pass in values we want to persist re-renders (ie. after a submission or http requests when the page reloads, so users wont loose their conversations). These are the values that are in the "name" attributes that are so important in the html files  
                return render_template("home.html", error="Please enter a name", code=code, name=name)
        
        # validate if room exists and that code is legit
        if join != False and not code:
            return render_template("home.html", error="Please enter a room code", code=code, name=name)
        
        room = code

        # create a new room if user wants to make one
        if create != False:
            room = gen_room(4, rooms)

            rooms[room] = {"members": 0, "messages": []}

        # if user is not making a new room, they must want to join an existing one. if they give incorrect room code then it doesn't exist
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist", code=code, name=name)
        
        # rather then storing info on a database or using authentication, we can store user's info on a server temporarily
        session["room"] = room
        session["name"] = name
            
        # finally, we can redirect the user to the chat room
        return redirect(url_for("room"))

    # if not post request, then just GET
    return render_template("home.html")

# route to individual chat room
@app.route("/room")
def room():
    # users should not be able to go into "/room" unless they have a legit name and room code
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
         return redirect(url_for("home"))

    # NOTE: adding messages allows the room to always populate with message history for the room (so long as there is someone in it). That way if a user refreshes, they don't lose their conversation history.
    return render_template("room.html", code=room, messages=rooms[room]["messages"]) 

# socket connection
@socketio.on("connect")
def connect(auth):
     # look in current session for name and code
     room = session.get("room")
     name = session.get("name")

     # ensure room and name are legit again (better to have extra layer of security)
     if not room or not name:
          return
     
     # if they have a room but for some reason its not a valid one, we can force the user out of it
     if room not in rooms:
          leave_room(room)
          return
     
     # join user to chat room
     join_room(room)

     # send json data to the room (can send to certain users, everyone, etc.)
     content = {
          "name": name, 
          "message": " has entered the chat room"
     }   

     send(content, to=room)
     print(f"{name} entered room {room}")

     # update room user count only after user connects and joins a room
     rooms[room]["members"] += 1
     print(f"{name} joined room {room}")


# socket disconnection
@socketio.on("disconnect")
def disconnect():
     room = session.get("room")
     name = session.get("name")
     leave_room(room)

    # update room count (or remove room is no one is there anymore)
     if room in rooms:
          rooms[room]["members"] -= 1
          if rooms[room]["members"] <= 0:
               del rooms[room]
               print(f"Room {room} has been deleted")


     # we are sending json data with name and message
     content = {
          "name": name, 
          "message": " has left the chat room"
     }   

     send(content, to=room)
     print(f"{name} left room {room}")

# defines how the server can send messages made from users
@socketio.on("message")
def message(data):
     room = session.get("room")
     if room not in rooms:
          return
     
     content = {
          "name": session.get("name"),
          "message": data["data"],
     }

     print(content)

    # all users in the room receive this message
     send(content, to=room)

     # NOTE: this is where the messages would be added to a database or server for permanent storage. 

     rooms[room]["messages"].append(content)

if __name__ == "__main__":
    # this will start the dev server.
    # NOTE: this command should only be used for dev purposes only, not production!
    socketio.run(app, debug=True) # debug attribute supports auto reload when server code changes
