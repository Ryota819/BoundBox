import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { AuthRoutingModule } from "./auth-routing.module";
import { AuthComponent } from "./auth.component";
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { CookieService } from "ngx-cookie-service";
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
@NgModule({
  declarations: [AuthComponent, LoginComponent, RegisterComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    AuthRoutingModule
  ],
  providers: [CookieService]
})
export class AuthModule {}
