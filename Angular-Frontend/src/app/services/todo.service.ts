import { Injectable } from '@angular/core';
import { HttpClientModule , HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Todo } from '../models/Todo';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':'application/json',
  })
};

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  todosUrl:string = 'https://jsonplaceholder.typicode.com/todos'

  constructor(private http:HttpClient) {
       
   }

  getTodos():Observable<Todo[]>{
    return this.http.get<Todo[]>('http://127.0.0.1:8000/first_app/todo/'); 
  }


  toggleCompleted(todo:Todo):Observable<any>{
    // console.log(todo.title);
    // console.log(todo.id);
    // const url =  this.todosUrl + '/' + todo.id;
    // console.log(url);
    return this.http.put(`http://127.0.0.1:8000/first_app/todo/${todo.id}`,{'completed':todo.completed},httpOptions);
    this.getTodos();
  }

  addTodo(todo:Todo):Observable<Todo>{
  return this.http.post('http://127.0.0.1:8000/first_app/todo/',todo,httpOptions);

  }

  deleteTodo(todo:Todo):Observable<Todo>{
    console.log('Inside Tode Delete Service');
    const url = `http://127.0.0.1:8000/first_app/todo/${todo.id}`;
    console.log(url);
    return this.http.delete<Todo>(url,httpOptions);
  }
}
