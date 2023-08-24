import datetime, pygame, math


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


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
            angle = (30*math.pi)/180*i
            x = math.cos(angle)*(self.radius-20)
            y = math.sin(angle)*(self.radius-20)
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
        angle = (hour*360/12-90)+minute*30/60
        end_x = self.x + math.cos((angle*math.pi)/180)*(self.radius/3)
        end_y = self.y + math.sin((angle*math.pi)/180)*(self.radius/3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (end_x, end_y))
        # draw minute line
        angle = (minute * 360 / 60 - 90)
        end_x = self.x + math.cos((angle * math.pi) / 180) * (self.radius / 1.5)
        end_y = self.y + math.sin((angle * math.pi) / 180) * (self.radius / 1.5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (end_x, end_y))


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