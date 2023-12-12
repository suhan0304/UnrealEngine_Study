from vpython import *
import random
import time

# 씬 설정
scene = canvas()

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

# 구체를 최대한 배치하여 원기둥 공간 채우기
num_spheres = 0
max_spheres = 500

while num_spheres < max_spheres:
    x = random.uniform(-cylinder_radius, cylinder_radius)
    y = random.uniform(-cylinder_radius, cylinder_radius)
    z = random.uniform(0, cylinder_height)

    # 원기둥 내부에 있는지 확인
    if x**2 + y**2 <= cylinder_radius**2:
        # 현재 위치에서 다른 구체들과 겹치지 않는지 확인
        overlap = False
        for obj in scene.objects:
            if isinstance(obj, sphere) and mag(vector(x, y, z) - obj.pos) < (sphere_radius + obj.radius):
                overlap = True
                break

        # 겹치지 않는 경우에만 구체 생성
        if not overlap:
            # 랜덤하게 색상 선택
            random_color = random.choice([color.red, color.purple, color.black])
            sphere(pos=vector(x, y, z), radius=sphere_radius, color=random_color)
            num_spheres += 1

            # 현재 생성된 구체 갯수 레이블 업데이트
            update_counts()

    rate(100)  # 배치 속도를 적절히 조절

    # 모든 구체를 생성했으면 종료
    if num_spheres >= max_spheres:
        print("Finished creating spheres on the cylinder.")
        break

# 초기 카메라 위치로 되돌리기
# scene.camera.pos = vector(0, -1, 1)
# scene.camera.axis = vector(0, 0.5, -0.5)

# 원기둥에서 일정 거리에 떨어진 위치에 초록 구체 생성
green_sphere_distance = 1.5  # 원기둥에서 떨어진 거리
green_sphere = sphere(pos=cylinder.pos + vector(0, 0, green_sphere_distance),
                      radius=sphere_radius, color=color.green)
print("Green sphere created at a distance from the cylinder.")
