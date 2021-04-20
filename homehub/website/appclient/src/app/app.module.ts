import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { ClockWidgetComponent } from './clock-widget/clock-widget.component';
import { CurrentWeatherComponent } from './current-weather/current-weather.component';
import { UpcomingWeatherComponent } from './upcoming-weather/upcoming-weather.component';
import { WordOfTheDayComponent } from './word-of-the-day/word-of-the-day.component';
import { BikeStationsComponent } from './bike-stations/bike-stations.component';
import { VulnerabilitiesComponent } from './vulnerabilities/vulnerabilities.component';
import { HolidaysComponent } from './holidays/holidays.component';

@NgModule({
  declarations: [
    AppComponent,
    ClockWidgetComponent,
    CurrentWeatherComponent,
    UpcomingWeatherComponent,
    WordOfTheDayComponent,
    BikeStationsComponent,
    VulnerabilitiesComponent,
    HolidaysComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
