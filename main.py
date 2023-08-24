import datetime, pygame, math


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def calculate_pos(angle, dist):
    x = math.cos((angle * math.pi) / 180) * dist
    y = math.sin((angle * math.pi) / 180) * dist
    return x, y


class Clock:

    current_time = None
    list_pos_points = []

    def __init__(self, scr, pos, r):
        self.screen = scr
        self.x, self.y = pos
        self.radius = r
        self.create_points()

    def create_points(self):
        for i in range(12):
            x, y = calculate_pos(30*i, self.radius-20)
            self.list_pos_points.append((self.x + x, self.y + y))

    def update(self):
        self.current_time = str(datetime.datetime.now()).split(' ')[1].split('.')[0]
        self.draw()

    def draw(self):
        # draw clock face
        img = pygame.font.SysFont(pygame.font.get_fonts()[0], 35).render(self.current_time, True, (255, 255, 255))
        self.screen.blit(img, (self.x-50, HEIGHT-35))
        # draw circle
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)
        # draw points
        for x, y in self.list_pos_points:
            pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 10)
        # draw hour line
        hour = int(self.current_time.split(':')[0])
        minute = int(self.current_time.split(':')[1])
        second = int(self.current_time.split(':')[2])
        angle = (hour * 360 / 12 - 90) + minute * 30 / 60
        end_x, end_y = calculate_pos(angle, self.radius / 2)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x + end_x, self.y + end_y))
        # draw minute line
        angle = (minute * 360 / 60 - 90) + second / 30
        end_x, end_y = calculate_pos(angle, self.radius / 1.5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x + end_x, self.y + end_y))
        # draw second line
        angle = (second * 360 / 60 - 90)
        end_x, end_y = calculate_pos(angle, self.radius / 1.2)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x + end_x, self.y + end_y))


def main():
    pygame.font.init()

    clock = Clock(screen, (WIDTH//2, HEIGHT//2), HEIGHT//2-40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))
        clock.update()
        pygame.display.update()


if __name__ == '__main__':
    main()