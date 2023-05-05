import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompaniesComponent } from './companies/companies.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { VacancyDetailsComponent } from './vacancy-details/vacancy-details.component';
import { VacancyTopTenComponent } from './vacancy-top-ten/vacancy-top-ten.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';
import { LoginComponent } from './login/login.component';
import {FormsModule} from "@angular/forms";
import {AuthInterceptor} from "./AuthInterceptor";
import { VacancyTopFiveteenComponent } from './vacancy-top-fiveteen/vacancy-top-fiveteen.component';
import { AboutComponent } from './about/about.component';

@NgModule({
  declarations: [
    AppComponent,
    CompaniesComponent,
    CompanyDetailsComponent,
    CompanyVacanciesComponent,
    VacanciesComponent,
    VacancyDetailsComponent,
    VacancyTopTenComponent,
    HomeComponent,
    AuthComponent,
    LoginComponent,
    VacancyTopFiveteenComponent,
    AboutComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    {
      provide:HTTP_INTERCEPTORS,
      useClass:AuthInterceptor,
      multi:true,
    }

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
