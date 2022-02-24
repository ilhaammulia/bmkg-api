import bmkg_api
import time


def save_log(data):
    """
    Save response from url to log
    """
    file = open('log.txt', 'a+')
    file.write(data + '\n')
    file.close()

def main():
    """
    Main program to run the request
    """
    response = bmkg_api.Api().request(0)
    if response != None:
        check_log = open('log.txt', 'r').read().splitlines()
        date_time = response['Infogempa']['gempa']['DateTime']
        if date_time in check_log:
            pass
        else:
            save_log(date_time)
            print(response)
    else:
        pass
        

if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
