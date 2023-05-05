import { ComponentFixture, TestBed } from '@angular/core/testing';
import { VacancyTopFiveteenComponent } from './vacancy-top-fiveteen.component';

describe('VacancyTopFiveteenComponent', () => {
  let component: VacancyTopFiveteenComponent;
  let fixture: ComponentFixture<VacancyTopFiveteenComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VacancyTopFiveteenComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VacancyTopFiveteenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
