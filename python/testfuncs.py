from spotifyfuncs import *

def check_info(title, artist):
    print("When searching for:")
    print(title, " by ", artist)
    print("returned")
    token = get_token()
    header = get_auth_header()
    id = search_for_song(title, artist, header)
    info = info_from_id(id, header)
    print(info[1], " by ", info[0])
    print("--------------------------")

def print_attributes(attributes_list):
    print("List average:")
    minutes = int(int(attributes_list[0]) / 1000 / 60)
    seconds = int(int(attributes_list[0]) / 1000 % 60)
    print(f'Duration: {minutes}:{seconds}')
    print(f"Acousticness: {attributes_list[1]:.2f}")
    print(f"Energy: {attributes_list[2]:.2f}")

def remove_null(arr):
    '''
    helper, removes null values from an array of ids, useful for testing average attributes
    in normal usage, null values are removed by main function
    '''
    # using list comprehension
    return [item for item in arr if item is not None]