# pfind

# --------------------------------
# Version: 1.3.0
# OS: Rocky Linux 8.7
# Last Modify: 2023.07.26.
# Made by: minninn, guaca123
# https://github.com/minninn/pfind
# --------------------------------

# 업데이트 내용
#
# 검색 대상 디렉토리 설정


# How to use
#
# git clone https://github.com/minninn/pfind.git
# cd pfind
# sh pfind.sh
# pfind -v (or --version)
> Version: 1.3.0
# pfind -h (or --help)
> pfind help

Find all files in working directory.

usage: pfind [options] [content]

options
    -v, --version: show version
    -h, --help: show this message
    -x, --exclude: Exclude Directories in search
                   pfind -x "directory"
    -c, --content: find files that include this content
                   pfind -c "content"
    -t, --target: Enter the path to search
                   pfind -t "directory"
