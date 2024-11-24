# When it comes to logging in Python, there are a lot of things to keep and mind and some things to set up, but if implemented correctly in the right project can help a lot in deciphering errors.
# NOTE: there are a few different approaches to logging. all of them provide the same core functionality, but mostly differ in format, reusability, complexity and flexibility:
'''
- programmatic configuration: which is what this file is doing. This defines everything in code (formatters, handlers, etc) which makes it very flexible, but can be a bit of a pain to set up. it should be used in smaller scripts or when logs are likely be remain static and simple. its possible and also a good idea to have some separate modules however (a sample example is the "logging_helper.py" file in this folder).
- dictionary configuration: a separate module specifically to provide a dictionary structure of how logging should be implemented. useful for larger projects where structure will improve clarity and modularity.   
- file configuration: define logging settings in a ".conf" file within the project folder. This is ideal when you need to manager configs in an external, human-readable format. its also useful in projects where logging needs to be adjusted separately from code (like in production)
''' 

# NOTE: this file and folder focus on programmatic config, so we first need to import the logging module
import logging

''' 
Understand that there are 5 main levels of logging:
- DEBUG (lvl 10)
- INFO (lvl 20)
- WARNING (lvl 30)
- ERROR (lvl 40)
- CRITICAL (lvl 50)
'''

# Only levels over 30 are shown by default, so often you want to customize a basicConfig if you want to show errors of any level.

# The documentation for logging comes from: https://docs.python.org/3/library/logging.html#logging.NOTSET

# There are all kinds of attributes you can use to customize the format of a basicConfig including: pathname, function name, modules,  etc.

# but, lets build off of some common attributes for a custom DEBUG log:
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s", datefmt="%m/%d/%y %H:%M:%S")

# passing in level=logging.DEBUG to the basicConfig means any logging level >= DEBUG (or 10) will have this format. If you were to put in INFO instead for example, then logging level 20+ would take the format, but anything less (such as DEBUG logs) would be ignored...

def main():
    # show some customized logging messages
    logging.debug("This is a debug message via basicConfig")
    logging.error("This is an error message via basicConfig")

    # using module logging_helper to create a logger
    from logging_helper import logging_helper_logger

    # create log handlers (which can dispatch log messages to specific destinations such as local files, send via http, etc.)
    main_log_handler = logging.getLogger(__name__) # this declares the prominent logger that will be used in this file
    stream_handler = logging.StreamHandler() # streams are essentially output in the console
    file_handler = logging.FileHandler("file.log") # declare what happens with files

    # set level for our log handlers (we'll do 2 for examples of different levels)
    stream_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.ERROR)

    # set format for our log handlers
    log_handler_formatter = logging.Formatter("%(filename)s - %(levelname)s - %(message)s")

    # now set formatter to handlers
    stream_handler.setFormatter(log_handler_formatter)
    file_handler.setFormatter(log_handler_formatter)

    # and add handlers to the main logger, which will ultimately be called
    main_log_handler.addHandler(stream_handler)
    main_log_handler.addHandler(file_handler)

    # call handler
    main_log_handler.warning("This is a warning message")
    main_log_handler.error("This is an error message")

    # NOTE: if you look in file.log, you'll only see ERROR logs because thats what the handler specified for FileHandler!

    # NOTE: logging can also use the stack trace
    import traceback

    try:
        a = [1,2,3]
        val = a[4]
    except:
        logging.error("The error is %s", traceback.format_exc())

    # NOTE: it is also possible that if you anticipate a lot of logs will occur and need to be outputted to a file, you can automatically set a limit (ex. 2kB), give a template file name, and then if that limit is hit, a new file will be created automatically with new logs being added there. Its also possible to put a timing function on when to create a new log file (so one for every new sec, min, day. etc.) and how many backup files can be allowed at once.
    # if a project ends up needing such an intense logging system, it might be a good idea to use a json logger to represent data for universal API integrations (there exist 3rd party tools on github for this specifically).
     


    

if __name__ == "__main__":
    main()