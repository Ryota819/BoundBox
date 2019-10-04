import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { AuthModule } from "./auth/auth.module";
import { MainModule } from "./main/main.module";

import { AppComponent } from "./app.component";

const routes: Routes = [{ path: "boxes", loadChildren: () => MainModule }];

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AuthModule,
    MainModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
