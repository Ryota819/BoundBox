import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LikeboxComponent } from './likebox.component';

describe('LikeboxComponent', () => {
  let component: LikeboxComponent;
  let fixture: ComponentFixture<LikeboxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LikeboxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LikeboxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
