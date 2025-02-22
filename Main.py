import PyBass.bass as b
import HoloInj as holoearth_injector
import ctypes as ct
currentdevice = int(-1)
def Main():
    if(b.BASS_INIT(device=currentdevice, freq=48000, flags=0, win=0, dsguid=0)):
        b.BASS_START()
        boom = b.BASS_StreamCreateFile(mem=0, filename=bytes("BABEJUMADIBA.mp3", "utf-8"), offset=0, length=0, flags=0x4)
        b.BASS_ChannelPlay(boom, False)
    else:
        print("Bass Is Not Started Successfully")
    kernel32 = ct.cdll.LoadLibrary("Kernel32.dll")
    kernel32.SetConsoleTitleW("HoloEarthInjector by RikkoMatsumatoOfficial")
    pathf = input("Write Path to You're DLL File for Game Holoearth: ")
    holoearth_injector.Inject(path_file=pathf)

if __name__ == "__main__":
    Main()
