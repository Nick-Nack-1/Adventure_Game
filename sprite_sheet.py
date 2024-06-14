import pygame
import Globals

class read_out():
	def __init__(self, file_name):
		self.main_sheet = pygame.image.load(file_name).convert_alpha()
	
	
	def Get_img(self,rectangle):
		## rectangle = [(img_top_left_pos),(img_size_x,img_size_y)]
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size)
		image.blit(self.main_sheet, (0,0), rect)
		image.set_colorkey((0,0,0))
		return image
	


class animate():
	def __init__(self, images_per_row, image_count):
		self.total_images = image_count
		self.images_p_row = images_per_row
		self.counter = 0
		self.index = 0
		self.Speed = 0
		self.sheet = None
		self.image_list = []
		self.y = 0
		self.images_done = 0
		self.Reader = None


	def Set_sheet(self, S_sheet):
		##Here it reads out all the images in the sprite sheet and puths them all in a list
		##Each time it gets to the end of a row(x) it adds 1 to the y
		##It will stop when the images done = the total images
		self.Reader = read_out(S_sheet)
		if not self.images_done == self.total_images:
			for x in range(self.images_p_row):
				self.image_list.append(self.Reader.Get_img([(x*16,self.y*16),(Globals.TILE_SIZE,Globals.TILE_SIZE)]))
				self.images_done +=1
			self.y +=1


	def Set_speed(self, speed):
		self.Speed = speed


	def Play(self):
		##Each time Play is called it just returns the next image in the list
		self.counter +=1
		if (self.counter-1) % self.Speed == 0:
			self.index += 1
			if self.index == self.total_images+1:
				self.index = 1
				return [self.image_list[self.index-1], True]
			
			return [self.image_list[self.index-1], False]


def rotate_img(img, deg, old_deg):
	#Rotates the image to a certain degree
	#If the image was already rotated to that degrre it won't be rotated any more
	return pygame.transform.rotate(img, deg-old_deg)
			
