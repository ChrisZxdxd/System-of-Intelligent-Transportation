import cv2
import mediapipe as mp
import time
import gc


def init():
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    th, tn = 0, 0

    return th, tn, pose


def distinguish(pose, cap):
    success, img = cap.read()  # 获取画面
    # 点位检测
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    return results

def work(cap1, cap2):
    th, tn, pose = init()

    while True:
        results1 = distinguish(pose, cap1)  # 开始识别
        results2 = distinguish(pose, cap2)  # 开始识别

        if results1.pose_landmarks or results2.pose_landmarks:
            if th < 10:
                th = th + 1
                print('检测到人员停留%d秒' % th)
                time.sleep(0.9)
                tn = 0  # 无人时间归零
            if th >= 10:
                print('开放绿灯！')
                th = 0  # 时间重置
                return 1
        else:
            tn = tn + 1
            time.sleep(0.9)
            if tn >= 6:
                th, tn = 0, 0
                print('6秒内无人，检测时间重置！')
                time.sleep(0.9)

        del results2, results1
        if ord('q') == cv2.waitKey(10):
            return 2

        gc.collect()

def main(cap1, cap2):
    th, tn, pose = init()

    while True:
        success, img1 = cap1.read()  # 获取画面
        results1 = distinguish(pose, img1)  # 开始识别

        success, img2 = cap2.read()  # 获取画面
        results2 = distinguish(pose, img2)  # 开始识别

        if results1.pose_landmarks or results2.pose_landmarks:
            if th < 10:
                th = th+1
                print('检测到人员停留%d秒' % th)
                time.sleep(1)
                tn = 0  # 无人时间归零
            if th >= 10:
                print('开放绿灯！')
                th = 0  # 时间重置
        else:
            tn = tn + 2
            time.sleep(2)
            if tn >= 6:
                th = 0
                tn = 0
                print('6秒内无人，检测时间重置！')
                time.sleep(2)

        del img1, results1
        del img2, results2
        if ord('q') == cv2.waitKey(10):
            break

        gc.collect()




if __name__ == '__main__':
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    main(cap1, cap2)

