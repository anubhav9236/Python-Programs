#include<stdio.h>
using namespace std;
#define SIZE 5
int queue[SIZE];
int front=-1,rear=-1;
void enqueue(int x){
    if((rear+1)%SIZE==front){
        printf("Queue is full\n");
    }
    else{
        if(front==-1)
        front=0;
        rear=(rear+1)%SIZE;
        queue[rear]=x;
        printf("%d inserted\n",x);
    }
}
void dequeue(){
    if(front==1){
        printf("Queue is Empty\n");
    }
    else{
        printf("%d deleted\n",queue[front]);
        if(front==rear){
            front=rear=-1;
        }
        else{
            front=(front+1)%SIZE;
        }
    }
}
void display(){
    if(front==-1){
        printf("Queue is Empty\n");
    }
    else{
        printf("Queue elements:");
        int i=front;
        while(i!=rear){
            printf("%d",queue[i]);
            i=(i+1)%SIZE;
        }
        printf("%d\n",queue[rear]);
    }
}
int main(){
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    dequeue();
    dequeue();
    display();
    enqueue(50);
    enqueue(60);
    display();
    return 0;
}