import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VacancyDetailsComponent } from './vacancy-details/vacancy-details.component';
import { CompaniesComponent } from './companies/companies.component';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';
import { VacancyTopTenComponent } from './vacancy-top-ten/vacancy-top-ten.component';

import { CompanyDetailsComponent } from './company-details/company-details.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { HomeComponent} from "./home/home.component";
import {AuthComponent} from "./auth/auth.component";
import {LoginComponent} from "./login/login.component";
import {VacancyTopFiveteenComponent} from "./vacancy-top-fiveteen/vacancy-top-fiveteen.component";
import {AboutComponent} from "./about/about.component";


const routes: Routes = [
  { path: 'api/companies', component: CompaniesComponent },
  { path: 'api/companies/:id', component: CompanyDetailsComponent},
  { path: 'api/companies/:id/vacancies', component: CompanyVacanciesComponent },
  { path: 'api/vacancies', component: VacanciesComponent},
  { path: 'api/vacancies/:id', component: VacancyDetailsComponent },
  { path: 'api/top_ten', component: VacancyTopTenComponent },
  { path: 'api/home', component: HomeComponent },
  {path:'api/auth',component:AuthComponent},
  {path:'api/login',component:LoginComponent},
  {path:'api/top_fiveteen',component:VacancyTopFiveteenComponent},
  {path:'api/about',component:AboutComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
