def ViewProfile():

    with open('Collection.txt','r') as file_in:
        content = file_in.readlines()

    from login import browser

    for i in content:
        browser.get(i)

if __name__ == '__main__':
    ViewProfile


