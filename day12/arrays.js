// let names = ["lav","niha","deepu"]
// console.log(names[1])
// names[3] = "sailu"
// console.log(names)

// names[1] = "sailu"
// console.log(names)

let arr2 = ["srinu","janu",10,29.5,true]
console.log(arr2)
console.log(arr2.length);
console.log("pop : ",arr2.pop());
arr2.pop()
console.log(arr2)

arr2.push(100)
console.log(" after push",arr2)

arr2.shift()
console.log("removing the starting element ",arr2)

x = arr2.unshift("niha")
console.log("adding element at starting " ,arr2)
console.log(x)

console.log("check wheather elemnet is present in it ",arr2.includes("janu"))

console.log("accesing index of element: ",arr2.indexOf("niha"))

console.log("after slice: ",arr2.slice(0,2))

console.log("After splice: ",arr2.splice(1,1))