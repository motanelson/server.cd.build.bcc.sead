[BITS 16]
[ORG 0x7C00]          ; Endereço de carregamento do bootloader

start:
    ; Configura os segmentos
    mov ax, 0x7d0     ; Base do setor de boot (0x7C00 / 16)
    mov ds, ax        ; Configurar DS
    mov es, ax        ; Configurar ES
    mov ss, ax        ; Configurar SS
    mov sp, 0xffff    ; Pilha no fim do setor de boot
    ; Saltar para o início do programa .com
    jmp 0x7d0:0x0100  ; O programa .com espera começar em 0x0100

times 510-($-$$) db 0 ; Preencher até 510 bytes
dw 0xAA55             ; Assinatura do setor de boot
coms: