#!/usr/bin/env python3

import os
import time


def reboot():
    screen = "mcnileflow"
    path = "/home/mcroot/test/SteamPunk_LPS_v23.5_serverpack"

    extinction = f"screen -S {screen} -p 0 -X stuff '/stop\015'"
    chgpath = f"screen -S {screen} -p 0 -X stuff 'cd {path}\015'"
    demarrage = f"screen -S {screen} -p 0 -X stuff './start.sh\015'"

    annonce = f"screen -S {screen} -p 0 -X stuff '/say [ScheduledTask] Redémarrage du serveur dans 1 minute...\015'"

    os.system(annonce)

    time.sleep(30)
    annonce_30sec = f"screen -S {screen} -p 0 -X stuff '/say [ScheduledTask] Redémarrage du serveur dans 30 secondes...\015'"
    os.system(annonce_30sec)

    time.sleep(15)
    annonce_15sec = f"screen -S {screen} -p 0 -X stuff '/say [ScheduledTask] Redémarrage dans:\015'"
    os.system(annonce_15sec)

    for i in range(10, 0, -1):
        countdown = f"screen -S {screen} -p 0 -X stuff '/say [ScheduledTask] {i}...\015'"
        os.system(countdown)
        time.sleep(1)

    os.system(extinction)
    time.sleep(10)
    enter_key = f"screen -S {screen} -p 0 -X stuff $'\\012'"
    os.system(enter_key)

    os.system(chgpath)
    os.system(demarrage)


if __name__ == '__main__':
    reboot()
