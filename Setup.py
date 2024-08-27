try:
    import sys
    import os

    print("Installando i moduli per il tool:")

    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python RedTiger.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")
        os.system("python3 RedTiger.py")

except Exception as e:
    print(e)
    os.system("pause")