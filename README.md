# Vision_based_LabyrinthGame

연세대학교 로봇동아리 로보인 프로젝트: Labyrinth Game using Vision and RL

### Protocol Prototype

![화면 캡처 2023-03-06 100506](https://user-images.githubusercontent.com/68832065/222997593-82f98321-64cb-4c79-92d4-accc78657ce7.png)

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

---
# Contributors

[Seoyeon Choi](https://github.com/n00Nspr1ng), [Minjun Chang](https://github.com/wkdalswns0427), Namhoon Kim, Seunghyun Roh, Jiyoung Chae
![image](https://user-images.githubusercontent.com/97090402/222885665-9824e687-1dd2-46f7-aefa-0ac921711ab8.png)
