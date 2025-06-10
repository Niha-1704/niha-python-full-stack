// creating Functions
// const s = function add(x , y)
// {
//     return x + y;
// }
// console.log(s(8,9))


//function expression
// const s = function(x) 
// {
//     return x * x;
// } 
// console.log(s(5))

//arrow function
// const sq = (x) =>{
//     return x * x
// }
// console.log(sq(6))

// const sq = x => x*x
// console.log(sq(6))

//anonymous func
// const greet = function(){
//     console.log("Hai")
// }
// greet()

//callback function
// const s = (name,func)=>{
//     console.log("Hello",name)
//     func();
// }
// s("hyderabad",()=>console.log("...."))


// function greet(name,callback){
//     console.log("Hello",name);
//     callback();
// }
// const gm = ()=> console.log("good morning")
// greet("janu",gm)


//higher order function
function area(x,func){
    return func(x);
}
const sq = x => x * x;
console.log(area(5,sq));