import cv2
from ultralytics import YOLO
import numpy as np
# 加载 YOLO 姿势识别模型
model = YOLO('yolo11n-pose.pt')

# 定义关键点名称
keypoint_names = [
    "Nose", "Left Eye", "Right Eye", "Left Ear", "Right Ear",
    "Left Shoulder", "Right Shoulder", "Left Elbow", "Right Elbow",
    "Left Wrist", "Right Wrist", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle"
]

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    if not ret:
        break

    # 使用模型进行姿势识别
    results = model(frame)

    # 获取姿势检测结果
    if results:  # 检查 results 列表是否为空
        try:
            keypoints = results[0].keypoints.cpu().numpy()
        except AttributeError:
            print("模型输出中没有 keypoints 属性。")
            continue
    else:
        print("未检测到任何目标。")
        continue

    # 可视化预测结果
    annotated_frame = results[0].plot()

    # 提取实际检测到的关键点的 xy 坐标和连线信息
    # 移除获取 skeleton 信息的代码
    # if len(keypoints) > 0:
    #     actual_keypoints = keypoints[0]  # 假设只有一个人被检测到
    #     actual_skeleton = results[0].keypoints.skeleton
    
    # 创建一个与当前帧相同大小的空图像
    empty_frame = np.zeros_like(frame)
    kp_index=0
    # 绘制实际检测到的关键点
    if len(keypoints) > 0:
        actual_keypoints = keypoints[0]  # 假设只有一个人被检测到
        for keypoint in actual_keypoints:
            # 检查 keypoint 的长度是否为 3
            if len(keypoint) == 1:
                # 修改为从第 1、2、3 列获取 x, y, visibility
                x = keypoint.data[0][kp_index][0]
                y = keypoint.data[0][kp_index][1]
                visibility = keypoint.data[0][kp_index][2]
                kp_index+=1
                if visibility > 0.1:  # 仅绘制可见的关键点
                   cv2.circle(empty_frame, (int(x), int(y)), 5, (0, 0, 255), -1)  # 绘制关键点
                   cv2.imshow('Pose Detection', empty_frame)
            else:
                print(f"Invalid keypoint format: {keypoint}")
    
    # 移除绘制连线的代码
    # for connection in actual_skeleton:
    #     start_idx, end_idx = connection
    #     start_point = actual_keypoints[start_idx]
    #     end_point = actual_keypoints[end_idx]
    #     if start_point[2] > 0 and end_point[2] > 0:  # 仅绘制两个关键点都可见的连线
    #         cv2.line(empty_frame, (int(start_point[0]), int(start_point[1])), (int(end_point[0]), int(end_point[1])), (0, 0, 255), 2)


    # 水平拼接当前帧和空图像
    combined_frame = np.hstack((annotated_frame, empty_frame))

    # 在窗口中显示拼接后的帧
    cv2.imshow('Pose Detection', combined_frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()