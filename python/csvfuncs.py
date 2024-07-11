from spotifyfuncs import search_for_song, get_auth_header, average_attributes, remove_feature
import csv
import os

def append_row(file_path, dict_data):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)
    with open(file_path, 'a', newline='') as csvfile:
        # Get the fieldnames from the dictionary keys
        fieldnames = dict_data.keys()
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header if the file does not exist
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(dict_data)

def process_csv(read_file_path, write_file_path, start_date="6/29/2024"):
    '''
    starting at a certain date, this will read in data to be analyzed
    '''
    with open(read_file_path, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        start = False
        row_count = 0

        #initialize variables for the week's data
        header = get_auth_header()
        curr_chart_week = start_date
        song_count = 0
        feature_count = 0
        weeks_on_chart = 0
        week_song_ids = []

        for row in csvreader:
            #once start date has been reached
            if row['chart_week'] == start_date:
                print("Start Date Reached")
                start = True
            if start:
                row_count += 1 #keep track of progress and number of api queries made

                if row_count % 10000 == 0: #if row count is a multiple of 10,000, which takes around 45 minutes
                    header = get_auth_header() #get a new token

                if row_count > 0 and (row_count % 50 == 0): #progress check every 5 weeks
                    print("Week of", curr_chart_week, "is processing")

                title = row['title']
                raw_artist = row['performer']
                artist = remove_feature(raw_artist)
                song_id = search_for_song(title, artist, header)
                if song_id:
                    if row['chart_week'] != curr_chart_week:
                        #if a new week has been reached we
                        #1. query the song analysis data
                        analysis_data = average_attributes(week_song_ids, header)
                        week_data = {
                            'chart_week' : curr_chart_week,
                            'song_count' : song_count,
                            'feature_count' : feature_count,
                            'avg_chart_weeks' : weeks_on_chart / song_count,
                            'avg_minutes' : int(analysis_data[0] / 1000 / 60),
                            'avg_seconds' : int(analysis_data[0] / 1000 % 60),
                            'avg_acousticness' : analysis_data[1],
                            'avg_energy' : analysis_data[2]
                        }
                        #2. write data to outut csv
                        append_row(write_file_path, week_data)
                        #3. reset variables for the next week
                        curr_chart_week = row['chart_week']
                        song_count = 0
                        feature_count = 0
                        weeks_on_chart = 0
                        week_song_ids = []
                    #append to current week
                    week_song_ids.append(song_id)
                    song_count += 1
                    if artist != raw_artist:
                        feature_count += 1
                    weeks_on_chart += int(row["wks_on_chart"])
                #if song cannot be found
                else:
                    print(title, " could not be found.")     
            #check if the start date has been reached yet

