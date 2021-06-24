from userApp import userApp
import random, string

@userApp.context_processor
def example():
    return dict(randomString=randomString)

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
