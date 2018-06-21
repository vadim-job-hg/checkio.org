import sendgrid
import json
import datetime
API_KEY = 'API KEY'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def how_spammed(str_date):
    end_time = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    start_time = end_time + datetime.timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
        'end_time': int(end_time.timestamp()),
        'start_time': int(start_time.timestamp())
    })
    data = json.loads(response.body)
    return len(data)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')