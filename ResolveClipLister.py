#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve scripting proof of concept. Make website from clip names. 
# Refer to Resolve V15 public beta 2 scripting API documentation for host setup.
# Copyright 2018 Igor Riđanović, www.hdhead.com

import DaVinciResolveScript
import csv

def getclipinfo(c):

	# Set header row
	cTable = [['#', 'Clip Name', 'Type', 'FPS', 'Duration', 'Resolution']]

	# Iterate through clips dictionary and get values.  
	# The keys start with 1.0 float for the first clip.
	for i in range(1, len(c) + 1):
		cName = c[float(i)].GetName()
		cType = c[float(i)].GetType()
		cFPS  = c[float(i)].GetFrameRate()
		cFPS  = str(round(cFPS, 2))

		cDur     = c[float(i)].GetDurationInFrames()
		if cDur != None:
			cDur = str(int(cDur))

		cRes     = c[float(i)].GetResolution()
		if cRes != None:
			cRes = str(int(cRes[1.0])) + ' x ' + str(int(cRes[2.0]))

		cTable.append([str(i), cName, cType, cFPS, cDur, cRes])
		
	return cTable

# Export CSV
def exportcsv(t):
	with open('clips.csv', 'wb') as csvfile:
		w = csv.writer(csvfile)
		w.writerows(t)

# Export HTML. Non-compliant but most browsers don't care.
def exporthtml(t):
	with open('clips.html', 'wb') as htmlfile:
		htmlfile.write('<table cellpadding = "5" width = 75%>')
		for c in t:
			htmlfile.write('<tr>')
			for i in c:
				htmlfile.write('<td>' + str(i) + '</td>')
			htmlfile.write('</tr>')
		htmlfile.write('</table>')
        
if __name__ == '__main__':

	# Instantiate Resolve objects
	resolve = DaVinciResolveScript.scriptapp('Resolve')
	pm      = resolve.GetProjectManager()
	proj    = pm.GetCurrentProject()
	mp      = proj.GetMediaPool()
	folder  = mp.GetRootFolder()
	clips   = folder.GetClips()

	clipList = getclipinfo(clips)

	# Outputs
	exportcsv(clipList)
	exporthtml(clipList)




