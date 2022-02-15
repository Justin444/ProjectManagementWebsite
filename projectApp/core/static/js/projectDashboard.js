//variables
let taskDragged;
let dropzones = document.querySelectorAll('.dropzone');
let priorities;
let dataColors = [
    {color:"red", title:"backlog"},
    {color:"yellow", title:"to do"},
    {color:"purple", title:"in progress"},
    {color:"blue", title:"validating"},
    {color:"green", title:"done"}
];
let dataTasks = {
    config: {
        maxid:0
    },
    cards:[]
};


//initialize
$(document).ready(()=> {
    $("#loadingScreen").addClass("d-none");
    initBoards();
    if(JSON.parse(localStorage.getItem('@project:data'))) {
        dataTasks = JSON.parse(localStorage.getItem('@project:data'));
        initComponents(dataTasks);
    }
    initTasks();
    $('#add').click(()=> {
        const title = $('#titleInput').val()!==''?$('#titleInput').val():null;
        const description = $('#descriptionInput').val()!==''?$('#descriptionInput').val():null;
        $('#titleInput').val('');
        $('#descriptionInput').val('');
        if(title && description) {
            let id = dataTasks.config.maxid+1;
            const newTask = {
                id,
                title,
                description,
                position:"red",
                priority: false
            }
            dataTasks.cards.push(newTask);
            dataTasks.config.maxid = id;
            save();
            appendComponents(newTask);
            initTasks();
        }
    });
    $("#deleteAll").click(()=> {
        dataTasks.cards = [];
        save();
    });
});


//functions
function initBoards() {    
    dataColors.forEach(item=> {
        let htmlString = `
			<div class="board">
				<h3 class="text-center">${item.title.toUpperCase()}</h3>
				<div class="dropzone" id="${item.color}"></div>
			</div>
        `
        $("#boardsContainer").append(htmlString)
    });
    let dropzones = document.querySelectorAll('.dropzone');
    dropzones.forEach(dropzone=> {
        dropzone.addEventListener('dragenter', dragenter);
        dropzone.addEventListener('dragover', dragover);
        dropzone.addEventListener('dragleave', dragleave);
        dropzone.addEventListener('drop', drop);
    });
}

function initTasks() {
    cards = document.querySelectorAll('.projectTask');
    cards.forEach(task=> {
        task.addEventListener('dragstart', dragstart);
        task.addEventListener('drag', drag);
        task.addEventListener('dragend', dragend);
    });
}

function initComponents(dataArray) {
    //create all the stored cards and put inside of the backlog area
    dataArray.cards.forEach(task=> {
        appendComponents(task); 
    })
}

function appendComponents(task) {
    //creates new task inside of the backlog area
    let htmlString = `
        <div id=${task.id.toString()} class="projectTask ${task.position}" draggable="true">
            <form class="row mx-auto justify-content-between">
                <span id="span-${task.id.toString()}" onclick="togglePriority(event)" class="material-icons priority ${task.priority? "is-priority": ""}">
                    star
                </span>
                <button class="invisibleBtn">
                    <span class="material-icons delete" onclick="deleteTask(${task.id.toString()})">
                        remove_circle
                    </span>
                </button>
            </form>
            <div class="content">               
                <h4 class="title">${task.title}</h4>
                <p class="description">${task.description}</p>
            </div>
        </div>
    `
    $(`#${task.position}`).append(htmlString);
    priorities = document.querySelectorAll(".priority");
}

function togglePriority(event) {
    event.target.classList.toggle("is-priority");
    dataTasks.cards.forEach(task=> {
        if(event.target.id.split('-')[1] === task.id.toString()) {
            task.priority=task.priority?false:true;
        }
    })
    save();
}

function deleteTask(id) {
    dataTasks.cards.forEach(task=> {
        if(task.id === id) {
            let index = dataTasks.cards.indexOf(task);
            console.log(index)
            dataTasks.cards.splice(index, 1);
            console.log(dataTasks.cards);
            save();
        }
    })
}


function removeClasses(taskDragged, color) {
    taskDragged.classList.remove('red');
    taskDragged.classList.remove('blue');
    taskDragged.classList.remove('purple');
    taskDragged.classList.remove('green');
    taskDragged.classList.remove('yellow');
    taskDragged.classList.add(color);
    position(taskDragged, color);
}

function save() {
    localStorage.setItem('@project:data', JSON.stringify(dataTasks));
}

function position(taskDragged, color) {
    const index = dataTasks.cards.findIndex(task => task.id === parseInt(taskDragged.id));
    dataTasks.cards[index].position = color;
    save();
}

//cards
function dragstart() {
    dropzones.forEach( dropzone=>dropzone.classList.add('highlight'));
    this.classList.add('is-dragging');
}

function drag() {}

function dragend() {
    dropzones.forEach( dropzone=>dropzone.classList.remove('highlight'));
    this.classList.remove('is-dragging');
}

function dragenter() {}

function dragover({target}) {
    this.classList.add('over');
    taskDragged = document.querySelector('.is-dragging');
    if(this.id ==="red") {
        removeClasses(taskDragged, "red");   
    } else if(this.id ==="yellow") {
        removeClasses(taskDragged, "yellow");
    } else if(this.id ==="purple") {
        removeClasses(taskDragged, "purple");
    } else if(this.id ==="blue") {
        removeClasses(taskDragged, "blue");
    } else if(this.id ==="green") {
        removeClasses(taskDragged, "green");
    }
    this.appendChild(taskDragged);
}

function dragleave() {
    this.classList.remove('over');
}

function drop() {
    this.classList.remove('over');
}