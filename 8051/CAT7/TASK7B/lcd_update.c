#include <reg51.h>
sfr ldata=0x90;
sbit rs=P1^3; sbit en=P1^2;
void delay() { int i,j; for(i=0;i<100;i++) for(j=0;j<127;j++); }
void send(unsigned char v, bit dat) { rs=dat; ldata=(ldata&0x0F)|(v&0xF0); en=1; delay(); en=0; ldata=(ldata&0x0F)|((v<<4)&0xF0); en=1; delay(); en=0; delay(); }
void cmd(unsigned char v) { send(v,0); }
void put(unsigned char v) { send(v,1); }
void main() { unsigned int n=0; cmd(0x28); cmd(0x0C); cmd(0x01); while(1) { cmd(0x80); put('V'); put('a'); put('l'); put('u'); put('e'); put(':'); put('0'+(n/100)%10); put('0'+(n/10)%10); put('0'+n%10); n++; if(n>999)n=0; delay(); } }
