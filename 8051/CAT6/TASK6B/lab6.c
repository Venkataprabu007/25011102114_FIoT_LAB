    #include <reg51.h>
    char ch;
    void timer_UART(){
        TMOD=0x20;
        TH1=0xFD;
        SCON=0x50;
        TR1=1;
        TI=0;
        RI=0;
    }

    void tx(char ch){
        SBUF=ch;
        while(TI==0);
        TI=0;
    }

    void main(){
        timer_UART();
        while(1){
            while(RI==0);
            ch=SBUF;
            tx(ch);
            RI=0;

        }
    }   