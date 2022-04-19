#!/usr/bin/python3

# @ashtoncross on github
# if you want this accessable from the terminal, edit ~/.bashrc to include: alias ytadd='python3 /dir/to/ytadd'
                                                                                # you could also chmod +x ytadd and then add ytadd to PATH.

import sys
import os

def main():
    #config stuff:
    newsboat_url = os.path.expanduser('~/.newsboat/urls')           # replace this with your URL file location. It should probably already be this.

    # -------------------------------

    valid_input = True

    try:
        channel_id = ('https://www.youtube.com/feeds/videos.xml?channel_id=' + sys.argv[1])
    except:
        print('Please enter a youtube Channel ID.')
        valid_input = False

    tags = []

    if valid_input:

        for i in range(2, 100, 1):
            try:
                tags.append('"' + sys.argv[i] + '"')
            except:
                break

        tag_output = ''
        for t in tags:
            tag_output += ' ' + t

        try:
            url_file = open(newsboat_url, 'a')
            url_file.write(f'{channel_id} {tag_output} \n')
            url_file.close()
            print(f'Sucessfully added:\n \'{channel_id + tag_output}\'\n            to\n \'{newsboat_url}\'')
        except FileNotFoundError:
            print('Couldn\'t find the specified URL file.')

if __name__ == '__main__':
    main()
