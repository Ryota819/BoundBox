import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { CookieService } from "ngx-cookie-service";
import { MainRoutingModule } from "./main-routing.module";
import { MainComponent } from "./main.component";
import { MenuComponent } from "./menu/menu.component";
import { ProfileComponent } from './profile/profile.component';
import { RecommendComponent } from './recommend/recommend.component';
import { LikeboxComponent } from './likebox/likebox.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [MainComponent, MenuComponent, ProfileComponent, RecommendComponent, LikeboxComponent, HomeComponent],
  imports: [
    CommonModule,
    MainRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [CookieService]
})
export class MainModule {}
