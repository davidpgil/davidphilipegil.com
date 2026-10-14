#!/usr/bin/env python3
"""Build davidphilipegil.com from src/ into dist/.

  python src/build.py

Project data lives in src/projects.json, other page copy in src/content.json,
page markup in src/templates/, and static assets in src/static/.
Nothing in src/ is ever written; dist/ is wiped and regenerated on each run.
"""
import html
import json
import shutil
import time
from pathlib import Path
from string import Template

SRC = Path(__file__).resolve().parent
DIST = SRC.parent / 'dist'
SITE = 'https://davidphilipegil.com'
RESUME = '/David_Philipe_Gil_Resume.pdf'
SHARE = {'src': 'img/share.jpg', 'w': 1200, 'h': 630, 'alt': 'DPG, David Philipe Gil: Tools and automation for creative teams'}
DEFAULT_DESC = 'David Philipe Gil, Creative Technologist and Technical Artist building tools and automation for creative teams.'
NAV = [('index.html', 'Home'), ('projects.html', 'Work'), (None, 'Resume'), ('contact.html', 'Contact')]
E = html.escape
ARROW = ('<svg class="ar" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
TILE_SIZES = {'wide': '(max-width:720px) 100vw, 66vw',
              'normal': '(max-width:720px) 100vw, (max-width:1000px) 50vw, 33vw'}

VER = time.strftime('%Y%m%d%H%M%S')
TEMPLATES = {p.stem: Template(p.read_text()) for p in (SRC / 'templates').glob('*.html')}
PROJECTS = json.loads((SRC / 'projects.json').read_text())['projects']
CONTENT = json.loads((SRC / 'content.json').read_text())


def render(name, **kw):
    return TEMPLATES[name].substitute(**kw)


def attrs(**kw):
    return ''.join(f' {k.rstrip("_").replace("_", "-")}="{E(str(v))}"' for k, v in kw.items() if v is not None)


def resume_link(cls=None, label='Resume', after=''):
    """Resume always opens the PDF in a new tab and says so."""
    return (f'<a{attrs(class_=cls)} href="{RESUME}" target="_blank" rel="noopener" '
            f'aria-label="Resume, PDF, opens in a new tab">{label} <span class="pdf" aria-hidden="true">PDF</span>{after}</a>')


def img(src, w, h, alt, root='', cls='', eager=False, pixel=False, extra=''):
    c = ' '.join(x for x in (cls, 'pixel' if pixel else '') if x)
    return (f'<img{attrs(class_=c or None)}{extra} src="{root}{src}" width="{w}" height="{h}" alt="{E(alt)}" '
            f'loading="{"eager" if eager else "lazy"}" decoding="async">')


def small_cover(src):
    return src.replace('-cover.webp', '-cover-sm.webp')


def srcset(src, root=''):
    return f'{root}{small_cover(src)} 480w, {root}{src} 900w'


def tile(p, size, root=''):
    cls = ' '.join(x for x in ('tile rv', size, 'contain' if p['contain'] else '') if x)
    cv = p['cover']
    sizes = TILE_SIZES['wide' if 'w8' in size else 'normal']
    im = img(cv['src'], cv['w'], cv['h'], p['title'] + ' cover', root, pixel=p['pixel'],
             extra=f' sizes="{sizes}" srcset="{srcset(cv["src"], root)}"')
    return (f'<a class="{cls}" data-cat="{p["category"]}" href="{root}projects/{p["slug"]}.html"><div class="ph">{im}</div>'
            f'<span class="arr">{ARROW}</span><div class="meta"><span class="cat">{p["category"]}</span>'
            f'<h3>{E(p["title"])}</h3><p class="tools">{E(" · ".join(p["tools"]))}</p></div></a>')


def seo(title, desc, path, image=None, noindex=False):
    image = image or SHARE
    url = f'{SITE}/{path}'
    tags = [f'<meta property="og:title" content="{E(title)}">',
            f'<meta property="og:description" content="{E(desc)}">',
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="David Philipe Gil">',
            f'<meta property="og:image" content="{SITE}/{image["src"]}">',
            f'<meta property="og:image:width" content="{image["w"]}"><meta property="og:image:height" content="{image["h"]}">',
            f'<meta property="og:image:alt" content="{E(image["alt"])}">',
            '<meta name="twitter:card" content="summary_large_image">',
            f'<meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}">',
            f'<meta name="twitter:image" content="{SITE}/{image["src"]}">']
    if noindex:
        tags.append('<meta name="robots" content="noindex">')
    else:
        tags[3:3] = [f'<meta property="og:url" content="{url}">', f'<link rel="canonical" href="{url}">']
    return ''.join(tags)


def page(out, title, body, path, depth=0, active='', desc=DEFAULT_DESC, image=None, noindex=False):
    root = '../' * depth
    nav = ''.join(resume_link() if h is None else
                  f'<a href="{root}{h}"{" aria-current=\"page\"" if t == active else ""}>{t}</a>' for h, t in NAV)
    html_ = render('layout', title=E(title), desc=E(desc), root=root, ver=VER, nav=nav, body=body,
                   seo=seo(title, desc, path, image, noindex))
    dest = DIST / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html_)


def build_home():
    marq = '<div class="marq" aria-hidden="true"><div>' + ''.join(f'<span>{t}</span>' for t in CONTENT['marquee'] * 2) + '</div></div>'
    caps = ''.join(f'<div class="cap rv"><b>0{i + 1}</b><h3>{c["title"]}</h3><p>{c["text"]}</p></div>'
                   for i, c in enumerate(CONTENT['capabilities']))
    feat = json.dumps([dict(u=f'projects/{p["slug"]}.html', i=p['cover']['src'], s=srcset(p['cover']['src']),
                            c=p['category'], t=p['title'], o=' · '.join(p['tools']), k=int(p['contain']), x=int(p['pixel']))
                       for p in PROJECTS], ensure_ascii=False).replace('</', '<\\/')
    body = render('home', arrow=ARROW, resume_ghost=resume_link('btn ghost mag'), marquee=marq,
                  tiles=''.join(tile(p, p['home_tile']) for p in PROJECTS[:6]), featjson=feat, caps=caps)
    page('index.html', 'David Philipe Gil · Creative Technologist', body, '', active='Home')


def build_work():
    cats = list(dict.fromkeys(p['category'] for p in PROJECTS))
    filters = ('<div class="filters rv" role="group" aria-label="Filter projects"><button aria-pressed="true" data-f="all">All</button>'
               + ''.join(f'<button aria-pressed="false" data-f="{c}">{c}</button>' for c in cats) + '</div>')
    body = render('work', count=len(PROJECTS), filters=filters, tiles=''.join(tile(p, p['tile']) for p in PROJECTS))
    page('projects.html', 'Work · David Philipe Gil', body, 'projects.html', active='Work')


def media_block(b, p):
    if b['type'] == 'note':
        return f'<p class="note rv">{E(b["text"])}</p>'
    if b['type'] == 'video':
        return (f'<div class="video rv"><iframe src="{E(b["src"])}" title="{E(p["title"])} video" loading="lazy" '
                f'allow="fullscreen" allowfullscreen></iframe></div>')
    ims = b['images']
    cls = 'gallery' if len(ims) > 1 else 'single'
    inner = ''.join(img(i['src'], i['w'], i['h'], i['alt'], '../', pixel=p['pixel'] or i['w'] <= 520) for i in ims)
    if p['pixel']:
        return f'<div class="frame rv"><div class="{cls}">{inner}</div></div>'
    return f'<div class="{cls} rv">{inner}</div>'


def build_projects():
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        pv, nx = PROJECTS[i - 1], PROJECTS[(i + 1) % n]
        hero = p['hero']
        body = render('project', hero_src=hero['src'], category=p['category'], title=E(p['title']),
                      stage_cls=' pix' if p['pixel'] else '',
                      hero_img=img(hero['src'], hero['w'], hero['h'], hero['alt'], '../', eager=True, pixel=p['pixel']),
                      summary=E(p['summary']), chips=''.join(f'<span>{E(t)}</span>' for t in p['tools']),
                      media=''.join(media_block(b, p) for b in p['blocks']),
                      prev_slug=pv['slug'], prev_title=E(pv['title']),
                      prev_img=img(pv['cover']['src'], pv['cover']['w'], pv['cover']['h'], '', '../'),
                      next_slug=nx['slug'], next_title=E(nx['title']),
                      next_img=img(nx['cover']['src'], nx['cover']['w'], nx['cover']['h'], '', '../'))
        cv = p['cover']
        page(f'projects/{p["slug"]}.html', f'{p["title"]} · David Philipe Gil', body, f'projects/{p["slug"]}.html', 1, 'Work',
             p['summary'], image={'src': cv['src'], 'w': cv['w'], 'h': cv['h'], 'alt': p['title'] + ' cover'})


def build_resume():
    r = CONTENT['resume']
    skills = ''.join(f'<div class="rv"><dt>{s["name"]}</dt><dd>{s["text"]}</dd></div>' for s in r['skills'])
    jobs = ''.join(f'<div class="job rv"><div><p class="when">{j["when"]}<br>{j["where"]}</p></div><div><h3>{E(j["title"])} · '
                   f'<span>{E(j["company"])}</span></h3><ul>{"".join(f"<li>{x}</li>" for x in j["points"])}</ul></div></div>'
                   for j in r['jobs'])
    body = render('resume', resume_primary=resume_link('btn pri mag', after=' ' + ARROW), summary=r['summary'], skills=skills, jobs=jobs,
                  education=''.join(f'<li class="rv">{e}</li>' for e in r['education']))
    page('resume.html', 'Resume · David Philipe Gil', body, 'resume.html', active='Resume')


def build_misc():
    page('contact.html', 'Contact · David Philipe Gil', render('contact'), 'contact.html', active='Contact')
    page('404.html', 'Page not found · David Philipe Gil', render('404'), '404.html', noindex=True)
    urls = ['', 'projects.html', 'resume.html', 'contact.html'] + [f'projects/{p["slug"]}.html' for p in PROJECTS]
    (DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + ''.join(f'<url><loc>{SITE}/{u}</loc></url>' for u in urls) + '</urlset>')
    (DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / 'static', DIST)
    build_home()
    build_work()
    build_projects()
    build_resume()
    build_misc()
    print(f'Built {len(list(DIST.rglob("*.html")))} pages into {DIST} (v={VER})')


if __name__ == '__main__':
    main()
