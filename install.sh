#!/usr/bin/env bash

# Installs motion-notify and all required dependencies.

# Install git and clone we-motion-listener into the destination directory
apt-get install git pip

rm -rf /etc/we-motion-listener
mkdir -p /etc/we-motion-listener
cp -r ../we-motion-listener /etc/
chown -R motion.motion /etc/we-motion-listener
chmod +x /etc/we-motion-listener/we-motion-listener.py

pip install python_sftp_client

# Create a new ssh key
mkdir -p /etc/we-motion-listener/.shh
ssh-keygen -f /etc/we-motion-listener/.ssh/id_rsa -q -P ""

# Create the log files and set ownership and permissions
mkdir -p /var/log/we-motion-listener/
touch /var/log/we-motion-listener/we-motion-listener.log
chown -R motion.motion /var/log/we-motion-listener/
chmod 664 /var/log/we-motion-listener/we-motion-listener.log

# Change the File permissions
chown motion.motion /etc/we-motion-listener/we-motion-listener.py
chown motion.motion /etc/we-motion-listener/we-motion-listener.cfg
chmod 744 /etc/we-motion-listener/we-motion-listener.py
chmod 600 /etc/we-motion-listener/we-motion-listener.cfg