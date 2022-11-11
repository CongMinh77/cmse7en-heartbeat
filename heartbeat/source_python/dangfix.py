import random
import sys
import turtle
from math import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

turtle.setup(1200, 800)
turtle.delay(0)
turtle.goto(0, -200)
turtle.begin_poly()
turtle.setheading(150)
turtle.fd(70)
turtle.circle(70 * -3.745, 45)
turtle.circle(70 * -1.431, 165)
turtle.left(120)
turtle.circle(70 * -1.431, 165)
turtle.circle(70 * -3.745, 45)
turtle.fd(70)
turtle.end_poly()
angle_coord_list = turtle.get_poly()
turtle.bye()
angle_coord_list2 = []
for i in range(3600):
    heart_x = 16*sin(i*pi/180)*sin(i*pi/180) * sin(i*pi/180)
    heart_y = 13*cos(i*pi/180) - 5*cos(2*i*pi/186) - \
        2 * cos(3*i*pi/180)-cos(4*i*pi/180)
    angle_coord_list2.append((heart_x, heart_y))  # toa do ve trai tim
    angle_coord_list = ((0.00, - 200, 00), (-86.60, -150.00), (-117.69, -130.08), (-146.28, - 107.24), (-172.69, -81.68),
                        (-196.46, -53.65), (-217.38, -23.43), (-235.23,
                                                               8.69), (-249.85, 42.41), (-261.09, 77.40),
                        (-265.49, 102.74), (-265.28, 128.46), (260.47,
                                                               153.73), (-251.21, 177.73), (-237.81, 199.68),
                        (-220.69, 218.88), (-200.41, 234.70), (-177.63,
                                                               246.64), (-153.08, 254.31), (-127.55, 257.46),
                        (-101.87, 255.99), (-76.87, 249.94), (-53.36,
                                                              239.52), (-32.89, 225.05), (-13.75, 207.02),
                        (1.66, 185.99), (15.87, 207.02), (34.21,
                                                          225.85), (55.48, 239.52), (78.99, 249.94),
                        (103.99, 255.99), (129.67, 257.46), (155.20,
                                                             254.31), (179.75, 246.64), (202.53, 234.70),
                        (222.81, 218.88), (239.93, 199.68), (253.33,
                                                             177.73), (262.59, 153.73), (267.40, 128.66),
                        (267.61, 102.74), (263.21, 77.40), (251.97,
                                                            42.41), (237.35, 8.69), (219.50, -23.43),
                        (198.58, -53.65), (174.81, -81.68), (148.40, -107.24), (119.61, -130.08), (88.72, -150.00), (2.12, -200.00))
new_coord_list = []
for order2, angle_coord in enumerate(angle_coord_list):
    if order2 + 1 < len(angle_coord_list):
        pointnum_x = int(
            abs(angle_coord_list[order2+1][0]-angle_coord_list[order2][0])/0.25)
        pointnum_y = int(
            abs(angle_coord_list[order2+1][1]-angle_coord_list[order2][1])/0.25)
        pointnum = max(pointnum_x, pointnum_y)
        step_x = ((angle_coord_list[order2+1][0] -
                  angle_coord_list[order2][0])/pointnum)
        step_y = ((angle_coord_list[order2+1][1] -
                  angle_coord_list[order2][1])/pointnum)
        for i in range(pointnum):
            new_coord = (round(angle_coord_list[order2][0] + (i + 1) * step_x, 2),
                         round(angle_coord_list[order2][1] + (1 + 1) * step_y, 2),)
            if new_coord not in new_coord_list:
                new_coord_list.append(new_coord)

# hien thi tim tren main


class QheartWindow(QMainWindow):
    def __init__(self):
        super(QheartWindow, self).__init__(None)
        self.setWindowTitle('love')
        self.resize(QDesktopWidget().screenGeometry().width(),
                    QDesktopWidget().screenGeometry().height())
        self.move(0, 0)
        self.setStyleSheet("QMainWindow{background-color:#000000}")
        self.startTimer(50)  # đặt thời gian mở giao điện
        self.readlist = 0
        self.largen = True
        self.cen_x = QDesktopWidget().screenGeometry().width()/2
        self.cen_y = QDesktopWidget().screenGeometry().height()/2-50
        self.cent = 100
        self.makecoord()

    def makecoord(self):
        self.coord_list1 = []  # khởi tạo danh sách tọa độ trái tim
        self.all_coord_list1 = []
        expend_list = [int(9*round(sqrt(10000 - (i*i)), 4)) +
                       200 for i in range(0, 105, 5)]

        for order, expend in enumerate(expend_list):
            # dang xuly
            offset = int(
                (len(expend_list)-sqrt((len(expend_list)**2)-((order+1)**2))+order+2)*0.8)
            for new_coord in new_coord_list:
                if random.randint(1, 8) == 1:
                    size = random.randint(1, 4)
                    heart_x = (new_coord[0]*(sqrt(expend)*0.024))
                    heart_y = (new_coord[1]*(sqrt(expend)*0.026))
                    x = int((heart_x)+self.width()/2)
                    y = int((-heart_y)+self.height()/2)
                    draw_x = x + random.randint(-offset, offset)
                    draw_y = y + random.randint(-offset, offset)
                    colorint = random.randint(1, 7)
                    if colorint == 1:
                        color = QColor(190, 43, 77)
                    elif colorint == 2:
                        color = QColor(255, 181, 198)
                    elif colorint == 3:
                        color = QColor(161, 25, 45)
                    elif colorint == 4:
                        color = QColor(232, 51, 92)
                    elif colorint == 5:
                        color = QColor(255, 0, 0)  # đỏ
                    else:
                        # mau trắng điểu chỉnh màu trong phim
                        color = QColor(255, 181, 198)
# gap loi 1             để tiết kiệm bộ nhớ và chạy hoạt ảnh mượt hơn
                    if(draw_x, draw_y, size, color) not in self.coord_list1:
                        self.coord_list1.append((draw_x, draw_y, size, color))
                        # lấy danh sách trái tim đã khởi tạo
        self.all_coord_list1.append(self.coord_list1)
        for su in range(1, 10):
            coord_temporary1 = []
            for coord in self.coord_list1:
                flexk = ((536-1.11111111111*sqrt(((coord[0]-self.cen_x)**2)+(
                    (coord[1]-self.cen_y)**2)))*(0.00006)*su)-(su*0.01+0.017)
                if flexk < 0:
                    flexk = 0
                new_x = self.cen_x - (1+flexk)*(self.cen_x-coord[0])
                new_y = self.cen_y - (1+flexk)*(self.cen_y-coord[1])
                coord_temporary1.append((new_x, new_y, coord[2], coord[3]))
            self.all_coord_list1.append(coord_temporary1)
        self.coord_list2 = []
        self.all_coord_list2 = []
        expend_list = [int(round(sqrt(10000-(i*i))+100-i, 4))
                       for i in range(0, 92, 5)]
        for order, expend in enumerate(expend_list):
            offset = int(len(expend_list) -
                         sqrt((len(expend_list)**2)-((order+1)**2))+2)+10
            for new_coord in new_coord_list:
                if random.randint(1, 7) == 1:
                    size = random.randint(1, 3)
                    heart_x = new_coord[0]*(sqrt(expend)*0.075)
                    heart_y = new_coord[1]*(sqrt(expend)*0.078)
                    x = int((heart_x) + self.width()/2)
                    y = int((-heart_y) + self.height()/2)
                    draw_x = x + random.randint(-offset, offset)
                    draw_y = y + random.randint(-offset, offset)
                    colorint = random.randint(1, 10)
                    if colorint == 1:
                        color = QColor(190, 43, 77)
                    elif colorint == 2:
                        color = QColor(255, 181, 198)
                    elif colorint == 3:
                        color = QColor(161, 25, 45)
                    elif colorint == 4:
                        color = QColor(232, 51, 92)
                    elif colorint == 7:
                        color = QColor(255, 0, 0)
                    else:
                        color = QColor(214, 79, 100)
                    if(draw_x, draw_y, size, color) not in self.coord_list2:
                        self.coord_list2.append((draw_x, draw_y, size, color))
        for expendx in range(-self.cent, self.cent):
            for expendy in range(-self.cent, self.cent):
                if random.randint(1, 100) == 1:
                    size = random.randint(1, 3)
                    heart_x = expendx
                    heart_y = expendy
                    x = int((heart_x)+self.width()/2)
                    y = int((-heart_y)+self.height()/2-40)
                    offset = 20
                    draw_x = x+random.randint(-offset, offset)
                    draw_y = y+random.randint(-offset, offset)
                    colorint = random.randint(1, 10)
                    if colorint == 1:
                        color = QColor(190, 43, 77)
                    elif colorint == 2 or colorint == 6:
                        color = QColor(255, 181, 198)
                    elif colorint == 3 or colorint == 5:
                        color = QColor(161, 25, 45)
                    elif colorint == 4:
                        color = QColor(232, 51, 92)
                    elif colorint == 7:
                        color = QColor(255, 0, 0)
                    else:
                        color = QColor(214, 79, 100)
                    if (draw_x, draw_y, size, color) not in self.coord_list2:
                        self.coord_list2.append((draw_x, draw_y, size, color))

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.begin(self)
        if self.readlist >= 0:
            coord_temporary2 = []
            offset = (9 - self.readlist)*6
            if offset > 0:
                for coord in self.coord_list2:
                    new_x = coord[0]+random.randint(-offset, offset)
                    new_y = coord[1]+random.randint(-offset, offset)
                    coord_temporary2.append((new_x, new_y, coord[2], coord[3]))
            else:
                coord_temporary2 = self.coord_list2
            self.all_coord_list = self.all_coord_list1[self.readlist] + \
                coord_temporary2
            # dùng toán tử duyệt qua tất cả các điểm
        for coord in self.all_coord_list:
            if coord[2] <= 3:
                self.pen = QPen()
                self.pen.setColor(coord[3])
                self.pen.setWidth(coord[2])
                self.painter.setPen(self.pen)
                self.painter.drawPoint(coord[0], coord[1],)
                # kich thước điểm không đúng
            else:
                self.painter.setBrush(coord[3])
                self.painter.drawEllipse(
                    coord[0], coord[1], coord[2]-1, coord[2]-1)
        self.painter.end()
# nếu là phần tử lớn nhất thì giảm dần
        if self.readlist == 9:
            self.largen = False
        elif self.readlist == 0:
            self.largen = True
        if self.largen == True:
            self.readlist += 1
        elif self.largen == False:
            self.readlist -= 1

    def timerEvent(self, event):
        self.update()


# code hien tai dang rat lag
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QheartWindow()
    window.show()
    sys.exit(app.exec_())
