import {Component, OnInit} from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  ngOnInit(){
    const token=localStorage.getItem('token');
    if(token){
      //if token exists in the local storage
      this.logged=true;
    }
  }
  constructor(private loginService:LoginService){

  }
  logged:boolean=false;
  username:string="";
  password:string="";


  login(){
    this.loginService.login(this.username,this.password).subscribe((data)=>{
      //console.log(data);
      localStorage.setItem('token',data.token);
      this.logged=true;

    });
  }
  logout(){
    localStorage.removeItem('token');
    //request to the django
    this.logged=false;
  }


}
