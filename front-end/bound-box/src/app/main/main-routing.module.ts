import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { MainComponent } from "./main.component";
import { HomeComponent } from "./home/home.component";
import { RecommendComponent } from "./recommend/recommend.component";
import { LikeboxComponent } from "./likebox/likebox.component";
import { ProfileComponent } from "./profile/profile.component";
import { AdminComponent } from "./admin/admin.component";
const routes: Routes = [
  {
    path: "",
    component: MainComponent,
    children: [
      { path: "", redirectTo: "home", pathMatch: "full" },
      { path: "home", component: HomeComponent },
      { path: "likebox", component: RecommendComponent },
      { path: "mybox", component: LikeboxComponent },
      { path: "profile", component: ProfileComponent },
      { path: "admin", component: AdminComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule {}
