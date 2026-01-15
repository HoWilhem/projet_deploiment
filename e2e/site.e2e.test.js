const request = require('supertest');

describe('TravelNow website', () => {
  it('loads homepage', async () => {
    const res = await request('http://localhost:3000').get('/');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('TravelNow');
  });
});
