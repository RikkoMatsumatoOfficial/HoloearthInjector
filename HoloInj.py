import pymem as p
import pymem.process as xz
from os import _exit as exitfunction
def Get_HoloearthProcess():
    try:
        return p.Pymem("Holoearth.exe")
    except:
        print("Not Founded Holoearth Process!!!")
        exitfunction(3312)
        

def Get_ProcessHandle():
    return Get_HoloearthProcess().process_handle

def Inject(path_file : str):
    convertbytes = bytes(path_file, "utf-8")
    xz.inject_dll(Get_ProcessHandle(), convertbytes)
