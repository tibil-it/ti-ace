import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwareComponent } from './aware.component';

describe('AwareComponent', () => {
  let component: AwareComponent;
  let fixture: ComponentFixture<AwareComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwareComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwareComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
