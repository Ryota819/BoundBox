import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";

import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { CookieService } from "ngx-cookie-service";
import { AuthModule } from "./auth/auth.module";
import { MainModule } from "./main/main.module";
import { MainComponent } from "./main/main.component";

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    AuthModule,
    MainModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule {}
