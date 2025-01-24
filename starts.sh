#!/usr/bin/bash
aaa=$1
nasm mysys.s -o /tmp/mysys.o
bcc -c -Md libdos.c -o libdos.a
bcc -c -Md libdos.c -o /tmp/libdos.a
cp app.data ./tmp/$aaa.iso