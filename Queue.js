// class queue{
//     constructor(){
//         this.array=[]
//     }
//     adding(element){
//         this.array.push(element)
//     }
//     removing(){
//         this.array.shift()
//     }
//     top(){
//         console.log(this.array[0])
//     }
//     isEmpty(){
//         return this.array.length==0
//     }
// }
// queue=new queue
// queue.adding(100)
// queue.adding(200)
// console.log(queue)
// queue.top()



class queue{
    constructor(){
        this.array=[]
    }
    adding(element){
        this.array.push(element);
    }
    removing(){
        this.array.shift()
    }
}
queue=new queue
queue.adding(10);
queue.removing();
queue.adding(20);
console.log(queue)