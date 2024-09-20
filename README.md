# SPOTIFY/BILLBOARD DATA ANALYSIS SUMMARY

## Goals

- Obtain a dataset from Spotify with characteristics for the top songs from every Billboard Hot 100 week since 1958
- Analyze the dataset and create visuals
- Find plausible explanations for patterns in the data

## Skills/Tools Used

- Querying the Spotify API
- Cleaning the Billboard dataset
- Incremental, test-driven development in Python
- Data analysis with pivot tables in Excel
- Creating charts in Excel

## Steps
1. Read in lines from the the raw data [csv](modifiedbillboarddata.csv)
2. Clean the raw data to be able to [search](https://developer.spotify.com/documentation/web-api/reference/search) for the [Spotify ID](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of each song 
    - `remove_feature()` and `clean_song_title()` functions
    - log if feature was removed so that data can be tracked
3. Save a list of song ids for each chart week and then [query](https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features) and average data
    - done by `average_attributes()` function
    - list method reduces GET requests from 20/chart week to 11
4. Write row for the week's average values in the output csv (result can be found [here](billboard_data.xlsx))
<br> *More detail can be found in my [Python code](python) documentation.*

## Conclusions

### Since the late 20th century the charts have been dominated by songs featuring multiple popular artists. Recently, this portion has greatly decreased.
![year vs % features](https://github.com/holdenellismain/SpotifyBillboard/assets/175176011/890dd5a1-8af6-41f3-b555-d8ad85ee50b1)
*Average percent of songs with features in the top 10 by year since 1958*
![year vs tiktok   features](https://github.com/holdenellismain/SpotifyBillboard/assets/175176011/2a51ee03-b992-4ce7-8d09-05369275b49f)
*Percent of songs with features in the top 10 for every week since Jan 2018, with a moving 2 week average*

TikTok has allowed for songs without the promotion of big record labels to gain popularity. Small artists without big features have more pull in the charts than ever before.

### Songs were made longer due to CDs and radio but have been getting shorter again
![year vs length](https://github.com/holdenellismain/SpotifyBillboard/assets/175176011/30cd96ff-b0c2-4697-90c7-801069685686)
*average song length by year since 1958*

Songs length used to be hard capped at under 3 minutes by Vinyl records but CDs and radio edits allowed artists to make longer songs and still publish them to a large audience.

### Popular songs have gotten less acoustic
![year vs acousticness](https://github.com/holdenellismain/SpotifyBillboard/assets/175176011/64d57b1e-732c-4f44-90ec-74120eb003a3)
*average acousticness by year since 1958*

Usage of electric instruments and digital production methods have changed the sound of music.

### Christmas Songs affect the charts a lot
![highest weeks on chart](https://github.com/holdenellismain/SpotifyBillboard/assets/175176011/81a1711b-e89b-4134-a425-67ab3b9dbd3b)

The charts are dominated by Christmas music in December and at the start of January in recent years.

## Sources

- Billboard Hot 100 Historical Data - [UT Data](https://github.com/utdata/rwd-billboard-data)
- TikTok Popularity - [Google Trends](https://trends.google.com/trends/explore?date=all&geo=US&q=tiktok&hl=en)
- Individual Billboard Weeks - [Billboard](https://www.billboard.com/charts/hot-100/)
