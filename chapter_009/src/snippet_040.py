import dropbox


def dropbox_connect() -> dropbox.dropbox_client.Dropbox:
    """
    This function connects to Dropbox and returns the API connection
    :return:    a connection to the Dropbox API
    """
    try:
        dbx = dropbox.Dropbox("<your access key>")
    except AuthError as e:
        print("Error connecting to Dropbox with access token: " + str(e))
    return dbx


if __name__ == "__main__":

    # set up connection
    dbx: dropbox.dropbox_client.Dropbox = dropbox_connect()
    print(dbx)
