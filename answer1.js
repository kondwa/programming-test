function popSnap(n) {
    let a = [];
    for (let i = 1; i <= n; i++){
        if (i % 3 == 0 && i % 5 == 0) {
            a.push("PopSnap");
        }else if (i % 3 == 0) {
            a.push("Pop");
        } else if (i % 5 == 0) {
            a.push("Snap");
        } else {
            a.push(i);
        }
    }
    return a;
}

console.log(popSnap(3))

console.log(popSnap(5))

console.log(popSnap(15))