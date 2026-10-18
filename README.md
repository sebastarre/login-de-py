# Al Revés

Grabá una palabra con el micrófono, escuchala normal y escuchala al revés. Los turnos los manejan los jugadores entre sí. Es una web app instalable (PWA), sin dependencias ni build.

Botones: **Grabar** (o **Volver a grabar**), **Escuchar** y **Escuchar al revés**.

## Probar

El micrófono solo funciona en `localhost` o HTTPS:

```
python3 -m http.server 8000
```

Abrí `http://localhost:8000`. Para usarlo en el celu, publicá la carpeta en cualquier hosting HTTPS
(GitHub Pages, Netlify, Vercel…) y usá "Agregar a pantalla de inicio" / "Instalar app".

## Cómo funciona

`MediaRecorder` graba, `decodeAudioData` lo pasa a PCM, se recorta el silencio y se invierte el
arreglo de muestras; la reproducción usa Web Audio.
