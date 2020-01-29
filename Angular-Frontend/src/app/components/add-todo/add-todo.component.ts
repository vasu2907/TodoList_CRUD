import { Component, OnInit,EventEmitter,Output } from '@angular/core';

@Component({
  selector: 'app-add-todo',
  templateUrl: './add-todo.component.html',
  styleUrls: ['./add-todo.component.scss']
})
export class AddTodoComponent implements OnInit {

  @Output() addTodo:EventEmitter<any> = new EventEmitter();

  title:string;

  constructor() { }

  ngOnInit() {
  }

  onSubmit(){
    const data = {
      'title':this.title,
    }    
    console.log("Inside ADDTODO Component");
    console.log(data['title']);
    this.addTodo.emit(data);
  }

}
