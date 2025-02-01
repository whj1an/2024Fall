def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE
    users_number = int(friends[0].strip()) #NUMBER OF USERS
    connections = [] #缓存
    for line in friends[1:]:
        line_split = line.split()
        user_u = int(line_split[0])
        user_v = int(line_split[1])
        connections.append((user_u, user_v))
    #sort
    connections.sort()

    for user in range(users_number):
        friends_list = []
        for u, v in connections:
            if u == user:
                friends_list.append(v)
            elif v == user:
                friends_list.append(u)
        if friends_list:
            network.append((user, friends_list))
    return network
