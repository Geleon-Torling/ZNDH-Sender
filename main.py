import smtplib
#import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    smtp_server = "localhost"
    port = 1025
    sender_email = "test@test.com"
    reciver_email = "test@otherhost.com"
    password = ""

#    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = reciver_email
    message.set_charset("utf-8")

    text = """\
    Hello!"""

    html = """\
    <html>
        <body>
            <p>Hello!</p>
        </body>
    </html>
    """

    part1 = MIMEText(text,"plain")
    part1.set_charset("utf-8")
    part2 = MIMEText(html,"html")
    part2.set_charset("utf-8")

    message.attach(part1)
    message.attach(part2)

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
#        server.starttls(context=context)
#        server.ehlo()
#        server.login(sender_email,password)
        server.sendmail(sender_email, reciver_email, message.as_string())
        server.quit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

