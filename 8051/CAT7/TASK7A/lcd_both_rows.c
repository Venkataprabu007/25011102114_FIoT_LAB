#include <reg51.h>
sfr ldata=0x90;
sbit rs=P1^3;
sbit en=P1^2;
void delay() { int i,j; for(i=0;i<100;i++) for(j=0;j<127;j++); }
void write_byte(unsigned char v, bit dat) {
    rs=dat; ldata=(ldata&0x0F)|(v&0xF0); en=1; delay(); en=0;
    ldata=(ldata&0x0F)|((v<<4)&0xF0); en=1; delay(); en=0; delay();
}
void main() {
    write_byte(0x20,0); write_byte(0x28,0); write_byte(0x0C,0); write_byte(0x01,0);
    write_byte(0x80,0); write_byte('I',1); write_byte('o',1); write_byte('T',1);
    write_byte(0xC0,0); write_byte('L',1); write_byte('C',1); write_byte('D',1);
    while(1);
}
