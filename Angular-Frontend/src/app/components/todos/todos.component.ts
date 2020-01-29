import { Component, OnInit } from '@angular/core';
import { Todo } from '../../models/Todo';
import { TodoService } from '../../services/todo.service';
// import { type } from 'os';
@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  todos:Todo[]=[];

  constructor(private todoService:TodoService) { }

  ngOnInit() {
      this.todoService.getTodos().subscribe(todos=>{
        console.log(todos['payload'].length);
        for(let i=0;i< todos['payload'].length; i++){
            console.log(todos['payload'][i]);
            let obj:Todo={'id': 0 ,'title':"",'completed':false};
            obj.id = todos['payload'][i]['pk'];
            obj.title = todos['payload'][i]['fields']['title'];
            obj.completed = todos['payload'][i]['fields']['completed'];
            this.todos.push(obj);
        }
      });  
  }

  deleteTodo(todo:Todo){
    this.todos = this.todos.filter(t=> t.id!=todo.id);
    this.todoService.deleteTodo(todo).subscribe();
  }

  addTodo(data){
    console.log("Inside AddTodo Service");
    console.log(data['title']);
    this.todoService.addTodo(data).subscribe(); 
    this.ngOnInit();
  }

}
