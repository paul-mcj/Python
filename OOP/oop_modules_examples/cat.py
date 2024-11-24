from pet import Pet

class Cat(Pet):
    def __init__(self:object, animal:str, name:str, age:int, yarn:bool=False) -> None:
        super().__init__(animal, name, age)

        self.yarn = yarn

    def likes_yarn(self:object) -> None:
        answer = "does not"
        if self.yarn:
            answer = "does"
        print(f"{self.name} {answer} like yarn")