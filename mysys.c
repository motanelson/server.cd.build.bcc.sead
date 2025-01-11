
//bcc -x -i -L -Md mysys.c -o mysys.com
#define varn 0xc080




void sputs(cc);
void scopy(s1,s2);
void scat(s1,s2);
void slower(s1);
int main()
{
        
	
	
	
	
	
	cls3(0x6020);
	sputs("hello world");
	
	for(;;);
	return 0;
}



void sputs(cc)
char *cc;
{
		int i=0;
while(cc[i]!=0){
		sputc(cc[i]);
		i++;
}
}
void scopy(s1,s2)
char *s1;
char *s2;
{
	char cc=0;
	int counter=0;
	do{
		s1[counter]=s2[counter];
		cc=s2[counter];
		counter++;
	}while(cc!=0);
	
}
void scat(s1,s2)
char *s1;
char *s2;
{
	char *s3;
	char cc=0;
	int counter=0;
	do{
		cc=s1[counter];
		counter++;
	}while(cc!=0);
	s3=s1+counter-1;
	scopy(s3,s2);
}

void slower(s1)
char *s1;
{
	char *s3;
	char cc=0;
	int counter=0;
	do{
		cc=s1[counter];
		if (cc>='A' && cc<='Z')s1[counter]=cc+32;
		counter++;
	}while(cc!=0);
}

#asm
.globl _cls3
.globl _sputc
.globl _printsss
_cls3:
    mov si,sp
    add si,*0x2
    mov dx,[si]
    mov ax,*0xb800
    push ds
    mov ds,ax
    
    mov ax,dx
    mov cx,*0x8a0
    mov si,*0x0
    
cls31:
    
    mov [si],ax    
    inc si
    inc si
    dec cx
    cmp cx,*0x0
    jnz cls31
    pop ds
    ret
_sputc:
    mov si,sp
    add si,*0x2
    mov al,[si]
    mov ah,*0x0E
    mov bh,*0x00
    mov bl,*0x07
    int *0x10
    ret
_printsss:
    mov al,*0x1
    mov ah,*0x13
    mov bh,*0x00
    mov bl,*0x07
    mov dh,*0x0
    mov bl,*0x0
    mov bp,*0x100
    mov cx,*2000
    int *0x10
    ret

#endasm

