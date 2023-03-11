# Vision_based_LabyrinthGame

연세대학교 로봇동아리 로보인 프로젝트: Labyrinth Game using Vision and RL

### Protocol Prototype

![crc](https://user-images.githubusercontent.com/68832065/224462272-75dc1f4a-ed3d-4447-bb47-38aac84fa0fb.JPG)

### Jetson Config

- I2C 접근 허가

```python
sudo usermod -aG i2c <username>
groupadd -f -r gpio
sudo usermod -a -G gpio <username>
```

- 아두이노 포트 접근 허가

```python
dmesg | grep tty
sudo chmod a+rw /dev/ttyACM0
```

- Docker 사용하는 경우

이미지 빌드
```
docker build -t myimage .
```

i2c 활성화하면서 컨테이너 실행
```
docker run --privileged myimage
```

---
# Contributors

[Seoyeon Choi](https://github.com/n00Nspr1ng), [Minjun Chang](https://github.com/wkdalswns0427), [Namhoon Kim](https://github.com/etoilekim), Seunghyun Roh, Jiyoung Chae
![image](https://user-images.githubusercontent.com/97090402/222885665-9824e687-1dd2-46f7-aefa-0ac921711ab8.png)
