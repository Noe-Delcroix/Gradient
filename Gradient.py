from math import floor,sqrt
import random
import time

import tkinter as tk

root = tk.Tk()


PosX =(root.winfo_screenwidth()//2)-(500//2)
PosY =(root.winfo_screenheight()//2)-(300//2)




import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (PosX,PosY)


import pygame
pygame.init()

app = pygame.display.set_mode((500,300), pygame.NOFRAME)
TitleScreen=pygame.image.load("TitleScreen.png").convert_alpha()
app.blit(TitleScreen,(0,0))
pygame.display.flip()


time.sleep(2)



win_s = 700
PosX =(root.winfo_screenwidth()//2)-(win_s//2)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (PosX,50)
pygame.display.set_caption("Gradient")
app = pygame.display.set_mode((win_s,win_s+50))

 



level=1
launched=True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched=False

	menu=True

	menu_s=7
	menu_cell_s=win_s/menu_s
	menu_select=level-1

	class menu_tile():
		def __init__(self,x,y):
			self.x=x
			self.y=y
			self.number=str((self.y*menu_s)+self.x+1)
			self.tile = 230-self.x*15-self.y*15
			self.tile = (self.tile,self.tile,self.tile)
		def render(self,sel_c):
			if str(menu_select+1)==self.number:
				self.color=sel_c
			else:
				try:
					open("level"+str(self.number)+".txt","r")
				except FileNotFoundError:
					self.color=(150,0,0)			
				else:
					self.color=(0,0,0)

			pygame.draw.rect(app,self.tile,(self.x*menu_cell_s,self.y*menu_cell_s,menu_cell_s+1,menu_cell_s+1))
			if len(self.number)==2:
				app.blit(pygame.font.SysFont("dejavusansextralight", int(menu_cell_s*0.8)).render(self.number, 1, self.color), (self.x*menu_cell_s,self.y*menu_cell_s+menu_cell_s*0.05))
			elif len(self.number)==3:
				app.blit(pygame.font.SysFont("dejavusansextralight", int(menu_cell_s*0.52)).render(self.number, 1, self.color), (self.x*menu_cell_s,self.y*menu_cell_s+menu_cell_s*0.2))
			else:
				app.blit(pygame.font.SysFont("dejavusansextralight", int(menu_cell_s*0.9)).render(self.number, 1, self.color), (self.x*menu_cell_s+menu_cell_s*0.25,self.y*menu_cell_s))



	list_menu=[]
	def Create_menu(x,y):
		ym=0
		while ym<y:
			xm=0
			while xm<x:
				mt=menu_tile(xm,ym)
				list_menu.append(mt)				
				xm+=1
			ym+=1


			

	def Render_menu(r_all,sel_c):
		app.blit(pygame.font.SysFont("dejavusansextralight", 35).render("Select a level and press SPACE !", 1, (255,255,255)), (75,win_s+5))
		for item in list_menu:
			if r_all==False:
				if item.number==str(menu_select+1):
					item.render(sel_c)
			else:
				item.render(sel_c)
		pygame.display.flip()

	def Render_menu_level(infos):
		grid_s = int(sqrt(len(infos)/2))
		cell_s = (win_s/2)/grid_s

		ypos=0
		kpos=0
		while ypos<grid_s:
			xpos=0
			while xpos<grid_s:
				
				pygame.draw.rect(app,(int(str(infos[kpos*2])[1:4]),int(str(infos[kpos*2])[5:8]),int(str(infos[kpos*2])[9:12])),(win_s/4+cell_s*xpos,350+cell_s*ypos,cell_s*1.05,cell_s+1.05))
				if str(infos[kpos*2+1])[0:4]=="True":
					pygame.draw.circle(app,(0,0,0),(int(win_s/4+cell_s*xpos+cell_s/2),int(350+cell_s*ypos+cell_s/2)),int(cell_s/15))
				
				
				xpos+=1
				kpos+=1
			ypos+=1
		pygame.display.flip()


	Create_menu(11,3)
	Render_menu(True,(255,255,255))
	file=open("level"+str(menu_select+1)+".txt","r")
	Render_menu_level(file.readlines())





	while menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menu=False
				launched=False
		MouseX=floor(pygame.mouse.get_pos()[0]/menu_cell_s)
		MouseY=floor(pygame.mouse.get_pos()[1]/menu_cell_s)
		if MouseY>=menu_s:
			MouseY=menu_s-1	
		if pygame.mouse.get_pressed()[0]:
			try:
				open("level"+str((MouseY*menu_s)+MouseX+1)+".txt","r")
			except FileNotFoundError:
				level=+0
			else:
				file=open("level"+str((MouseY*menu_s)+MouseX+1)+".txt","r")
				Render_menu_level(file.readlines())
				if not menu_select==(MouseY*menu_s)+MouseX:
					Render_menu(False,(0,0,0))
				menu_select=(MouseY*menu_s)+MouseX
				Render_menu(False,(255,255,255))
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_SPACE]:
			level = int(menu_select+1)
			menu=False



	playing = True

	file = open("level"+str(level)+".txt","r")

	infos = file.readlines()

	moves = 0
	grid_s = int(sqrt(len(infos)/2))
	cell_s = win_s/grid_s
	select_x=0
	select_y=-1


	class Tile():
		def __init__(self,x,y,r,g,b,number,lock):
			self.x=x
			self.y=y
			self.r=r
			self.g=g
			self.b=b
			self.lock=lock
			self.number=number
		def render(self):
			pygame.draw.rect(app,(self.r,self.g,self.b),(self.x*cell_s,self.y*cell_s,cell_s+1,cell_s+1))
			if self.x == select_x and self.y== select_y:
				pygame.draw.circle(app,(0,0,0),(int(self.x*cell_s+cell_s/2),int(self.y*cell_s+cell_s/2)),int(cell_s/5),5)
			if self.lock == "True":
				pygame.draw.circle(app,(0,0,0),(int(self.x*cell_s+cell_s/2),int(self.y*cell_s+cell_s/2)),int(cell_s/15),0)
		def switch(self,x1,y1,x2,y2):
			if self.x == x1 and self.y== y1:		
				self.x=x2
				self.y=y2

			elif self.x == x2 and self.y== y2:		
				self.x=x1
				self.y=y1


	list_tiles=[]
	list_locked=[]

	def Create_Gradient():
		ypos=0
		kpos=0
		while ypos<grid_s:
			xpos=0
			while xpos<grid_s:
					
				t1=Tile(xpos,ypos,int(str(infos[kpos*2])[1:4]),int(str(infos[kpos*2])[5:8]),int(str(infos[kpos*2])[9:12]),kpos,str(infos[kpos*2+1])[0:4])
				list_tiles.append(t1)
				list_locked.append(str(infos[kpos*2+1])[0:4])

				xpos+=1
				kpos+=1
			ypos+=1






	def Render_Gradient():
		pygame.draw.rect(app,(0,0,0),(0,win_s,win_s,50))
		app.blit(pygame.font.SysFont("dejavusansextralight", 35).render("Moves : {}".format(moves), 1, (255,255,255)), (5,win_s+5))
		app.blit(pygame.font.SysFont("dejavusansextralight", 35).render("Press ESCAPE to quit", 1, (255,255,255)), (win_s-380,win_s+5))		
		for item in list_tiles:
			item.render()
		pygame.display.flip()


	def Mix_Gradient(Iterations):
		i=0
		while i<Iterations:
			MX1=random.randint(0,grid_s-1)
			MY1=random.randint(0,grid_s-1)
			while list_locked[(MY1*grid_s)+MX1]=="True":
				MX1=random.randint(0,grid_s-1)
				MY1=random.randint(0,grid_s-1)

			MX2=random.randint(0,grid_s-1)
			MY2=random.randint(0,grid_s-1)
			while list_locked[(MY2*grid_s)+MX2]=="True":
				MX2=random.randint(0,grid_s-1)
				MY2=random.randint(0,grid_s-1)
			for item in list_tiles:
				item.switch(MX1,MY1,MX2,MY2)

			i+=1

	def Check_win():
		Win = True
		for item in list_tiles:
			if not item.number == (item.y*grid_s)+item.x:
				Win=False

		return Win

	if playing and launched:
		Create_Gradient()
		Render_Gradient()
		app.blit(pygame.font.SysFont("dejavusansextralight", 30).render("Left click to select, right click to switch", 1, (20,20,20)), (50,win_s*0.57))
		app.blit(pygame.font.SysFont("dejavusansextralight", 85).render("Fix the gradient", 1, (20,20,20)), (7,win_s*0.43))
		pygame.display.flip()
		time.sleep(3)
		Mix_Gradient(50)
		Render_Gradient()




	while playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing=False
				launched=False	

		MouseX=floor(pygame.mouse.get_pos()[0]/cell_s)
		MouseY=floor(pygame.mouse.get_pos()[1]/cell_s)
		if MouseY>=grid_s:
			MouseY=grid_s-1

		if list_locked[(MouseY*grid_s)+MouseX]=="Fals":
			if pygame.mouse.get_pressed()[0]:
				select_x=MouseX
				select_y=MouseY
				Render_Gradient()
			if pygame.mouse.get_pressed()[2] and select_y>=0:
				if MouseX==select_x and MouseY==select_y :
					moves+=0
				else:
					moves+=1			
				for item in list_tiles:
					item.switch(select_x,select_y,MouseX,MouseY)
				Render_Gradient()
				select_x=MouseX
				select_y=MouseY
				if Check_win():
					app.blit(pygame.font.SysFont("arial", int(win_s*0.9)).render("☼", 1, (255,255,255)), (int(win_s/11),int(-win_s/20)))		
					pygame.display.flip()
					time.sleep(1.5)
					playing=False
					app.fill((0,0,0))
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_ESCAPE]:
			app.fill((0,0,0))
			playing=False

				
