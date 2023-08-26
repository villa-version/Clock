import datetime, pygame, math


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def calculate_pos(angle, dist):
    x = math.cos((angle * math.pi) / 180) * dist
    y = math.sin((angle * math.pi) / 180) * dist
    return x, y


class Clock:

    current_time = None
    list_pos_points = []
    list_pos_numbers = []

    def __init__(self, scr, pos, r):
        self.screen = scr
        self.x, self.y = pos
        self.radius = r
        self.create_points()

    def create_points(self):
        for i in range(60):
            if i % 5 == 0:
                x, y = calculate_pos(30 * i//5 - 90, self.radius - 20)
                self.list_pos_points.append({'number': i//5, 'pos': (self.x + x, self.y + y), 'is_hour': True})
                x, y = calculate_pos(30 * i//5 - 90, self.radius + 15)
                self.list_pos_numbers.append({'number': i//5 if i//5 != 0 else 12, 'pos': (self.x + x - 5, self.y + y - 15)})
            else:
                x, y = calculate_pos(6 * i - 90, self.radius - 20)
                self.list_pos_points.append({'number': i, 'pos': (self.x + x, self.y + y), 'is_hour': False})

    def update(self):
        self.current_time = datetime.datetime.now()
        self.draw()

    def draw(self):
        # draw clock face
        img = pygame.font.SysFont(pygame.font.get_fonts()[0], 35).render(f'{self.current_time:%H:%M:%S}', True, (255, 255, 255))
        self.screen.blit(img, (0, HEIGHT-35))
        # draw circle
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)
        # draw points
        for item in self.list_pos_points:
            pygame.draw.circle(self.screen, (0, 0, 0), (item['pos'][0], item['pos'][1]), 5 if item['is_hour'] else 1)
        # draw numbers
        for item in self.list_pos_numbers:
            img = pygame.font.SysFont(pygame.font.get_fonts()[0], 24).render(str(item['number']), True, (255, 255, 255))
            self.screen.blit(img, (item['pos'][0], item['pos'][1]))
        # draw hour line
        hour, minute, second = self.current_time.hour, self.current_time.minute, self.current_time.second
        angle = (hour * 360 / 12 - 90) + minute * 30 / 60
        end_x, end_y = calculate_pos(angle, self.radius / 2)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x + end_x, self.y + end_y), 5)
        # draw minute line
        angle = (minute * 360 / 60 - 90) + second * 6 / 60
        end_x, end_y = calculate_pos(angle, self.radius / 1.5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x + end_x, self.y + end_y), 2)
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
