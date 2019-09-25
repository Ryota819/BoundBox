import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
declare var $: any;

@Component({
  selector: "app-menu",
  templateUrl: "./menu.component.html",
  styleUrls: ["./menu.component.css"]
})
export class MenuComponent implements OnInit {
  constructor() {}

  ngOnInit() {
    $(".nav-button").click(() => {
      $(".nav-button").toggleClass("change");
    });
    $(window).scroll(function() {
      let position = $(this).scrollTop();
      if (position >= 200) {
        $(".nav-menu").addClass("custom-navbar");
      } else {
        $(".nav-menu").removeClass("custom-navbar");
      }
    });
  }
}
