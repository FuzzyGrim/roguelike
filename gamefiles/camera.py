import pygame

import constants
import globalvars

class ObjCamera:
    def __init__(self):
        self.width = constants.CAMERA_WIDTH
        self.height = constants.CAMERA_HEIGHT
        self.x, self.y = (0, 0) 
        
    @property
    def rectangle(self):
        pos_rect = pygame.Rect((0, 0), (constants.CAMERA_WIDTH, constants.CAMERA_HEIGHT))
        
        pos_rect.center = (self.x, self.y)
    
        return pos_rect
    
    @property
    def map_address(self):
        map_x = self.x // constants.CELL_WIDTH
        map_y = self.y // constants.CELL_HEIGHT
        
        return (map_x, map_y)
    
    def update(self):
        
        target_x = globalvars.PLAYER.x * constants.CELL_WIDTH + (constants.CELL_WIDTH / 2)
        target_y = globalvars.PLAYER.y * constants.CELL_HEIGHT + (constants.CELL_HEIGHT / 2)
        
        distance_x, distance_y = self.map_dist((target_x, target_y))
        
        self.x += int(distance_x * .5)
        self.y += int(distance_y * .5)    
        
    def win_to_map(self, coords):
        
        tar_x, tar_y = coords

        #convert window coords to distace from camera
        cam_d_x, cam_d_y = self.cam_dist((tar_x, tar_y))

        #distance from cam -> map coord
        map_p_x = self.x + cam_d_x
        map_p_y = self.y + cam_d_y

        return((map_p_x, map_p_y))
        
        
    def map_dist(self, coords):
        
        new_x, new_y = coords
        
        dist_x = new_x - self.x
        dist_y = new_y - self.y
        
        return (dist_x, dist_y)
    
    def cam_dist(self, coords):
        
        win_x, win_y = coords
        
        dist_x = win_x - (self.width / 2)
        dist_y = win_y - (self.height / 2)
        
        return (dist_x, dist_y)   