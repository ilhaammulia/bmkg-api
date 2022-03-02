import bmkg_api
import time


def main():
    """
    Main program to run the request
    """
    response = bmkg_api.Api().request(0)
    temp_resp = []
    if response != None:
        date_time = response['Infogempa']['gempa']['DateTime']
        if date_time in temp_resp: pass
        else:
            temp_resp.clear()
            temp_resp.append(date_time)
            print(response)
    else: pass
        

if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
