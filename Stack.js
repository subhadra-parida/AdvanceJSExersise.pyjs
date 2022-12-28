class Stack{
    constructor(){
        this.arr=[]
    }
    adding(element){
        this .arr.push(element)
    }
    removing(){
        this.arr.pop()
    }
    top(){
        this.empty
    }
    isEmpty(){
        if(this.arr.length==0){
            console.log("Stack is empty.")
        }
        else{
            console.log("Stack is not empty.")
        }
    }
}
let stack=new Stack
stack.adding(10)
stack.adding(20)
console.log(stack)
stack.removing()
console.log(stack)
stack.isEmpty()
console.log(stack)

