from .tasks import reverser


result = reverser.delay("this is a test string")
print(result.result)
