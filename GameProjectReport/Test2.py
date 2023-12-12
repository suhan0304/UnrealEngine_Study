from vpython import *
import random

# 씬 생성
scene = canvas()

# 원통의 속성
num_spheres = 100  # 구체의 개수
radius = 1  # 구체의 반지름
cylinder_radius = 5  # 원통의 반지름

# 구체들을 담을 리스트
spheres = []

# 구체들을 랜덤한 위치에 생성
for _ in range(num_spheres):
    sphere_object = sphere(pos=vector(random.uniform(-cylinder_radius, cylinder_radius),
                                      random.uniform(-cylinder_radius, cylinder_radius),
                                      random.uniform(-cylinder_radius, cylinder_radius)),
                           radius=radius, color=color.blue)
    spheres.append(sphere_object)

# 프레임 간격 설정
dt = 0.01

while True:
    rate(100)  # 초당 100회 업데이트

    # 더 이상 이동 코드가 없음 (구체들은 정적으로 고정됨)
