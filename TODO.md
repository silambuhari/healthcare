# Vercel CSS Fix - TODO Progress

**Approved Plan**: Pure static deployment (root index.html + absolute CSS paths + vercel.json rewrites).

**Step 1: [DONE] Create root index.html** (copied from templates/index.html, fixed CSS to `/static/index.css`, disabled form POST).

**Step 2: [DONE] Update vercal.json** (added static/ rewrite rule).

**Step 3: [PENDING] User redeploys to Vercel** (git push or vercel CLI, check https://healthcare-q9km.vercel.app/).

**Step 4: [PENDING] Verify CSS loads** (F12 → Network: no 404 for /static/index.css & images).

**Future**: Serverless Flask functions for form backend (api/ folder).
