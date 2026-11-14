#include <reg51.h>
char text[] = "Hello from 8051\r\n";
unsigned char i;
void uart_init() { TMOD=0x20; TH1=0xFD; SCON=0x50; TR1=1; }
void tx(char ch) { SBUF=ch; while(TI==0); TI=0; }
void main() {
    uart_init();
    while(1) { for(i=0;text[i]!=0;i++) tx(text[i]); }
}
