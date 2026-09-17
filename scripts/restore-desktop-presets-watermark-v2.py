from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='DUSKREEL DESKTOP PRESETS + WATERMARK RESTORE V2'
if marker in s:
    print('restore v2 already installed')
    raise SystemExit(0)

patch=r'''<style>
/* DUSKREEL DESKTOP PRESETS + WATERMARK RESTORE V2 */
@media (min-width:761px){
  #duskRestoreTools{display:block!important;position:fixed;right:18px;top:68px;width:250px;max-height:calc(100vh - 88px);overflow:auto;z-index:90;background:var(--panel,#1E1220);border:1px solid var(--line,#4A2A52);border-radius:10px;padding:10px;box-shadow:0 18px 45px rgba(0,0,0,.45)}
  #duskRestoreTools .dr-head{font-size:12px;font-weight:700;margin:0 0 7px;color:#fff}
  #duskRestoreTools .dr-sub{font-size:10px;color:var(--ink-dim,#CBA6D1);margin:0 0 7px}
  #duskRestorePresets{display:grid;grid-template-columns:repeat(3,1fr);gap:5px}
  #duskRestorePresets button{height:30px;min-width:0;padding:3px 4px;border:1px solid var(--line,#4A2A52);border-radius:5px;background:var(--panel-2,#2A1830);color:#fff;font-size:10px;font-weight:600;cursor:pointer}
  #duskRestorePresets button:hover,#duskRestorePresets button.active{background:var(--magenta,#E619A6);border-color:var(--magenta-bright,#FF4FC3)}
  #duskRestoreWatermark{margin-top:10px;padding-top:9px;border-top:1px solid var(--line,#4A2A52)}
  #duskRestoreWatermark input[type=text]{width:100%;height:30px;padding:5px 7px;background:var(--panel-2,#2A1830);border:1px solid var(--line,#4A2A52);border-radius:5px;color:#fff;font-size:11px}
  #duskRestoreWatermark label{display:block;margin:6px 0 3px;color:var(--ink-dim,#CBA6D1);font-size:9px}
  #duskRestoreWatermark input[type=range]{width:100%;height:18px}
  #duskRestoreWatermark .dr-row{display:flex;gap:5px;margin-top:6px}
  #duskRestoreWatermark button{flex:1;height:28px;border:1px solid var(--line,#4A2A52);border-radius:5px;background:var(--panel-2,#2A1830);color:#fff;font-size:10px;cursor:pointer}
  #duskRestoreWatermark .dr-primary{background:var(--magenta,#E619A6);border-color:var(--magenta,#E619A6)}
  #duskRestoreBadge{position:absolute;left:50%;top:50%;z-index:26;transform:translate(-50%,-50%);display:none;color:#fff;font-weight:700;text-shadow:0 2px 8px #000;white-space:nowrap;cursor:move;user-select:none;pointer-events:auto}
}
@media (max-width:760px){#duskRestoreTools{display:none!important}}
</style>
<script>
(function(){
  function findImageNodes(){
    var ids=['afterCanvas','previewCanvas','mainCanvas','editorCanvas','imageCanvas'],out=[];
    ids.forEach(function(id){var e=document.getElementById(id);if(e&&!out.includes(e))out.push(e);});
    document.querySelectorAll('main canvas,main .stage img,main .canvas img,main .canvas-area img').forEach(function(e){if(!out.includes(e))out.push(e);});
    return out;
  }
  var presets=[
    ['Natural','brightness(1.02) contrast(1.04) saturate(1.02)'],['Bright','brightness(1.14) contrast(.96) saturate(1.05)'],['Vivid','saturate(1.45) contrast(1.12)'],
    ['Warm','sepia(.12) saturate(1.18) brightness(1.04)'],['Cool','hue-rotate(175deg) saturate(1.10)'],['Cinematic','contrast(1.28) saturate(.82) brightness(.94)'],
    ['Portrait','brightness(1.05) contrast(.94) saturate(.92)'],['Soft','brightness(1.08) contrast(.88) saturate(.88)'],['Drama','contrast(1.38) brightness(.88) saturate(.90)'],
    ['Film','contrast(1.10) saturate(.84) sepia(.10)'],['Vintage','sepia(.32) contrast(1.06) saturate(.82)'],['Noir','grayscale(1) contrast(1.30)'],
    ['Ocean','hue-rotate(180deg) saturate(1.28) contrast(1.06)'],['Sunset','sepia(.18) hue-rotate(345deg) saturate(1.30)'],['Glam','brightness(1.10) contrast(.96) saturate(1.08)'],
    ['Food','saturate(1.48) contrast(1.12) brightness(1.02)'],['Travel','saturate(1.25) contrast(1.10) brightness(1.04)'],['Night','brightness(.72) contrast(1.30) saturate(.92)']
  ];
  function install(){
    if(document.getElementById('duskRestoreTools'))return;
    var box=document.createElement('section');box.id='duskRestoreTools';
    box.innerHTML='<div class="dr-head">Presets</div><div class="dr-sub">Quick photo looks</div><div id="duskRestorePresets"></div><div id="duskRestoreWatermark"><div class="dr-head">Watermark</div><div class="dr-sub">Add your own watermark — off by default</div><input id="drWmText" type="text" placeholder="Your name or brand"><label>Size <span id="drWmSizeV">30</span>px</label><input id="drWmSize" type="range" min="10" max="100" value="30"><label>Opacity <span id="drWmOpacityV">70</span>%</label><input id="drWmOpacity" type="range" min="5" max="100" value="70"><label>Rotation <span id="drWmRotateV">0</span>°</label><input id="drWmRotate" type="range" min="-180" max="180" value="0"><div class="dr-row"><button id="drWmApply" class="dr-primary">Add / Update</button><button id="drWmRemove">Remove</button></div></div>';
    document.body.appendChild(box);
    var grid=box.querySelector('#duskRestorePresets');
    presets.forEach(function(item){var b=document.createElement('button');b.type='button';b.textContent=item[0];b.onclick=function(){findImageNodes().forEach(function(e){e.style.filter=item[1];});grid.querySelectorAll('button').forEach(function(x){x.classList.remove('active')});b.classList.add('active');};grid.appendChild(b);});
    var stage=document.querySelector('main .stage')||document.querySelector('.stage');
    if(stage){if(getComputedStyle(stage).position==='static')stage.style.position='relative';var badge=document.createElement('div');badge.id='duskRestoreBadge';stage.appendChild(badge);}
    var badge=document.getElementById('duskRestoreBadge');
    function sync(){if(!badge)return;var t=document.getElementById('drWmText').value.trim();badge.textContent=t;badge.style.fontSize=document.getElementById('drWmSize').value+'px';badge.style.opacity=document.getElementById('drWmOpacity').value/100;badge.style.transform='translate(-50%,-50%) rotate('+document.getElementById('drWmRotate').value+'deg)';badge.style.display=t?'block':'none';document.getElementById('drWmSizeV').textContent=document.getElementById('drWmSize').value;document.getElementById('drWmOpacityV').textContent=document.getElementById('drWmOpacity').value;document.getElementById('drWmRotateV').textContent=document.getElementById('drWmRotate').value;}
    ['drWmSize','drWmOpacity','drWmRotate','drWmText'].forEach(function(id){document.getElementById(id).addEventListener('input',sync);});
    document.getElementById('drWmApply').onclick=sync;document.getElementById('drWmRemove').onclick=function(){document.getElementById('drWmText').value='';sync();};sync();
    if(badge&&stage){var drag=false,dx=0,dy=0;badge.addEventListener('pointerdown',function(e){drag=true;badge.setPointerCapture(e.pointerId);var r=badge.getBoundingClientRect();dx=e.clientX-r.left;dy=e.clientY-r.top;});badge.addEventListener('pointermove',function(e){if(!drag)return;var r=stage.getBoundingClientRect();badge.style.left=Math.max(0,Math.min(r.width,e.clientX-r.left-dx))+'px';badge.style.top=Math.max(0,Math.min(r.height,e.clientY-r.top-dy))+'px';});badge.addEventListener('pointerup',function(){drag=false;});}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',install,{once:true});else install();
  setTimeout(install,500);setTimeout(install,1500);
})();
</script>
'''
s=s.replace('</head>',patch+'</head>',1)
p.write_text(s,encoding='utf-8')
print('restored visible desktop presets and optional watermark controls')
