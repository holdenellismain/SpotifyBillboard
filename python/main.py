from csvfuncs import process_csv

read_file_path = 'C:/Users/fires/Downloads/modifiedbillboarddata.csv'
write_file_path = 'C:/Users/fires/Python Projects/Spotify/billboardweekdataV2.csv'

starting_date = input("Enter the date to start reading the database from: ")
process_csv(read_file_path, write_file_path, starting_date)
print("Processing complete")
