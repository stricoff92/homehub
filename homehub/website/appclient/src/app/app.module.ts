import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { ClockWidgetComponent } from './clock-widget/clock-widget.component';

@NgModule({
  declarations: [
    AppComponent,
    ClockWidgetComponent
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
