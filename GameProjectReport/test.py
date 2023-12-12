from vpython import *
import math
import random
from tqdm import tqdm

# 그래픽 화면 생성
scene = canvas(title="Colored Spheres Tightly Filling a Cylinder", width=800, height=400)

# 구체들의 초기 설정
num_spheres = 200  # 구체의 갯수
cylinder_radius = 2  # 작은 반지름으로 조절
cylinder_length = 5  # 짧은 길이로 조절
sphere_radius = 0.2  # 구체의 반지름

# 구체 간의 최소 거리 (구체들이 겹치지 않게 배치하기 위한 최소 간격)
min_distance = 0.99 * sphere_radius

# 각 색상별로 구체를 저장하는 리스트 초기화
red_spheres = []
purple_spheres = []
black_spheres = []

# 각 색상별 구체의 갯수를 저장하는 변수 초기화
red_count = 0
purple_count = 0
black_count = 0

for i in tqdm(range(num_spheres), desc="Generating Spheres", unit="sphere"):
    # 구체의 중심 좌표 계산
    while True:
        theta = 2 * math.pi * random.uniform(0, 1)
        phi = math.pi * random.uniform(0, 1)
        
        x = cylinder_radius * math.sin(phi) * math.cos(theta)
        y = cylinder_radius * math.sin(phi) * math.sin(theta)
        z = cylinder_length * random.uniform(0, 1)
        
        # 구체 간의 거리 체크
        is_valid = all(mag(vector(x, y, z) - s.pos) < min_distance for s in red_spheres + purple_spheres + black_spheres)
        if is_valid:
            break
    
    # 랜덤하게 색상 선택
    sphere_color = random.choice([color.red, color.purple, color.black])
    
    # 각 색상별로 구체를 저장하는 리스트에 추가
    if sphere_color == color.red:
        red_spheres.append(sphere(pos=vector(x, y, z), radius=sphere_radius, color=sphere_color))
        red_count += 1
    elif sphere_color == color.purple:
        purple_spheres.append(sphere(pos=vector(x, y, z), radius=sphere_radius, color=sphere_color))
        purple_count += 1
    elif sphere_color == color.black:
        black_spheres.append(sphere(pos=vector(x, y, z), radius=sphere_radius, color=sphere_color))
        black_count += 1

    # 각 구체 갯수 출력
    print(f"Red Count: {red_count}, Purple Count: {purple_count}, Black Count: {black_count}")

