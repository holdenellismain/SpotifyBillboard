from csvfuncs import process_csv

'''
old method:
processes ~20,000 before getting rate limited
around 0.225 seconds per line
'''
read_file_path = 'C:/Users/fires/Downloads/modifiedbillboarddata.csv'
write_file_path = 'C:/Users/fires/Python Projects/Spotify/billboardweekdataV2.csv'

starting_date = input("Enter the date to start reading the database from: ")
process_csv(read_file_path, write_file_path, starting_date)
print("Processing complete")
                 
"""
# Open the CSV file
with open(read_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Loop through each row in the CSV file
    current_date = ""
    week_list = []
    features_count = 0 #count the number of songs in the week that have features, could be interesting
    count = 0
    for row in csv_reader:
        #keep track of progress
        count += 1
        title = row['title']
        raw_artist = row['performer']
        #remove the feature to help with search
        artist = remove_feature(raw_artist)
        
        #find song id for row
        song_id = search_for_song(title, artist, header)
        if song_id:
            date = row['chart_week']
            #if the date is the same as the previous line, add the song id to the list for that week
            if date == current_date:
                week_list.append(song_id)
                if artist != raw_artist:
                    features_count += 1
            else:
                #if there were songs for the week (not first row or failure in searches)
                if len(week_list) > 5:
                    week_stats = average_attributes(week_list, header)
                    week_stats.append(current_date)
                    week_stats.append(features_count)
                    append_row(write_file_path, week_stats)
                    #print progress
                    print(f'Progress: {(count / LINES) * 100:.2f}%')
                #reset for the new week
                header = get_auth_header() #get a new header every once and a while so that it doesn't time out parsing a large file
                week_list = [song_id]
                current_date = date
                if artist != raw_artist:
                    features_count = 1
                else:
                    features_count = 0
        else:
            print(title, " could not be found.")"""
            


