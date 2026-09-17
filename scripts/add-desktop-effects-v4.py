from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '/* DUSKREEL DESKTOP EFFECTS V4 */'
if marker in s:
    print('Desktop effects V4 already installed')
    raise SystemExit(0)

patch = r'''<style>
/* DUSKREEL DESKTOP EFFECTS V4 */
@media (min-width:761px){
  #duskEffectsV2{max-height:260px;overflow-y:auto;padding-right:3px;}
  #duskEffectsV2 .dusk-effects-title{position:sticky;top:0;z-index:2;padding:3px 0;background:var(--panel,#171119);}
  #duskEffectsV4 button{min-width:0;height:30px;padding:0 7px;border:1px solid var(--line,#4A2A52);border-radius:5px;background:var(--panel-2,#2A1830);color:var(--ink-dim,#CBA6D1);font-size:10px;font-weight:600;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:.12s ease;}
  #duskEffectsV4 button:hover{background:var(--panel-3,#331D3B);color:#fff;border-color:var(--magenta,#E619A6);}
  #duskEffectsV4 button.active{background:var(--magenta,#E619A6);border-color:var(--magenta-bright,#FF4FC3);color:#fff;}
}
</style>
<script>
/* DUSKREEL DESKTOP EFFECTS V4 JS */
(function(){
  const effects = [
    ['Portrait','brightness(1.04) contrast(1.02) saturate(.92)'],
    ['Natural','brightness(1.02) contrast(1.04) saturate(1.02)'],
    ['Clean','brightness(1.06) contrast(1.10) saturate(1.05)'],
    ['Fresh','brightness(1.10) contrast(1.03) saturate(1.16)'],
    ['Rich','contrast(1.18) saturate(1.30) brightness(.98)'],
    ['Punch','contrast(1.35) saturate(1.38) brightness(.98)'],
    ['Crisp','contrast(1.28) brightness(1.03) saturate(1.08)'],
    ['HDR','contrast(1.42) saturate(1.24) brightness(1.01)'],
    ['Moody','brightness(.82) contrast(1.28) saturate(.88)'],
    ['Shadow','brightness(.88) contrast(1.38) saturate(.92)'],
    ['Midnight','brightness(.68) contrast(1.42) saturate(.82)'],
    ['Mystic','brightness(.92) contrast(1.18) hue-rotate(275deg) saturate(1.12)'],
    ['Ocean','hue-rotate(175deg) saturate(1.24) contrast(1.05)'],
    ['Aqua','hue-rotate(155deg) saturate(1.35) brightness(1.03)'],
    ['Lavender','hue-rotate(260deg) saturate(1.12) brightness(1.06)'],
    ['Plum','hue-rotate(300deg) saturate(1.28) contrast(1.06)'],
    ['Berry','hue-rotate(325deg) saturate(1.34) contrast(1.04)'],
    ['Coral','hue-rotate(340deg) saturate(1.24) brightness(1.04)'],
    ['Peach','sepia(.16) hue-rotate(350deg) saturate(1.18) brightness(1.08)'],
    ['Honey','sepia(.24) saturate(1.34) brightness(1.06)'],
    ['Copper','sepia(.32) saturate(1.28) contrast(1.08)'],
    ['Rust','sepia(.30) hue-rotate(345deg) saturate(1.45) contrast(1.08)'],
    ['Olive','sepia(.16) hue-rotate(45deg) saturate(1.18) contrast(1.06)'],
    ['Emerald','hue-rotate(80deg) saturate(1.40) contrast(1.05)'],
    ['Forest','hue-rotate(65deg) saturate(1.18) brightness(.88) contrast(1.16)'],
    ['Electric','saturate(1.72) contrast(1.22) brightness(1.03)'],
    ['Neon','saturate(1.90) contrast(1.28) brightness(1.06)'],
    ['Pastel','saturate(.70) contrast(.86) brightness(1.14)'],
    ['Candy','saturate(1.30) contrast(.92) brightness(1.10)'],
    ['Cloud','saturate(.58) contrast(.86) brightness(1.16)'],
    ['Silver','grayscale(.72) contrast(1.16) brightness(1.08)'],
    ['Platinum','grayscale(.88) contrast(1.24) brightness(1.05)'],
    ['Charcoal','grayscale(1) contrast(1.38) brightness(.84)'],
    ['Classic','contrast(1.08) saturate(.92) sepia(.06)'],
    ['Retro','sepia(.38) contrast(1.12) saturate(.88)'],
    ['Polaroid','brightness(1.10) contrast(.90) saturate(.86) sepia(.10)'],
    ['Faded Film','contrast(.88) saturate(.70) brightness(1.12) sepia(.08)'],
    ['Film Gold','contrast(1.10) saturate(.90) sepia(.20) brightness(1.03)'],
    ['Cine Dark','brightness(.82) contrast(1.34) saturate(.78) sepia(.07)'],
    ['Cine Blue','brightness(.92) contrast(1.28) saturate(.78) hue-rotate(185deg)'],
    ['Cine Teal','contrast(1.25) saturate(.82) hue-rotate(160deg)'],
    ['Soft Skin','brightness(1.05) contrast(.90) saturate(.88)'],
    ['Bright Skin','brightness(1.15) contrast(.94) saturate(.94)'],
    ['Studio','brightness(1.08) contrast(1.06) saturate(.96)'],
    ['Wedding','brightness(1.12) contrast(.92) saturate(.86) sepia(.08)'],
    ['Travel','saturate(1.25) contrast(1.10) brightness(1.04)'],
    ['Food','saturate(1.48) contrast(1.12) brightness(1.02)'],
    ['Landscape','saturate(1.38) contrast(1.20) brightness(1.01)'],
    ['Night','brightness(.72) contrast(1.30) saturate(.92)'],
    ['Street','contrast(1.34) saturate(.84) brightness(.94)'],
    ['Urban','contrast(1.26) saturate(.76) brightness(.92)'],
    ['Soft Noir','grayscale(1) contrast(1.20) brightness(1.02)'],
    ['High Key','brightness(1.24) contrast(.82) saturate(.86)'],
    ['Low Key','brightness(.76) contrast(1.42) saturate(.84)'],
    ['Bleach','contrast(1.28) saturate(.56) brightness(1.04)'],
    ['Cross Process','contrast(1.30) saturate(1.24) hue-rotate(18deg)'],
    ['Chrome','contrast(1.46) saturate(.72) brightness(1.02)'],
    ['Glam','brightness(1.10) contrast(.96) saturate(1.06) sepia(.05)'],
    ['Magic','brightness(1.08) contrast(.88) saturate(1.08) hue-rotate(320deg)'],
    ['Fairy','brightness(1.12) contrast(.84) saturate(.92) hue-rotate(290deg)'],
    ['Aurora','saturate(1.34) hue-rotate(125deg) brightness(1.05) contrast(1.08)']
  ];

  function nodes(){
    const ids=['afterCanvas','previewCanvas','mainCanvas','editorCanvas','imageCanvas'];
    const out=[];
    ids.forEach(id=>{const e=document.getElementById(id);if(e&&!out.includes(e))out.push(e);});
    document.querySelectorAll('main canvas,main .stage img,main .canvas img,main .canvas-area img').forEach(e=>{if(!out.includes(e))out.push(e);});
    return out;
  }

  function install(){
    const base=document.getElementById('duskEffectsV2');
    if(!base || document.getElementById('duskEffectsV4')) return;
    const wrap=document.createElement('div');
    wrap.id='duskEffectsV4';
    wrap.style.cssText='display:grid;grid-template-columns:repeat(6,minmax(58px,1fr));gap:6px;margin-top:6px;';
    effects.forEach(([name,filter])=>{
      const b=document.createElement('button');
      b.type='button'; b.textContent=name; b.title=name;
      b.addEventListener('click',()=>{
        nodes().forEach(el=>{el.style.filter=filter;el.dataset.duskEffect=name;});
        document.querySelectorAll('#duskEffectsV2 button,#duskEffectsV4 button').forEach(x=>x.classList.remove('active'));
        b.classList.add('active');
        window.dispatchEvent(new CustomEvent('duskreel-effect-change',{detail:{name,filter}}));
      });
      wrap.appendChild(b);
    });
    base.parentNode.insertBefore(wrap,base.nextSibling);
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(install,50)); else setTimeout(install,50);
})();
</script>
'''
needle='</head>'
if needle not in s:
    raise SystemExit('Could not find </head>')
s=s.replace(needle,patch+needle,1)
p.write_text(s,encoding='utf-8')
print('Added 60 more compact desktop effects')
