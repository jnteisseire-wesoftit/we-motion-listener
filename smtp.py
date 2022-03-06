import smtplib
import logging
from datetime import datetime

logger = logging.getLogger('we-motion-listener')


class SmtpAction():

    @staticmethod
    def do_action(config):
        SmtpAction.send_email(config)

    @staticmethod
    def send_email(config, msg=''):
        # SMTP account credentials
        username = config.config_obj.get('SmtpAction', 'user')
        password = config.config_obj.get('SmtpAction', 'password')
        from_name = config.config_obj.get('SmtpAction', 'name')

        # Recipient email address (could be same as from_addr)
        recipient = config.config_obj.get('SmtpAction', 'recipient')

        # Subject line for email
        subject = config.config_obj.get('SmtpAction', 'subject')

        senddate = datetime.strftime(datetime.now(), '%Y-%m-%d')
        m = "Date: %s\r\nFrom: %s <%s>\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (
            senddate, from_name, username, recipient, subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(username, recipient, m + msg)
        server.quit()
