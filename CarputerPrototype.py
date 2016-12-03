#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CarputerPrototype.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

# import graphics library
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import math
import cairo
# Import Core Systems
import time
import sys, string

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

channelOneValue = 0
channelTwoValue = 0
channelThreeValue = 0
channelFourValue = 0
channelFiveValue = 0
channelSixValue = 0
channelSevenValue = 0
channelEightValue = 0
channelOneValues = []
channelTwoValues = []
channelThreeValues = []
channelFourValues = []
channelFiveValues = []
channelSixValues = []
channelSevenValues = []
channelEightValues = []
debugInputsWindowDoPauseReading = False

# Software SPI configuration:
CLK  = 6
MISO = 13
MOSI = 19
CS   = 26
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Cairo
TEXT = 'cairo'
BORDER_WIDTH = 10

# local tracking
currentWindowDisplayed = 0

class CarputerMechanics:
	

	
		
	def update_gauge(self, dt):
		# Software SPI configuration:
		CLK  = 6
		MISO = 13
		MOSI = 19
		CS   = 26
		mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		
		channelOneValue = mcp.read_adc(0)

		channelTwoValue = mcp.read_adc(1)

		channelThreeValue = mcp.read_adc(2)

		channelFourValue = mcp.read_adc(3)

		channelFiveValue = mcp.read_adc(4)

		channelSixValue = mcp.read_adc(5)

		channelSevenValue = mcp.read_adc(6)

		channelEightValue = mcp.read_adc(7)


	
class CarputerPrototype(object):

	# terminates app when invokes via signal delete_event
	def close_application(self, widget, event, data=None):
		gtk.main_quit()
		return False
		
	def hello(self, widget, data=None):
		print "Hello World"
		
	def callback(self, widget, data):
		print "Hello again - %s was pressed" % data
		
		CLK  = 6
		MISO = 13
		MOSI = 19
		CS   = 26
		mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		
		channelOneValue = mcp.read_adc(0)
		self.channelOneLabel.set_text("Channel 1: {0}".format(channelOneValue))

	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def destroy(self, widget, data=None):
		gtk.main_quit()
	

	
	def __init__(self, timeout):
		# create the splashscreen
		self.splashscreenWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.splashscreenWindow.set_border_width(10)

		self.splashscreenWindow.fullscreen()
		self.splashscreenWindow.show()
		
		# create horizontal box
		self.splashscreenVBox1 = gtk.VBox(False, 0)
		self.splashscreenVBox1.show()
		self.splashscreenWindow.add(self.splashscreenVBox1)
		
		# create the title words
		self.splashscreenTitleLabel = gtk.Label()
		self.splashscreenTitleLabel.set_text("Rude Boy Racing Carputer PROTOTYPE -- Click To Begin...")
		self.splashscreenTitleLabel.show()
		self.splashscreenVBox1.pack_start(self.splashscreenTitleLabel)
		
		# show the splash screen image
		self.splashscreenImage = gtk.Image()
		self.splashscreenImage.set_from_file("rudeBoyRacingSmallSquare.jpg")
		self.splashscreenImage.set_pixel_size(self.splashscreenImage.get_pixel_size() * 4)
		self.splashscreenImage.show()
		self.splashscreenButton = gtk.Button()
		self.splashscreenButton.add(self.splashscreenImage)
		self.splashscreenButton.show()
		self.splashscreenVBox1.pack_start(self.splashscreenButton)
		self.splashscreenButton.connect("clicked", self.splashscreenClickthrough)
		
		self.applicationStartTime = time.time()
		self.applicationDebugWindowOpen = False
		
		
		gobject.idle_add(self.waitOnSplashscreenForABitThenContinue)
		
	def waitOnSplashscreenForABitThenContinue(self):
		if self.applicationDebugWindowOpen is False:
			if time.time() > self.applicationStartTime + 3.0:
				self.splashscreenClickthrough()
				
	def splashscreenClickthrough(self, timeout):
		self.createMainWindow()
		self.splashscreenWindow.destroy()
		gobject.idle_add(self.mainWindowUpdate)
		currentWindowDisplayed = 1
		
	def mainWindowUpdate(self):
		self.mainWindowGauge1Button.set_label("Gauge 1: {0}".format(mcp.read_adc(0)))
		if currentWindowDisplayed is not 1:
			return False
	
	def createMainWindow(self):
		
		# create the main window
		self.mainWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.mainWindow.connect("delete_event", self.close_application)
		self.mainWindow.set_border_width(100)
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
		self.mainWindow.fullscreen()
		self.mainWindow.show()
		
		# create menu bar
		#self.menu_bar = gtk.MenuBar()
		#self.menu_bar.show()
		# pack in to splash screen's HBox
		#self.splashscreenHBox1.pack_start(self.menu_bar)
		# create menu list
		#self.controlMenu = gtk.Menu()
		#self.controlMenu.show()
		# create Control menu options
		#self.controlMenuQuit_item = gtk.MenuItem("Quit")
		# add menu options to Control Menu
		#self.controlMenu.append(self.controlMenuQuit_item)
		# attach callback
		#self.controlMenuQuit_item.connect_object("activate", self.destroy, "file.quit")
		# show menu options
		#self.controlMenuQuit_item.show()
		
		# create the main Vertical Box
		self.mainWindowVBox1 = gtk.VBox(False, 0)
		self.mainWindow.add(self.mainWindowVBox1)
		self.mainWindowVBox1.show()
		
		# create the top-level Horizontal Box
		self.mainWindowHBox1 = gtk.HBox(False, 0)
		self.mainWindowVBox1.pack_start(self.mainWindowHBox1)
		self.mainWindowHBox1.show()
		
		# Create Debug Inputs Button
		self.mainWindowDebugInputsButton = gtk.Button(label="Debug Inputs")
		self.mainWindowHBox1.pack_start(self.mainWindowDebugInputsButton)
		self.mainWindowDebugInputsButton.show()
		self.mainWindowDebugInputsButton.connect("clicked", self.debugInputsWindow)
		
		# Create 2nd Button
		self.mainWindowButton2 = gtk.Button(label="Button 2")
		self.mainWindowHBox1.pack_start(self.mainWindowButton2)
		self.mainWindowButton2.show()
		
		# Create the Quit Button
		self.mainWindowQuitButton = gtk.Button(label="Quit")
		self.mainWindowHBox1.pack_start(self.mainWindowQuitButton)
		self.mainWindowQuitButton.show()
		self.mainWindowQuitButton.connect("clicked", self.destroy)
		
		# create the mid-level Horizontal Box
		self.mainWindowHBox2 = gtk.HBox(False,0)
		self.mainWindowVBox1.pack_start(self.mainWindowHBox2)
		self.mainWindowHBox2.show()
		
		
		
		# Gauge Button 1 - As Cairo Drawing Area
		self.mainWindowGauge1Button = gtk.Button(label="Gauge 1")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge1Button)
		self.mainWindowGauge1Button.show()
		self.mainWindowGauge1Button.connect("clicked", self.gauge1ButtonCallback)
		# Gauge Button 2
		self.mainWindowGauge2Button = gtk.Button(label="Gauge 2")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge2Button)
		self.mainWindowGauge2Button.show()
		self.mainWindowGauge2Button.connect("clicked", self.gauge2ButtonCallback)
		# Gauge Button 3
		self.mainWindowGauge3Button = gtk.Button(label="Gauge 3")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge3Button)
		self.mainWindowGauge3Button.show()
		self.mainWindowGauge3Button.connect("clicked", self.gauge3ButtonCallback)
		# Gauge Button 4
		self.mainWindowGauge4Button = gtk.Button(label="Gauge 4")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge4Button)
		self.mainWindowGauge4Button.show()
		self.mainWindowGauge4Button.connect("clicked", self.gauge4ButtonCallback)
		# Gauge Button 5
		self.mainWindowGauge5Button = gtk.Button(label="Gauge 5")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge5Button)
		self.mainWindowGauge5Button.show()
		self.mainWindowGauge5Button.connect("clicked", self.gauge5ButtonCallback)
		# Gauge Button 6
		self.mainWindowGauge6Button = gtk.Button(label="Gauge 6")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge6Button)
		self.mainWindowGauge6Button.show()
		self.mainWindowGauge6Button.connect("clicked", self.gauge6ButtonCallback)
		# Gauge Button 7
		self.mainWindowGauge7Button = gtk.Button(label="Gauge 7")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge7Button)
		self.mainWindowGauge7Button.show()
		self.mainWindowGauge7Button.connect("clicked", self.gauge7ButtonCallback)
		# Gauge Button 8
		self.mainWindowGauge8Button = gtk.Button(label="Gauge 8")
		self.mainWindowHBox2.pack_start(self.mainWindowGauge8Button)
		self.mainWindowGauge8Button.show()
		self.mainWindowGauge8Button.connect("clicked", self.gauge8ButtonCallback)
		
		
		
		
		
		# create the bottom-level Horizontal Box
		self.mainWindowHBox3 = gtk.HBox(False,0)
		self.mainWindowVBox1.pack_start(self.mainWindowHBox3)
		self.mainWindowHBox3.show()
		
	def gauge1ButtonCallback(self, timeout):
		print("Gauge 1 Button Clicked")
		currentWindowDisplayed = 10
		self.gauge1WindowSetup()
		self.mainWindow.destroy()
		
	def gauge1ButtonUpdate(self):
		print("Updating Gauge 1")
		
		
	def gauge2ButtonCallback(self, timeout):
		print("Gauge 2 Button Clicked")
		currentWindowDisplayed = 20
		self.gauge2WindowSetup()
		self.mainWindow.destroy()
		
	def gauge2ButtonUpdate(self):
		print("Updating Gauge 2")
		
	def gauge3ButtonCallback(self, timeout):
		print("Gauge 3 Button Clicked")
		currentWindowDisplayed = 30
		self.gauge3WindowSetup()
		self.mainWindow.destroy()
		
	def gauge3ButtonUpdate(self):
		print("Updating Gauge 3")
		
	def gauge4ButtonCallback(self, timeout):
		print("Gauge 4 Button Clicked")
		currentWindowDisplayed = 40
		self.gauge4WindowSetup()
		self.mainWindow.destroy()

	def gauge4ButtonUpdate(self):
		print("Updating Gauge 4")
		
	def gauge5ButtonCallback(self, timeout):
		print("Gauge 5 Button Clicked")
		currentWindowDisplayed = 50
		self.gauge5WindowSetup()
		self.mainWindow.destroy()
		
	def gauge5ButtonUpdate(self):
		print("Updating Gauge 5")
		
	def gauge6ButtonCallback(self, timeout):
		print("Gauge 6 Button Clicked")
		currentWindowDisplayed = 60
		self.gauge6WindowSetup()
		self.mainWindow.destroy()

	def gauge6ButtonUpdate(self):
		print("Updating Gauge 6")

	def gauge7ButtonCallback(self, timeout):
		print("Gauge 7 Button Clicked")
		currentWindowDisplayed = 70
		self.gauge7WindowSetup()
		self.mainWindow.destroy()
		
	def gauge7ButtonUpdate(self):
		print("Updating Gauge 7")
		
	def gauge8ButtonCallback(self, timeout):
		print("Gauge 8 Button Clicked")	
		currentWindowDisplayed = 80
		self.gauge8WindowSetup()
		self.mainWindow.destroy()
		
	def gauge8ButtonUpdate(self):
		print("Updating Gauge 8")
	
	def backToMainWindowCallback(self):
		self.createMainWindow()
		
	def updateGauge1Window(self):
		self.gauge1WindowTopLabel.set_text("Gauge 1:{0}".format(mcp.read_adc(0)))
		if currentWindowDisplayed is not 10:
			return False
	
	def gauge1WindowSetup(self):
		# create the fullscreen window
		self.gauge1Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge1Window.connect("delete_event", self.close_application)
		self.gauge1Window.set_border_width(100)
		self.gauge1Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge1Window.fullscreen()
		self.gauge1Window.show()
		
		self.gauge1VBox1 = gtk.VBox(False, 0)
		self.gauge1Window.add(self.gauge1VBox1)
		self.gauge1VBox1.show()
		
		self.gauge1HBox1 = gtk.HBox(False,0)
		self.gauge1VBox1.pack_start(self.gauge1HBox1)
		self.gauge1HBox1.show()
		
		self.gauge1WindowTopLabel = gtk.Label()
		self.gauge1WindowTopLabel.set_text("Gauge 1:{0}".format(mcp.read_adc(0)))
		self.gauge1HBox1.pack_start(self.gauge1WindowTopLabel)
		self.gauge1WindowTopLabel.show()
		
		self.gauge1WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge1HBox1.pack_start(self.gauge1WindowBackToMainButton)
		self.gauge1WindowBackToMainButton.show()
		self.gauge1WindowBackToMainButton.connect("clicked",self.gauge1BackToMainCallback)
		
		gobject.idle_add(self.updateGauge1Window)
	
	def gauge1BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge1Window.destroy()

	def updateGauge2Window(self):
		self.gauge2WindowTopLabel.set_text("Gauge 2:{0}".format(mcp.read_adc(1)))
		if currentWindowDisplayed is not 20:
			return False
	
	def gauge2WindowSetup(self):
		# create the fullscreen window
		self.gauge2Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge2Window.connect("delete_event", self.close_application)
		self.gauge2Window.set_border_width(100)
		self.gauge2Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge2Window.fullscreen()
		self.gauge2Window.show()
		
		self.gauge2VBox1 = gtk.VBox(False, 0)
		self.gauge2Window.add(self.gauge2VBox1)
		self.gauge2VBox1.show()
		
		self.gauge2HBox1 = gtk.HBox(False,0)
		self.gauge2VBox1.pack_start(self.gauge2HBox1)
		self.gauge2HBox1.show()
		
		self.gauge2WindowTopLabel = gtk.Label()
		self.gauge2WindowTopLabel.set_text("Gauge 2:{0}".format(mcp.read_adc(0)))
		self.gauge2HBox1.pack_start(self.gauge2WindowTopLabel)
		self.gauge2WindowTopLabel.show()
		
		self.gauge2WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge2HBox1.pack_start(self.gauge2WindowBackToMainButton)
		self.gauge2WindowBackToMainButton.show()
		self.gauge2WindowBackToMainButton.connect("clicked",self.gauge2BackToMainCallback)
		
		gobject.idle_add(self.updateGauge2Window)
	
	def gauge2BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge2Window.destroy()
		
	def updateGauge3Window(self):
		self.gauge3WindowTopLabel.set_text("Gauge 3:{0}".format(mcp.read_adc(2)))
		if currentWindowDisplayed is not 30:
			return False
	
	def gauge3WindowSetup(self):
		# create the fullscreen window
		self.gauge3Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge3Window.connect("delete_event", self.close_application)
		self.gauge3Window.set_border_width(100)
		self.gauge3Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge3Window.fullscreen()
		self.gauge3Window.show()
		
		self.gauge3VBox1 = gtk.VBox(False, 0)
		self.gauge3Window.add(self.gauge3VBox1)
		self.gauge3VBox1.show()
		
		self.gauge3HBox1 = gtk.HBox(False,0)
		self.gauge3VBox1.pack_start(self.gauge3HBox1)
		self.gauge3HBox1.show()
		
		self.gauge3WindowTopLabel = gtk.Label()
		self.gauge3WindowTopLabel.set_text("Gauge 3:{0}".format(mcp.read_adc(2)))
		self.gauge3HBox1.pack_start(self.gauge3WindowTopLabel)
		self.gauge3WindowTopLabel.show()
		
		self.gauge3WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge3HBox1.pack_start(self.gauge3WindowBackToMainButton)
		self.gauge3WindowBackToMainButton.show()
		self.gauge3WindowBackToMainButton.connect("clicked",self.gauge3BackToMainCallback)
		
		gobject.idle_add(self.updateGauge3Window)
	
	def gauge3BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge3Window.destroy()

	def updateGauge4Window(self):
		self.gauge4WindowTopLabel.set_text("Gauge 4:{0}".format(mcp.read_adc(3)))
		if currentWindowDisplayed is not 40:
			return False
	
	def gauge4WindowSetup(self):
		# create the fullscreen window
		self.gauge4Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge4Window.connect("delete_event", self.close_application)
		self.gauge4Window.set_border_width(100)
		self.gauge4Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge4Window.fullscreen()
		self.gauge4Window.show()
		
		self.gauge4VBox1 = gtk.VBox(False, 0)
		self.gauge4Window.add(self.gauge4VBox1)
		self.gauge4VBox1.show()
		
		self.gauge4HBox1 = gtk.HBox(False,0)
		self.gauge4VBox1.pack_start(self.gauge4HBox1)
		self.gauge4HBox1.show()

		self.gauge4WindowTopLabel = gtk.Label()
		self.gauge4WindowTopLabel.set_text("Gauge 4:{0}".format(mcp.read_adc(3)))
		self.gauge4HBox1.pack_start(self.gauge4WindowTopLabel)
		self.gauge4WindowTopLabel.show()
		
		self.gauge4WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge4HBox1.pack_start(self.gauge4WindowBackToMainButton)
		self.gauge4WindowBackToMainButton.show()
		self.gauge4WindowBackToMainButton.connect("clicked",self.gauge4BackToMainCallback)
		
		gobject.idle_add(self.updateGauge4Window)
	
	def gauge4BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge4Window.destroy()
		
	def updateGauge5Window(self):
		self.gauge5WindowTopLabel.set_text("Gauge 5:{0}".format(mcp.read_adc(4)))
		if currentWindowDisplayed is not 50:
			return False
	
	def gauge5WindowSetup(self):
		# create the fullscreen window
		self.gauge5Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge5Window.connect("delete_event", self.close_application)
		self.gauge5Window.set_border_width(100)
		self.gauge5Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge5Window.fullscreen()
		self.gauge5Window.show()
		
		self.gauge5VBox1 = gtk.VBox(False, 0)
		self.gauge5Window.add(self.gauge5VBox1)
		self.gauge5VBox1.show()
		
		self.gauge5HBox1 = gtk.HBox(False,0)
		self.gauge5VBox1.pack_start(self.gauge5HBox1)
		self.gauge5HBox1.show()
		
		self.gauge5WindowTopLabel = gtk.Label()
		self.gauge5WindowTopLabel.set_text("Gauge 5:{0}".format(mcp.read_adc(4)))
		self.gauge5HBox1.pack_start(self.gauge5WindowTopLabel)
		self.gauge5WindowTopLabel.show()
		
		self.gauge5WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge5HBox1.pack_start(self.gauge5WindowBackToMainButton)
		self.gauge5WindowBackToMainButton.show()
		self.gauge5WindowBackToMainButton.connect("clicked",self.gauge5BackToMainCallback)
		
		gobject.idle_add(self.updateGauge5Window)
	
	def gauge5BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge5Window.destroy()

	def updateGauge6Window(self):
		self.gauge6WindowTopLabel.set_text("Gauge 6:{0}".format(mcp.read_adc(5)))
		if currentWindowDisplayed is not 60:
			return False
	
	def gauge6WindowSetup(self):
		# create the fullscreen window
		self.gauge6Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge6Window.connect("delete_event", self.close_application)
		self.gauge6Window.set_border_width(100)
		self.gauge6Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge6Window.fullscreen()
		self.gauge6Window.show()
		
		self.gauge6VBox1 = gtk.VBox(False, 0)
		self.gauge6Window.add(self.gauge6VBox1)
		self.gauge6VBox1.show()
	
		self.gauge6HBox1 = gtk.HBox(False,0)
		self.gauge6VBox1.pack_start(self.gauge6HBox1)
		self.gauge6HBox1.show()
		
		self.gauge6WindowTopLabel = gtk.Label()
		self.gauge6WindowTopLabel.set_text("Gauge 6:{0}".format(mcp.read_adc(5)))
		self.gauge6HBox1.pack_start(self.gauge6WindowTopLabel)
		self.gauge6WindowTopLabel.show()
		
		self.gauge6WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge6HBox1.pack_start(self.gauge6WindowBackToMainButton)
		self.gauge6WindowBackToMainButton.show()
		self.gauge6WindowBackToMainButton.connect("clicked",self.gauge6BackToMainCallback)
		
		gobject.idle_add(self.updateGauge6Window)
	
	def gauge6BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge6Window.destroy()
		
	def updateGauge7Window(self):
		self.gauge7WindowTopLabel.set_text("Gauge 7:{0}".format(mcp.read_adc(6)))
		if currentWindowDisplayed is not 70:
			return False
	
	def gauge7WindowSetup(self):
		# create the fullscreen window
		self.gauge7Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge7Window.connect("delete_event", self.close_application)
		self.gauge7Window.set_border_width(100)
		self.gauge7Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge7Window.fullscreen()
		self.gauge7Window.show()
		
		self.gauge7VBox1 = gtk.VBox(False, 0)
		self.gauge7Window.add(self.gauge7VBox1)
		self.gauge7VBox1.show()
		
		self.gauge7HBox1 = gtk.HBox(False,0)
		self.gauge7VBox1.pack_start(self.gauge7HBox1)
		self.gauge7HBox1.show()
		
		self.gauge7WindowTopLabel = gtk.Label()
		self.gauge7WindowTopLabel.set_text("Gauge 7:{0}".format(mcp.read_adc(6)))
		self.gauge7HBox1.pack_start(self.gauge7WindowTopLabel)
		self.gauge7WindowTopLabel.show()
		
		self.gauge7WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge7HBox1.pack_start(self.gauge7WindowBackToMainButton)
		self.gauge7WindowBackToMainButton.show()
		self.gauge7WindowBackToMainButton.connect("clicked",self.gauge7BackToMainCallback)
		
		gobject.idle_add(self.updateGauge7Window)
	
	def gauge7BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge7Window.destroy()

	def updateGauge8Window(self):
		self.gauge8WindowTopLabel.set_text("Gauge 8:{0}".format(mcp.read_adc(7)))
		if currentWindowDisplayed is not 80:
			return False
	
	def gauge8WindowSetup(self):
		# create the fullscreen window
		self.gauge8Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.gauge8Window.connect("delete_event", self.close_application)
		self.gauge8Window.set_border_width(100)
		self.gauge8Window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6700))
		self.gauge8Window.fullscreen()
		self.gauge8Window.show()
		
		self.gauge8VBox1 = gtk.VBox(False, 0)
		self.gauge8Window.add(self.gauge8VBox1)
		self.gauge8VBox1.show()
		
		self.gauge8HBox1 = gtk.HBox(False,0)
		self.gauge8VBox1.pack_start(self.gauge8HBox1)
		self.gauge8HBox1.show()

		self.gauge8WindowTopLabel = gtk.Label()
		self.gauge8WindowTopLabel.set_text("Gauge 8:{0}".format(mcp.read_adc(7)))
		self.gauge8HBox1.pack_start(self.gauge8WindowTopLabel)
		self.gauge8WindowTopLabel.show()
		
		self.gauge8WindowBackToMainButton = gtk.Button(label="MAIN")
		self.gauge8HBox1.pack_start(self.gauge8WindowBackToMainButton)
		self.gauge8WindowBackToMainButton.show()
		self.gauge8WindowBackToMainButton.connect("clicked",self.gauge8BackToMainCallback)
		
		gobject.idle_add(self.updateGauge8Window)
	
	def gauge8BackToMainCallback(self, timeout):

		self.backToMainWindowCallback()
		self.gauge8Window.destroy()
	
	def debugInputsWindow(self, timeout):
		global channelOneValue
		global debugInputsWindowDoPauseReading
		
		self.applicationDebugWindowOpen = True
		

		
		# create new window
		self.debugInputsWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		
		# set title
		self.debugInputsWindow.set_title("DEBUG Inputs Window")
		
		
		# set window border
		self.debugInputsWindow.set_border_width(100)
		
		# create vertical layout
		self.debugInputsWindowVertBox1 = gtk.VBox(False, 0)
		
		# create horizontal layout
		self.debugInputsWindowHorizButtonBox1 = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelOneBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelTwoBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelThreeBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelFourBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelFiveBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelSixBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelSevenBox = gtk.HBox(False, 0)
		self.debugInputsWindowHorizChannelEightBox = gtk.HBox(False, 0)
		
		# create button
		self.debugInputsWindowButton1 = gtk.Button(label="Pause Readings")
		# connect button clicked recieved signal to call hello function
		self.debugInputsWindowButton1.connect("clicked", self.debugInputsWindowPauseReadingsClicked, "Pause Readings")
		# pack button into box
		self.debugInputsWindowHorizButtonBox1.pack_start(self.debugInputsWindowButton1, True, True, 0)
		# also make the window disappear when clicked
		#self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
		# display button
		self.debugInputsWindowButton1.show()
		

		
		self.channelOneLabel = gtk.Label("Channel 1: {0}".format(mcp.read_adc(0)))
		self.channelOneLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelOneBox.pack_start(self.channelOneLabel, True, True, 0)
		self.channelOneLabel.show()
		self.channelOneDescriptionLabel = gtk.Label("Channel 1 Average: {0}".format(mcp.read_adc(0)))
		self.channelOneDescriptionLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelOneBox.pack_start(self.channelOneDescriptionLabel, True, True, 0)
		self.channelOneDescriptionLabel.show()
		
		self.channelTwoLabel = gtk.Label("Channel 2: {0}".format(mcp.read_adc(1)))
		self.channelTwoLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelTwoBox.pack_start(self.channelTwoLabel, True, True, 0)
		self.channelTwoLabel.show()
		
		self.channelThreeLabel = gtk.Label("Channel 3: {0}".format(mcp.read_adc(2)))
		self.channelThreeLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelThreeBox.pack_start(self.channelThreeLabel, True, True, 0)
		self.channelThreeLabel.show()
		
		self.channelFourLabel = gtk.Label("Channel 4: {0}".format(mcp.read_adc(3)))
		self.channelFourLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelFourBox.pack_start(self.channelFourLabel, True, True, 0)
		self.channelFourLabel.show()
		
		self.channelFiveLabel = gtk.Label("Channel 5: {0}".format(mcp.read_adc(4)))
		self.channelFiveLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelFiveBox.pack_start(self.channelFiveLabel, True, True, 0)
		self.channelFiveLabel.show()
		
		self.channelSixLabel = gtk.Label("Channel 6: {0}".format(mcp.read_adc(5)))
		self.channelSixLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelSixBox.pack_start(self.channelSixLabel, True, True, 0)
		self.channelSixLabel.show()
		
		self.channelSevenLabel = gtk.Label("Channel 7: {0}".format(mcp.read_adc(6)))
		self.channelSevenLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelSevenBox.pack_start(self.channelSevenLabel, True, True, 0)
		self.channelSevenLabel.show()
		
		self.channelEightLabel = gtk.Label("Channel 8: {0}".format(mcp.read_adc(7)))
		self.channelEightLabel.set_alignment(0.5,0.5)
		self.debugInputsWindowHorizChannelEightBox.pack_start(self.channelEightLabel, True, True, 0)
		self.channelEightLabel.show()
		

		
		# show the horizontal boxes
		self.debugInputsWindowHorizButtonBox1.show()
		self.debugInputsWindowHorizChannelOneBox.show()
		self.debugInputsWindowHorizChannelTwoBox.show()
		self.debugInputsWindowHorizChannelThreeBox.show()
		self.debugInputsWindowHorizChannelFourBox.show()
		self.debugInputsWindowHorizChannelFiveBox.show()
		self.debugInputsWindowHorizChannelSixBox.show()
		self.debugInputsWindowHorizChannelSevenBox.show()
		self.debugInputsWindowHorizChannelEightBox.show()
		
		# add horizontal box to vertical box
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizButtonBox1)
		
		#separator
		self.firstSeparator = gtk.HSeparator()
		self.debugInputsWindowVertBox1.add(self.firstSeparator)
		self.firstSeparator.show()
		
		# add the horizontal channel boxes
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelOneBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelTwoBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelThreeBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelFourBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelFiveBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelSixBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelSevenBox)
		self.debugInputsWindowVertBox1.add(self.debugInputsWindowHorizChannelEightBox)
		
		#show the vert box layout
		self.debugInputsWindowVertBox1.show()
		self.debugInputsWindow.add(self.debugInputsWindowVertBox1)
		
		#show the window
		self.debugInputsWindow.show()
		
		self.channelOneValues = []
		self.channelTwoValues = []
		self.channelThreeValues = []
		self.channelFourValues = []
		self.channelFiveValues = []
		self.channelSixValues = []
		self.channelSevenValues = []
		self.channelEightValues = []
		
		# use gobject to do the reoccurance
		gobject.idle_add(self.updateInputs)
	
	def debugInputsWindowPauseReadingsClicked(self):
		global debugInputsWindowDoPauseReading
		debugInputsWindowDoPauseReading = not debugInputsWindowDoPauseReading
	
	def updateInputs(self):
		def mean(numbers):
			if len(numbers) > 1:
				return float(sum(numbers) / len(numbers))
			else:
				print(len(numbers))
				return 1

		# Software SPI configuration:
		CLK  = 6
		MISO = 13
		MOSI = 19
		CS   = 26
		mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		

		
		channelOneValues.insert(0, mcp.read_adc(0))
		if len(channelOneValues) > 19:
			del(channelOneValues[19:20])
		#self.channelOneAverage = 0
		#for value in channelOneValues:
		#	self.channelOneAverage += value
		self.channelOneAverage = mean(channelOneValues)
		print("average: {0} ".format(self.channelOneAverage))
		print("contains {0} members".format(len(channelOneValues)))
		
		# Update text on screen
		self.channelOneLabel.set_text("Channel 1: {0}".format(mcp.read_adc(0)))
		self.channelOneDescriptionLabel.set_text("Channel 1 Average: {0}".format(self.channelOneAverage))
		self.channelTwoLabel.set_text("Channel 2: {0}".format(mcp.read_adc(1)))
		self.channelThreeLabel.set_text("Channel 3: {0}".format(mcp.read_adc(2)))
		self.channelFourLabel.set_text("Channel 4: {0}".format(mcp.read_adc(3)))
		self.channelFiveLabel.set_text("Channel 5: {0}".format(mcp.read_adc(4)))
		self.channelSixLabel.set_text("Channel 6: {0}".format(mcp.read_adc(5)))
		self.channelSevenLabel.set_text("Channel 7: {0}".format(mcp.read_adc(6)))
		self.channelEightLabel.set_text("Channel 8: {0}".format(mcp.read_adc(7)))
		
		return True
	def main(self):

		#self.updateInputs()
		gtk.main()
		return 0


if __name__ == '__main__':
	base = CarputerPrototype(1)

	base.main()
	#gtk.main()

