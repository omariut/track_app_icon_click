import psutil,getpass
import time
user_name = getpass.getuser()
import subprocess
import sys
import mail

old_record ={}
while True:


    try:
        listed = sys.argv[1]
    except IndexError:
        listed = []

    get = lambda cmd: subprocess.check_output(cmd).decode("utf-8").strip()

    def check_wtype(w_id):
        # check the type of window; only list "NORMAL" windows
        return "_NET_WM_WINDOW_TYPE_NORMAL" in get(["xprop", "-id", w_id])

    def get_process(w_id):
        # get the name of the process, owning the window
        proc = get(["ps", "-p", w_id, "-o", "comm="])
        proc = "gnome-terminal" if "gnome-terminal" in proc else proc
        return proc
   
    wlist = [l.split() for l in subprocess.check_output(["wmctrl", "-lp"])\
            .decode("utf-8").splitlines()]
    try:
        validprocs = set([get_process(w[2]) for w in wlist if check_wtype(w[0]) == True])
    except:
        pass
    record={}

    for item in psutil.process_iter():
        name = item.name()
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item.create_time()))
        if name in validprocs :
            record[name]= start_time



    for key,value in record.items():
        if value != old_record.get(key):
            with open("record.txt","a", encoding = 'utf-8') as f:
                #time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))
                f.write(f"{key} ===> {value}\n")
                
    old_record = record
    try:
        mail.send_mail()
    except:
        pass
    time.sleep(2)
