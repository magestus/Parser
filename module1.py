import urllib.request
from bs4 import BeautifulSoup
import premailer
import logging

<<<<<<< HEAD




def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


=======
 
 
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()
 
 
>>>>>>> origin/master
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    head = soup.find('head')
    table = soup.find('div', {"class": "Search-list"})
<<<<<<< HEAD

=======
 
>>>>>>> origin/master
    result_html = premailer.Premailer('<html>' + str(head) + '<body>' + str(table) + '</body></html>',
                                      cssutils_logging_level=logging.CRITICAL).transform()
    with open('result.html', 'w') as f_obj_out:
        f_obj_out.write(result_html)

<<<<<<< HEAD
    #print(result_html)

    send_mail()


=======
    #print(table)
 
    send_mail()
 
 
>>>>>>> origin/master
def send_mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
<<<<<<< HEAD

    fromaddr = "beatsoup4test@gmail.com"
    toaddr = "beatsoup4test@gmail.com"
    mypass = "Potestim1111"

=======
 
    fromaddr = "beatsoup4test@gmail.com"
    toaddr = "beatsoup4test@gmail.com"
    mypass = "Potestim1111"
 
>>>>>>> origin/master
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "your_desired_subject"
<<<<<<< HEAD

    with open('result.html') as f_obj:
        body = f_obj.read()

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 25)
=======
 
    with open('result.html') as f_obj:
        body = f_obj.read()
 
    msg.attach(MIMEText(body, 'html'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
>>>>>>> origin/master
    server.ehlo()
    server.starttls()
    server.login("beatsoup4test@gmail.com", "Potestim1111")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
<<<<<<< HEAD

def main():
    search_text = input('Vvedite zapros: ')
    parse(get_html(
        'https://www.fabrikant.ru/trades/procedure/search/?type=1&query={}&procedure_stage=1&price_from=&price_to=&currency=0&date_type=date_publication&date_from=&date_to=&ensure=all&section_type%5B%5D=ds300&count_on_page=10&order_by=default&order_direction=1'.format(
            search_text)))

=======
 
 
def main():
    search_text = input('Vvedite zapros: ')
    parse(get_html('https://www.fabrikant.ru/trades/procedure/search/?type=1&query={}&procedure_stage=1&price_from=&price_to=&currency=0&date_type=date_publication&date_from=&date_to=&ensure=all&section_type%5B%5D=ds300&count_on_page=10&order_by=default&order_direction=1'.format(search_text)))
 
>>>>>>> origin/master

if __name__ == "__main__":
    main()