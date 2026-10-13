import os
H=os.path.dirname(os.path.abspath(__file__))
import json,html,re
exec(open(os.path.join(H,'_meta.py')).read())
S=os.path.dirname(H)
import time
VER=time.strftime('%Y%m%d%H%M%S')
D2={d['name']:d for d in json.load(open(os.path.join(H,'projects.json')))}
for p in P: p['hero']=D2[p['name']]['hero']
PIX={'Game Pixel Art','Pixel UI and Environments'}
CONTAIN={'Bird Character Frames','Game Pixel Art'}
SIZE={'PSD Localization Extendscript':'w8 h2','Luxury Banner & Email':'h2','Cryptocurrency Believe in someETHing':'w8','Game Pixel Art':'h2','Casino Game Production':'','Multipage Dynamic Casino Game Rules':''}
HOMESIZE={'PSD Localization Extendscript':'w8 h2'}
NAV=[('index.html','Home'),('projects.html','Work'),('resume.html','Resume'),('contact.html','Contact')]
E=html.escape
ARR='<svg class="ar" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def page(title,body,depth=0,active='',desc='David Philipe Gil, Creative Technologist and Technical Artist building tools and automation for creative teams.',extra=''):
  r='../'*depth
  nav=''.join((f'<a href="/David_Philipe_Gil_Resume.pdf" target="_blank" rel="noopener">{t}</a>' if t=='Resume' else f'<a href="{r}{h}"{" aria-current=\"page\"" if t==active else ""}>{t}</a>') for h,t in NAV)
  return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="theme-color" content="#05070d">
<link rel="preload" href="{r}fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{r}fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}style.css?v={VER}"><link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website">{extra}
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap bar"><a class="brand" href="{r}index.html"><i aria-hidden="true">DPG</i>David Philipe Gil</a><button class="menu" aria-expanded="false" aria-controls="nav">Menu</button><nav class="main" id="nav" aria-label="Main">{nav}</nav></div></header>
<main id="main">{body}</main>
<footer class="site"><div class="wrap foot"><span>© 2026 David Philipe Gil · Creative Technologist</span><nav aria-label="Social"><a href="mailto:davidpgil@protonmail.com">Email</a><a href="https://www.linkedin.com/in/davidpgil/">LinkedIn</a><a href="https://github.com/davidpgil">GitHub</a></nav></div></footer>
<script src="{r}app.js?v={VER}" defer></script></body></html>'''
def img(src,size,alt,r='',cls='',eager=False,pix=False):
  w,h=size; c=(cls+(' pixel' if pix else '')).strip()
  return f'<img{" class=%s"%chr(34)+c+chr(34) if c else ""} src="{r}{src}" width="{w}" height="{h}" alt="{E(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async">'
def tile(p,size,r=''):
  cls=('tile rv '+size+(' contain' if p['name'] in CONTAIN else '')).strip()
  return f'<a class="{cls}" data-cat="{p["cat"]}" href="{r}projects/{p["slug2"]}.html"><div class="ph">{img(p["cover_local"],p["cover_size"],p["title"]+" cover",r,eager=False,pix=p["name"] in PIX).replace(' src=',' sizes="'+('(max-width:720px) 100vw, 66vw' if 'w8' in size else '(max-width:720px) 100vw, (max-width:1000px) 50vw, 33vw')+'" srcset="'+r+p['cover_local'].replace('-cover.webp','-cover-sm.webp')+' 480w, '+r+p['cover_local']+' 900w" src=',1)}</div><span class="arr">{ARR}</span><div class="meta"><span class="cat">{p["cat"]}</span><h3>{E(p["title"])}</h3><p class="tools">{E(" · ".join(p["tools"]))}</p></div></a>'
tools=['Python','JavaScript','Adobe ExtendScript','Photoshop','After Effects','Illustrator','HTML5','ComfyUI','Stable Diffusion','Spine','Git','Perforce']
mq='<div class="marq" aria-hidden="true"><div>'+''.join(f'<span>{t}</span>' for t in tools*2)+'</div></div>'
caps=[('Creative tools','Python, JavaScript, and ExtendScript tools that automate repeatable production work for artists.'),('Pipelines','JSON-driven localization and HTML5 layout systems with scripted export to production.'),('Generative AI','ComfyUI and Stable Diffusion workflows, plus agent harnesses and local agentic LLM inference.'),('Enablement','Onboarding, troubleshooting, artist training, and clear workflow guides that teams repeat with confidence.')]
home=f'''<section class="hero"><div class="bgf" aria-hidden="true"></div><canvas class="fx" aria-hidden="true"></canvas><div class="wrap">
<span class="eyebrow">Creative Technologist · Technical Artist</span>
<h1 class="disp">Tools and automation for <span class="gt">creative teams.</span></h1>
<p class="lede">I build scripts, pipelines, and workflows that give artists more time for creative work, built on years of production in Python, JavaScript, Adobe ExtendScript, HTML5, and the Adobe Creative Cloud.</p>
<div class="ctas"><a class="btn pri mag" href="projects.html">View work {ARR}</a><a class="btn ghost mag" href="/David_Philipe_Gil_Resume.pdf" target="_blank" rel="noopener">Resume</a></div></div><span class="scrollhint">Scroll</span></section>
{mq}
<section class="sec"><div class="wrap"><div class="sh rv"><div><span class="eyebrow">Portfolio work</span><h2 class="big disp">Available now.<br><span class="gt" style="display:block;font-size:.6em;line-height:1.05;margin-top:.25em">Let’s build better tools for your team.</span></h2></div><a class="link" href="projects.html">All projects <span class="ar" aria-hidden="true">→</span></a></div>
<div class="bento feat">{"".join(tile(p,HOMESIZE.get(p["name"],"")) for p in P[:6])}</div><script>window.FEAT={{FEATJSON}}</script></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="sh rv"><div><span class="eyebrow">Capabilities</span><h2 class="big disp">What I bring.</h2></div></div>
<div class="caps">{"".join(f'<div class="cap rv"><b>0{i+1}</b><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(caps))}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="band rv"><span class="eyebrow">Get in touch</span><h2 class="disp" style="margin-top:20px">Let’s <span class="gt">talk.</span></h2><div class="ctas"><a class="btn pri mag" href="contact.html">Get in touch {ARR}</a><a class="btn ghost mag" href="/David_Philipe_Gil_Resume.pdf" target="_blank" rel="noopener">Resume</a></div></div></div></section>'''
FEATJSON=json.dumps([dict(u='projects/'+p['slug2']+'.html',i=p['cover_local'],s=p['cover_local'].replace('-cover.webp','-cover-sm.webp')+' 480w, '+p['cover_local']+' 900w',c=p['cat'],t=p['title'],o=' · '.join(p['tools']),k=int(p['name'] in CONTAIN),x=int(p['name'] in PIX)) for p in P],ensure_ascii=False).replace('</','<\\/')
home=home.replace('{FEATJSON}',FEATJSON)
open(f'{S}/index.html','w').write(page('David Philipe Gil · Creative Technologist',home,active='Home'))
cats=[]
[cats.append(p['cat']) for p in P if p['cat'] not in cats]
filt='<div class="filters rv" role="group" aria-label="Filter projects"><button aria-pressed="true" data-f="all">All</button>'+''.join(f'<button aria-pressed="false" data-f="{c}">{c}</button>' for c in cats)+'</div>'
work=f'''<section class="ph1"><div class="wrap"><span class="eyebrow">Work · {len(P)} projects</span><h1 class="disp">Portfolio <span class="gt">work.</span></h1><p class="lede">Creative tools, game art, motion, and marketing design.</p></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap">{filt}<div class="bento" style="grid-auto-flow:dense">{"".join(tile(p,SIZE.get(p["name"],"")) for p in P)}</div></div></section>'''
open(f'{S}/projects.html','w').write(page('Work · David Philipe Gil',work,active='Work'))
for i,p in enumerate(P):
  r='../'; parts=[]; texts=list(textmap.get(p['name'],[])); pix=p['name'] in PIX
  for b in p['blocks']:
    if b['t']=='text':
      if texts: parts.append(f'<p class="note rv">{E(texts.pop(0))}</p>')
    elif b['t']=='video' and b['src']:
      src=b['src'].replace('&amp;','&').replace('www.youtube.com','www.youtube-nocookie.com')
      parts.append(f'<div class="video rv"><iframe src="{E(src)}" title="{E(p["title"])} video" loading="lazy" allow="fullscreen" allowfullscreen></iframe></div>')
    elif b.get('local'):
      ims=b['local']; cls='gallery' if len(ims)>1 else 'single'
      inner=f'<div class="{cls}">'+''.join(img(s,sz,f'{p["title"]} image {k+1}',r,pix=pix or sz[0]<=520) for k,(s,sz) in enumerate(ims))+'</div>'
      parts.append(f'<div class="frame rv">{inner}</div>' if pix else inner.replace(f'class="{cls}"',f'class="{cls} rv"',1))
  pv,nx=P[i-1],P[(i+1)%len(P)]
  hs,hz=p['hero']
  body=f'''<section class="chero"><div class="blur" style="background-image:url(../{hs})" aria-hidden="true"></div>
<div class="wrap"><a class="back" href="../projects.html"><span class="ar al" aria-hidden="true">←</span> All work</a><br><span class="eyebrow">{p["cat"]}</span><h1 class="disp">{E(p["title"])}</h1></div>
<div class="wrap"><div class="stage{' pix' if pix else ''}">{img(hs,hz,p["title"]+" key image",r,eager=True,pix=pix)}</div></div></section>
<article class="wrap"><div class="intro rv"><p>{E(p["summary"])}</p><dl class="facts"><div><dt>Discipline</dt><dd>{p["cat"]}</dd></div><div><dt>Tools</dt><dd class="chips">{"".join(f"<span>{E(t)}</span>" for t in p["tools"])}</dd></div></dl></div>
<div class="media">{"".join(parts)}</div>
<nav class="pn" aria-label="More projects"><a href="{pv["slug2"]}.html">{img(pv["cover_local"],pv["cover_size"],"",r)}<small><span class="ar al" aria-hidden="true">←</span> Previous</small><strong>{E(pv["title"])}</strong></a><a class="nx" href="{nx["slug2"]}.html">{img(nx["cover_local"],nx["cover_size"],"",r)}<small>Next <span class="ar" aria-hidden="true">→</span></small><strong>{E(nx["title"])}</strong></a></nav></article>
<dialog class="lb" aria-label="Image viewer"><img alt=""><button class="x" aria-label="Close">×</button><button class="p" aria-label="Previous image">←</button><button class="n" aria-label="Next image">→</button></dialog>'''
  open(f'{S}/projects/{p["slug2"]}.html','w').write(page(f'{p["title"]} · David Philipe Gil',body,1,'Work',p['summary'],f'<meta property="og:image" content="https://davidphilipegil.com/{p["cover_local"]}">'))
jobs=[('Technical Artist','High 5 Games','Feb 2018 – Jul 2025','New York, NY',['Owned tool support for artists: install help, onboarding, triage, troubleshooting, and fixes','Built Python, JavaScript, and ExtendScript tools that automated repeatable production work','Built a JSON-driven Photoshop pipeline that turned one approved design into variants in many languages','Built an HTML5 and jQuery game-rules system with scripted export to production','Turned artist feedback into prioritized fixes and features, shipped in Git and Perforce','Trained artists on tools and export workflows and documented each workflow']),
('Generative AI Artist and Creative Tools Builder','Self-Employed','Feb 2026 – Present','Remote',['Build ComfyUI and Stable Diffusion workflows with Python helpers for generation, upscaling, and cleanup','Work with agent harnesses and local agentic LLM inference on my own hardware']),
('Digital Production Artist, Contract','Tiffany & Co.','Oct 2017 – Feb 2018','New York, NY',['Adapted brand assets for web, digital billboard, and campaign formats in Photoshop and After Effects']),
('Digital Graphic Designer','High 5 Games','Jan 2014 – Sep 2017','New York, NY',['Produced and localized game logos and assets across many locales, with format checks and QA']),
('Moderator and Digital Artist, Part-time','QiDao Protocol','Jan 2021 – Sep 2026','Remote',['Wrote Python scripts to pull, process, and chart business metrics; designed assets for community campaigns']),
('Digital Artist and Technical Artist','Powerhead Games, Sifteo, and others','2000 – 2013','New York, NY and Remote',['Planned art workflows and specs for mobile and handheld games; built Photoshop batch automations'])]
skills=[('Code','Python, JavaScript, Adobe ExtendScript, JSON, jQuery, HTML, CSS'),('Version control','Git and Perforce'),('Creative tooling','Photoshop, Illustrator, After Effects, InDesign, Figma, Spine'),('Generative AI','ComfyUI and Stable Diffusion image workflows; agent harnesses and local agentic LLM inference'),('Enablement','User support, onboarding, troubleshooting, artist training, workflow guides')]
res=f'''<section class="ph1"><div class="wrap"><span class="eyebrow">Resume</span><h1 class="disp">Creative <span class="gt">technologist.</span></h1><p class="lede">Tools and automation for creative teams · Open to NYC and Remote</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap rs"><aside class="rv"><a class="btn pri mag" href="/David_Philipe_Gil_Resume.pdf" target="_blank" rel="noopener">Resume {ARR}</a><a class="btn ghost mag" href="contact.html">Contact</a></aside><div>
<h2 class="rv">Summary</h2><p class="sum rv">Creative technologist with 7 years of hands-on work inside a creative team, keeping its tools running, improving what was already built, and building new solutions around real artist needs. I turn artist feedback into tool improvements, automate repeatable production work so artists have more time for creative work, and teach each workflow to the team.</p>
<h2 class="rv">Skills</h2><dl class="skills">{"".join(f'<div class="rv"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in skills)}</dl>
<h2 class="rv">Experience</h2>{"".join(f'<div class="job rv"><div><p class="when">{w}<br>{l}</p></div><div><h3>{E(t)} · <span>{E(c)}</span></h3><ul>{"".join(f"<li>{x}</li>" for x in b)}</ul></div></div>' for t,c,w,l,b in jobs)}
<h2 class="rv">Education</h2><ul class="edu"><li class="rv">BFA, Computer Art · School of Visual Arts</li><li class="rv">Frontend Web Development Nanodegree · Udacity</li><li class="rv">C and C++ Programming · NYU SPS</li></ul></div></div></section>'''
open(f'{S}/resume.html','w').write(page('Resume · David Philipe Gil',res,active='Resume'))
con=f'''<section class="ph1"><div class="wrap"><span class="eyebrow">Contact</span><h1 class="disp">Work <span class="gt">together.</span></h1><p class="lede">Open to creative technologist, technical artist, and creative tools roles in the NYC metro area or remote across the US.</p>
<ul class="clinks"><li><a href="mailto:davidpgil@protonmail.com"><small>Email</small><span>davidpgil@protonmail.com</span></a></li><li><a href="https://www.linkedin.com/in/davidpgil/"><small>LinkedIn</small><span>in/davidpgil</span></a></li><li><a href="https://github.com/davidpgil"><small>GitHub</small><span>davidpgil</span></a></li></ul></div></section>'''
open(f'{S}/contact.html','w').write(page('Contact · David Philipe Gil',con,active='Contact'))
open(f'{S}/404.html','w').write(page('Page moved · David Philipe Gil','<section class="ph1" style="min-height:70vh"><div class="wrap"><span class="eyebrow">404</span><h1 class="disp">This page <span class="gt">moved.</span></h1><p class="lede"><a class="link" href="/index.html">Head back home</a> or browse the <a class="link" href="/projects.html">work</a>.</p></div></section>'))
open(f'{S}/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#39ff14"/><stop offset=".25" stop-color="#22f5a0"/><stop offset=".5" stop-color="#38bdf8"/><stop offset=".7" stop-color="#8f6bff"/><stop offset="1" stop-color="#ff2bd6"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="42" font-family="Helvetica,Arial,sans-serif" font-size="21" font-weight="800" letter-spacing="-1" fill="#05070d" text-anchor="middle">DPG</text></svg>')
open(f'{S}/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>https://davidphilipegil.com/{u}</loc></url>' for u in ['','projects.html','resume.html','contact.html']+[f'projects/{p["slug2"]}.html' for p in P])+'</urlset>')
open(f'{S}/robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://davidphilipegil.com/sitemap.xml\n')
