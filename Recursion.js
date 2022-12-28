const recursion=(a)=>{
    if (a==1){
        return 1
    }
    else{
        return q*recursion(a-1)
    }
}
console.log(recursion(5))

