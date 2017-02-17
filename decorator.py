def meet(self):
    def wrapped():
        return self() + " friend!"
    return wrapped
@meet
def hello():
    return "Hello"
print (hello())