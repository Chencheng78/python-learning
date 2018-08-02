import os
import subprocess

'''
Usage: cut a video stream into several short slices. 
Parameters:
    number : define how many slices you want to generate.
    start_time: define where the video start to cut.(seconds)
    step: define the steps between every slices.(seconds)
    duration: the length of every slices (seconds)
E.g.
    'cut(2, 1, 5, 20, 'miya.mkv', 'test.mp4')' will generate 2 slices which last 20s from 'miya.mkv'.
    the first slice starts at 1s, and the second starts at 6s.
'''


def cut(number, start_time, step, duration, input_file, output_file):
    for i in range(number):
        output_split = output_file.split('.')
        output_split[0] = output_split[0] + '_' + str(i)
        output = '.'.join(output_split)
        cmd = 'ffmpeg.exe -ss %i -t %i -accurate_seek -i %s -codec copy %s' % (start_time, duration, input_file, output)
        print cmd
        a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = a.stdout.read()
        print line
        start_time += step

if __name__ == '__main__':
    os.chdir('K:\\ffmpeg-20180319-e5b4cd4-win64-static\\bin')
    cut(2, 1, 5, 20, 'miya.mkv', 'test.mp4')
