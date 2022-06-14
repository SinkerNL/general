#!/bin/bash

read -p 'email-address: ' EMAILADDR

echo 'Creating sshkey for: ' $EMAILADDR

ssh-keygen -t ed25519 -C "${EMAILADDR}"

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519 > /dev/null 2>&1
echo "Clearing output for clear copy pasting!"
sleep 2
clear

cat ~/.ssh/id_ed25519.pub

