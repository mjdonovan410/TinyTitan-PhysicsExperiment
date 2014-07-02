import pygame, os, sys
from pygame.locals import *
from Tkinter import Tk
from tkFileDialog import askopenfilename

global FPS
FPS = 90

def left_key(curFrame,frame_range):
	if curFrame > frame_range[0]:
		curFrame -= 1
	return curFrame

def right_key(curFrame,frame_range):
	if curFrame < frame_range[1]:
		curFrame += 1
	return curFrame
	
def button_pressed(screen,curFrame,str,frame_range):
	if str == "stepf":
		return right_key(curFrame,frame_range)
	elif str == "stepb":
		return left_key(curFrame,frame_range)
	elif str == "skipf":
		if curFrame+(FPS/2) >= frame_range[1]:
			return frame_range[1]
		else:
			return curFrame+(FPS/2)
	elif str == "skipb":
		if curFrame-(FPS/2) <= frame_range[0]:
			return frame_range[0]
		else:
			return curFrame-(FPS/2)
	elif str == "load":
		Tk().withdraw()
		infile = askopenfilename(filetypes=[("H264 Video","*.h264")])
		
		if infile != '':
			cleanDir()
			font = pygame.font.SysFont("BankGothic Md BT",108)
			label = font.render("PLEASE WAIT",1,(255,0,0))
			screen.blit(label,(100,300))
			pygame.display.update()
			os.system("mkdir ffmpeg_temp")
			frames = change_vid(infile)
			screen.blit(pygame.image.load("Images/bg.png"),(0,0))
			screen.blit(pygame.image.load("Images/pic_temp.png"),(720-(480+10),10))
			return frames
			
	elif str == "start":
		return frame_range[0]
	elif str == "end":
		return frame_range[1]
		
def change_vid(infile):
	os.system("ffmpeg -i "+infile+" -r 25 -f image2 ffmpeg_temp/%05d.jpg")
	path, dirs, files = os.walk("./ffmpeg_temp/").next()
	frames = []
	for i in files:
		frames.append(pygame.image.load("./ffmpeg_temp/"+i))
	return frames
	
def exitAndClean():
	pygame.quit()
	sys.exit()
	
def cleanDir():
	os.system("rm ./ffmpeg_temp/*.jpg")
	os.system("rmdir ./ffmpeg_temp")