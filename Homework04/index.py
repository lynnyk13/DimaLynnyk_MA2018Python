import simplegui
import random

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2, 1]
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD1_POS = HEIGHT / 2
PAD2_POS = HEIGHT / 2
paddle_vel = 3
paddle1_vel = 0
paddle2_vel = 0
scores1 = 0
scores2 = 0


def new_game(right):
    global ball_pos, ball_vel
    global WIDTH
    global HEIGHT
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = -random.randrange(120, 240) / 100
    if right == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60, 180) / 100


def restart():
    global PAD1_POS, PAD2_POS, HEIGHT, scores1, scores2
    scores1 = 0
    paddle1_vel = 0
    scores2 = 0
    PAD1_POS = HEIGHT / 2
    PAD2_POS = HEIGHT / 2
    new_game(ball_vel[0] > 0)


def draw(canvas):
    global scores1, scores2, PAD1_POS, PAD2_POS, paddle1_vel, paddle2_vel, ball_pos, ball_vel, PAD1_POS, PAD2_POS

    canvas.draw_text(str(scores1), (200, 60), 40, "Blue")
    canvas.draw_text(str(scores2), (400, 60), 40, "Red")
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    canvas.draw_polygon([[0, PAD1_POS], [PAD_WIDTH, PAD1_POS],[ PAD_WIDTH, (PAD1_POS) + PAD_HEIGHT], [0, (PAD1_POS) + PAD_HEIGHT]], 2, "White", "Blue")
    canvas.draw_polygon([[WIDTH, PAD2_POS], [WIDTH - PAD_WIDTH, PAD2_POS], [WIDTH - PAD_WIDTH,PAD2_POS + PAD_HEIGHT], [WIDTH, PAD2_POS + PAD_HEIGHT]], 2, "White", "Red")

    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "Red", "White")

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if (PAD1_POS <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (PAD1_POS >= 0 and paddle1_vel < 0):
        PAD1_POS += paddle1_vel
    elif (PAD2_POS <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (PAD2_POS >= 0 and paddle2_vel < 0):
        PAD2_POS += paddle2_vel

    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH or ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:

        if PAD1_POS < ball_pos[1] < PAD1_POS + PAD_HEIGHT and ball_vel[0] < 0:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1

        elif PAD2_POS < ball_pos[1] < PAD2_POS + PAD_HEIGHT and ball_vel[0] > 0:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            if ball_vel[0] > 0:
                scores1 += 1

            else:
                scores2 += 1
            new_game(ball_vel[0] < 0)

    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] *= -1


def keydown(key):
    global paddle1_vel, paddle2_vel, PAD2_POS, PAD1_POS, keydown1, keydown2, keyup1, keyup2

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel


def keyup(key):
    global paddle1_vel, paddle2_vel, keydown1, keydown2, keyup2, keyup1
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


frame = simplegui.create_frame("Game", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart Game", restart, 200)
frame.start()
