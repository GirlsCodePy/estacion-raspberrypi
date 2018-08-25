from time import strftime, localtime, sleep

while True:
    print(strftime(" %S", localtime()))
    sleep(3)
