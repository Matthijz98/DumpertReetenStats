from models import Show, Video
import csv
import datetime

with open('../../data/shows.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        print(row[1])
        created = Show.objects.get_or_create(show_title=row[1],
                                   show_date=datetime.datetime.strptime(row[2], "%Y-%m-%d").date(),
                                   show_dumpert_id=row[3],
                                   show_youtube_id=row[4],
                                   show_description=row[5])

