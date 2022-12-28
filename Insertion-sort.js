a=[5,3,4,2,1]
// for (i=1;i<a.length;i++){
//     key=a[i]
//     j=i
//     while (j!=0 && key<a[j-1]){
//         // temp=a[j]
//         // a[j]=a[j-1]
//         // a[j-1]=temp
//         a[j],a[j-1]==a[j-1],a[j]

//         j-=1
//     }
// }
// console.log(a)
// a=[5,3,4,2,1]
for (i=1;i<a.length;i++){
    key=a[i]
    j=i
    while (j!=0 && a[j]<a[j-1]){
        temp=a[j]
        a[j]=a[j-1]
        a[j-1]=temp
        j-=1
    }
}
console.log(a)
