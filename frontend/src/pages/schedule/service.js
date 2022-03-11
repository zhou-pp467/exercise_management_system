import { request } from 'umi';

export async function getCalendarData () {
  return request('/api/get_calendar_data');
}

export async function getDayData (value) {
  return request('/api/get_day_data?date=' + value);
}
