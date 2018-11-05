

def validate_query_data(query_latitude, query_longitude, query_radius):
    validate_context = {
        'status': True,
        'error': ''
    }

    if query_latitude and query_longitude and query_radius:

        if query_latitude:
            try:
                query_latitude = float(query_latitude)
                if query_latitude < -90 or query_latitude >90 :
                    validate_context['status'] = False
                    validate_context['error'] = 'Latitude should be in between -90 and 90'
                    return validate_context
            except Exception as e:
                print(e)
                validate_context['status'] = False
                validate_context['error'] = 'Latitude should be in between -90 and 90'
                return validate_context

        if query_longitude:
            try:
                query_longitude = float(query_longitude)
                if query_longitude < -180 or query_longitude >180:
                    validate_context['status'] = False
                    validate_context['error'] = 'Longitude should be between -180 and 180'
                    return validate_context
            except Exception as e:
                print(e)
                validate_context['status'] = False
                validate_context['error'] = 'Longitude should be between -180 and 180'
                return validate_context

        if query_radius:
            try:
                query_radius = float(query_radius)
                if query_radius < 0:
                    validate_context['status'] = False
                    validate_context['error'] = 'Radius should be greater than or equal to zero'
                    return validate_context
            except Exception as e:
                validate_context['status'] = False
                validate_context['error'] = 'Radius should be greater than or equal to zero'
                return validate_context
        return validate_context
    validate_context['status'] = False
    validate_context['error'] = 'Missing Parameters'
    return validate_context
