import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BasicHorizontalCardComponent } from './basic-horizontal-card.component';

describe('BasicHorizontalCardComponent', () => {
  let component: BasicHorizontalCardComponent;
  let fixture: ComponentFixture<BasicHorizontalCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BasicHorizontalCardComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BasicHorizontalCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
