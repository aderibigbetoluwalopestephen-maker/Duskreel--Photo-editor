from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Keep the existing desktop effect-box cleanup.
effect_marker = '/* DUSKREEL DESKTOP EFFECT BOX CLEANUP V1 */'
if effect_marker not in s:
    patch = r'''<style>
/* DUSKREEL DESKTOP EFFECT BOX CLEANUP V1 */
@media (min-width: 761px){
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

# Repair desktop image importing without touching the existing editor renderer.
# Capture-phase handling runs before the old change listener, preventing a broken
# or conflicting importer from swallowing the selected file.
upload_marker = '/* DUSKREEL DESKTOP IMAGE UPLOAD FIX V1 */'
if upload_marker not in s:
    upload_patch = r'''<script>
/* DUSKREEL DESKTOP IMAGE UPLOAD FIX V1 */
(function(){
  function installDesktopUploadFix(){
    const input = document.getElementById('photoInput');
    if(!input || input.dataset.duskUploadFix === '1') return;
    input.dataset.duskUploadFix = '1';

    const imageExtensions = new Set([
      'jpg','jpeg','jpe','jfif','png','webp','gif','bmp','dib','avif',
      'ico','tif','tiff','heic','heif','apng','jxl','jp2','j2k','jpf','jpm','jpx'
    ]);

    function isImageFile(file){
      if(!file) return false;
      const type = String(file.type || '').toLowerCase();
      if(type.startsWith('image/')) return true;
      const name = String(file.name || '').toLowerCase();
      const dot = name.lastIndexOf('.');
      return dot >= 0 && imageExtensions.has(name.slice(dot + 1));
    }

    function readImage(file){
      return new Promise((resolve,reject)=>{
        if(!isImageFile(file)) return reject(new Error('Unsupported image file'));
        const reader = new FileReader();
        reader.onload = event => {
          const img = new Image();
          img.onload = () => resolve(img);
          img.onerror = () => reject(new Error('The selected image could not be decoded by this browser.'));
          img.src = event.target.result;
        };
        reader.onerror = () => reject(reader.error || new Error('Could not read the selected image.'));
        reader.readAsDataURL(file);
      });
    }

    input.addEventListener('change', async function(event){
      event.preventDefault();
      event.stopImmediatePropagation();

      const files = Array.from(input.files || []).filter(isImageFile);
      if(!files.length){
        input.value = '';
        return;
      }

      try{
        if(typeof state === 'undefined' || !state || !Array.isArray(state.photos)){
          throw new Error('Duskreel editor state is not ready.');
        }

        for(const file of files){
          try{
            const img = await readImage(file);
            state.photos.push({
              id: (crypto && crypto.randomUUID) ? crypto.randomUUID() : ('photo-' + Date.now() + '-' + Math.random().toString(36).slice(2)),
              name: file.name || 'Image',
              img,
              spots: [],
              crop: null,
              edit: DEFAULT_EDIT()
            });
          }catch(error){
            console.warn('Duskreel could not open image:', file.name, error);
          }
        }

        if(state.photos.length && state.activeIndex === -1) state.activeIndex = 0;
        if(typeof renderThumbs === 'function') renderThumbs();
        if(typeof renderStageVisibility === 'function') renderStageVisibility();
        if(typeof render === 'function') render();
        if(typeof pushHistory === 'function') pushHistory();
      }finally{
        // Allow the same file to be selected again after editing/removing it.
        input.value = '';
      }
    }, true);
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', installDesktopUploadFix, {once:true});
  }else{
    installDesktopUploadFix();
  }
})();
</script>
'''
    needle = '</body>'
    if needle not in s:
        raise SystemExit('Could not find </body> in index.html')
    s = s.replace(needle, upload_patch + needle, 1)

p.write_text(s, encoding='utf-8')
print('Desktop effect cleanup and image upload fix are installed')
