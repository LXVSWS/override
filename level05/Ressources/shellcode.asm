section .text
	global _start

_start:
	xor eax, eax	; set eax register to 0
	xor ebx, ebx	; set ebx register to 0
	mov al, 11		; moves 11 into al register (execve syscall number)
	mov [esp], ebx	; moves the value of ebx into the memory location that esp is currently pointing to (on top of the stack)
	push "n/sh"		; push the second part of the string (execve first argument)
	push "//bi"		; push the first part of the string (execve first argument)
	mov ebx, esp	; push the fully string null terminated to ebx
	int 0x80		; interrupt to execute execve syscall
