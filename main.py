<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 500px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        .input-section {
            display: flex;
            justify-content: space-between;
        }
        input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            padding: 10px 15px;
            margin-left: 5px;
            border: none;
            background: #28a745;
            color: white;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
        ul {
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }
        li {
            background: #fafafa;
            padding: 10px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        li.completed {
            text-decoration: line-through;
            color: gray;
        }
        .delete-btn {
            background: #dc3545;
            border: none;
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
        }
        .delete-btn:hover {
            background: #c82333;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>To-Do List</h2>
        <div class="input-section">
            <input type="text" id="taskInput" placeholder="Enter a new task">
            <button id="addTaskBtn">Add</button>
        </div>
        <ul id="taskList"></ul>
    </div>

    <script>
        const taskInput = document.getElementById('taskInput');
        const addTaskBtn = document.getElementById('addTaskBtn');
        const taskList = document.getElementById('taskList');

        addTaskBtn.addEventListener('click', addTask);
        taskInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                addTask();
            }
        });

        function addTask() {
            const taskText = taskInput.value.trim();
            if (taskText === '') return;

            const li = document.createElement('li');
            li.textContent = taskText;

            li.addEventListener('click', function() {
                li.classList.toggle('completed');
            });

            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.classList.add('delete-btn');
            deleteBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                li.remove();
            });

            li.appendChild(deleteBtn);
            taskList.appendChild(li);
            taskInput.value = '';
        }
    </script>

</body>
</html>
