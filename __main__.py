import time

import auth
import mail
import shop
import utils


def send_email(subject, text):
    print("sending email")

    credentials = auth.get_credentials()
    gmail_service = auth.get_gmail_service(credentials)

    message = mail.create_message("hoffmannnick97@gmail.com", subject, text)
    mail.send_message(gmail_service, message)


print("started switchbot")

log_file = open(utils.get_file("bot.log"), "a")
# utils.init_log_file(log_file)

print(utils.get_time())

urls = ["https://www.saturn.de/de/product/_nintendo-switch-grau-neue-edition-2584584.html",
        "https://www.saturn.de/de/product/_nintendo-switch-neon-rot-neon-blau-neue-edition-2584585.html",
        "https://www.mediamarkt.de/de/product/_switch-grau-neue-edition-nintendo-switch-konsolen-2584584.html",
        "https://www.mediamarkt.de/de/product/_switch-neon-rot-neon-blau-neue-edition-nintendo-switch-konsolen-2584585.html", ]
# "https://www.saturn.de/de/product/_nintendo-switch-lite-t%C3%BCrkis-2576513.html"
# "https://www.mediamarkt.de/de/product/_switch-lite-t%C3%BCrkis-nintendo-switch-konsolen-2576513.html"

for url in urls:
    print("=====================")
    result = shop.check_availability(url)
    if result:
        send_email("SWITCH AVAILABLE", result)
    time.sleep(3)

print("done")
