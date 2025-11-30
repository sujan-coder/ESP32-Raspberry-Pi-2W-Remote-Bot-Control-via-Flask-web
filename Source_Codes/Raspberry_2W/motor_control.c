#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>

int main() {
    int uart = open("/dev/serial0", O_RDWR | O_NOCTTY);
    if (uart == -1) {
        perror("Error opening UART");
        return 1;
    }

    struct termios options;
    tcgetattr(uart, &options);
    options.c_cflag = B115200 | CS8 | CLOCAL | CREAD;
    options.c_iflag = IGNPAR;
    options.c_oflag = 0;
    options.c_lflag = 0;
    tcflush(uart, TCIFLUSH);
    tcsetattr(uart, TCSANOW, &options);

    printf("Type motor commands (F/B/L/R/S):\n");
    
    while (1) {
        char cmd;
        scanf(" %c", &cmd);
        write(uart, &cmd, 1);
        printf("Sent: %c\n", cmd);
    }

    close(uart);
    return 0;
}

