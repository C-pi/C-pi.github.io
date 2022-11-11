import datetime
import os
import subprocess

process = subprocess.Popen("vim _temp_blog", shell=True)
process.wait()
sourcefile=open("_temp_blog","r")
sourcetext=sourcefile.read().split('\n')
sourcefile.close()
date=datetime.datetime
blogname=sourcetext[0]

filename=str(date.now()).split()[0]+"-"+blogname.replace(" ","-")+".markdown"
blogfile=open(filename,"x")

frontmatter=f'''--- 
layout: post 
title: {blogname}  
date:  {date.now()} 
categories: simple blog post 
--- 
'''

blogpost='\n'.join(sourcetext[1:])

blogfile.write(frontmatter+blogpost)
blogfile.close()
os.remove("_temp_blog")
