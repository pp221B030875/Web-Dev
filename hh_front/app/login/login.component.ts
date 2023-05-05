import {Component, OnInit} from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  ngOnInit(){
    const token=localStorage.getItem('jwt');
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
      localStorage.setItem('jwt',data.token);
      this.logged=true;
      this.loginService.getUserType(this.username).subscribe((data)=>{
        localStorage.setItem('user_type',data.user_type);
        localStorage.setItem('username',this.username);
      });
    });
  }
  logout(){
    localStorage.removeItem('jwt');
    localStorage.removeItem('username');
    localStorage.setItem('user_type','-1');
    //request to the django
    this.logged=false;
  }


}
