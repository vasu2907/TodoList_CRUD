import { Component, OnInit, Input,EventEmitter,Output  } from '@angular/core';
import { Todo } from '../../models/Todo';
import { TodoService } from '../../services/todo.service';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.scss']
})
export class TodoItemComponent implements OnInit {

  @Input('todo') private todo:Todo;
  @Output() deleteTodo:EventEmitter<Todo> = new EventEmitter();


  constructor(private todoService:TodoService) { }

  ngOnInit() {
  }


  setClasses(){
    let classes = {
      todo:true,
      'is-complete':this.todo.completed,
    }
    return classes;
  }

  onToggle(todo){
    todo.completed = !todo.completed;
    this.todoService.toggleCompleted(todo).subscribe();
  }

  onDelete(todo){
    console.log("Delete");
    this.deleteTodo.emit(todo);
  }




}
