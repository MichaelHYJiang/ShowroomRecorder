#!/usr/bin/env python

# ----------------------------------------------------------------
# Showroom Stream Downloader
# Written by Michael
# April 20th 2021
# ----------------------------------------------------------------

import os
import time
import argparse

UG_TEMP = 'you-get_info_temp'


# parsing m3u8 link from room URL using you-get
def get_m3u8_url(room_url):
    try:
        os.system('you-get -u ' + room_url + ' > ' + UG_TEMP)
    except KeyboardInterrupt:
        pass
    
    with open(UG_TEMP, 'r', encoding='utf-8') as f:
        for line in f:
            if 'https' in line and 'm3u8' in line:
                return line.strip()[2:-2]  # result contains square brackets and quotes
    return None


# generate formatted time as recored file prefix
def get_time():
    t0 = time.localtime()
    time_stamp = '{:04d}-{:02d}-{:02d}_{:02d}-{:02d}-{:02d}'.format(t0.tm_year, t0.tm_mon, t0.tm_mday, t0.tm_hour, t0.tm_min, t0.tm_sec)
    return time_stamp


def parse_arguments():
    parser = argparse.ArgumentParser(description='Record live stream from Showroom.')
    parser.add_argument('--url', '-U', type=str, default='https://www.showroom-live.com/tsukishiro_chiya ',
                        help='Specify room URL (Default is \"https://www.showroom-live.com/tsukishiro_chiya\").')
    parser.add_argument('--name', '-N', type=str, default='Chiya',
                        help='Specify suffix name of the recored file (Default is \"Chiya\").')
    parser.add_argument('--version', '-V', action='version', version='Showroom Recorder v0.1')

    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    
    url = args.url
    
    print('Parsing webpage, acquiring m3u8 playlist link... (If live is not on, press \"Ctrl + C\" to exit.)')
    url = get_m3u8_url(url)
    if url is None:
        print('Live stream not found.')
        return
    print('Found:', url)
    
    live_name = args.name
    filename = get_time() + '_' + live_name + '.mp4'
    
    try:
        os.system('ffmpeg -i {}  -c copy -bsf:a aac_adtstoasc {}'.format(url, filename))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
