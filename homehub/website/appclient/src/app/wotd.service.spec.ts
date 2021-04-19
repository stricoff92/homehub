import { TestBed } from '@angular/core/testing';

import { WotdService } from './wotd.service';

describe('WotdService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WotdService = TestBed.get(WotdService);
    expect(service).toBeTruthy();
  });
});
