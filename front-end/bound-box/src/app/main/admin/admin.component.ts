import { Component, OnInit, HostListener } from "@angular/core";
import { GlobalService } from "../../global.service";
import { ApiService } from "../../api.service";
import { User } from "../../models/user";
import { Subscription } from "rxjs/Subscription";
import { FormGroup, FormBuilder, FormControl } from "@angular/forms";
import { environment } from "../../../environments/environment";
import { Router } from "@angular/router";
@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  baseurl = environment.baseurl;
  files: any = [];
  userSub: Subscription;
  account: User = new User();
  form: FormGroup;
  next: string = "";
  imageInput: FormGroup;
  constructor(
    private apiService: ApiService,
    private global: GlobalService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      user: [""]
    });
    this.userSub = this.global.user.subscribe(me => (this.account = me));
    this.global.me = JSON.parse(localStorage.getItem("account"));
    this.form.get("user").setValue(this.account.id);
    if (this.account.is_staff == false) {
      this.router.navigate(["/home"]);
    }
    this.apiService.getNotCheckedImage().subscribe(
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
  update(id, index, tag) {
    this.imageInput = this.formBuilder.group({
      image: [id],
      updateTag: [tag]
    });
    this.apiService.updateTag(this.imageInput.value).subscribe(
      res => {
        console.log(res)
      },
      err => console.log(err)
    );
  }

}
