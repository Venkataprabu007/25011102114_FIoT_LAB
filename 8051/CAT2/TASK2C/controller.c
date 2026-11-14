#include <reg51.h>
sbit led1 = P1^1;
sbit led2 = P1^2;
sbit led3 = P1^3;
sbit led4 = P1^4;
sbit button = P3^2;
unsigned char mode = 0;
unsigned char count = 0;
void delay() {
    int i, j;
    for(i = 0; i < 300; i++)
        for(j = 0; j < 400; j++);
}
void main() {
    button = 1;
    while(1) {
        if(button == 0) {
            delay();
            if(button == 0) {
                mode = (mode + 1) % 4;
                while(button == 0);
            }
        }
        if(mode == 0) { led1=1; led2=0; led3=0; led4=0; delay(); led1=0; led2=1; delay(); led2=0; led3=1; delay(); led3=0; led4=1; delay(); }
        else if(mode == 1) { P1 = ((count++ & 15) << 1); delay(); }
        else if(mode == 2) { led1=1; led2=0; led3=1; led4=0; delay(); led1=0; led2=1; led3=0; led4=1; delay(); }
        else { P1 = 0x1E; delay(); P1 = 0; delay(); }
    }
}
