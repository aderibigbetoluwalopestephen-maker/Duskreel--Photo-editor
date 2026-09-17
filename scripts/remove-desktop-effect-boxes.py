from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '/* DUSKREEL DESKTOP EFFECT BOX CLEANUP V1 */'
if marker in s:
    print('Desktop effect cleanup already installed')
    raise SystemExit(0)

patch = r'''<style>
/* DUSKREEL DESKTOP EFFECT BOX CLEANUP V1 */
@media (min-width: 761px){
  /* Remove the tiny empty effect tiles shown beneath the Effects heading on desktop. */
  #fxGrid,
  .fxGrid{
    display:none !important;
  }
}
</style>
'''
needle = '</head>'
if needle not in s:
    raise SystemExit('Could not find </head> in index.html')
s = s.replace(needle, patch + needle, 1)
p.write_text(s, encoding='utf-8')
print('Desktop effect boxes removed')
