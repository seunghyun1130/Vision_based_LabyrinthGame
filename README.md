# Vision_based_LabyrinthGame

연세대학교 로봇동아리 로보인 프로젝트: Labyrinth Game using Vision and RL

### Protocol Prototype

Movement

```shell
[0x02, 0x00, 0x01, 0x00, 0x00, 0xff, 0xff, 0x03]
[init, seq_h, seq_l, dir, ang, crc_h, crc_l, end]
```

CRC는 추후 업데이트 예정

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
  
    
# Contributors
Seoyeon Choi, Minjun Chang, Namhoon Kim, Seunghyun Roh, Jiyoung Chae
![image](https://user-images.githubusercontent.com/97090402/222885665-9824e687-1dd2-46f7-aefa-0ac921711ab8.png)
