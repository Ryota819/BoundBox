import { NgModule, Component } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { MainModule } from "./main/main.module";

const routes: Routes = [{ path: "boxes", loadChildren: () => MainModule }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
