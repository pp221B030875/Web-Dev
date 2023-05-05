import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-vacancy-top-fiveteen',
  templateUrl: './vacancy-top-fiveteen.component.html',
  styleUrls: ['./vacancy-top-fiveteen.component.css']
})
export class VacancyTopFiveteenComponent implements OnInit{
  vacancies: Vacancy[] = [];
  constructor(private service: VacancyService){}
  ngOnInit(): void{
    this.service.getTop15Vacancies().subscribe((vacancies)=>{
      this.vacancies = vacancies
    })
  }
}
