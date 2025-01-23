#!/usr/bin/bash
aaa=$1
cp app.data ./tmp/$aaa.iso
bcc -x -i -L -Md ./uploads/$aaa.c -o /tmp/$aaa.com 
cat /tmp/mysys.o /tmp/$aaa.com > /tmp/$aaa.bin
dd if=/tmp/$aaa.bin of=./tmp/$aaa.iso bs=1k seek=58 conv=notrunc
rm /tmp/$aaa.o
rm /tmp/$aaa.com
rm /tmp/$aaa.bin
