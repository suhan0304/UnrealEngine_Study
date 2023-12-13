from vpython import *
import random
import time

# 씬 설정
scene = canvas(width=800, height=600)  # 원하는 크기로 지정

# 원기둥의 속성 정의
cylinder_radius = 0.5  # 원기둥의 반지름
cylinder_height = 2  # 원기둥의 높이

# 구체의 속성 정의
sphere_radius = 0.05  # 구체의 반지름

# 원기둥 공간을 정의
cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, cylinder_height), radius=cylinder_radius, opacity=0.3)

# 사용자가 확인할 색상별 구체 개수 초기화
num_red_spheres = 0
num_purple_spheres = 0
num_black_spheres = 0

# 사용자가 설정할 초기 비율
initial_red_ratio = 0.4  # 빨강 구체 비율
initial_purple_ratio = 0.4  # 보라 구체 비율
initial_black_ratio = 0.2  # 검정 구체 비율

# 초기 비율에 따라 생성할 구체의 총 개수
total_spheres = 500

# 사용자가 확인할 색상별 구체 개수 업데이트 함수
def update_counts():
    global num_red_spheres, num_purple_spheres, num_black_spheres
    num_red_spheres = 0
    num_purple_spheres = 0
    num_black_spheres = 0

    for obj in scene.objects:
        if isinstance(obj, sphere):
            if obj.color == color.red:
                num_red_spheres += 1
            elif obj.color == color.purple:
                num_purple_spheres += 1
            elif obj.color == color.black:
                num_black_spheres += 1

    # 화면에 출력할 label 업데이트
    label_text.text = f"Si (Red): {num_red_spheres}\nC (Purple): {num_purple_spheres}\nO (Black): {num_black_spheres}"

# 화면에 출력할 label 생성
label_text = label(pos=vector(0, -cylinder_radius, cylinder_height), text="Si (Red): 0\nC (Purple): 0\nO (Black): 0", height=15)

# 초기 카메라 위치 및 방향 조정
scene.camera.pos = vector(0, 0, 0)
scene.camera.axis = vector(1, 0, 0)  # X 축 방향으로 조정

# 초기 비율에 따라 구체를 최대한 배치하여 원기둥 공간 채우기
num_spheres = 0

for _ in range(int(total_spheres * initial_red_ratio)):
    x = random.uniform(-cylinder_radius, cylinder_radius)
    y = random.uniform(-cylinder_radius, cylinder_radius)
    z = random.uniform(0, cylinder_height)

    # 원기둥 내부에 있는지 확인
    if x**2 + y**2 <= cylinder_radius**2:
        sphere(pos=vector(x, y, z), radius=sphere_radius, color=color.red)
        num_spheres += 1

for _ in range(int(total_spheres * initial_purple_ratio)):
    x = random.uniform(-cylinder_radius, cylinder_radius)
    y = random.uniform(-cylinder_radius, cylinder_radius)
    z = random.uniform(0, cylinder_height)

    # 원기둥 내부에 있는지 확인
    if x**2 + y**2 <= cylinder_radius**2:
        sphere(pos=vector(x, y, z), radius=sphere_radius, color=color.purple)
        num_spheres += 1

for _ in range(int(total_spheres * initial_black_ratio)):
    x = random.uniform(-cylinder_radius, cylinder_radius)
    y = random.uniform(-cylinder_radius, cylinder_radius)
    z = random.uniform(0, cylinder_height)

    # 원기둥 내부에 있는지 확인
    if x**2 + y**2 <= cylinder_radius**2:
        sphere(pos=vector(x, y, z), radius=sphere_radius, color=color.black)
        num_spheres += 1

# 현재 생성된 구체 갯수 레이블 업데이트
update_counts()

# 화면 업데이트
scene.autoscale = False
scene.center = vector(0, 0, cylinder_height / 2)  # 원기둥이 중앙에 오도록 조정

# 자동으로 업데이트
update_interval = 5  # 초 단위 간격으로 업데이트
next_update_time = time.time() + update_interval

while True:
    if time.time() >= next_update_time:
        # 사용자가 확인할 색상별 구체 개수 업데이트
        update_counts()
        # 다음 업데이트 시간 설정
        next_update_time = time.time() + update_interval

        # 모든 구체를 생성했으면 종료
        if num_spheres >= total_spheres:
            print("Finished creating spheres on the cylinder.")
            break

    rate(1)  # 낮은 속도로 루프를 돌면서 대기
