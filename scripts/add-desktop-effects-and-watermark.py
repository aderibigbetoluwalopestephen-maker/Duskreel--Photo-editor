from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '/* DUSKREEL DESKTOP EFFECTS V2 */'
if marker in s:
    print('Desktop effects V2 already installed')
    raise SystemExit(0)

patch = r'''<style>
/* DUSKREEL DESKTOP EFFECTS V2 */
@media (min-width:761px){
  /* Replace the old tiny/empty effect tiles with compact usable controls. */
  #fxGrid, .fxGrid{display:grid !important;grid-template-columns:repeat(6,minmax(58px,1fr));gap:6px !important;padding:4px 0 !important;align-items:stretch;}
  #duskEffectsV2{display:grid;grid-template-columns:repeat(6,minmax(58px,1fr));gap:6px;margin-top:8px;max-width:100%;}
  #duskEffectsV2 button{min-width:0;height:30px;padding:0 7px;border:1px solid var(--line,#4A2A52);border-radius:5px;background:var(--panel-2,#2A1830);color:var(--ink-dim,#CBA6D1);font-size:10px;font-weight:600;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:.12s ease;}
  #duskEffectsV2 button:hover{background:var(--panel-3,#331D3B);color:#fff;border-color:var(--magenta,#E619A6);}
  #duskEffectsV2 button.active{background:var(--magenta,#E619A6);border-color:var(--magenta-bright,#FF4FC3);color:#fff;}
  #duskEffectsV2 .dusk-effects-title{grid-column:1/-1;font-size:11px;font-weight:700;color:#fff;margin:0 0 2px;}

  /* Keep watermark controls compact without removing the tool. */
  #watermarkControls,.watermark-controls,#watermarkPanel,.watermark-panel{padding:8px !important;gap:6px !important;max-width:420px !important;}
  #watermarkControls input,#watermarkControls select,.watermark-controls input,.watermark-controls select,#watermarkPanel input,#watermarkPanel select,.watermark-panel input,.watermark-panel select{height:28px !important;padding:4px 7px !important;font-size:11px !important;}
  #watermarkControls button,.watermark-controls button,#watermarkPanel button,.watermark-panel button{height:28px !important;padding:0 9px !important;font-size:11px !important;}
  #watermarkControls label,.watermark-controls label,#watermarkPanel label,.watermark-panel label{font-size:10.5px !important;margin:0 0 3px !important;}
}
</style>
<script>
/* DUSKREEL DESKTOP EFFECTS V2 JS */
(function(){
  const effects = [
    ['Normal','none'],['Vivid','saturate(1.35) contrast(1.08)'],['Bright','brightness(1.18)'],['Contrast','contrast(1.35)'],['Warm','sepia(.18) saturate(1.28)'],['Cool','hue-rotate(18deg) saturate(1.08)'],
    ['Mono','grayscale(1) contrast(1.08)'],['Noir','grayscale(1) contrast(1.55) brightness(.88)'],['Sepia','sepia(.85) contrast(1.05)'],['Vintage','sepia(.35) contrast(1.08) saturate(.82)'],['Fade','saturate(.72) brightness(1.08) contrast(.9)'],['Matte','contrast(.88) saturate(.78) brightness(1.04)'],
    ['Drama','contrast(1.55) saturate(1.12) brightness(.93)'],['Pop','saturate(1.65) contrast(1.18)'],['Glow','brightness(1.12) saturate(1.18)'],['Dream','brightness(1.08) contrast(.9) saturate(.9)'],['Film','contrast(1.12) saturate(.9) sepia(.12)'],['Golden','sepia(.28) saturate(1.35) brightness(1.04)'],
    ['Rose','sepia(.12) hue-rotate(315deg) saturate(1.28)'],['Teal','hue-rotate(155deg) saturate(1.18)'],['Blue','hue-rotate(185deg) saturate(1.15)'],['Purple','hue-rotate(275deg) saturate(1.18)'],['Green','hue-rotate(75deg) saturate(1.2)'],['Sunset','sepia(.25) hue-rotate(330deg) saturate(1.4)'],
    ['Soft','brightness(1.06) contrast(.9) blur(.15px)'],['Sharp','contrast(1.22) saturate(1.08)'],['B&W Soft','grayscale(1) contrast(.92) brightness(1.06)'],['B&W High','grayscale(1) contrast(1.7)'],['Cinematic','contrast(1.28) saturate(.78) sepia(.08)'],['Frost','saturate(.75) brightness(1.12) hue-rotate(10deg)'],
    ['Inkwell','grayscale(1) contrast(1.35) brightness(.95)'],['Lush','saturate(1.5) brightness(1.02)'],['Clear','contrast(1.18) saturate(1.08) brightness(1.03)'],['Dark','brightness(.78) contrast(1.2)'],['Light','brightness(1.28) contrast(.94)'],['Autumn','sepia(.22) hue-rotate(350deg) saturate(1.25)']
  ];

  function targetNodes(){
    const ids=['afterCanvas','previewCanvas','mainCanvas','editorCanvas','imageCanvas'];
    const found=[];
    ids.forEach(id=>{const el=document.getElementById(id);if(el)found.push(el);});
    document.querySelectorAll('main canvas').forEach(el=>{if(!found.includes(el))found.push(el);});
    document.querySelectorAll('main .stage img, main .canvas img, main .canvas-area img').forEach(el=>{if(!found.includes(el))found.push(el);});
    return found;
  }

  function applyFilter(filter,name,button){
    const nodes=targetNodes();
    nodes.forEach(el=>{el.style.filter=filter;el.dataset.duskEffect=name;});
    document.querySelectorAll('#duskEffectsV2 button').forEach(b=>b.classList.remove('active'));
    if(button)button.classList.add('active');
    window.dispatchEvent(new CustomEvent('duskreel-effect-change',{detail:{name,filter}}));
  }

  function install(){
    if(document.getElementById('duskEffectsV2')) return;
    const fx=document.getElementById('fxGrid') || document.querySelector('.fxGrid');
    if(!fx) return;
    fx.style.display='none';
    const wrap=document.createElement('div');
    wrap.id='duskEffectsV2';
    const title=document.createElement('div');
    title.className='dusk-effects-title';
    title.textContent='Effects';
    wrap.appendChild(title);
    effects.forEach(([name,filter])=>{
      const b=document.createElement('button');
      b.type='button';b.textContent=name;b.title=name;
      b.addEventListener('click',()=>applyFilter(filter,name,b));
      wrap.appendChild(b);
    });
    fx.parentNode.insertBefore(wrap,fx.nextSibling);
    applyFilter('none','Normal',wrap.querySelector('button'));
  }

  function boot(){
    install();
    setTimeout(install,300);
    setTimeout(install,1000);
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot); else boot();
})();
</script>
'''

needle = '</head>'
if needle not in s:
    raise SystemExit('Could not find </head> in index.html')
s = s.replace(needle, patch + needle, 1)
p.write_text(s, encoding='utf-8')
print('Desktop effects V2 and compact watermark controls installed')
