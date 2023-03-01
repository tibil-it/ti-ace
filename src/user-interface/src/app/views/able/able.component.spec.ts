import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AbleComponent } from './able.component';

describe('AbleComponent', () => {
  let component: AbleComponent;
  let fixture: ComponentFixture<AbleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AbleComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AbleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
