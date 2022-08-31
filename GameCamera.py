from pygame import Rect

def complex_camera(camera, target_rect, sceen_width, screen_height):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + int(sceen_width/2), -t + int(screen_height/2), w, h
    l = min(0, l) 								# stop scrolling at the left edge
    l = max(-(camera.width - sceen_width), l)		# stop scrolling at the right edge
    t = max(-(camera.height - screen_height), t)	# stop scrolling at the bottom
    t = min(0, t)								# stop scrolling at the top
    return Rect(l, t, w, h)

class PlayerCamera(object):
    def __init__(self, level_width, level_height, sceen_width, screen_height):
        self.camera_func = complex_camera
        self.state = Rect(0, 0, level_width, level_height)
        self.sceen_width = sceen_width
        self.screen_height = screen_height

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect, self.sceen_width, self.screen_height)







