from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL DESKTOP PRESETS 1X1 V1'
if marker in s:
    print('Desktop presets 1x1 already installed')
    raise SystemExit(0)

patch = r'''<style>
/* DUSKREEL DESKTOP PRESETS 1X1 V1 */
@media (min-width:761px){
  #duskEffectsV2,#duskEffectsV4{
    grid-template-columns:repeat(8,30px)!important;
    gap:5px!important;
    padding:3px!important;
    max-height:220px!important;
    overflow-y:auto!important;
    align-items:start!important;
  }
  #duskEffectsV2 button,#duskEffectsV4 button{
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
    white-space:normal!important;
    overflow:hidden!important;
    text-overflow:clip!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    text-align:center!important;
  }
}
</style>
'''
if '</head>' not in s:
    raise SystemExit('Could not find </head>')
s = s.replace('</head>', patch + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Made desktop preset/effect buttons compact 1:1 squares like Crop tools')
