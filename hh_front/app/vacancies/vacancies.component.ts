import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [

  ];
  newVacancy:string="";

  constructor(private service: VacancyService){

  }
  ngOnInit(): void{
    this.service.getVacancies().subscribe((vacancies)=>{
      this.vacancies = vacancies
      console.log(vacancies)
    })
  }

  addVacancy() {
    if (this.newVacancy.length) {
        this.service.createVacancy(this.newVacancy).subscribe((vacancy) => {
        this.vacancies.push(vacancy);
        this.newVacancy = '';
      });
    }
  }

  deleteVacancy(vacancy_id:number)
  {
    this.service.deleteVacancy(vacancy_id).subscribe((data)=>{
      this.vacancies=this.vacancies.filter((vacancy)=>vacancy.id!==vacancy_id);
    });
  }

}
