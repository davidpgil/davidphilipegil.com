(()=>{const d=document,w=window,rm=matchMedia('(prefers-reduced-motion: reduce)').matches,fine=matchMedia('(hover:hover) and (pointer:fine)').matches,raf=requestAnimationFrame;
d.documentElement.classList.add('js');
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
const rv=el=>io.observe(el);d.querySelectorAll('.rv').forEach((el,i)=>{el.style.setProperty('--d',(i%4)*70+'ms');rv(el)});
// header: sentinel observer instead of scroll handler
const hd=d.querySelector('header.site'),sn=d.createElement('div');sn.className='sentinel';d.body.prepend(sn);new IntersectionObserver(e=>hd.classList.toggle('scrolled',!e[0].isIntersecting)).observe(sn);
const mb=d.querySelector('.menu');mb&&(mb.onclick=()=>{const o=hd.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
// featured rotation
const fb=d.querySelector('.bento.feat'),FD=w.FEAT;
if(fb&&FD){const sh=a=>{for(let i=a.length;i--;){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]]}return a};
 const q=sh(FD.slice()),tiles=[...fb.querySelectorAll('.tile')],put=(t,p)=>{t.href=p.u;t.dataset.cat=p.c;t.classList.toggle('contain',!!p.k);const im=t.querySelector('img');im.src=p.i;im.srcset=p.s||'';im.alt=p.t+' cover';im.classList.toggle('pixel',!!p.x);t.querySelector('.cat').textContent=p.c;t.querySelector('h3').textContent=p.t;t.querySelector('.tools').textContent=p.o};
 tiles.forEach((t,i)=>put(t,q[i]));let nx=tiles.length%q.length,sl=0,hov=0,vis=1,pz=0;
 const tb=d.querySelector('.feat-toggle');if(tb&&!rm){tb.hidden=false;tb.onclick=()=>{pz=!pz;tb.dataset.paused=pz?1:0;tb.querySelector('.lbl').textContent=pz?'Play':'Pause';tb.setAttribute('aria-label',pz?'Play featured project rotation':'Pause featured project rotation')};tb.setAttribute('aria-label','Pause featured project rotation')}
 const pre=()=>{const p=q[nx%q.length];const i=new Image();i.decoding='async';i.src=p.i};pre();
 fb.addEventListener('pointerenter',()=>hov=1);fb.addEventListener('pointerleave',()=>hov=0);fb.addEventListener('focusin',()=>hov=1);fb.addEventListener('focusout',()=>hov=0);
 new IntersectionObserver(e=>vis=e[0].isIntersecting).observe(fb);
 if(!rm)setInterval(()=>{if(pz||hov||!vis||d.hidden)return;const shown=new Set(tiles.map(t=>t.getAttribute('href')));let p=q[nx%q.length],g=0;while(shown.has(p.u)&&g++<q.length){nx++;p=q[nx%q.length]}
  const t=tiles[sl];sl=(sl+1)%tiles.length;nx++;const im=new Image();im.src=p.i;(im.decode?im.decode():Promise.resolve()).catch(()=>{}).then(()=>{const ph=t.querySelector('.ph'),o=ph.querySelector('img'),n=o.cloneNode();n.srcset=p.s||'';n.src=p.i;n.alt=p.t+' cover';n.classList.toggle('pixel',!!p.x);n.className+=' xf';ph.appendChild(n);t.classList.add('swap');raf(()=>raf(()=>{n.classList.add('on');t.classList.toggle('contain',!!p.k)}));setTimeout(()=>{o.remove();n.classList.remove('xf','on');put(t,p);t.classList.remove('swap');pre()},650)})},3000)}
if(fine&&!rm){
 // tilt: rAF throttled, transform only
 d.querySelectorAll('.tile').forEach(t=>{let e0=null,pend=0;const up=()=>{pend=0;if(!e0)return;const r=t.getBoundingClientRect(),x=(e0.clientX-r.left)/r.width-.5,y=(e0.clientY-r.top)/r.height-.5;t.style.transform=`perspective(900px) rotateY(${x*5}deg) rotateX(${-y*5}deg)`;t.style.setProperty('--mx',(x+.5)*100+'%');t.style.setProperty('--my',(y+.5)*100+'%')};
  t.addEventListener('pointermove',e=>{e0=e;if(!pend){pend=1;raf(up)}},{passive:true});t.addEventListener('pointerleave',()=>{e0=null;t.style.transform=''})});
 d.querySelectorAll('.mag').forEach(b=>{let e0,pend=0;b.addEventListener('pointermove',e=>{e0=e;if(pend)return;pend=1;raf(()=>{pend=0;if(!e0)return;const r=b.getBoundingClientRect();b.style.transform=`translate(${(e0.clientX-r.left-r.width/2)*.25}px,${(e0.clientY-r.top-r.height/2)*.35}px)`})},{passive:true});b.addEventListener('pointerleave',()=>{e0=null;b.style.transform=''})});
 // ember cursor: DPR 1, sprite cache, idle stop
 const ec=d.createElement('canvas');ec.className='ember';ec.setAttribute('aria-hidden','true');d.body.appendChild(ec);
 const x=ec.getContext('2d'),P=[],MX=40,SP=[],SS=64;
 for(let k=0;k<36;k++){const c=d.createElement('canvas');c.width=c.height=SS;const g=c.getContext('2d'),r=g.createRadialGradient(32,32,0,32,32,32),h=k*10;r.addColorStop(0,`hsla(${h},100%,88%,1)`);r.addColorStop(.35,`hsla(${h},100%,60%,.55)`);r.addColorStop(1,`hsla(${h},100%,50%,0)`);g.fillStyle=r;g.fillRect(0,0,SS,SS);SP.push(c)}
 const spr=(X,Y,R,h,a)=>{x.globalAlpha=a>1?1:a;x.drawImage(SP[((h%360+360)%360)/10|0],X-R,Y-R,R*2,R*2)};
 let W,H,px=-99,py=-99,ex=-99,ey=-99,hov=0,hv=0,h0=0,lt=0,on=0,idle=0;
 const sz=()=>{W=ec.width=innerWidth;H=ec.height=innerHeight};sz();addEventListener('resize',sz,{passive:true});
 const sp=()=>({x:ex+(Math.random()-.5)*8,y:ey+(Math.random()-.5)*8,vx:(Math.random()-.5)*.6,vy:-(.6+Math.random()*1.4),l:1,dl:.014+Math.random()*.024,r:3+Math.random()*6,h:h0+Math.random()*120});
 const go=()=>{if(!on&&!d.hidden){on=1;lt=performance.now();raf(fr)}};
 addEventListener('pointermove',e=>{if(e.pointerType!=='mouse')return;const dv=Math.hypot(e.clientX-px,e.clientY-py);px=e.clientX;py=e.clientY;if(ex<0){ex=px;ey=py}hov=!!e.target.closest('a,button,.tile,[role=button],input,label');idle=0;for(let i=0;i<Math.min(3,1+dv/16)&&P.length<MX;i++)P.push(sp());go()},{passive:true});
 d.addEventListener('pointerleave',()=>{px=py=-99});
 const fr=t=>{if(d.hidden){on=0;return}const dt=Math.min((t-lt)/16.7,3)||1;lt=t;h0=(h0+3*dt)%360;
  ex+=(px-ex)*.35;ey+=(py-ey)*.35;hv+=(hov-hv)*.15;idle+=dt;x.clearRect(0,0,W,H);
  if(px<0&&!P.length){on=0;return}
  x.globalCompositeOperation='lighter';
  if(px>=0&&idle<120&&Math.random()<.5*dt&&P.length<MX)P.push(sp());
  for(let i=P.length;i--;){const p=P[i];p.x+=p.vx*dt+Math.sin(t/90+i)*.35;p.y+=p.vy*dt;p.vy-=.02*dt;p.l-=p.dl*dt;if(p.l<=0){P.splice(i,1);continue}const f=p.l*(.7+Math.random()*.3);spr(p.x,p.y,p.r*(1.6+f*2),p.h+(1-p.l)*60,f*.85)}
  if(px>=0){const s=1+hv*1.4,fl=.92+Math.random()*.08;spr(ex,ey,60*s*fl,h0,.45);spr(ex,ey,22*s*fl,h0+40,.9);spr(ex,ey,6*s,h0,1);
   if(hv>.05){x.globalAlpha=1;x.strokeStyle=`hsla(${h0},100%,75%,${hv*.6})`;x.lineWidth=1.5;x.beginPath();x.arc(ex,ey,21*s,0,7);x.stroke()}}
  x.globalAlpha=1;x.globalCompositeOperation='source-over';
  // keep animating while visible ember or particles; core stays lit ~3s after last move then sleeps
  if(px>=0&&idle>180&&!P.length){on=0;return}raf(fr)};
 d.addEventListener('visibilitychange',()=>{if(!d.hidden&&px>=0)go()});
}
d.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{d.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x===b));d.querySelectorAll('.bento .tile').forEach(t=>t.hidden=!(b.dataset.f==='all'||t.dataset.cat===b.dataset.f))});
const lb=d.querySelector('dialog.lb');if(lb){const im=lb.querySelector('img'),ims=[...d.querySelectorAll('.media img')];let k=0;
 const show=i=>{k=(i+ims.length)%ims.length;im.src=ims[k].currentSrc||ims[k].src;im.alt=ims[k].alt;im.className=ims[k].classList.contains('pixel')?'pixel':''};
 ims.forEach((x,i)=>{x.tabIndex=0;x.setAttribute('role','button');x.setAttribute('aria-label','Enlarge '+x.alt);const o=()=>{show(i);lb.showModal()};x.onclick=o;x.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();o()}}});
 lb.querySelector('.p').onclick=()=>show(k-1);lb.querySelector('.n').onclick=()=>show(k+1);lb.querySelector('.x').onclick=()=>lb.close();
 lb.onclick=e=>{if(e.target===lb)lb.close()};lb.onkeydown=e=>{if(e.key==='ArrowLeft')show(k-1);if(e.key==='ArrowRight')show(k+1)}}
// hero shader: DPR .5, 30fps cap, 4 octaves, offscreen/hidden pause
const cv=d.querySelector('canvas.fx');if(!cv)return;const g=cv.getContext('webgl',{antialias:false,alpha:false,depth:false,stencil:false,powerPreference:'low-power',preserveDrawingBuffer:false});if(!g)return;
const fs=`precision mediump float;uniform vec2 r;uniform float t;uniform vec2 m;
float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+1.),f.x),f.y);}
float fb(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p=p*2.03+vec2(1.7,9.2);a*=.5;}return v*1.07;}
void main(){vec2 uv=gl_FragCoord.xy/r;vec2 p=uv*vec2(r.x/r.y,1.)*2.2;float T=t*.05;
vec2 q=vec2(fb(p+T),fb(p+vec2(5.2,1.3)-T));vec2 mm=(m-uv)*vec2(r.x/r.y,1.);float md=exp(-dot(mm,mm)*5.);
float f=fb(p+2.4*q+vec2(T*1.6,-T)+mm*md*.8);
vec3 ink=vec3(.02,.03,.06),navy=vec3(.03,.10,.17),blue=vec3(.13,.55,.97),vio=vec3(1.,.17,.84),cy=vec3(.22,1.,.08);
vec3 c=mix(ink,navy,smoothstep(.2,.7,f));float gm=smoothstep(.48,.85,f)*smoothstep(.3,.72,1.-q.x);c=mix(c,cy,gm*.85);c+=cy*pow(gm,3.)*.22;c=mix(c,blue,smoothstep(.55,.9,f)*smoothstep(.3,.7,q.x)*.8);c=mix(c,vio,smoothstep(.55,.95,q.y)*.7*f);
c+=md*.12*vec3(.35,1.,.3);c*=1.-.55*smoothstep(.3,1.1,length(uv-vec2(.7,.55)))*.6;c=mix(c,ink,smoothstep(.55,0.,uv.y)*.55);
gl_FragColor=vec4(c,1);}`;
const shd=(ty,s)=>{const o=g.createShader(ty);g.shaderSource(o,s);g.compileShader(o);return o},pr=g.createProgram();
g.attachShader(pr,shd(g.VERTEX_SHADER,'attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}'));g.attachShader(pr,shd(g.FRAGMENT_SHADER,fs));g.linkProgram(pr);if(!g.getProgramParameter(pr,g.LINK_STATUS))return;g.useProgram(pr);
g.bindBuffer(g.ARRAY_BUFFER,g.createBuffer());g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),g.STATIC_DRAW);g.enableVertexAttribArray(0);g.vertexAttribPointer(0,2,g.FLOAT,false,0,0);
const U=k=>g.getUniformLocation(pr,k),ur=U('r'),ut=U('t'),um=U('m');let M=[.7,.5],S=[.7,.5],vis=1,t0=performance.now(),last=0,lp=0;
const rs=()=>{cv.width=Math.round(cv.clientWidth*.5);cv.height=Math.round(cv.clientHeight*.5);g.viewport(0,0,cv.width,cv.height);g.uniform2f(ur,cv.width,cv.height)};rs();addEventListener('resize',rs,{passive:true});
cv.parentElement.addEventListener('pointermove',e=>{const b=cv.getBoundingClientRect();M=[(e.clientX-b.left)/b.width,1-(e.clientY-b.top)/b.height]},{passive:true});
const draw=now=>{S[0]+=(M[0]-S[0])*.1;S[1]+=(M[1]-S[1])*.1;g.uniform1f(ut,rm?20:(now-t0)/1000+20);g.uniform2f(um,S[0],S[1]);g.drawArrays(g.TRIANGLES,0,3)};
cv.classList.add('on');if(rm){draw(0);return}
const L=now=>{lp=0;if(!vis||d.hidden)return;lp=1;raf(L);if(now-last<32)return;last=now;draw(now)};
new IntersectionObserver(e=>{vis=e[0].isIntersecting;if(vis&&!lp)raf(L)}).observe(cv);d.addEventListener('visibilitychange',()=>{if(!d.hidden&&vis&&!lp)raf(L)});raf(L);
})();
