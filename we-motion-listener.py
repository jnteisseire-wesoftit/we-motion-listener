#!/usr/bin/python3
import sys
import logging
import logging.handlers
import argparse

from config import Config
from smtp import SmtpAction
from sftp import SftpAction


def handle_event(args):

    # Load config file
    config = Config(args.config)

    # setup logger
    logger = logging.getLogger('we-motion-listener')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(logging.Formatter(
        '[WEMOTIONLISTENER] [%(asctime)s] [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    try:
        SftpAction.upload_file(config, args.filename)
        SmtpAction.send_email(
            config, 'Motion detected ')
    except Exception as e:
        SmtpAction.send_email(
            config, 'Motion detected ' + e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='we-motion-listener')

    parser.add_argument('-f', '--filename',
                        help='full path of the file name')

    parser.add_argument('-c', '--config', help='config file',
                        default='/etc/we-motion-listener/we-motion-listener.cfg')

    parser.add_argument('-v', '--event', help='event number')

    args = parser.parse_args()

    handle_event(args)
