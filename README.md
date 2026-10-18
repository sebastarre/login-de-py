# Al Revés

Juego para un solo celular (se pasan el teléfono). Es una web app instalable (PWA), sin dependencias ni build.

1. Un jugador graba una palabra (y la escribe, solo para verificar al final).
2. El siguiente la escucha **al revés** y se graba imitando exactamente lo que oyó.
3. Esa imitación se reproduce **al revés** y tiene que adivinar la palabra original. Acierta = +1 punto.

Los roles rotan cada ronda (2 a 6 jugadores).

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
