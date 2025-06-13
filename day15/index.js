let todo = JSON.parse(localStorage.getItem("todo"));
if(todo == null)
    todo = []
console.log(todo);

const displayTodo = ()=>{

    const todoContainer = document.getElementById("todo-container");
    todoContainer.innerHTML = "";
    todo.forEach((element, index)=>{
        const todoItem = document.createElement("div");
        todoItem.classList.add("item");
        todoItem.classList.add("pending");
        todoItem.innerText = `${index + 1}. ${element}`;
        
        todoItem.innerHTML = `
        <p>${index + 1}. ${element}</p>
        <select>
            <option value = "pending">Pending</option>
            <option value = "done">Done</option>
        </select>
        `
        const opt = todoItem.querySelector("select");
        opt.addEventListener("change",()=>{
            if (opt.value === "done"){
                todoItem.style.backgroundColor = "green";
            }
            else{
                todoItem.style.backgroundColor = "red";
            }
        })
        todoContainer.append(todoItem);
    })
}

displayTodo(); // displays the todo on call

const button = document.getElementById("addButton")
button.addEventListener("click" , ()=>{
    const input = document.getElementById("todoName")
    todo.push(input.value);
    localStorage.setItem("todo" , JSON.stringify(todo));
    input.value = "";
    displayTodo();
});




//local storage:

// document.body.append(
//     (()=>{
//         let h1 = document.createElement("h1");
//         h1.innerText = localStorage.getItem("name");
//         return h1;
//     })()
// )