#!/usr/bin/env bash

# Installs motion-notify and all required dependencies.

# Install git and clone we-motion-listener into the destination directory
apt-get install git
git clone https://github.com/jnteisseire-wesoftit/we-motion-listener
chown -R motion.motion /etc/we-motion-listener
chmod +x /etc/we-motion-listener/we-motion-listener.py


# Create the log files and lock files and set ownership and permissions
touch /var/log/we=motion-listener/we-motion-listener.log
chown motion.motion /var/log/we-motion-listener/we-motion-listener.log
chmod 664 /var/log/we-motion-listener/we-motion-listener.log
