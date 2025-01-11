printf "\033c\033[43;30m"
ls *.c
printf "give me a .c file bcc? "
read aaa
cp app.data cd1.iso
nasm mysys.s -o /tmp/mysys.o
bcc -c -Md libdos.c -o libdos.a
bcc -c -Md libdos.c -o /tmp/libdos.a
bcc -x -i -L -Md $aaa -o /tmp/mysys.com
cat /tmp/mysys.o /tmp/mysys.com > /tmp/sys.bin
dd if=/tmp/sys.bin of=cd1.iso bs=1k seek=58 conv=notrunc
qemu-system-x86_64 -cdrom cd1.iso