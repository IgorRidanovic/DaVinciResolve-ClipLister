#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve scripting proof of concept. Make website from clip names. 
# Refer to Resolve V15 public beta 2 scripting API documentation for host setup.
# Copyright 2018 Igor Riđanović, www.hdhead.com

import DaVinciResolveScript
import csv
from operator import itemgetter

def getclipinfo(c):
	counter = 1

	# Set header row
	cTable  = [['#', 'Clip Name', 'Type', 'FPS', 'Duration', 'Resolution']]

	# Convert dictionary to list and iterate to get values. 
	clips = c.values()
	for i in clips:

		cFPS = i.GetFrameRate()
		cFPS = str(round(cFPS, 2))

		cDur = i.GetDurationInFrames()
		if cDur != None:
			cDur = str(int(cDur))

		cRes = i.GetResolution()
		if cRes != None:
			cRes = str(int(cRes[1.0])) + ' x ' + str(int(cRes[2.0]))

		cTable.append([str(counter), i.GetName(), i.GetType(), cFPS, cDur, cRes])
		counter += 1
	
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




