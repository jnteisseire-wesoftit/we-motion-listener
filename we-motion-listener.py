#!/usr/bin/python3
import sys
import logging
import logging.handlers
import argparse


from config import Config
from smtp import SmtpAction
from sftp import SftpAction

logger = logging.getLogger('we-motion-listener')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(logging.DEBUG)
#handler = logging.StreamHandler(sys.stdout)
handler = logging.handlers.RotatingFileHandler('/var/log/we-motion-listener/we-motion-listener.log',
                                               maxBytes=1048576,
                                               backupCount=3)

handler.setFormatter(logging.Formatter(
    '[WEMOTIONLISTENER] [%(asctime)s] [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def handle_event(config_file, event, movie_file):
    logger.debug(event)

    # Load config file
    config = Config(config_file)

    #SmtpAction.send_email(config, 'Motion detected')
    SftpAction.upload_file(config, movie_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='we-motion-listener')

    parser.add_argument('-e', '--event', help='type of motion event', choices=[
                        'on_event_start', 'on_picture_save', 'on_movie_end'], default='on_movie_end')
    parser.add_argument(
        '-f', '--filename', help='full path of the file name')

    parser.add_argument('-c', '--config', help='config file',
                        default='we-motion-listener.cfg')

    args = parser.parse_args()

    handle_event(args.config, args.event, args.filename)
