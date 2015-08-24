from ics import Calendar
import urllib.request
import csv

# Download Calendar
url = "https://www.google.com/calendar/ical/nytimes.com_c9hche3raajglitokho7rvu664@group.calendar.google.com/public/basic.ics"
c = Calendar(urllib.request.urlopen(url).read().decode('utf-8'))

# Create CSV File
csvfile = open("election_primaries.csv", "w", newline="")
calwriter = csv.writer(csvfile, delimiter=",")

# Read information from the calendar and write the
# information we need to the CSV file.
for i in range(0, len(c.events)):
    state = c.events[i].location
    election = c.events[i].name
    date = c.events[i].begin.format("MMMM D")

    #print([state, election, date])
    calwriter.writerow([state, election, date])
