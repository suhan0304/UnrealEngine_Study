from vpython import *
import random

# 씬 생성
scene = canvas()

# 구체 생성
sphere_object = sphere(pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)),
                       radius=1, color=color.blue)

# 랜덤한 속도 생성
velocity = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))

# 프레임 간격 설정
dt = 0.01

while True:
    rate(100)  # 초당 100회 업데이트

    # 현재 위치에 속도를 더함
    sphere_object.pos += velocity * dt

    # 벽에 닿았을 경우 속도를 반전
    if abs(sphere_object.pos.x) > 5:
        velocity.x *= -1
    if abs(sphere_object.pos.y) > 5:
        velocity.y *= -1
    if abs(sphere_object.pos.z) > 5:
        velocity.z *= -1
