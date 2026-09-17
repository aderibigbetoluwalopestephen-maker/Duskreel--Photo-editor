from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='DUSKREEL DESKTOP PRESETS COMPACT V1'
if marker in s:
    print('already installed')
    raise SystemExit
patch='''<style>\n/* DUSKREEL DESKTOP PRESETS COMPACT V1 */\n@media (min-width:761px){\n  /* Match preset controls to the compact Crop tool footprint. */\n  #duskEffectsV2{display:grid!important;grid-template-columns:repeat(6,minmax(54px,1fr))!important;gap:5px!important;max-height:none!important;overflow:visible!important;padding:4px!important;}\n  #duskEffectsV2 button{min-width:0!important;width:100%!important;height:30px!important;padding:4px 5px!important;margin:0!important;border-radius:5px!important;font-size:10px!important;line-height:1.05!important;}\n  /* Remove the old tiny/empty effect boxes completely. */\n  #fxGrid,.fxGrid,#fxGrid>*{display:none!important;width:0!important;height:0!important;min-width:0!important;min-height:0!important;padding:0!important;margin:0!important;border:0!important;box-shadow:none!important;}\n  #fxGrid:empty,.fxGrid:empty{display:none!important;}\n}\n</style>\n<script>\n(function(){\n  function clean(){\n    document.querySelectorAll('#fxGrid,.fxGrid').forEach(function(el){el.style.setProperty('display','none','important');el.setAttribute('aria-hidden','true');});\n  }\n  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',clean,{once:true}); else clean();\n  setTimeout(clean,300); setTimeout(clean,1000);\n})();\n</script>\n'''
s=s.replace('</head>',patch+'</head>',1)
p.write_text(s,encoding='utf-8')
print('desktop presets compacted and old effect boxes removed')
