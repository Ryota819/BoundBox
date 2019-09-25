import { NgModule } from "@angular/core";

import { Routes, RouterModule } from "@angular/router";
import { HomeComponent } from "./home/home.component";
import { RecommendComponent } from "./recommend/recommend.component";
import { LikeboxComponent } from "./likebox/likebox.component";
import { ProfileComponent } from "./profile/profile.component";

const routes: Routes = [
  { path: "home", component: HomeComponent },
  { path: "recommend", component: RecommendComponent },
  { path: "likebox", component: LikeboxComponent },
  { path: "profile", component: ProfileComponent }
];
@NgModule({
  declarations: [],
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule {}
