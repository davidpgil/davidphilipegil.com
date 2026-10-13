import os
H=globals().get('H') or os.path.dirname(os.path.abspath(__file__))
import json,html,os
from PIL import Image
D=json.load(open(os.path.join(H,'projects.json')))
S=os.path.dirname(H)
order=['PSD Localization Extendscript','Multipage Dynamic Casino Game Rules','Casino Game Production','Luxury Banner & Email','Cryptocurrency Believe in someETHing','Instructional Video','Chinese Casino Game Logos','Pixel UI and Environments','Game Pixel Art','Bird Character Frames','Papercraft Pirate Ships','Cosmic Human Design']
meta={
'PSD Localization Extendscript':('Localization Pipeline Script','Tools & Automation','A script that translates a specially formatted Photoshop file based on a specially formatted JSON file, built while working at High 5 Games. The video shows the script in action.'),
'Multipage Dynamic Casino Game Rules':('Multipage Dynamic Game Rules','Tools & Automation','These pages were laid out in HTML5. High 5 Games needed the final pages as JPEGs, so I wrote scripts that capture image snapshots of the HTML layout using PhantomJS, a scriptable headless web browser.'),
'Casino Game Production':('Casino Game Production','Motion','Motion graphics and game art production for casino games.'),
'Luxury Banner & Email':('Luxury Banner & Email','Marketing Design','Banner and email marketing design for a luxury brand.'),
'Cryptocurrency Believe in someETHing':('Believe in someETHing','Motion','An animated cryptocurrency piece about Ethereum.'),
'Instructional Video':('Instructional Video','Motion','Instructional video titled “How does a predictive model work?”'),
'Chinese Casino Game Logos':('Chinese Casino Game Logos','Game Art','Logo designs for Chinese-themed casino games.'),
'Pixel UI and Environments':('Pixel UI and Environments','Game Art','Pixel art user interface and environments for a mobile game.'),
'Game Pixel Art':('Game Pixel Art','Game Art','Pixel art for a mobile rhythm game.'),
'Bird Character Frames':('Bird Character Frames','Game Art','Child-like paper cut-out styled character sprites for an unreleased mobile game.'),
'Papercraft Pirate Ships':('Papercraft Pirate Ships','Illustration','Vector pirate ships designed in a papercraft style.'),
'Cosmic Human Design':('Cosmic Human Design','Illustration','A cosmic human design illustration.'),
}
textmap={'Pixel UI and Environments':['A composition of the different environments in the game.','The following are avatars created for a sister game named Cube Buddies.']}
byname={d['name']:d for d in D}
P=[byname[n] for n in order]
for p in P: p['slug2']=p['slug'].lower(); p['title'],p['cat'],p['summary']=meta[p['name']]
