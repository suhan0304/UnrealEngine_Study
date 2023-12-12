from vpython import *
import math

# 씬 생성
scene = canvas()

# 원기둥의 속성
num_spheres = 1000  # 구체의 개수
radius = 0.1  # 구체의 반지름
cylinder_radius = 5  # 원기둥의 반지름
cylinder_height = 10  # 원기둥의 높이

# 구체들을 담을 리스트
spheres = []

# 각도에 따른 원기둥 표면상의 점을 생성하고 그 위치에 구체를 배치
for i in range(num_spheres):
    theta = i * (2 * pi / num_spheres)
    x = cylinder_radius * math.cos(theta)
    y = cylinder_radius * math.sin(theta)
    z = cylinder_height * (i / num_spheres) - cylinder_height / 2
    sphere_object = sphere(pos=vector(x, y, z), radius=radius, color=color.blue)
    spheres.append(sphere_object)
