def tranform_response(responses, response_id):
    transformed_response = {
        "response_id": response_id
    }

    for response in responses:
        transformed_response[response.field_name] = response.value
    
    return transformed_response