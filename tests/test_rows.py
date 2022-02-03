"""Row values for the testing the fake db."""

row_1 = {'p_id': 14, 'first_name': 'lke', 'height_feet': 0, 'height_inches': 0,
         'last_name': 'Anigbogu', 'position': 'C', 'weight_pounds': 0, 'id': 12,
         'abbreviation': 'IND', 'city': 'Indiana', 'conference': 'East',
         'division': 'Central', 'full_name': 'Indiana Pacers', 'name': 'Pacers'}    # delete

row_2 = {'p_id': 15, 'first_name': 'Hiya', 'height_feet': 7.8, 'height_inches': 9.8,
         'last_name': 'Anig', 'position': 'A', 'weight_pounds': 67, 'id': 19,
         'abbreviation': 'BOS', 'city': 'Boston', 'conference': 'West',
         'division': 'Atlantic', 'full_name': 'Boston Acers', 'name': 'Acers'}

row_3 = {'p_id': 67, 'first_name': 'Hina', 'height_feet': 98, 'height_inches': 24,
         'last_name': 'Knicks', 'position': 'C', 'weight_pounds': 454, 'id': 89,
         'abbreviation': 'NYK', 'city': 'Newyork', 'conference': 'East',
         'division': 'Atlantic', 'full_name': 'Newyork Knicks', 'name': 'Knicks'}

row_4 = {'p_id': 34, 'first_name': 'Piya', 'height_feet': 9.6, 'height_inches': 567,
         'last_name': 'Brown', 'position': 'B', 'weight_pounds': 65, 'id': 2,
         'abbreviation': 'TOR', 'city': 'Torronto', 'conference': 'West',
         'division': 'Pacific', 'full_name': 'Torronto Piston', 'name': 'Piston'}   # delete

row_5 = {'p_id': 15, 'first_name': 'David', 'height_feet': 7.8, 'height_inches': 9.8,
         'last_name': 'Brown', 'position': 'A', 'weight_pounds': 688, 'id': 98,
         'abbreviation': 'BOS', 'city': 'Boston', 'conference': 'West',
         'division': 'Southwest', 'full_name': 'Boston Acers', 'name': 'Thunder'}   # error

row_6 = {'p_id': 78, 'first_name': '', 'height_feet': 0, 'height_inches': 9.8,
         'last_name': 'Anig', 'position': 'A', 'weight_pounds': 67, 'id': 19,
         'abbreviation': 'BOS', 'city': 'Boston', 'conference': '',
         'division': '', 'full_name': 'Boston Acers', 'name': 'Acers'}

row_7 = {'p_id': '[89]', 'first_name': 'gdg', 'height_feet': 0, 'height_inches': 9.8,
         'last_name': 'Anig', 'position': 'A', 'weight_pounds': 87, 'id': 19,
         'abbreviation': 'BOS', 'city': 'Boston', 'conference': '',
         'division': 'Atlantic', 'full_name': {'key': 78}, 'name': 'Brown'}     # error

row_8 = {'p_id': 89, 'first_name': 'bjh', 'height_feet': 98, 'height_inches': 5.7,
         'last_name': 'bug', 'position': 'U', 'weight_pounds': 878, 'id': [14],
         'abbreviation': 'BOS', 'city': 'Boston', 'conference': 'West',
         'division': 'Atlantic', 'full_name': 'Peter York', 'name': 'York'}     # error

row_9 = {'p_id': 5, 'first_name': 'uyty', 'height_feet': 3.4, 'height_inches': 23,
         'last_name': 'buy', 'position': 'A', 'weight_pounds': 87, 'id': 19,
         'abbreviation': 'CAL', 'city': 'California', 'conference': 'East',
         'division': 'Southwest', 'full_name': 'Hello Peter', 'name': 'Peter'}

row_10 = {'p_id': 90, 'first_name': 'nui', 'height_feet': {'hello': 'fyt'}, 'height_inches': 678,
          'last_name': 'buy', 'position': 'A', 'weight_pounds': 34, 'id': 34,
          'abbreviation': 'TOR', 'city': 'Torronto', 'conference': 'East',
          'division': 'west', 'full_name': 'iuyui', 'name': 'Brown'}     # error

row_0 = {'p_id': 90, 'first_name': 'gdg', 'height_feet': 67, 'height_inches': 224,
          'last_name': 'ytfy', 'position': 'H', 'weight_pounds': 576, 'id': 78,
          'abbreviation': 'BOS', 'city': 'Boston', 'conference': 'West',
          'division': 'Atlantic', 'full_name': 'buyu', 'name': 'vuygu'}

# row_12 = {'p_id': 2, 'first_name': 'uyu', 'height_feet': 67, 'height_inches': 224,
#           'last_name': 'biui', 'position': 'H', 'weight_pounds': 576, 'id': 78,
#           'abbreviation': 'BOS', 'city': 'Boston', 'conference': 'West',
#           'division': 'Atlantic', 'full_name': 'buyu', 'name': 'vuygu'}
