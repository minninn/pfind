#!/bin/sh

# -------------------------
# Version: 1.1.3
# Last Modify: 2023.04.10.
# Made By: minninn
# -------------------------

python3 -m pip install tqdm

USER_SHELL=`echo $SHELL | cut -c 6-`
DIR_PATH=`pwd`
echo $USER_SHELL

if [ "$USER_SHELL" == "zsh" ];then
    echo `mkdir ~/.zprofile`
    echo `echo alias pfind="'python3 $DIR_PATH/pfind.py'" > ~/.zprofile`
    . ~/.zprofile
fi

if [ "$USER_SHELL" == "bash" ]; then
    echo `echo alias pfind="'python3 $DIR_PATH/pfind.py'" > ~/.bashrc`
    . ~/.bashrc
fi


PYTHON_PATH=`which python3`
sed -i "s|python_path|$PYTHON_PATH|" $DIR_PATH/pfind.py
