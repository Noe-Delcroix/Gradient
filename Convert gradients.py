import pygame


win_s = 600


pygame.init()
pygame.display.set_caption("Gradient test")
app = pygame.display.set_mode((win_s,win_s))

Gradient=pygame.image.load("New_Gradient.png").convert_alpha()
Locked=pygame.image.load("New_Locked.png").convert_alpha()

grid_s = pygame.Surface.get_height(Gradient)
pixel_s = win_s/grid_s

Gradient = pygame.transform.scale(Gradient,(win_s,win_s))
Locked = pygame.transform.scale(Locked,(win_s,win_s))

app.blit(Locked,(0,0))
app.blit(Gradient,(0,0))
pygame.display.flip()



def Get_Color():

	file = open("levelNew.txt","w")  
	y=0
	while y<grid_s:
		x=0
		while x<grid_s:
			info = Gradient.get_at((int(pixel_s*x)+1,int(pixel_s*y)+1))
			if len(str(info[0]))==1:
				r="00"+str(info[0])
			elif len(str(info[0]))==2:
				r="0"+str(info[0])
			else:
				r=str(info[0])

			if len(str(info[1]))==1:
				g="00"+str(info[1])
			elif len(str(info[1]))==2:
				g="0"+str(info[1])
			else:
				g=str(info[1])

			if len(str(info[2]))==1:
				b="00"+str(info[2])
			elif len(str(info[2]))==2:
				b="0"+str(info[2])
			else:
				b=str(info[2])




			print("({},{},{})".format(r,g,b))
			file.write("({},{},{})\n".format(r,g,b))

			info = Locked.get_at((int(pixel_s*x)+1,int(pixel_s*y)+1))
			if info == (0,0,0,255):
				print("True")
				file.write("True\n")
			else:
				print("False")
				file.write("False\n")



			x+=1
		y+=1
Get_Color()
