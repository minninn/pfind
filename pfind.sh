#!/bin/zsh

USER_SHELL=`echo $SHELL | cut -c 6-`
DIR_PATH=`pwd`
echo $USER_SHELL

if [ "$USER_SHELL" == "zsh" ];then
    echo `mkdir ~/.zprofile`
    echo `echo alias pfind='python3 $DIR_PATH/pfind.py' > .zprofile`
fi

