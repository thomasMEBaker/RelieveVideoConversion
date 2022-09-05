# RelieveVideoConversion

Go to your program’s directory and run:

pyinstaller yourprogram.py
This will generate the bundle in a subdirectory called dist.

pyinstaller -F yourprogram.py
Adding -F (or --onefile) parameter will pack everything into single "exe".

pyinstaller -F --paths=<your_path>\Lib\site-packages  yourprogram.py
running into "ImportError" you might consider side-packages.

 pip install pynput==1.6.8

important 

pyuic5 -x testGUI.ui -o test.py to generate from QT to py file
