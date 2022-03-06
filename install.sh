#!/usr/bin/env bash

# Installs motion-notify and all required dependencies.

# Install git and clone we-motion-listener into the destination directory
# apt-get install git pip

rm -rf /etc/we-motion-listener

mkdir -p /etc/we-motion-listener
cp -r ../we-motion-listener /etc/
chown -R motion.motion /etc/we-motion-listener

# pip install python_sftp_client

# Create a new ssh key
mkdir -p /etc/we-motion-listener/.ssh
ssh-keygen -f /etc/we-motion-listener/.ssh/id_rsa -q -P ""

# Change the File permissions
chown motion.motion /etc/we-motion-listener/we-motion-listener.py
chown motion.motion /etc/we-motion-listener/we-motion-listener.cfg
chmod 744 /etc/we-motion-listener/we-motion-listener.py
chmod 600 /etc/we-motion-listener/we-motion-listener.cfg