# FREEBOX — visual assets

Approved accents: teal `#1BC2A8`, blue `#4FB0D6`, gold `#F6B93B`, coral `#FF8A5C`. Background `#0E1A1E`, surface `#16272B`, border `#28413F`, text `#EAF3F1`.

Crew: FREYA / ENGINEERING · KRIPTO / SYSTEMS · TRACE / HARDWARE · LIRA / SECURITY. Preserve the approved illustrated crew panel; change labels locally rather than redesigning it.

`assets/freebox/social-preview.png`: 1280×640 cover, ready for repository Settings → Social preview. File presence alone does not configure the GitHub social preview setting.

## Regenerate animated links

Use Python with Pillow and DejaVu Sans fonts installed. Generators are under `scripts/`:

- `render-links.py` — four navigation links.
- `render-projects.py` — six original project links.
- `render-sockpuppet.py` — seventh project link using exactly the same renderer.

Each card is 520×160, 48 frames × 60 ms, infinite loop. Check every exported GIF is nonempty, decodes, and frames differ before publishing. Keep each asset below 5 MiB. Do not publish intermediary frames.

README assets and links must be checked with `python3 scripts/check-assets.py`. Illustration assets were generated with ImageGen; code-native link animations are rendered with Pillow.
