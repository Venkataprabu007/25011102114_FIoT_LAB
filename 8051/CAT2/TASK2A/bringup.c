#include <reg51.h>
sbit led = P1^0;
void delay() {
    int i, j;
    for(i = 0; i < 300; i++)
        for(j = 0; j < 400; j++);
}
void main() {
    while(1) {
        led = 0;
        delay();
        led = 1;
        delay();
    }
}
