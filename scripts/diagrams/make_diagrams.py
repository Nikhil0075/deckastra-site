import base64, os, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]

BLUE = '#1d4ed8'
BLUE2 = '#2563eb'
TINT = '#eaf1ff'
INK = '#111827'
MUTED = '#4b5563'
LINE = '#64748b'
CARD_STROKE = '#d3ddf0'
RED = '#b42318'
RED_TINT = '#fdecea'
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

ICONS = {
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-5.8 6.5-5.8s6.5 2.2 6.5 5.8"/><circle cx="17" cy="9" r="2.8"/><path d="M16.5 14.4c3 .2 5 2.1 5 5"/>',
    'user-check': '<circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3.1-6.5 7-6.5 1.6 0 3 .4 4.2 1.1"/><path d="M15 17l2.5 2.5L22 15"/>',
    'bot': '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4.5"/><circle cx="12" cy="3.5" r="1.2"/><circle cx="9" cy="14" r="1.3"/><circle cx="15" cy="14" r="1.3"/><path d="M2 13v3M22 13v3"/>',
    'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.4 8.2-8 9-4.6-.8-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'cog': '<circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="7.5"/><path d="M12 1.5v3M12 19.5v3M1.5 12h3M19.5 12h3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 12.5l9 5 9-5"/><path d="M3 17l9 5 9-5"/>',
    'file': '<path d="M6 2h8.5L20 7.5V22H6z"/><path d="M14 2v6h6"/>',
    'cloud': '<path d="M7 19h10.5a4.5 4.5 0 0 0 .4-9 6.5 6.5 0 0 0-12.6 1.6A3.8 3.8 0 0 0 7 19z"/>',
    'database': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    'bucket': '<ellipse cx="12" cy="6" rx="8" ry="2.5"/><path d="M4 6l2 14c.3 1.2 3 2 6 2s5.7-.8 6-2l2-14"/>',
    'key': '<circle cx="8" cy="15" r="4.5"/><path d="M11.2 11.8L20 3M17 6l3 3M14.5 8.5l2 2"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
    'server': '<rect x="3" y="3.5" width="18" height="7" rx="1.5"/><rect x="3" y="13.5" width="18" height="7" rx="1.5"/><path d="M7 7h.01M7 17h.01"/>',
    'activity': '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
    'branch': '<circle cx="6" cy="5" r="2.2"/><circle cx="6" cy="19" r="2.2"/><circle cx="18" cy="7" r="2.2"/><path d="M6 7.2v9.6M18 9.2c0 4.5-6 4-12 7.6"/>',
    'package': '<path d="M12 2.5l8.5 4.7v9.6L12 21.5l-8.5-4.7V7.2z"/><path d="M12 12l8.5-4.8M12 12v9.5M12 12L3.5 7.2"/>',
    'x-circle': '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    'history': '<path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1"/><path d="M3 4v5h5"/><path d="M12 7.5V12l3 2"/>',
    'code': '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6"/>',
    'tag': '<path d="M3 12.5V3h9.5l8.5 8.5-9.5 9.5z"/><circle cx="7.5" cy="7.5" r="1.6"/>',
    'check': '<path d="M4.5 12.5l5 5L20 7"/>',
    'pen': '<path d="M4 20h4.5L20 8.5 15.5 4 4 15.5z"/><path d="M13.5 6l4.5 4.5"/>',
    'save': '<path d="M5 3h11l3 3v15H5z"/><path d="M8 3v5h7V3M8 21v-7h8v7"/>',
    'undo': '<path d="M9 14L4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/>',
    'play': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M10 8.5v4.5l4-2.25z"/><path d="M8 21h8"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7.5a4 4 0 0 1 8 0V11"/>',
}


class Svg:
    def __init__(self, w, h, title, desc):
        self.w, self.h = w, h
        self.parts = []
        self.title, self.desc = title, desc

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=17, weight=400, color=INK, anchor='start'):
        self.add(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')

    def icon(self, name, cx, cy, r=26, color=BLUE, bg=TINT):
        s = (r * 1.15) / 24
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}"/>')
        self.add(f'<g transform="translate({cx - 12 * s:.2f},{cy - 12 * s:.2f}) scale({s:.3f})" fill="none" stroke="{color}" stroke-width="{2 / s * 1.1:.2f}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')

    def card(self, x, y, w, h, title, lines=(), icon=None, tone='default', badge=None, dashed=False):
        stroke, fill, icolor, ibg = CARD_STROKE, '#ffffff', BLUE, TINT
        if tone == 'accent':
            stroke = '#9db7ee'
        if tone == 'negative':
            stroke, fill, icolor, ibg = '#f3c3bd', '#fffafa', RED, RED_TINT
        if tone == 'muted':
            stroke, fill = '#d9dee7', '#fbfcfe'
        dash = ' stroke-dasharray="7 6"' if dashed else ''
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{dash} filter="url(#shadow)"/>')
        tx = x + 22
        block = 26 + 23 * len(lines)
        ty = y + h / 2 - block / 2 + 20
        if icon:
            self.icon(icon, x + 46, y + h / 2, 25, icolor, ibg)
            tx = x + 88
        self.text(tx, ty, title, 20, 650)
        for i, line in enumerate(lines):
            self.text(tx, ty + 26 + 23 * i, line, 16.5, 400, MUTED)
        if badge:
            bw = 11 + 8.6 * len(badge)
            self.add(f'<rect x="{x + w - bw - 14}" y="{y + 14}" width="{bw}" height="24" rx="12" fill="{TINT}"/>')
            self.text(x + w - bw / 2 - 14, y + 31, badge, 13, 650, BLUE, 'middle')

    def group(self, x, y, w, h, label, fill='#f6f8fd', stroke='#c9d6f0', dashed=True, size=15):
        dash = ' stroke-dasharray="8 7"' if dashed else ''
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{dash}/>')
        self.text(x + 20, y + 30, label.upper(), size, 700, BLUE)

    def arrow(self, pts, label=None, lx=None, ly=None, color=LINE, width=2.2, dashed=False):
        d = 'M' + ' L'.join(f'{px},{py}' for px, py in pts)
        dash = ' stroke-dasharray="7 6"' if dashed else ''
        marker = 'arrowBlue' if color == BLUE2 else 'arrow'
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"{dash} marker-end="url(#{marker})"/>')
        if label:
            if lx is None:
                (ax, ay), (bx, by) = pts[0], pts[1]
                lx, ly = (ax + bx) / 2, (ay + by) / 2
            self.label(lx, ly, label)

    def label(self, lx, ly, label):
        lines = label.split('\n')
        w = max(len(l) for l in lines) * 8.1 + 18
        h = 22 * len(lines) + 6
        self.add(f'<rect x="{lx - w / 2:.1f}" y="{ly - h / 2:.1f}" width="{w:.1f}" height="{h}" rx="6" fill="#ffffff" stroke="#e5e9f2"/>')
        for i, l in enumerate(lines):
            self.text(lx, ly - h / 2 + 19 + 22 * i, l, 15, 500, '#334155', 'middle')

    def image(self, x, y, w, h, path):
        data = base64.b64encode(open(os.path.join(HERE, path), 'rb').read()).decode()
        cid = f'clip{len(self.parts)}'
        self.add(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/></clipPath>')
        self.add(f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})" href="data:image/jpeg;base64,{data}"/>')
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="#d3ddf0" stroke-width="1.4"/>')

    def save(self, name):
        head = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" role="img" aria-labelledby="t d" font-family="{FONT}">
<title id="t">{escape(self.title)}</title><desc id="d">{escape(self.desc)}</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{LINE}"/></marker>
<marker id="arrowBlue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{BLUE2}"/></marker>
<filter id="shadow" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#1e3a8a" flood-opacity="0.08"/></filter>
</defs>
<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>
'''
        with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(head + '\n'.join(self.parts) + '\n</svg>\n')


# ---------- 01 System context ----------
s = Svg(1600, 900, 'Deckastra system context',
        'People and external coding agents work through the Deckastra studio and workspace authority. Deterministic engines render the shared audience view and PDF or PowerPoint exports. AI and media providers are optional and governed.')
s.text(40, 52, 'PEOPLE AND AGENTS', 15, 700, BLUE)
s.card(40, 90, 330, 104, 'Presentation author', ['Creates, edits, presents'], 'user')
s.card(40, 250, 330, 104, 'Reviewer or approver', ['Decides on every proposal'], 'user-check')
s.card(40, 410, 330, 130, 'External coding agent', ['Antigravity · Claude Code', 'Codex · other MCP clients'], 'bot', tone='accent')
s.card(40, 700, 330, 104, 'Audience', ['View-only link'], 'users')

s.group(450, 30, 740, 840, 'Deckastra product boundary', fill='#f5f8ff', stroke='#93b0ec')
s.add(f'<rect x="480" y="80" width="680" height="320" rx="12" fill="#ffffff" stroke="{CARD_STROKE}" stroke-width="1.6" filter="url(#shadow)"/>')
s.icon('monitor', 526, 128, 25)
s.text(568, 125, 'Web or desktop studio', 20, 650)
s.text(568, 149, 'Canvas, inspector, review, presenter', 16.5, 400, MUTED)
s.image(500, 176, 640, 204, 'studio.jpg')
s.card(480, 450, 330, 130, 'Workspace authority', ['Versioned .mydeck document', 'Proposals and history'], 'shield', tone='accent')
s.card(830, 450, 330, 130, 'Deterministic engines', ['Layout, render, animation', 'Same scene everywhere'], 'cog')
s.card(480, 640, 330, 110, 'Shared audience view', ['View-only, live ink'], 'play')
s.card(830, 640, 330, 110, 'Export worker', ['Background PDF and PPTX jobs'], 'layers')
s.text(820, 840, 'Agents propose. Engines compose. People approve.', 16, 600, BLUE, 'middle')

s.text(1240, 52, 'OUTSIDE SERVICES', 15, 700, BLUE)
s.card(1240, 450, 320, 130, 'AI and media providers', ['Translation, voice, media', 'Optional, credit-governed'], 'cloud', tone='muted', dashed=True)
s.add(f'<rect x="1240" y="640" width="320" height="110" rx="12" fill="#ffffff" stroke="{CARD_STROKE}" stroke-width="1.6" filter="url(#shadow)"/>')
for i, (lbl, col) in enumerate([('PDF', '#b42318'), ('PPTX', '#c2410c')]):
    fx = 1268 + i * 74
    s.add(f'<path d="M{fx} 660h34l14 14v58h-48z" fill="#ffffff" stroke="{col}" stroke-width="2"/>')
    s.add(f'<path d="M{fx + 34} 660v14h14" fill="none" stroke="{col}" stroke-width="2"/>')
    s.add(f'<rect x="{fx - 6}" y="700" width="{44 if lbl == "PDF" else 54}" height="20" rx="4" fill="{col}"/>')
    s.text(fx + (16 if lbl == 'PDF' else 21), 715, lbl, 12.5, 700, '#ffffff', 'middle')
s.text(1420, 692, 'Exports', 20, 650)
s.text(1420, 716, 'With a report', 16.5, 400, MUTED)

s.arrow([(370, 142), (480, 142)], 'creates, edits', 425, 116)
s.arrow([(370, 302), (480, 302)], 'reviews', 425, 276)
s.arrow([(370, 475), (430, 475), (430, 515), (480, 515)], 'scoped MCP:\nread, propose, export', 410, 590, color=BLUE2, width=2.6)
s.arrow([(645, 400), (645, 450)])
s.arrow([(810, 515), (830, 515)])
s.arrow([(645, 580), (645, 640)])
s.arrow([(995, 580), (995, 640)])
s.arrow([(1160, 515), (1240, 515)], 'governed\nrequests', 1200, 420, dashed=True)
s.arrow([(1160, 695), (1240, 695)], 'PDF, PPTX', 1200, 625)
s.arrow([(480, 752), (420, 752), (370, 752)], 'view-only', 425, 790)
s.save('01-system-context.svg')


# ---------- 04 Change proposal lifecycle ----------
s = Svg(1600, 820, 'Change proposal lifecycle',
        'Agent requests and your own edits become a PatchOperation list and a version-bound proposal, validated against the current head. Agent changes go to human review; approved or direct edits apply as one transaction that creates a new version with an inverse for undo. Rejected, expired, invalid or stale work never changes the deck.')
s.text(40, 46, 'WHERE A CHANGE COMES FROM', 15, 700, BLUE)
s.card(40, 70, 300, 104, 'Agent or assistant', ['MCP or assistant request'], 'bot', tone='accent')
s.card(40, 196, 300, 104, 'Your own edit', ['Canvas gesture, inspector', 'or a sync update'], 'pen')
s.card(390, 126, 270, 104, 'PatchOperation list', ['Typed operations'], 'code')
s.card(700, 126, 250, 104, 'Proposal', ['Bound to a version'], 'tag')
s.card(1000, 126, 300, 104, 'Validate', ['Against the current head'], 'check')
s.arrow([(340, 122), (365, 122), (365, 162), (390, 162)], color=BLUE2, width=2.6)
s.arrow([(340, 248), (365, 248), (365, 196), (390, 196)])
s.arrow([(660, 178), (700, 178)], color=BLUE2, width=2.6)
s.arrow([(950, 178), (1000, 178)], color=BLUE2, width=2.6)

# decision diamond
cx, cy = 1135, 370
s.add(f'<path d="M{cx} {cy - 62} L{cx + 105} {cy} L{cx} {cy + 62} L{cx - 105} {cy} Z" fill="#ffffff" stroke="#9db7ee" stroke-width="1.8" filter="url(#shadow)"/>')
s.text(cx, cy - 4, 'Agent change?', 18, 650, INK, 'middle')
s.text(cx, cy + 20, 'needs approval', 15, 400, MUTED, 'middle')
s.arrow([(1135, 230), (1135, 308)], color=BLUE2, width=2.6)

# human review card with screenshot
s.add(f'<rect x="1300" y="250" width="270" height="330" rx="12" fill="#ffffff" stroke="#9db7ee" stroke-width="1.8" filter="url(#shadow)"/>')
s.icon('user-check', 1342, 292, 24)
s.text(1378, 289, 'Human review', 20, 650)
s.text(1378, 312, 'You decide', 16.5, 400, MUTED)
s.image(1318, 334, 234, 150, 'review.jpg')
s.text(1320, 512, 'Compare before and after,', 15.5, 400, MUTED)
s.text(1320, 534, 'play proposed motion,', 15.5, 400, MUTED)
s.text(1320, 556, 'approve or reject.', 15.5, 400, MUTED)
s.arrow([(1240, 370), (1300, 370)], 'yes', 1268, 344, color=BLUE2, width=2.6)

s.card(620, 318, 330, 110, 'Apply as one change', ['transactions.applyPatch', 'Document must stay valid'], 'layers', tone='accent')
s.arrow([(1030, 370), (950, 370)], 'no: your own edit', 990, 300)
s.arrow([(1300, 520), (1250, 520), (1250, 620), (840, 620), (840, 428)], 'approve', 1045, 620, color=BLUE2, width=2.6)

s.card(1300, 660, 270, 100, 'Closed, no change', ['Rejected or expired'], 'x-circle', tone='negative')
s.arrow([(1435, 580), (1435, 660)], 'reject or expire', 1435, 622)
s.card(560, 700, 330, 100, 'Refused', ['Current version is kept'], 'x-circle', tone='negative')
s.arrow([(700, 428), (700, 700)], 'invalid or stale', 700, 560)
s.arrow([(1040, 230), (1040, 262), (995, 262), (995, 742), (890, 742)], 'stale', 995, 680, dashed=True)

s.card(240, 318, 320, 110, 'New version', ['Saved with its inverse'], 'save')
s.arrow([(620, 373), (560, 373)])
s.card(240, 478, 320, 104, 'Persist and reconcile', ['Every window agrees'], 'server')
s.arrow([(400, 428), (400, 478)])
s.card(240, 632, 320, 104, 'Version history', ['Preview and restore'], 'history')
s.arrow([(400, 582), (400, 632)])
s.add('<rect x="40" y="478" width="170" height="258" rx="12" fill="#fbfcfe" stroke="#d9dee7" stroke-width="1.6" stroke-dasharray="7 6"/>')
s.icon('undo', 125, 530, 24)
for i, l in enumerate(['Undo applies', 'the inverse as', 'a new change,', 'so history', 'stays complete.']):
    s.text(125, 586 + 24 * i, l, 16, 400, MUTED, 'middle')
s.save('04-change-proposal-lifecycle.svg')


# ---------- 06 Google Cloud topology ----------
s = Svg(1600, 900, 'Sanitized Google Cloud topology',
        'Browsers and the desktop client sign in through Identity Platform and reach Cloud Run web and API services. The API uses Cloud SQL, storage buckets and secret references, hands export work to a Cloud Run worker, and calls Vertex AI and Translation only for governed requests. GitHub Actions builds images into Artifact Registry for deployment.')
s.text(40, 52, 'CLIENTS', 15, 700, BLUE)
s.card(40, 180, 280, 100, 'Web browser', ['Deckastra web app'], 'globe')
s.card(40, 330, 280, 100, 'Desktop client', ['Local app'], 'monitor')

s.group(370, 24, 1200, 670, 'Google Cloud project (sanitized)', fill='#f7f9fe', stroke='#93b0ec', size=15)
s.group(400, 70, 360, 590, 'Identity and entry', fill='#ffffff', stroke='#d3ddf0')
s.card(420, 116, 320, 100, 'Identity Platform', ['OIDC sign-in'], 'lock')
s.card(420, 290, 320, 100, 'Cloud Run: web', ['Serves the web app'], 'server', tone='accent')
s.card(420, 470, 320, 100, 'Cloud Run: API', ['Application API'], 'server', tone='accent')

s.group(800, 70, 360, 300, 'Background work', fill='#ffffff', stroke='#d3ddf0')
s.card(820, 116, 320, 100, 'Export worker', ['Cloud Run, PDF and PPTX'], 'layers')
s.card(820, 240, 320, 100, 'Migration job', ['Cloud Run job, schema'], 'cog')

s.group(1190, 70, 360, 300, 'Providers and operations', fill='#ffffff', stroke='#d3ddf0')
s.card(1210, 116, 320, 100, 'AI providers', ['Vertex AI, Translation'], 'cloud', tone='muted', dashed=True)
s.card(1210, 240, 320, 100, 'Logging, metrics', ['and alerts'], 'activity')

s.group(800, 400, 750, 260, 'Private data services', fill='#ffffff', stroke='#d3ddf0')
s.card(820, 446, 340, 90, 'Cloud SQL', ['PostgreSQL'], 'database')
s.card(820, 552, 340, 90, 'Secret references', [], 'key')
s.card(1190, 446, 340, 58, 'Assets bucket', [], 'bucket')
s.card(1190, 515, 340, 58, 'Exports bucket', [], 'bucket')
s.card(1190, 584, 340, 58, 'Font-pack bucket', [], 'bucket')

s.arrow([(320, 230), (360, 230), (360, 340), (420, 340)], 'HTTPS', 365, 300)
s.arrow([(320, 360), (380, 360), (380, 520), (420, 520)], 'API calls', 340, 470)
s.arrow([(320, 200), (380, 200), (380, 166), (420, 166)], 'sign in', 360, 140, dashed=True)
s.arrow([(580, 390), (580, 470)])
s.arrow([(740, 520), (800, 520)], None)
s.arrow([(740, 495), (780, 495), (780, 166), (820, 166)], 'jobs', 780, 330)
s.arrow([(1140, 166), (1210, 166)], None, dashed=True)
s.arrow([(980, 340), (980, 400)])
s.label(1175, 140, 'governed')

s.text(370, 742, 'DELIVERY', 15, 700, BLUE)
s.card(370, 760, 320, 100, 'GitHub Actions', ['CI and release'], 'branch')
s.card(760, 760, 320, 100, 'Build source', ['Short-lived'], 'package')
s.card(1150, 760, 320, 100, 'Artifact Registry', ['Container images'], 'package', tone='accent')
s.arrow([(690, 810), (760, 810)])
s.arrow([(1080, 810), (1150, 810)])
s.arrow([(1310, 760), (1310, 694)], 'deploy', 1360, 727)
s.save('06-google-cloud-topology.svg')
print('ok')
