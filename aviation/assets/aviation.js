/* The Window Seat - shared script: data, formatting, the flight detail panel and the zoomable map.
   Data comes from <script id="calz" type="application/json"> on each page; the world outline from world.js. */
(function(){
'use strict';
var D=JSON.parse(document.getElementById('calz').textContent), W=window.CALZ_WORLD||{land:'',visited:''};
var BY={};D.flights.forEach(function(f){BY[f.id]=f;});
var NS='http://www.w3.org/2000/svg', REDUCED=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function el(tag,attrs,parent){var e=document.createElementNS(NS,tag);for(var k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],DAY=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
function date(iso,long){var p=iso.split('-'),d=new Date(Date.UTC(+p[0],p[1]-1,+p[2]));return (long?DAY[d.getUTCDay()]+' ':'')+(+p[2])+' '+MON[p[1]-1]+' '+p[0];}
function dur(m){if(m==null)return '–';return Math.floor(m/60)+'h '+('0'+m%60).slice(-2)+'m';}
function delay(m){
  if(m==null)return{t:'Not recorded',c:'na'};
  if(m<0)return{t:(-m)+' min early',c:'ok'};
  if(m===0)return{t:'On time',c:'ok'};
  if(m<=15)return{t:m+' min late',c:'ok'};
  return{t:m+' min late',c:m<45?'late':'vlate'};}
function status(f){var a=delay(f.arr_delay);if(f.arr_delay==null&&f.est_arr_delay!=null){var h=Math.round(f.est_arr_delay/60);return{t:(f.est_arr_delay>0?'≈'+(h>=1?h+'h':f.est_arr_delay+' min')+' late':'Landed'),c:f.est_arr_delay>=45?'vlate':'late'};}if(f.arr_delay==null)return{t:'Landed',c:'na'};if(f.arr_delay<=0)return{t:f.arr_delay<0?'Early':'On time',c:'ok'};return f.arr_delay<=15?{t:'On time',c:'ok'}:{t:'Late',c:a.c};}
function apt(c){return D.airports[c]||{name:c,city:c};}
function miles(n){return n.toLocaleString('en-GB')+' mi';}

/* ---------- the map ---------- */
function makeMap(box,o){
  o=o||{};
  var svg=el('svg',{viewBox:'0 0 1000 524',role:'group','aria-label':o.label||'World map of flight routes'},null);
  box.appendChild(svg);
  var base=el('g',{},svg);
  var grat=el('g',{'class':'grat'},base);
  for(var lat=-60;lat<=80;lat+=20)el('path',{d:line(function(t){return[-180+360*t,lat];}),'class':'grat'},grat);
  for(var lon=-180;lon<=180;lon+=30)el('path',{d:line(function(t){return[lon,-60+140*t];}),'class':'grat'},grat);
  el('path',{d:W.land,'class':'land'},base);el('path',{d:W.visited,'class':'visited'},base);
  var gR=el('g',{},svg),gH=el('g',{},svg),gA=el('g',{},svg),gF=el('g',{},svg);
  var vb={x:0,y:0,w:1000,h:524},routes={},apts={},shown=[];
  function line(fn){var d='';for(var i=0;i<=40;i++){var p=proj(fn(i/40));d+=(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);}return d;}
  function upp(){return vb.w/Math.max(1,box.clientWidth);}
  function apply(){svg.setAttribute('viewBox',vb.x+' '+vb.y+' '+vb.w+' '+vb.h);var s=upp();
    /* labels: busiest airports first; a label that would overlap one already placed is hidden (zoom in to see it) */
    var placed=[],codes=Object.keys(apts).sort(function(x,y){return(D.airports[y].uses||0)-(D.airports[x].uses||0);});
    codes.forEach(function(c){var a=apts[c],dir=D.airports[c].lab||'ne',w=c.length*7.4*s,h=11*s,dx=dir.indexOf('w')>=0?-7*s-w:7*s,dy=dir.indexOf('s')>=0?h+4*s:-6*s;
      a.c.setAttribute('r',4.5*s);a.c.setAttribute('stroke-width',1.5*s);a.t.setAttribute('font-size',11*s);a.t.style.strokeWidth=(3*s)+'px';a.t.setAttribute('x',a.x+dx);a.t.setAttribute('y',a.y+dy);
      var bx=[a.x+dx,a.y+dy-h,a.x+dx+w,a.y+dy],hit=placed.some(function(p){return!(bx[2]<p[0]||bx[0]>p[2]||bx[3]<p[1]||bx[1]>p[3]);});
      a.t.style.display=hit?'none':'';if(!hit){placed.push(bx);placed.push([a.x-5*s,a.y-5*s,a.x+5*s,a.y+5*s]);}});
    if(o.onView)o.onView();}
  function aspect(){return Math.max(.2,box.clientHeight/Math.max(1,box.clientWidth));}
  function fit(bb,pad){
    if(!bb){bb=[0,40,1000,470];}
    pad=pad==null?.18:pad;var w=Math.max(bb[2]-bb[0],30),h=Math.max(bb[3]-bb[1],20),cx=(bb[0]+bb[2])/2,cy=(bb[1]+bb[3])/2;
    w*=1+pad*2;h*=1+pad*2;var a=aspect();if(h/w>a)w=h/a;else h=w*a;
    if(w>1400){w=1400;h=w*a;}
    vb={x:cx-w/2,y:cy-h/2,w:w,h:h};apply();}
  function draw(list,colourBy){
    gR.textContent='';gH.textContent='';gA.textContent='';routes={};apts={};shown=list;
    var groups={},used={};
    list.forEach(function(f){var k=f.arc;(groups[k]=groups[k]||[]).push(f);used[f.dep]=1;used[f.arr]=1;});
    Object.keys(groups).sort(function(a,b){return groups[b].length-groups[a].length;}).forEach(function(k){
      var A=D.arcs[k],n=groups[k].length,w=Math.min(1.6+n*.45,6.5);
      var p=el('path',{d:A.d,'class':'route',stroke:A.color,'stroke-width':w},gR);
      var lab=apt(A.a).city+' to '+apt(A.b).city+(A.via?' via '+A.via:'')+', '+A.airline_name+', '+n+(n===1?' flight':' flights');
      var h=el('path',{d:A.d,'class':'route hit',tabindex:o.interactive?0:-1,role:'button','aria-label':lab},gH);
      var t=el('title',{},h);t.textContent=lab;
      routes[k]={p:p,h:h,n:n,flights:groups[k]};
      if(o.onRoute){h.addEventListener('click',function(e){if(!moved)o.onRoute(k,groups[k]);});h.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();o.onRoute(k,groups[k]);}});}
    });
    Object.keys(used).forEach(function(c){var a=D.airports[c];var g=el('g',{'class':'apt',tabindex:o.interactive?0:-1,role:'button','aria-label':a.name+' ('+c+')'},gA);
      var ci=el('circle',{cx:a.x,cy:a.y,r:4},g),tx=el('text',{x:a.x+7,y:a.y-6},g);tx.textContent=c;
      apts[c]={g:g,c:ci,t:tx,x:a.x,y:a.y};
      if(o.onAirport){g.addEventListener('click',function(){if(!moved)o.onAirport(c);});g.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();o.onAirport(c);}});}});
    apply();}
  function bbox(list){var x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;list.forEach(function(f){var b=D.arcs[f.arc].bb;x0=Math.min(x0,b[0]);y0=Math.min(y0,b[1]);x1=Math.max(x1,b[2]);y1=Math.max(y1,b[3]);});return list.length?[x0,y0,x1,y1]:null;}
  function select(key,code){
    for(var k in routes){var r=routes[k];r.p.classList.remove('dim','sel');
      if(key&&k!==key)r.p.classList.add('dim');if(key&&k===key)r.p.classList.add('sel');
      if(code){var A=D.arcs[k];if(A.a!==code&&A.b!==code)r.p.classList.add('dim');}}
    for(var c in apts)apts[c].g.classList.toggle('sel',c===code);}
  /* zoom + pan: wheel, drag, pinch */
  var pts={},moved=false,start=null;
  function toUser(cx,cy){var r=svg.getBoundingClientRect();return[vb.x+(cx-r.left)/r.width*vb.w,vb.y+(cy-r.top)/r.height*vb.h];}
  function zoomAt(f,cx,cy){var u=toUser(cx,cy),nw=Math.min(1600,Math.max(18,vb.w*f));f=nw/vb.w;vb={x:u[0]-(u[0]-vb.x)*f,y:u[1]-(u[1]-vb.y)*f,w:nw,h:vb.h*f};apply();}
  if(o.interactive){
    svg.addEventListener('wheel',function(e){e.preventDefault();zoomAt(e.deltaY>0?1.2:1/1.2,e.clientX,e.clientY);},{passive:false});
    svg.addEventListener('pointerdown',function(e){pts[e.pointerId]=[e.clientX,e.clientY];moved=false;start={vb:Object.assign({},vb),p:[e.clientX,e.clientY],d:dist()};});
    svg.addEventListener('pointermove',function(e){if(!pts[e.pointerId])return;pts[e.pointerId]=[e.clientX,e.clientY];var ids=Object.keys(pts);
      if(ids.length===1){var dx=e.clientX-start.p[0],dy=e.clientY-start.p[1];if(Math.abs(dx)+Math.abs(dy)>4){moved=true;svg.classList.add('drag');try{svg.setPointerCapture(e.pointerId);}catch(_){}}
        if(moved){var s=start.vb.w/Math.max(1,svg.getBoundingClientRect().width);vb={x:start.vb.x-dx*s,y:start.vb.y-dy*s,w:start.vb.w,h:start.vb.h};apply();}}
      else if(ids.length===2&&start.d){moved=true;var d=dist(),a=pts[ids[0]],b=pts[ids[1]];var f=start.d/d;var nw=Math.min(1600,Math.max(18,start.vb.w*f));var mid=[(a[0]+b[0])/2,(a[1]+b[1])/2];
        var r=svg.getBoundingClientRect(),ux=start.vb.x+(mid[0]-r.left)/r.width*start.vb.w,uy=start.vb.y+(mid[1]-r.top)/r.height*start.vb.h,k=nw/start.vb.w;
        vb={x:ux-(ux-start.vb.x)*k,y:uy-(uy-start.vb.y)*k,w:nw,h:start.vb.h*k};apply();}});
    function up(e){delete pts[e.pointerId];svg.classList.remove('drag');if(Object.keys(pts).length===1){var id=Object.keys(pts)[0];start={vb:Object.assign({},vb),p:pts[id],d:0};}setTimeout(function(){moved=false;},0);}
    svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);
    function dist(){var ids=Object.keys(pts);if(ids.length<2)return 0;var a=pts[ids[0]],b=pts[ids[1]];return Math.hypot(a[0]-b[0],a[1]-b[1]);}
  }
  addEventListener('resize',function(){var c=[vb.x+vb.w/2,vb.y+vb.h/2];vb.h=vb.w*aspect();vb.y=c[1]-vb.h/2;apply();});
  /* the plane used by the replay */
  var plane=null;
  function fly(f,ms,done){var r=routes[f.arc];if(!r){done();return;}
    if(!plane)plane=el('circle',{r:5,'class':'plane'},gF);plane.setAttribute('r',5.5*upp());
    var L=r.p.getTotalLength(),t0=null;
    function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/ms),s=f.rev?1-k:k,pt=r.p.getPointAtLength(L*s);plane.setAttribute('cx',pt.x);plane.setAttribute('cy',pt.y);
      if(k<1)raf=requestAnimationFrame(step);else done();}
    var raf=requestAnimationFrame(step);return function(){cancelAnimationFrame(raf);};}
  function hidePlane(){if(plane){plane.remove();plane=null;}}
  return{svg:svg,draw:draw,fit:fit,bbox:bbox,select:select,fly:fly,hidePlane:hidePlane,routes:function(){return routes;},zoom:function(f){var r=svg.getBoundingClientRect();zoomAt(f,r.left+r.width/2,r.top+r.height/2);}};
}
/* Natural Earth I projection - identical to world.py */
function proj(ll){var l=ll[0]*Math.PI/180,p=ll[1]*Math.PI/180,p2=p*p,p4=p2*p2,K=500/2.7349;
  var x=l*(0.8707-0.131979*p2+p4*(-0.013791+p4*(0.003971*p2-0.001529*p4))),y=p*(1.007226+p2*(0.015085+p4*(-0.044475+0.028874*p2-0.005916*p4)));
  return[500+x*K,262-y*K];}

/* ---------- the flight detail panel ---------- */
var dlg=null;
function openFlight(id){var f=BY[id];if(!f)return;
  if(!dlg){dlg=document.createElement('dialog');dlg.className='fd';dlg.setAttribute('aria-labelledby','fd-t');document.body.appendChild(dlg);
    dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close();});}
  var A=apt(f.dep),B=apt(f.arr),dd=delay(f.dep_delay),ad=delay(f.arr_delay),nx=f.arr_next_day?' <small>(+1 day)</small>':'';
  function kv(k,v){return '<div><dt>'+k+'</dt><dd>'+v+'</dd></div>';}
  dlg.style.setProperty('--c',f.color);
  dlg.innerHTML='<div class="fd-h"><p class="kick">'+esc(f.airline_name)+' · '+esc(f.flight)+'</p><h2 id="fd-t" class="route">'+f.dep+' → '+f.arr+'</h2><p>'+esc(A.city)+' to '+esc(B.city)+' · '+date(f.date,true)+'</p>'+
    '<button type="button" class="fd-x" aria-label="Close">×</button></div><div class="fd-b"><div class="mapbox fd-mini" aria-hidden="true"></div><dl class="kv">'+
    kv('Aircraft',esc(f.family||'Not recorded')+(f.variant?' <small>'+esc(f.variant)+'</small>':''))+
    kv('Registration',f.reg?'<a href="/aviation/aircraft/#'+esc(f.reg)+'">'+esc(f.reg)+'</a>':'Not recorded')+
    kv('Callsign',esc(f.callsign||'Not recorded'))+kv('Distance',miles(f.miles))+kv('Flight time',dur(f.duration)+(f.duration_estimated?' <small>(timetable)</small>':''))+
    kv('Departure',(f.sched_dep||'–')+' scheduled'+(f.act_dep?'<br>'+f.act_dep+' actual · <span class="st '+dd.c+'">'+dd.t+'</span>':''))+
    kv('Arrival',(f.sched_arr||'–')+' scheduled'+nx+(f.act_arr?'<br>'+f.act_arr+' actual · <span class="st '+ad.c+'">'+ad.t+'</span>':(f.est_arr?'<br>≈'+f.est_arr+' estimated · <span class="st vlate">about '+Math.round(f.est_arr_delay/60)+' hours late</span>':'')))+
    kv('From',esc(A.name)+' <small>'+f.dep+' · '+esc(A.icao)+'</small>')+kv('To',esc(B.name)+' <small>'+f.arr+' · '+esc(B.icao)+'</small>')+
    '</dl><p class="note">Times are local at each airport. Distance is the great-circle distance between the airports.'+(f.duration_estimated?' No actual times were recorded for this flight, so its flight time comes from the timetable.':'')+(f.note?' '+esc(f.note):'')+'</p></div>';
  dlg.querySelector('.fd-x').addEventListener('click',function(){dlg.close();});
  if(dlg.showModal)dlg.showModal();else dlg.setAttribute('open','');
  var m=makeMap(dlg.querySelector('.fd-mini'),{label:'Route map'});m.draw([f]);m.fit(D.arcs[f.arc].bb,.35);}

document.addEventListener('click',function(e){var b=e.target.closest('[data-flight]');if(b){e.preventDefault();openFlight(b.getAttribute('data-flight'));}});
window.CALZ={data:D,byId:BY,date:date,dur:dur,delay:delay,status:status,apt:apt,miles:miles,esc:esc,makeMap:makeMap,openFlight:openFlight,reduced:REDUCED};
})();
