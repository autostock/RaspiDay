#include <ctype.h>
#include <sys/time.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


main(int argc, char **argv) {
	fd_set selectset;
	struct timeval timeout;
	int ret;
	int var=0;
	int count=0;
	int tmout=160;
	int maxcount=0;

	while(argc--) {
		if(strcmp("-t", *argv)==0) {
			tmout=atoi(*++argv); // in millis
		} else if(strcmp("-c", *argv)==0) {
			maxcount=atoi(*++argv);
		} else {
			*argv++;
		}
	}

	for(int i=0;  ; i++) {
		FD_ZERO(&selectset);
		FD_SET(0,&selectset);
		timeout.tv_sec = 0;
		timeout.tv_usec = tmout*1000;
		ret =  select(1,&selectset,NULL,NULL,&timeout);
		if(ret == 0) {
			//timeout
			if (count) {
				count=0;
				printf("\n");
				fflush(stdout);
			}
		} else if(ret == -1) {
		  printf("error\n");
		} else {
		   // stdin has data, read it
		   // (we know stdin is readable, since we only asked for read events
		   //and stdin is the only fd in our select set.
			count++;
			int size = read(0, &var, 1);
			// test for EOF
			if (var==-1) {
				return 0;
			}
			printf("%02x", var);
			if (maxcount>0 && count==maxcount) {
				count=0;
				printf("\n");
				fflush(stdout);
			}
		}
	}
}