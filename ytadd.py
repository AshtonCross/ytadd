#!/usr/bin/python3

# @kashermash on github

import sys
import os

#config stuff:
newsboat_url = os.path.expanduser('~/.newsboat/urls')           # replace this with your URL file location. It should probably already be this.

# -------------------------------

try:
    mode = sys.argv[1]
except:
    mode = None

if mode == 'help':
    pass
if mode == 'tags':
    pass
else:
    # Add mode

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
