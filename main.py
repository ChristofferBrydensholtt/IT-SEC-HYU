from PIL import ImageGrab
from datetime import datetime

def screenshot():

    now = datetime.now()

    dt_string = now.strftime("%H.%M.%S")
    snapshot = ImageGrab.grab()
    save_path = "C:\\Users\\Christoffer\\Documents\\SecretScreenshots\\ss" +  dt_string + ".png"
    snapshot.save(save_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screenshot()
