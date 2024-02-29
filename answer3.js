

function flatten(a) {
    let r=[];
    
    for (let i = 0; i < a.length; i++){
        if (a[i] instanceof Array) {
            r.push(...flatten(a[i]));
        } else {
            r.push(a[i]);
        }
    }
    return r;
}

let nested = [1, [2, 3], [[4], [5]]];

console.log(flatten(nested));