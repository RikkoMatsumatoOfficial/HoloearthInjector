@echo off

title HoloearthInjector Compiler
pyinstaller Main.py --console --onefile --collect-all "PyBass"
