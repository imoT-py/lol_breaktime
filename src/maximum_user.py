# get the maximum user number in a match
def maximum_user(data):
    
    print("maximum user")
    max_user = 0

    while True:
        try:
            puuid = data['info']['participants'][max_user]['puuid']
            max_user += 1
        
        except IndexError:
            break
        
    return max_user