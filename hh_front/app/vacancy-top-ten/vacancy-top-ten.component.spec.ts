import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VacancyTopTenComponent } from './vacancy-top-ten.component';

describe('VacancyTopTenComponent', () => {
  let component: VacancyTopTenComponent;
  let fixture: ComponentFixture<VacancyTopTenComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VacancyTopTenComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VacancyTopTenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
