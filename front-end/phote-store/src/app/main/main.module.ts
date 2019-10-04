import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MainComponent } from "./main.component";

import { Routes, RouterModule } from "@angular/router";
import { MainRoutingModule } from "./main-routing.module";
import { HomeComponent } from "./home/home.component";
import { MenuComponent } from "./menu/menu.component";
import { ProfileComponent } from "./profile/profile.component";
import { RecommendComponent } from "./recommend/recommend.component";
import { LikeboxComponent } from "./likebox/likebox.component";
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";

const routes: Routes = [{ path: "boxes", component: MainComponent }];

@NgModule({
  declarations: [
    MainComponent,
    HomeComponent,
    MenuComponent,
    ProfileComponent,
    RecommendComponent,
    LikeboxComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    MainRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  exports: [RouterModule]
})
export class MainModule {}
