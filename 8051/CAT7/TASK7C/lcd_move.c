#include <reg51.h>
sfr ldata=0x90; sbit rs=P1^3; sbit en=P1^2;
sbit key_up=P2^4;
sbit key_down=P2^5;
sbit key_left=P2^6;
sbit key_right=P2^7;
void delay() { int i,j; for(i=0;i<100;i++) for(j=0;j<127;j++); }
void lcd(unsigned char v, bit d) { rs=d; ldata=(ldata&15)|(v&0xF0); en=1; delay(); en=0; ldata=(ldata&15)|((v<<4)&0xF0); en=1; delay(); en=0; }
void main() { unsigned char row=0,col=0; P2=0xF0; lcd(0x28,0); lcd(0x0C,0); lcd(0x01,0); while(1) { if(key_up==0) { if(row) row--; } if(key_down==0) { if(row<1) row++; } if(key_left==0) { if(col) col--; } if(key_right==0) { if(col<15) col++; } lcd(0x80+(row?0x40:0)+col,0); lcd('A',1); delay(); } }
