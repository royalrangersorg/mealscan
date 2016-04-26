#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import os
import datetime
import time
import pyglet
import json
import requests


class MScan(wx.Dialog):

    def __init__(
        self,
        parent,
        id,
        title,
        ):

        self.dlg = wx.Dialog.__init__(self, parent, id, title,
                size=(1200, 800))

	with open('settings.json') as data_file:
    		self.settings = json.load(data_file)

        self.dest = os.path.dirname(os.path.realpath('__file__')) \
            + '/mealscan.txt'

        if os.path.exists(self.dest) == False:
            with open(self.dest, 'w') as f:
                f.write('')
                f.close()

        self.meals = {}
        self.meals['BFAST'] = "Breakfast"
        self.meals["LUNCH"] = "Lunch"
        self.meals["DINNR"] = "Dinner"

        self.scans = []

        self.btn1 = wx.Button(self, 5, 'Check', (500, 250), (100, 25))
        font2 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.btn1.SetFont(font2)

        self.txt = wx.TextCtrl(self, 4, '', (100, 250), (400, 25))
        font3 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.txt.SetFont(font3)

        self.Bind(wx.EVT_BUTTON, self.MyPress, self.btn1)
        self.txt.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

        self.label1 = wx.StaticText(
            self,
            1,
            'Please Scan the Tag',
            (10, 10),
            (100, 30),
            wx.ALIGN_LEFT,
            )
        font1 = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.label1.SetFont(font1)

        self.label2 = wx.StaticText(
                                    self,
                                    1,
                                    '',
                                    (100, 290),
                                    (300, 300),
                                    wx.ALIGN_LEFT,
                                    )
        font3 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.label2.SetFont(font3)

        self.label = wx.StaticText(
            self,
            2,
            '',
            (100, 160),
            (500, 80),
             wx.ALIGN_CENTRE_HORIZONTAL,
            )
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)
        self.Centre()
        self.txt.SetFocus()
        fr = self.ShowModal()

        # fr.ShowFullScreen()

        self.Destroy()

    def MyPress(self, event):
    	  val = self.txt.GetValue()

          if (not val):
                return

          if self.SetTag(val):
                self.label.SetBackgroundColour('green')
                self.label.SetLabel('Tag [' + val + '] Accepted!')

          else:
                self.label.SetBackgroundColour('red')
                self.label.SetLabel(
                    'Tag [' + val + '] already scanned for ' + self.meals[self.CurrentMeal()])

          self.txt.SetValue('')

    def CurrentMeal(self):
        hr = int(time.strftime('%H', time.localtime()))
        ml = ''
        if hr > 15 and hr < 25:
            ml = 'DINNR'
        if hr > 10 and hr < 16:
            ml = 'LUNCH'
        if hr > 5 and hr < 11:
            ml = 'BFAST'
        return ml

    def beep(self):

	mus = "bell.wav"
	music = pyglet.resource.media(mus)
	music.play()
#	pyglet.app.run()
# app.MainLoop()

    def SetTag(self, code):
            ml = self.CurrentMeal()
            dt = time.strftime('%Y-%m-%d', time.localtime())  # %H:%M:%S
            tm = time.strftime('%H:%M:%S', time.localtime())  # %H:%M:%S
            data = dt + '|' + ml + '|' + code
            test = data + "|"

            self.scans.append(code)

            payload = {'meal': ml, 'code': code, 'location': self.settings[
                'location'], 'date': dt, 'time': tm}

      

            if len(self.scans) > 10:
                    self.scans = self.scans[
                        len(self.scans) - 10:len(self.scans)]
            self.label2.SetLabel("Last 10 Scans:\n\n" +
                                 "\n".join(reversed(self.scans)))

            if self.settings['localonly'] == True:

            	print "Running local only"

                if test in open(self.dest).read():
	            	print "FAIL-" + data + "|" + tm

	                self.beep()

	                return False
	                
                else:
	                
	                with open(self.dest, 'ab') as f:
	                    f.write(data + "|"+tm+'\n')
	
	                    print "PASS-"+data + "|"+tm
	                return True
            else:
            
                print "Remote check"
                
                resp = {}
                
                try:
                    r = requests.post(self.settings['host'], data=payload)
                    resp = json.loads(r.text)
                
                
                
                except Exception as e:
                    print "Unable to make http connection"
                    
                    if test in open(self.dest).read():
                        resp['pass'] = False
                       
                    else:
                        
                        resp['pass'] = True
                        
                
         
                
                if resp['pass']==False:
	            	print "FAIL-" + data + "|" + tm

	                self.beep()

	                return False
	                
                else:
	                
	                with open(self.dest, 'ab') as f:
	                    f.write(data + "|"+tm+'\n')
                        
                        print "PASS-"+data + "|"+tm
	                return True
                
                

	        	

    def onKeyPress(self, event):
        keycode = event.GetKeyCode()

        # print keycode

        if keycode == wx.WXK_RETURN:
            # print 'you pressed enter!'
            # print self.txt.GetValue()
            val = self.txt.GetValue()

            if self.SetTag(val):
                self.label.SetBackgroundColour('green')
                self.label.SetLabel('Tag ['+val+'] Accepted!')
            else:
                self.label.SetBackgroundColour('red')
                self.label.SetLabel('Tag ['+val+'] already scanned for '+ self.meals[self.CurrentMeal()])

            self.txt.SetValue('')

        event.Skip()


app = wx.App(0)
MScan(None, -1, 'Meal Scan 1.0')
app.MainLoop()