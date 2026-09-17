from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL OPTIONAL WATERMARK V2'
if marker in s:
    print('Watermark V2 already installed')
    raise SystemExit

patch = r'''<style>
/* DUSKREEL OPTIONAL WATERMARK V2 */
@media (min-width:761px){
  #duskWatermarkBtn{display:inline-flex!important;align-items:center;gap:6px;background:#2A1830;border:1px solid #4A2A52;color:#fff;border-radius:7px;padding:7px 10px;cursor:pointer;font-size:12px}
  #duskWatermarkPanel{position:fixed;right:18px;top:62px;z-index:80;width:245px;background:#1E1220;border:1px solid #4A2A52;border-radius:10px;padding:12px;box-shadow:0 18px 45px rgba(0,0,0,.5);display:none}
  #duskWatermarkPanel.show{display:block}
  #duskWatermarkPanel h4{margin:0 0 9px;font-size:13px}
  #duskWatermarkPanel label{display:block;color:#CBA6D1;font-size:10px;margin:7px 0 4px}
  #duskWatermarkPanel input[type=text]{width:100%;background:#2A1830;border:1px solid #4A2A52;color:#fff;border-radius:6px;padding:7px}
  #duskWatermarkPanel input[type=range]{width:100%}
  #duskWatermarkPanel .wm-row{display:flex;gap:6px}
  #duskWatermarkPanel button{flex:1;border:1px solid #4A2A52;background:#2A1830;color:#fff;border-radius:6px;padding:7px;cursor:pointer;font-size:11px}
  #duskWatermarkPanel button.primary{background:#E619A6;border-color:#E619A6}
  #duskWatermarkBadge{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:25;color:#fff;font-weight:700;font-size:30px;letter-spacing:1px;text-shadow:0 2px 8px #000;pointer-events:auto;cursor:move;user-select:none;display:none;white-space:nowrap}
}
</style>
<script>
(function(){
  function setup(){
    if(document.getElementById('duskWatermarkBtn')) return;
    var host=document.querySelector('header .brand') || document.querySelector('header');
    if(!host) return;
    var btn=document.createElement('button'); btn.id='duskWatermarkBtn'; btn.type='button'; btn.textContent='Watermark';
    host.parentElement.appendChild(btn);
    var panel=document.createElement('div'); panel.id='duskWatermarkPanel'; panel.innerHTML=
      '<h4>Watermark</h4>'+
      '<label>Text</label><input id="duskWmText" type="text" placeholder="Your name or brand">'+
      '<label>Size <span id="duskWmSizeVal">30</span>px</label><input id="duskWmSize" type="range" min="10" max="100" value="30">'+
      '<label>Opacity <span id="duskWmOpacityVal">70</span>%</label><input id="duskWmOpacity" type="range" min="5" max="100" value="70">'+
      '<label>Rotation <span id="duskWmRotateVal">0</span>°</label><input id="duskWmRotate" type="range" min="-180" max="180" value="0">'+
      '<div class="wm-row"><button id="duskWmApply" class="primary">Add / Update</button><button id="duskWmRemove">Remove</button></div>';
    document.body.appendChild(panel);
    var stage=document.querySelector('main .stage') || document.querySelector('.stage') || document.querySelector('main');
    if(stage){ if(getComputedStyle(stage).position==='static') stage.style.position='relative'; var badge=document.createElement('div'); badge.id='duskWatermarkBadge'; badge.textContent=''; stage.appendChild(badge); }
    var badge=document.getElementById('duskWatermarkBadge');
    function sync(){
      if(!badge) return;
      badge.textContent=document.getElementById('duskWmText').value.trim();
      badge.style.fontSize=document.getElementById('duskWmSize').value+'px';
      badge.style.opacity=(document.getElementById('duskWmOpacity').value/100);
      badge.style.transform='translate(-50%,-50%) rotate('+document.getElementById('duskWmRotate').value+'deg)';
      badge.style.display=badge.textContent?'block':'none';
      document.getElementById('duskWmSizeVal').textContent=document.getElementById('duskWmSize').value;
      document.getElementById('duskWmOpacityVal').textContent=document.getElementById('duskWmOpacity').value;
      document.getElementById('duskWmRotateVal').textContent=document.getElementById('duskWmRotate').value;
    }
    btn.addEventListener('click',function(){panel.classList.toggle('show');});
    ['duskWmSize','duskWmOpacity','duskWmRotate'].forEach(function(id){document.getElementById(id).addEventListener('input',sync);});
    document.getElementById('duskWmApply').addEventListener('click',sync);
    document.getElementById('duskWmRemove').addEventListener('click',function(){document.getElementById('duskWmText').value='';sync();});
    if(badge){
      var dragging=false,ox=0,oy=0;
      badge.addEventListener('pointerdown',function(e){dragging=true;badge.setPointerCapture(e.pointerId);ox=e.clientX-badge.getBoundingClientRect().left;oy=e.clientY-badge.getBoundingClientRect().top;});
      badge.addEventListener('pointermove',function(e){if(!dragging)return;var r=stage.getBoundingClientRect();var x=Math.max(0,Math.min(r.width,e.clientX-r.left-ox));var y=Math.max(0,Math.min(r.height,e.clientY-r.top-oy));badge.style.left=x+'px';badge.style.top=y+'px';});
      badge.addEventListener('pointerup',function(){dragging=false;});
    }
    // Put the watermark into the main editor canvas immediately before export.
    function paintWatermark(){
      if(!badge || !badge.textContent) return;
      var c=document.querySelector('#afterCanvas') || document.querySelector('#mainCanvas') || document.querySelector('#editorCanvas') || document.querySelector('main canvas');
      if(!c || !c.getContext) return;
      var ctx=c.getContext('2d'); if(!ctx) return;
      var cr=c.getBoundingClientRect(), br=badge.getBoundingClientRect();
      var sx=c.width/cr.width, sy=c.height/cr.height;
      var x=(br.left+br.width/2-cr.left)*sx, y=(br.top+br.height/2-cr.top)*sy;
      var size=parseFloat(getComputedStyle(badge).fontSize)*sx;
      ctx.save(); ctx.globalAlpha=parseFloat(getComputedStyle(badge).opacity)||.7; ctx.fillStyle='#fff'; ctx.font='700 '+size+'px Arial'; ctx.textAlign='center'; ctx.textBaseline='middle';
      ctx.translate(x,y); ctx.rotate((parseFloat(document.getElementById('duskWmRotate').value)||0)*Math.PI/180); ctx.shadowColor='rgba(0,0,0,.7)'; ctx.shadowBlur=8; ctx.fillText(badge.textContent,0,0); ctx.restore();
    }
    document.addEventListener('click',function(e){
      var t=e.target; if(t && (t.id==='exportAll' || t.closest && t.closest('#exportAll'))) setTimeout(paintWatermark,0);
    },true);
    sync();
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',setup,{once:true}); else setup();
  setTimeout(setup,700); setTimeout(setup,1800);
})();
</script>
'''
# Add after the old removal patch so the new optional UI can be used.
s = s.replace('</head>', patch + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Optional watermark controls installed')
