import javaobj
import pprint
import os
import json
import time
import datetime

WZHOOH = """ ∧＿∧
( ･ω･｡)つ━☆・*。
⊂　 ノ 　　　・゜+.
しーＪ　　　°。+ *´¨)
　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)
　　　　　　　　　　(¸.·´ (¸.·'* ☆ вжух!"""

OUT_DIR = "parsed"

F_IN = "/home/user/.advLdap (copy)/connections.dat"
F_OUT = "/home/user/.advLdap/connections.dat"

DATA = [
    "/home/user/.advLdap/0.dat",
    "/home/user/.advLdap/1.dat",
    "/home/user/.advLdap/2.dat",
    F_OUT,
]

def debug():
    os.makedirs(OUT_DIR, exist_ok=True)

    for file in DATA:
        with open(file, "rb") as f:
            print()
            print(file)
            pobj = javaobj.load(f)
            pprint.pprint(vars(pobj))
            with open(os.path.join(OUT_DIR, file.replace("/", "_")), "w") as f:
                f.write(pprint.pformat(vars(pobj)))

    print()

def hack_the_fucking_bank(file_in, file_out):
    print("Parsing fucking capitalists database...", file_in)

    with open(file_in, "rb") as f:
        properties = javaobj.load(f)

    dt_installed = datetime.datetime.utcfromtimestamp(properties.installedTimeStamp / 1000)
    days_ago = (datetime.datetime.now() - dt_installed).days

    print("You have installed this program on {}".format(dt_installed))
    print("It's {} days ago.".format(days_ago))

    if days_ago >= 14:
        print("Oh, no! The trial period is over! Shit!")
    else:
        print("The trial period is not over.")

    print("Let's do some magic!")

    print()
    print("installedTimeStamp:", properties.installedTimeStamp)
    print("trialVersionExpired:", properties.trialVersionExpired)

    print()
    print(WZHOOH)
    print()

    properties.installedTimeStamp = (int(time.time())) * 1000
    properties.trialVersionExpired = False
    print("installedTimeStamp:", properties.installedTimeStamp)
    print("trialVersionExpired:", properties.trialVersionExpired)
    print()

    print("O_o WOW! Some magic happened and program has been hacked :D")

    with open(file_out, "wb") as f:
        f.write(javaobj.dumps(properties))

    print("Database saved to", file_out)

    print()
    print("FUCK LICENSES @ DO ANYTHING WHAT YOU WANT (c) 2022")

if __name__ == '__main__':
    # debug()
    hack_the_fucking_bank(F_OUT, F_OUT)
