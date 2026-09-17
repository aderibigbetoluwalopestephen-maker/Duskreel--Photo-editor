from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '/* DUSKREEL DESKTOP EFFECTS V3 FINAL */'
if marker in s:
    print('Desktop effects V3 already installed')
    raise SystemExit(0)

patch = r'''<style>
/* DUSKREEL DESKTOP EFFECTS V3 FINAL */
@media (min-width:761px){
  /* Keep the legacy empty grid hidden; use the new compact named buttons instead. */
  #fxGrid,.fxGrid{display:none !important;}
  #duskEffectsV2{display:grid !important;grid-template-columns:repeat(6,minmax(58px,1fr));gap:6px !important;}
}
</style>
'''
needle = '</head>'
if needle not in s:
    raise SystemExit('Could not find </head> in index.html')
s = s.replace(needle, patch + needle, 1)
p.write_text(s, encoding='utf-8')
print('Final desktop effect layout cleanup installed')
