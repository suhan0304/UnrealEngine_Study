from vpython import *
import random

# 씬 설정
scene = canvas()

# 원기둥의 속성 정의
cylinder_radius = 1  # 원기둥의 반지름
cylinder_height = 3  # 원기둥의 높이

# 구체의 속성 정의
sphere_radius = 0.05  # 구체의 반지름

# 원기둥 공간을 정의
cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, cylinder_height), radius=cylinder_radius, opacity=0.3)

# 구체를 최대한 배치하여 원기둥 공간 채우기
num_spheres = 0
max_spheres = 500

while num_spheres < max_spheres:
    x = random.uniform(-cylinder_radius, cylinder_radius)
    y = random.uniform(-cylinder_radius, cylinder_radius)
    z = random.uniform(0, cylinder_height)

    # 원기둥 내부에 있는지 확인
    if x**2 + y**2 <= cylinder_radius**2:
        # 구체 생성
        sphere(pos=vector(x, y, z), radius=sphere_radius, color=color.blue)
        num_spheres += 1

    rate(100)  # 배치 속도를 적절히 조절
