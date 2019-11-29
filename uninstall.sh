#!/usr/bin/env bash

# delete the envman "executable"
rm /usr/local/bin/envman

# prompt for removal of all saveds envs
read -p "Would you like to delete all saved .env files? [y/N]" DELETE_ENVS

if [ $DELETE_ENVS = "y" -o $DELETE_ENVS = "Y" ]
then
  rm -r ~/envs
fi