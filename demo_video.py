import sys
sys.path.append('.')
import shutil
from multi_person_tracker import MPT
from multi_person_tracker.data import video_to_images
import os
import glob


def main():
    directory = os.getcwd() + "/videos/"
    files = glob.glob(directory + "*.mp4")

    f = open("report.txt", "w+")

    for fn in files :
        report_local = submain(fn)
        print('file : {} | humans " {}'.format(fn, report_local))
        f.write(report_local)
        f.flush()

    f.close


def submain(vf):
    image_folder = video_to_images(vf)
    mot = MPT(
        display=False,
        detector_type='yolo',  # 'maskrcnn'``
        batch_size=10,
        detection_threshold=0.7,
        yolo_img_size=416,
        output_format="dict"
    )

    #result = mot(image_folder, output_file='sample.mp4')
    result = mot(image_folder, output_file=None)

    shutil.rmtree(image_folder)

    return f'filename {vf} | humans recognized {len(result)}'


if __name__ == '__main__':
    main()

