import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-vacancy-top-ten',
  templateUrl: './vacancy-top-ten.component.html',
  styleUrls: ['./vacancy-top-ten.component.css']
})
export class VacancyTopTenComponent implements OnInit{
  vacancies: Vacancy[] = [];
  constructor(private service: VacancyService){}
  ngOnInit(): void{
    this.service.getTopVacancies().subscribe((vacancies)=>{
      this.vacancies = vacancies
    })
  }
}
