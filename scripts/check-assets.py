"""Validate local README images without external badge-service dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Images(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag != 'img':
            return
        source = attrs.get('src', '')
        if source.startswith(('https://', 'http://')):
            return
        path = (ROOT / source).resolve()
        if not source or not path.is_relative_to(ROOT) or not path.is_file():
            raise SystemExit(f'Missing or invalid image: {source}')
        if path.suffix == '.svg':
            ET.parse(path)
        print(f'OK {source}')

Images().feed((ROOT / 'README.md').read_text())
