import { Component } from '@angular/core';
import { HttpClientModule , HttpHeaders, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'todolist';
  sometext:string;
  stext:string;
  constructor(private http:HttpClient) {
       
  }
  testf(){

    let test_var= this.http.get('http://localhost:8000/first_app/todo/').subscribe(
      res => {
        console.log(res);
        this.sometext = res[0]['payload'];
      },
      error => {
        console.log(error);
      }
    );

    // console.log(test_var);
    return test_var;
  }


  onSubmit(){
    // console.log('here');
    const todo = {
      title:this.title,
      completed:false
    }
    this.testf();
    
  }

  onPostSubmit(){
    const data = {
      text: "Vasu",
    }

    console.log(data);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin':'*',
      })
    };

    let test_var = this.http.post<any>('http://localhost:8000/first_app/todo/',JSON.stringify(data),httpOptions).subscribe(
      res => {

      },
      error => {

      }
    );

  }
  
}
