import os

for i in range(1000):
    cmd = input("[root@python test]$")
    if cmd:
        if cmd == "exit":
            print("logout")
            break
        else:
            # print("run %s" % cmd, )
            os.system(cmd)
    else:
        continue


