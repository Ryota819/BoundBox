import { Component, OnInit, HostListener } from "@angular/core";
import { GlobalService } from "../../global.service";
import { ApiService } from "../../api.service";
import { User } from "../../models/user";
import { Subscription } from "rxjs/Subscription";
import { FormGroup, FormBuilder } from "@angular/forms";
import { environment } from "../../../environments/environment";
@Component({
  selector: "app-home",
  templateUrl: "./home.component.html",
  styleUrls: ["./home.component.css"]
})
export class HomeComponent implements OnInit {
  baseurl = environment.baseurl;
  files: any = [];
  userSub: Subscription;
  account: User = new User();
  form: FormGroup;
  next: string = "";
  emphathyInput: FormGroup;
  constructor(
    private apiService: ApiService,
    private global: GlobalService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      user: [""]
    });
    this.userSub = this.global.user.subscribe(me => (this.account = me));
    this.global.me = JSON.parse(localStorage.getItem("account"));
    this.form.get("user").setValue(this.account.id);
    this.apiService.getImage().subscribe(
      res => {
        this.files = res["result"];
        this.next = res["next"];
      },
      err => { }
    );
    $(".gallery-list-item").click(function () {
      let value = $(this).attr("data-filter");
      if (value === "all") {
        $(".filter").show(300);
      } else {
        $(".filter")
          .not("." + value)
          .hide(300);
        $(".filter")
          .filter("." + value)
          .show(300);
      }
    });

    $(".gallery-list-item").click(function () {
      $(this)
        .addClass("active-item")
        .siblings()
        .removeClass("active-item");
    });
  }
  @HostListener("window:scroll", ["$event"])
  onWindowScroll() {
    if (window.innerHeight + window.scrollY === document.body.scrollHeight) {
      this.apiService.getNextImage(this.next).subscribe(
        res => {
          Array.prototype.push.apply(this.files, res["result"]);
          this.next = res["next"];
        },
        err => { }
      );
    }
  }
  sendLikeIt(id, index) {
    this.emphathyInput = this.formBuilder.group({
      image: [id],
      empathizer: [this.form.get("user").value],
      kind: ["LIKE"]
    });
    this.apiService.createEmpathy(this.emphathyInput.value).subscribe(
      res => {
        if (res.message) {
          // 追加
          this.files[index].no_of_empathy = this.files[index].no_of_empathy - 1;
        } else {
          // 削除
          this.files[index].no_of_empathy = this.files[index].no_of_empathy + 1;
        }
      },
      err => console.log(err)
    );
  }
}
