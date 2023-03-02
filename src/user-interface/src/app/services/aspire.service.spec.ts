import { TestBed } from '@angular/core/testing';

import { AspireService } from './aspire.service';

describe('AspireService', () => {
  let service: AspireService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AspireService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
