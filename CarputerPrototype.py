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
		
		global channelOneValue
		
		# Software SPI configuration:
		CLK  = 6
		MISO = 13
		MOSI = 19
		CS   = 26
		mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		
		# create new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		
		# set title
		self.window.set_title("Hello buttons!")
		
		# connect delete_event to function
		self.window.connect("delete_event", self.delete_event)
		
		# link the 'destroy' callback to removing the window
		self.window.connect("destroy", self.destroy)
		
		# set window border
		self.window.set_border_width(10)
		
		# create vertical layout
		self.vertBox1 = gtk.VBox(False, 0)
		
		# create horizontal layout
		self.horizButtonBox1 = gtk.HBox(False, 0)
		self.horizChannelOneBox = gtk.HBox(False, 0)
		self.horizChannelTwoBox = gtk.HBox(False, 0)
		self.horizChannelThreeBox = gtk.HBox(False, 0)
		self.horizChannelFourBox = gtk.HBox(False, 0)
		self.horizChannelFiveBox = gtk.HBox(False, 0)
		self.horizChannelSixBox = gtk.HBox(False, 0)
		self.horizChannelSevenBox = gtk.HBox(False, 0)
		self.horizChannelEightBox = gtk.HBox(False, 0)
		
		# create button
		self.button1 = gtk.Button(label="Hello World")
		# connect button clicked recieved signal to call hello function
		self.button1.connect("clicked", self.callback, "button 1")
		# pack button into box
		self.horizButtonBox1.pack_start(self.button1, True, True, 0)
		# also make the window disappear when clicked
		#self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
		# display button
		self.button1.show()
		
		self.button2 = gtk.Button("Button 2")
		self.button2.connect("clicked", self.callback, "button 2")
		self.horizButtonBox1.pack_start(self.button2, True, True, 0)
		self.button2.show()
		

		
		self.channelOneLabel = gtk.Label("Channel 1: {0}".format(mcp.read_adc(0)))
		self.channelOneLabel.set_alignment(0.5,0.5)
		self.horizChannelOneBox.pack_start(self.channelOneLabel, True, True, 0)
		self.channelOneLabel.show()
		self.channelOneDescriptionLabel = gtk.Label("Channel 1 Average: {0}".format(mcp.read_adc(0)))
		self.channelOneDescriptionLabel.set_alignment(0.5,0.5)
		self.horizChannelOneBox.pack_start(self.channelOneDescriptionLabel, True, True, 0)
		self.channelOneDescriptionLabel.show()
		
		self.channelTwoLabel = gtk.Label("Channel 2: {0}".format(mcp.read_adc(1)))
		self.channelTwoLabel.set_alignment(0.5,0.5)
		self.horizChannelTwoBox.pack_start(self.channelTwoLabel, True, True, 0)
		self.channelTwoLabel.show()
		
		self.channelThreeLabel = gtk.Label("Channel 3: {0}".format(mcp.read_adc(2)))
		self.channelThreeLabel.set_alignment(0.5,0.5)
		self.horizChannelThreeBox.pack_start(self.channelThreeLabel, True, True, 0)
		self.channelThreeLabel.show()
		
		self.channelFourLabel = gtk.Label("Channel 4: {0}".format(mcp.read_adc(3)))
		self.channelFourLabel.set_alignment(0.5,0.5)
		self.horizChannelFourBox.pack_start(self.channelFourLabel, True, True, 0)
		self.channelFourLabel.show()
		
		self.channelFiveLabel = gtk.Label("Channel 5: {0}".format(mcp.read_adc(4)))
		self.channelFiveLabel.set_alignment(0.5,0.5)
		self.horizChannelFiveBox.pack_start(self.channelFiveLabel, True, True, 0)
		self.channelFiveLabel.show()
		
		self.channelSixLabel = gtk.Label("Channel 6: {0}".format(mcp.read_adc(5)))
		self.channelSixLabel.set_alignment(0.5,0.5)
		self.horizChannelSixBox.pack_start(self.channelSixLabel, True, True, 0)
		self.channelSixLabel.show()
		
		self.channelSevenLabel = gtk.Label("Channel 7: {0}".format(mcp.read_adc(6)))
		self.channelSevenLabel.set_alignment(0.5,0.5)
		self.horizChannelSevenBox.pack_start(self.channelSevenLabel, True, True, 0)
		self.channelSevenLabel.show()
		
		self.channelEightLabel = gtk.Label("Channel 8: {0}".format(mcp.read_adc(7)))
		self.channelEightLabel.set_alignment(0.5,0.5)
		self.horizChannelEightBox.pack_start(self.channelEightLabel, True, True, 0)
		self.channelEightLabel.show()
		

		
		# show the horizontal boxes
		self.horizButtonBox1.show()
		self.horizChannelOneBox.show()
		self.horizChannelTwoBox.show()
		self.horizChannelThreeBox.show()
		self.horizChannelFourBox.show()
		self.horizChannelFiveBox.show()
		self.horizChannelSixBox.show()
		self.horizChannelSevenBox.show()
		self.horizChannelEightBox.show()
		
		# add horizontal box to vertical box
		self.vertBox1.add(self.horizButtonBox1)
		
		#separator
		self.firstSeparator = gtk.HSeparator()
		self.vertBox1.add(self.firstSeparator)
		self.firstSeparator.show()
		
		# add the horizontal channel boxes
		self.vertBox1.add(self.horizChannelOneBox)
		self.vertBox1.add(self.horizChannelTwoBox)
		self.vertBox1.add(self.horizChannelThreeBox)
		self.vertBox1.add(self.horizChannelFourBox)
		self.vertBox1.add(self.horizChannelFiveBox)
		self.vertBox1.add(self.horizChannelSixBox)
		self.vertBox1.add(self.horizChannelSevenBox)
		self.vertBox1.add(self.horizChannelEightBox)
		
		#show the vert box layout
		self.vertBox1.show()
		self.window.add(self.vertBox1)
		
		#show the window
		self.window.show()
		
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
	#def main(self):

		#self.updateInputs()
		#gtk.main()
		#return 0


if __name__ == '__main__':
	base = CarputerPrototype(1)

	#base.main()
	gtk.main()

