import pygame
import random
import numpy as np
import cv2
from collections import deque

ball_list = deque(maxlen=15)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_SIZE = 10


# define range of skin color in HSV
lower_skin = np.array([0, 48, 80], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)
#
cap = cv2.VideoCapture(0)

cur_frame = None

def cvimage_to_pygame(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
        self.change_x = random.randrange(-2, 10)
        self.change_y = random.randrange(-2, 10)
        self.color = ( random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))


def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    #ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    #ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    # Speed and direction of rectangle
    #ball.change_x = random.randrange(-2, 30)
    #ball.change_y = random.randrange(-20, 3)

    return ball

def make_ball02(position):
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = position[0]
    ball.y = position[1]
    return ball

def get_skinXY():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # cv2.imwrite('frame.jpg', frame)
    global cur_frame
    cur_frame = frame

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only skin colors
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 4)


    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = (0, 0)
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if radius > 100:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    return center

def main():
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball = make_ball()
    ball_list.appendleft(ball)

    # -------- Main Program Loop -----------
    while not done:
        skinPositon=get_skinXY()
        if skinPositon[0] != 0 and skinPositon[1] != 0:
            ball=make_ball02(skinPositon)
            ball_list.appendleft(ball)

		# --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.appendleft(ball)

        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # --- Drawing
        # Set the screen background
        # screen.fill(BLACK)
        # frameImg = pygame.image.load('frame.jpg')
        frameImg = cvimage_to_pygame(cur_frame)
        screen.blit(frameImg,(0,0))
        # Draw the balls
        i = 1
        for ball in ball_list:
            ball.y -=20
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], int(BALL_SIZE*i*0.4))
            i += 1

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(10)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()