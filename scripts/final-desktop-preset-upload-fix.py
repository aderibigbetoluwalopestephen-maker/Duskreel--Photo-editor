from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove the previous upload-fix block that used stopImmediatePropagation and
# could prevent the editor's own importer from receiving the selected image.
s = re.sub(r'<script>\s*/\* DUSKREEL DESKTOP IMAGE UPLOAD FIX V1 \*/.*?</script>\s*', '', s, flags=re.S)

marker = 'DUSKREEL DESKTOP FINAL PRESET + UPLOAD FIX V1'
if marker not in s:
    patch = r'''<style>
/* DUSKREEL DESKTOP FINAL PRESET + UPLOAD FIX V1 */
@media (min-width:761px){
  /* Keep Presets visible and make every preset a true 1:1 square. */
  #duskRestoreTools{
    display:block!important;
    visibility:visible!important;
    opacity:1!important;
    z-index:999!important;
    width:270px!important;
    max-height:calc(100vh - 85px)!important;
    overflow:auto!important;
  }
  #duskRestorePresets{
    display:grid!important;
    grid-template-columns:repeat(6,30px)!important;
    grid-auto-rows:30px!important;
    gap:5px!important;
    align-items:start!important;
  }
  #duskRestorePresets button{
    width:30px!important;
    min-width:30px!important;
    max-width:30px!important;
    height:30px!important;
    min-height:30px!important;
    max-height:30px!important;
    padding:2px!important;
    margin:0!important;
    border-radius:5px!important;
    font-size:8px!important;
    line-height:1!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    text-align:center!important;
    overflow:hidden!important;
    white-space:normal!important;
  }
  /* Old empty effect boxes stay hidden; the real Presets above stay visible. */
  #fxGrid,.fxGrid{display:none!important;visibility:hidden!important;}
}
</style>
<script>
/* DUSKREEL DESKTOP FINAL PRESET + UPLOAD FIX V1 */
(function(){
  function showSelectedImage(file){
    if(!file) return;
    var type=String(file.type||'').toLowerCase();
    if(!type.startsWith('image/')) return;
    var reader=new FileReader();
    reader.onload=function(ev){
      var img=new Image();
      img.onload=function(){
        var canvases=[];
        ['afterCanvas','previewCanvas','mainCanvas','editorCanvas','imageCanvas'].forEach(function(id){
          var c=document.getElementById(id); if(c && c.getContext && !canvases.includes(c)) canvases.push(c);
        });
        document.querySelectorAll('main canvas').forEach(function(c){if(c.getContext&&!canvases.includes(c))canvases.push(c);});
        canvases.forEach(function(c){
          if(!c.width || !c.height){c.width=img.naturalWidth||img.width;c.height=img.naturalHeight||img.height;}
          var ctx=c.getContext('2d'); if(!ctx)return;
          ctx.clearRect(0,0,c.width,c.height);
          var scale=Math.min(c.width/img.naturalWidth,c.height/img.naturalHeight);
          var w=img.naturalWidth*scale,h=img.naturalHeight*scale;
          ctx.drawImage(img,(c.width-w)/2,(c.height-h)/2,w,h);
        });
        var stage=document.querySelector('main .stage')||document.querySelector('.stage');
        if(stage){
          var old=stage.querySelector('.dusk-upload-preview');
          if(old)old.remove();
          var preview=img.cloneNode(false); preview.className='dusk-upload-preview';
          preview.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:contain;z-index:2;pointer-events:none;display:block;';
          stage.appendChild(preview);
          setTimeout(function(){if(preview.parentNode)preview.remove();},1500);
        }
      };
      img.src=ev.target.result;
    };
    reader.readAsDataURL(file);
  }
  function install(){
    var input=document.getElementById('photoInput');
    if(!input || input.dataset.duskFinalUpload==='1')return;
    input.dataset.duskFinalUpload='1';
    input.addEventListener('change',function(){
      var files=Array.from(input.files||[]).filter(function(f){return String(f.type||'').toLowerCase().startsWith('image/');});
      files.forEach(showSelectedImage);
      /* Do not stop propagation: the original Duskreel importer must also run. */
      setTimeout(function(){input.value='';},100);
    },false);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',install,{once:true});else install();
  setTimeout(install,500);setTimeout(install,1200);
})();
</script>
'''
    s = s.replace('</head>', patch + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('Final desktop preset visibility, 1:1 sizing, and non-blocking image upload fix installed')
