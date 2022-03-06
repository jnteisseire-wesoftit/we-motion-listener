import paramiko
import logging
import os

logger = logging.getLogger('we-motion-listener')


class SftpAction():

    @staticmethod
    def do_action(config, file):
        SftpAction.upload_file(config, file)

    @staticmethod
    def upload_file(config, file):
        # SMTP account credentials
        host = config.config_obj.get('SftpAction', 'host')
        port = config.config_obj.getint('SftpAction', 'port')
        username = config.config_obj.get('SftpAction', 'username')
        remotepath = config.config_obj.get('SftpAction', 'remotepath')
        private_key_file = config.config_obj.get(
            'SftpAction', 'private_key_file')

        transport = paramiko.Transport((host, port))

        try:
            xSx_key = paramiko.RSAKey.from_private_key_file(private_key_file)
        except paramiko.SSHException:
            xSx_key = paramiko.DSSKey.from_private_key_file(private_key_file)

        transport.connect(username=username, pkey=xSx_key)

        # Connect
        sftp = paramiko.SFTPClient.from_transport(transport)
        logger.debug("uplaod file %s to %s%s", file,
                     remotepath, os.path.basename(file))
        sftp.put(file, remotepath + os.path.basename(file))
        sftp.close()

        transport.close()
