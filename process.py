def process_status(status_dictionary):
    if status_dictionary['status'] == 'active':
        print('Active State')
    elif status_dictionary['status'] == 'inactive':
        print('Inactive State')
    else:
        print('Unknown State')
