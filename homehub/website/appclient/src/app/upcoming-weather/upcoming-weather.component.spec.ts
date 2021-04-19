import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpcomingWeatherComponent } from './upcoming-weather.component';

describe('UpcomingWeatherComponent', () => {
  let component: UpcomingWeatherComponent;
  let fixture: ComponentFixture<UpcomingWeatherComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpcomingWeatherComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpcomingWeatherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
