#include  <stdio.h>
#include  <signal.h>
int rakesh_verified = 1;
int ravi_verified = 1;
int main(int argc,char *argv[]){
        void handler_1(int);
        void handler_2(int);

        if(signal(SIGUSR1,handler_1) == SIG_ERR){
                printf("Unable to excecute 1");
        }

        if(signal(SIGUSR2,handler_2) == SIG_ERR){
                printf("Unable to excecute 2");
        }

        char *newargv[] = {NULL,NULL};
        char *newenviron[] = {NULL};
        
	pid_t  pid2  = -1;
        pid_t  pid1  = -1;
        pid1 = fork();
	if(pid1>0){
		pause();
	}                        			     //create first process
        if(pid1 == 0){                                      //first child initiation              
                execv(argv[1]);
        }if(pid1!=0){               
		pid2 = fork();
		if(pid2 > 0){
			pause();              
                }                //create second process
        }
        if(pid1<0){
                printf("Wrong Command");
        }

        if(pid2 == 0){                                    //second child initiation
                execv(argv[2]);
        }
        if(pid1 > 0 && pid2 > 0){                          //parent intitiation

                int pi1 = pid1;
                int pi2 = pid2;
                kill(pid1,SIGUSR1);
                kill(pid2,SIGUSR1);
                sleep(1);
                printf("Lost and Found, going home now.\n");
        }
        return 0;
}

void handler_1(int sig){
        signal(sig,SIG_IGN);
        printf("I can hear you, Ravi!\n");
        signal(SIGUSR1,handler_1);
}

void handler_2(int sig){
        signal(sig,SIG_IGN);
        printf("I can hear you, Rakesh!\n");
        signal(SIGUSR2,handler_2);
}

                                                                         

