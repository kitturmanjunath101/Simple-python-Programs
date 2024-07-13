import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if (0<=timestamp<5):
    print("mid night")
elif(5<=timestamp<12):
    print("good morning")
elif(12<=timestamp<17):
    print("good afternoon")
elif(17<=timestamp<21):
    print("good evening ")
else:
    print("good night")