# Architecture diagrams

`make_diagrams.py` draws diagrams 01, 04 and 06; `more_diagrams.py` imports it and draws 02, 03, 05, 07 and 08. The JPEG thumbnails are embedded into 01 and 04.

```bash
cd scripts/diagrams
python more_diagrams.py ../../docs/public/diagrams
node ../generate-asset-manifest.mjs
```
