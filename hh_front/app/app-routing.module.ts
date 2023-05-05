import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VacancyDetailsComponent } from './vacancy-details.component';
import { CompaniesComponent } from './companies.component';
import { CompanyVacanciesComponent } from './company-vacancies.component';
import { VacancyTopTenComponent } from './vacancy-top-ten.component';

import { CompanyDetailsComponent } from './company-details.component';
import { VacanciesComponent } from './vacancies.component';
import { HomeComponent} from "./home.component";
import {AuthComponent} from "./auth.component";
import {LoginComponent} from "./login.component";
import {VacancyTopFiveteenComponent} from "./vacancy-top-fiveteen.component";
import {AboutComponent} from "./about.component";


const routes: Routes = [
  { path: 'companies', component: CompaniesComponent },
  { path: 'companies/:id', component: CompanyDetailsComponent},
  { path: 'companies/:id/vacancies', component: CompanyVacanciesComponent },
  { path: 'vacancies', component: VacanciesComponent},
  { path: 'vacancies/:id', component: VacancyDetailsComponent },
  { path: 'top_ten', component: VacancyTopTenComponent },
  { path: 'home', component: HomeComponent },
  {path:'auth',component:AuthComponent},
  {path:'login',component:LoginComponent},
  {path:'top_fiveteen',component:VacancyTopFiveteenComponent},
  {path:'about',component:AboutComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
