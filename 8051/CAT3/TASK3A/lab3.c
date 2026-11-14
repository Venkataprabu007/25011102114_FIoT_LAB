#include <reg51.h>

sbit led0 = P1^1;
sbit led1 = P1^2;
sbit led2 = P1^3;
sbit led3 = P1^4;

sbit row1 = P2^7;
sbit col2 = P2^2;
sbit col1=P2^1;
int stat;
int mode = 0;
int num = 0;

void delay2() {
    int i, j;
    for(i = 0; i < 2; i++)
        for(j = 0; j < 127; j++);
}


int keypress() {
    row1 = 0;
	  stat=0;

    if(col2 == 0 || col1 ==0) {
        delay2();

        if(col2 == 0) {
            while(col2 == 0);   
						stat=1;
            return 1;
        }
				else if(col1==0){
						while(col1==0);
					   stat=2;
							return 1;
				}
    }

    return 0;
}


int intr() {

    if(keypress()) {
		if(stat==1){
        mode = (mode + 1) % 4;
        num = 0;
        return 1;
		}
			else if(stat==2){
					mode=mode-1;
					if(mode<0){mode=3;}
					num=0;
					return 1;
		}
	}

    return 0;
}


int delay() {

    int i, j;

    for(i = 0; i < 300; i++) {

        for(j = 0; j < 400; j++);

        if(intr())
            return 1;
    }

    return 0;
}


void counter() {

    int a;

    if(intr()) return;

    a = num;

    led0 = a % 2;
    a /= 2;

    led1 = a % 2;
    a /= 2;

    led2 = a % 2;
    a /= 2;

    led3 = a % 2;

    if(delay())
        return;
}

void seq() {

    if(intr()) return;

    led0 = 1;
    led1 = 0;
    led2 = 0;
    led3 = 0;
    if(delay()) return;

    led0 = 0;
    led1 = 1;
    if(delay()) return;

    led1 = 0;
    led2 = 1;
    if(delay()) return;

    led2 = 0;
    led3 = 1;
    if(delay()) return;

    led3 = 0;
}


void pattern1() {

    if(intr()) return;

    led0 = 1;
    led1 = 0;
    led2 = 1;
    led3 = 0;

    if(delay()) return;

    led0 = 0;
    led1 = 1;
    led2 = 0;
    led3 = 1;

    if(delay()) return;
}

void pattern2() {

    if(intr()) return;

    led0 = 1;
    led1 = 1;
    led2 = 1;
    led3 = 1;

    if(delay()) return;

    led0 = 0;
    led1 = 0;
    led2 = 0;
    led3 = 0;

    if(delay()) return;
}

void main() {

    while(1) {

        if(intr())
            continue;

        switch(mode) {

            case 0:
                seq();
                break;

            case 1:
                num++;
						   if(num>15){num=0;}
                counter();
                break;

            case 2:
                pattern1();
                break;

            case 3:
                pattern2();
                break;
        }
    }
}