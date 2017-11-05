def unmarshall(db_object):

    return {
        "name": db_object.get_name(),
        "age": db_object.get_age()
}