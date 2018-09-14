Davinci Resolve Clip Lister

DaVinci Resolve V15 introduced the scripting API allowing user to automate traditionally manual procedures via Python or Lua.

This script saves master bin clips and certain metadata to CSV and HTML files. Similar user assisted functionality already exists in Resolve. The purpose of this script is to demonstrate the possibility of automating such process.

Requirements and Dependencies

You need Resolve V15, of course as well as Python. You also need to add several system environment variables described in the API documentation. Alternately you can make your Python script aware of the location of the fusionscript.dll (fusionscript.so) and DaVinciResolveScript.py which are installed along with DaVinci Resolve v15.

Update September 13, 2018

The GetFrameRate() and GetDuration() methods from the public beta release of Resolve 15 have been deprecated in the Resolve V15 official release.

They have been replaced with GetClipProperty() method.
