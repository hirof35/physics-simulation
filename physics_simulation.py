import pybullet as p
import pybullet_data
import time
import random

# 1. 物理エンジンの初期化
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

# 地面
p.loadURDF("plane.urdf")

# 2. 100個の物体を生成
box_ids = []
for i in range(100):
    # ランダムな位置 (x, y, z)
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    z = 2 + i * 0.5  # 縦に長く並べる
    
    # ランダムな色を設定するために、まずは箱をロード
    obj_id = p.loadURDF("cube.urdf", [x, y, z], globalScaling=0.3)
    
    # 見た目をカラフルにする
    color = [random.random(), random.random(), random.random(), 1]
    p.changeVisualShape(obj_id, -1, rgbaColor=color)
    
    box_ids.append(obj_id)

print("シミュレーション開始！")
print("Ctrl + マウスドラッグでカオスに拍車をかけられます。")

# 3. 実行ループ
while True:
    p.stepSimulation()
    time.sleep(1./240.)
