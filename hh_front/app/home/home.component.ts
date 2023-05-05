import {Component, OnInit} from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  user_type:string='';
  ngOnInit(){
    var type = localStorage.getItem('user_type');
    if (type) this.user_type = type;
    else if(type == '-1') this.user_type ='-1';
  }
}
