import turtle
import time
import random

# Oyun hızı ve skorlar
delay = 0.1
score = 0
high_score = 0

# Ekranı ayarla
wn = turtle.Screen()
wn.title("Yılan Oyunu - Python / Turtle")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Otomatik güncellemeyi kapat (FPS'i biz kontrol edeceğiz)

# Yılanın kafası
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Yemek
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Yılanın gövde parçaları
segments = []

# Skor yazısı
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Kontrol fonksiyonları
def go_up():
    if head.direction != "down":  # Tam tersine dönememesi için
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Hareket fonksiyonu
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klavye dinleme
wn.listen()
wn.onkeypress(go_up, "Up")       # Yukarı ok
wn.onkeypress(go_down, "Down")   # Aşağı ok
wn.onkeypress(go_left, "Left")   # Sol ok
wn.onkeypress(go_right, "Right") # Sağ ok

# Ana oyun döngüsü
while True:
    wn.update()

    # Kenarlara çarpma kontrolü
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Gövdeyi gizle
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Skoru sıfırla
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Yemek ile çarpışma kontrolü
    if head.distance(food) < 20:
        # Yemeği rastgele yeni bir yere taşı
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Yeni gövde parçası ekle
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

        # Oyunu biraz hızlandır
        delay -= 0.001

        # Skoru arttır
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Gövdeyi öne taşı (sondan başa doğru)
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # İlk gövde parçasını kafanın olduğu yere koy
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Kafayı hareket ettir
    move()

    # Gövdeye çarpma kontrolü
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Gövdeyi gizle
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Skoru resetle
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)