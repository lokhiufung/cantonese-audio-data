from datetime import date, timedelta


def get_dates(start_date, end_date):
    y_start, m_start, d_start = start_date.split('-')
    y_end, m_end, d_end = end_date.split('-')

    d1 = date(int(y_start), int(m_start), int(d_start))  # start date
    d2 = date(int(y_end), int(m_end), int(d_end))  # end date
    delta = d2 - d1  # timedelta

    date_list = [str(d1 + timedelta(i)) for i in range(delta.days + 1)]
    return date_list
