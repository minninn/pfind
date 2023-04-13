# pfind

# --------------------------------
# Version: 1.2.0
# OS: Rocky Linux 8.7
# Last Modify: 2023.04.13.
# Made by: minninn, guaca123
# https://github.com/minninn/pfind
# --------------------------------

# 업데이트 내용
#
# 검색에서 제외할 디렉토리 지정 옵션(exclude) 추가


# How to use
#
# git clone https://github.com/minninn/pfind.git
# cd pfind
# sh pfind.sh
# pfind -v (or --version)
> Version: 1.2.0
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
