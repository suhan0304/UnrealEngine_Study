from vpython import *

# 씬 설정
scene = canvas()

# 원기둥의 속성 정의
num_layers = 10  # 전선의 높이를 구성하는 구체의 층 수
num_beads_per_layer = 20  # 각 층당 구체의 수
radius = 1  # 전선의 반지름

# 구체들을 원기둥 표면에 채워 넣어 전선 생성
for i in range(num_layers):
    layer_theta = 2 * pi / num_beads_per_layer

    for j in range(num_beads_per_layer):
        theta = j * layer_theta
        x = radius * cos(theta)
        y = radius * sin(theta)
        z = i * (2 * radius / num_layers) - radius  # 높이를 조절하여 원기둥 표면에 배치

        # 구체 생성
        bead = sphere(pos=vector(x, y, z), radius=0.05, color=color.blue)

# VPython 루프 시작
while True:
    rate(60)
