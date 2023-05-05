import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from '../models';
import { VacancyService } from '../vacancy.service';
import { CompanyService } from '../company.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-vacancy-details',
  templateUrl: './vacancy-details.component.html',
  styleUrls: ['./vacancy-details.component.css']
})
export class VacancyDetailsComponent implements OnInit{
  vacancy: Vacancy
  company: Company
  constructor( private route: ActivatedRoute, private VacancyService: VacancyService, private CompanyService: CompanyService) {
    this.vacancy = {} as Vacancy;
    this.company = {} as Company;
  }
  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.VacancyService.getVacancy(id).subscribe((vacancy) => {
          this.vacancy = vacancy;
          this.CompanyService.getCompany(vacancy.company).subscribe((company) => {
            this.company = company;
          })
        })
      }
    });
  }

}
