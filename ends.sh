#!/usr/bin/bash
aaa=$1
cat /tmp/mysys.o /tmp/$aaa.com > /tmp/$aaa.bin
dd if=/tmp/$aaa.bin of=./tmp/$aaa.iso bs=1k seek=58 conv=notrunc
rm /tmp/$aaa.o
rm /tmp/$aaa.com
rm /tmp/$aaa.bin