from make_diagrams import Svg, LINE, BLUE, BLUE2, MUTED, INK, CARD_STROKE


def note(s, x, y, w, h, lines, size=16):
    s.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fbfcfe" stroke="#9db7ee" stroke-width="1.6" stroke-dasharray="7 6"/>')
    top = y + h / 2 - (len(lines) - 1) * 12 + 6
    for i, l in enumerate(lines):
        s.text(x + w / 2, top + 24 * i, l, size, 600 if i == 0 else 400, BLUE if i == 0 else MUTED, 'middle')


# ---------- 02 Monorepo components ----------
s = Svg(1600, 800, 'Monorepo components',
        'Document and scene engines feed the authoring and authority libraries and the export libraries. Those libraries power five application surfaces: the Next.js web app, the Electron desktop app, the FastAPI authority, the headless worker and the MCP server.')
s.group(40, 30, 470, 740, 'Document and scene engines')
for i, (t, sub, ic) in enumerate([('presentation-schema', 'Canonical .mydeck contract', 'file'),
                                  ('presentation-core', 'Transactions', 'code'),
                                  ('layout-engine, renderer', 'Deterministic scene', 'layers'),
                                  ('animation-engine', 'Motion and timing', 'play'),
                                  ('deck-presets', 'Reviewed templates', 'tag')]):
    s.card(64, 80 + i * 136, 422, 110, t, [sub], ic)
s.group(565, 30, 470, 330, 'Authoring and authority')
s.card(589, 80, 422, 110, 'editor, editor-ui', ['Canvas and inspector'], 'pen')
s.card(589, 216, 422, 110, 'workspace-contracts', ['and workspace-client'], 'shield', tone='accent')
s.group(565, 440, 470, 330, 'Export libraries')
s.card(589, 490, 422, 110, 'export-core', ['Shared export pipeline'], 'cog')
s.card(589, 626, 422, 110, 'export-pdf, export-pptx', ['Format adapters'], 'file')
s.arrow([(800, 600), (800, 626)])
s.group(1090, 30, 470, 740, 'Application surfaces')
for i, (t, sub, ic) in enumerate([('Next.js web', 'Browser studio', 'globe'),
                                  ('Electron desktop', 'Local studio', 'monitor'),
                                  ('FastAPI authority', 'Workspace API', 'server'),
                                  ('Headless worker', 'Render and export jobs', 'layers'),
                                  ('MCP server', 'Agent tools', 'bot')]):
    s.card(1114, 80 + i * 136, 422, 110, t, [sub], ic, tone='accent' if i == 4 else 'default')
s.arrow([(510, 200), (565, 200)], 'model and\ntransactions', 537, 140)
s.arrow([(510, 610), (565, 610)], 'scene and\nmotion', 537, 550)
s.arrow([(1035, 200), (1090, 200)], 'editor and\nclient', 1062, 140)
s.arrow([(1035, 610), (1090, 610)], 'PDF and\nPPTX', 1062, 550)
s.save('02-monorepo-components.svg')


# ---------- 03 Generation and rendering ----------
s = Svg(1600, 820, 'Generation and deterministic rendering',
        'A brief, template or draft goes to a model or deterministic planner, which writes a structured story plan. After an outline review, the deterministic composer produces a validated .mydeck document, resolved into an IntermediateScene that drives the editable canvas, presenting, previews, and the PDF and PowerPoint adapters with degradation reports. The model proposes meaning; code owns coordinates, timing and validation.')
row = [('Brief or template', ['Or an existing draft'], 'pen', 'default'),
       ('Planner', ['Model or deterministic'], 'bot', 'accent'),
       ('Story plan', ['Intent, copy, semantic', 'layout'], 'file', 'default'),
       ('Outline review', ['Draft checked by you'], 'user-check', 'default'),
       ('Composer', ['Deterministic'], 'cog', 'accent')]
for i, (t, sub, ic, tone) in enumerate(row):
    s.card(40 + i * 310, 70, 270, 120, t, sub, ic, tone=tone)
    if i:
        s.arrow([(40 + i * 310 - 40, 130), (40 + i * 310, 130)], 'approved' if i == 4 else None, 40 + i * 310 - 20, 98)
note(s, 350, 240, 890, 70, ['Model proposes meaning. Code owns coordinates, timing and validation.'], 18)
s.arrow([(485, 240), (485, 190)], 'design boundary', 485, 214, dashed=True)
s.arrow([(1240, 275), (1330, 275), (1330, 190)], 'enforces', 1290, 250, dashed=True)
s.card(1280, 370, 280, 120, 'Validated .mydeck', ['Structured document'], 'shield', tone='accent')
s.arrow([(1450, 190), (1450, 370)])
s.card(900, 370, 310, 120, 'IntermediateScene', ['Resolved geometry', 'and semantics'], 'layers')
s.arrow([(1280, 430), (1210, 430)], 'schema\nvalidation', 1245, 520)
s.group(40, 560, 1520, 230, 'Derived outputs, all from the same scene')
outs = [('Editable canvas', ['Direct authoring'], 'monitor'),
        ('Present', ['Presenter and audience'], 'play'),
        ('Previews', ['Preview, critic images'], 'layers'),
        ('PDF adapter', ['PDF plus degradation', 'report'], 'file'),
        ('PPTX adapter', ['PowerPoint plus', 'degradation report'], 'file')]
for i, (t, sub, ic) in enumerate(outs):
    s.card(64 + i * 296, 620, 280, 130, t, sub, ic)
s.arrow([(1055, 490), (1055, 560)])
s.save('03-generation-rendering.svg')


# ---------- 05 Desktop local runtime ----------
s = Svg(1600, 920, 'Desktop local runtime',
        'Inside the Deckastra Electron process, the React renderer talks to the Electron main process over IPC and to a same-origin proxy over relative HTTP only. The main process injects a per-launch secret, supervises the FastAPI sidecar on a random loopback port, and publishes a scoped 12-hour grant to the MCP adapter that coding agents use. The sidecar owns the local SQLite workspace, files and the bundled render worker. Cloud credentials stay in the main process.')
s.card(40, 110, 260, 100, 'Windows user', ['Edits and presents'], 'user')
s.card(40, 750, 260, 110, 'Coding agent', ['Antigravity, Claude', 'Code, Codex'], 'bot', tone='accent')
s.group(330, 40, 1230, 450, 'Deckastra Electron process')
s.card(360, 100, 320, 110, 'React renderer', ['editor-ui'], 'monitor')
s.card(760, 100, 340, 110, 'Electron main', ['Native host and', 'supervisor'], 'shield', tone='accent')
s.card(1190, 100, 340, 90, 'Presenter window', [], 'play')
s.card(760, 300, 340, 110, 'Attachment publisher', ['Scoped grants for agents'], 'key')
s.card(360, 280, 320, 100, 'Same-origin proxy', ['Request proxy'], 'server')
note(s, 1190, 300, 340, 110, ['Security property', 'The renderer never gets', 'the port or launch secret'])
s.arrow([(300, 160), (360, 160)])
s.arrow([(680, 155), (760, 155)], 'IPC', 720, 128)
s.arrow([(1100, 145), (1190, 145)])
s.arrow([(930, 210), (930, 300)])
s.arrow([(420, 210), (420, 280)], 'relative\nHTTP only', 420, 245)
s.arrow([(800, 210), (800, 240), (600, 240), (600, 280)], 'injects per-launch secret', 700, 240)
s.group(330, 530, 860, 370, 'Private loopback runtime')
s.card(360, 590, 360, 110, 'FastAPI sidecar', ['Random loopback port'], 'server', tone='accent')
s.card(360, 760, 360, 100, 'MCP adapter', ['Agent tool calls'], 'bot')
for i, (t, ic) in enumerate([('Local SQLite workspace', 'database'), ('Assets, exports, backups', 'bucket'), ('Render and export worker', 'layers')]):
    s.card(830, 580 + i * 102, 340, 84, t, [], ic)
s.add(f'<path d="M800 622 V826" stroke="{LINE}" stroke-width="2.2" fill="none"/>')
s.arrow([(720, 645), (800, 645)])
for i in range(3):
    s.arrow([(800, 622 + i * 102), (830, 622 + i * 102)])
s.arrow([(420, 380), (420, 590)])
s.arrow([(1100, 175), (1160, 175), (1160, 515), (680, 515), (680, 590)], 'supervise and restart', 920, 515)
s.arrow([(760, 380), (745, 380), (745, 810), (720, 810)], '12-hour\ngrant', 760, 735, color=BLUE2, width=2.6)
s.arrow([(300, 805), (360, 805)])
s.arrow([(540, 760), (540, 700)])
s.card(1230, 600, 330, 120, 'Account and providers', ['Optional gateway'], 'cloud', tone='muted', dashed=True)
s.arrow([(1190, 660), (1230, 660)], 'gateway\naddress only', 1210, 760, dashed=True)
s.arrow([(1040, 100), (1040, 66), (1580, 66), (1580, 660), (1560, 660)], 'credentials stay\nin main', 1505, 540, dashed=True)
s.save('05-desktop-local-runtime.svg')


# ---------- 07 Auth, storage and export (sequence) ----------
actors = [('Web or desktop', 'monitor'), ('Identity provider', 'lock'), ('Workspace API', 'server'),
          ('PostgreSQL', 'database'), ('Object storage', 'bucket'), ('Export worker', 'layers')]
X = [150, 380, 610, 840, 1070, 1300]
steps = [
    ('Open a workspace', [(0, 1, 'Authenticate'), (1, 0, 'OIDC account token'), (0, 2, 'Authorized workspace request'),
                          (2, 2, 'Verify token, membership, capability'), (2, 3, 'Read presentation head'),
                          (3, 2, 'Versioned document state'), (2, 0, 'Workspace response')]),
    ('Upload media', [(0, 2, 'Request upload grant'), (2, 2, 'Validate type, size and quota'),
                      (2, 0, 'Short-lived signed upload'), (0, 4, 'Upload bytes directly'), (0, 2, 'Complete upload'),
                      (2, 3, 'Record asset metadata, ownership')]),
    ('Export the current deck', [(0, 2, 'Save, export pinned version'), (2, 3, 'Create durable export job'),
                                 (2, 5, 'Dispatch isolated work'), (5, 3, 'Load pinned document and job'),
                                 (5, 4, 'Read private assets'), (5, 5, 'Build scene and target file'),
                                 (5, 4, 'Write private export'), (5, 3, 'Store result and report'),
                                 (0, 2, 'Poll or receive task status'), (2, 0, 'Short-lived private download')]),
]
ROW = 48
total = sum(len(m) for _, m in steps)
H = int(150 + total * ROW + len(steps) * 70 + 30)
s = Svg(1450, H, 'Authentication, storage and export',
        'Sequence: the client signs in with the identity provider and sends an authorized request that the workspace API verifies against PostgreSQL. Media uploads use a short-lived signed URL straight to private object storage. Exports create a durable job in PostgreSQL that an isolated worker runs, writing the file and report to private storage before the client gets a short-lived private download.')
# Layer order: step bands, then lifelines, then actor cards and messages on top.
y = 150
for title, msgs in steps:
    bh = len(msgs) * ROW + 54
    s.add(f'<rect x="30" y="{y}" width="1390" height="{bh}" rx="14" fill="#f6f8fd" stroke="#dbe4f6" stroke-width="1.4"/>')
    s.text(50, y + 28, title.upper(), 15, 700, BLUE)
    y += bh + 16
for (name, ic), x in zip(actors, X):
    s.add(f'<path d="M{x} 120 V{H - 30}" stroke="#a9bde6" stroke-width="2" stroke-dasharray="4 6"/>')
    s.add(f'<rect x="{x - 105}" y="20" width="210" height="96" rx="12" fill="#ffffff" stroke="{CARD_STROKE}" stroke-width="1.6" filter="url(#shadow)"/>')
    s.icon(ic, x, 52, 20)
    s.text(x, 100, name, 17, 650, INK, 'middle')
s.add('<g stroke="#f6f8fd" stroke-width="5" paint-order="stroke" stroke-linejoin="round">')
y = 150
n = 1
for title, msgs in steps:
    y += 54
    for a, b, label in msgs:
        cy = y + ROW / 2
        if a == b:
            x = X[a]
            if a == len(X) - 1:
                s.add(f'<path d="M{x} {cy - 4} h-40 v18 h34" fill="none" stroke="{LINE}" stroke-width="2" marker-end="url(#arrow)"/>')
                s.text(x - 52, cy + 10, f'{n}. {label}', 15.5, 400, '#334155', 'end')
            else:
                s.add(f'<path d="M{x} {cy - 4} h40 v18 h-34" fill="none" stroke="{LINE}" stroke-width="2" marker-end="url(#arrow)"/>')
                s.text(x + 52, cy + 10, f'{n}. {label}', 15.5, 400, '#334155')
        else:
            x1, x2 = X[a], X[b]
            d = 1 if x2 > x1 else -1
            col = BLUE2 if a == 0 or b == 0 else LINE
            s.add(f'<path d="M{x1} {cy + 10} H{x2 - d * 4}" fill="none" stroke="{col}" stroke-width="2.2" marker-end="url(#{"arrowBlue" if col == BLUE2 else "arrow"})"/>')
            s.text((x1 + x2) / 2, cy + 2, f'{n}. {label}', 15.5, 400, '#334155', 'middle')
        n += 1
        y += ROW
    y += 16
s.add('</g>')
s.save('07-auth-storage-export-connections.svg')


# ---------- 08 Scaling, failure and cost controls ----------
s = Svg(1600, 880, 'Scaling, failure and cost controls',
        'Interactive API traffic, heavy exports and paid AI requests each go to their own compute boundary: API revisions, an export worker running one job per instance, and a provider gateway. Durable state lives in PostgreSQL and private object storage. Release, job, spend, recovery and telemetry controls are applied at those boundaries. These are configured controls; live operational proof is separate.')
s.group(40, 30, 420, 470, 'Demand')
s.group(510, 30, 520, 470, 'Independent compute')
s.group(1080, 30, 480, 470, 'Durable state')
dem = [('Interactive traffic', ['API requests'], 'globe'), ('Paid AI requests', ['Media, translation, speech'], 'cloud'), ('Heavy exports', ['CPU and memory bound'], 'layers')]
cmp = [('API revisions', ['Scale to zero, bounded', 'max, request concurrency'], 'server'),
       ('Provider gateway', ['Timeouts, classified', 'errors'], 'shield'),
       ('Export worker', ['One job per instance,', 'bounded instances'], 'layers')]
for i, ((t, sub, ic), (t2, sub2, ic2)) in enumerate(zip(dem, cmp)):
    y = 80 + i * 138
    s.card(64, y, 372, 116, t, sub, ic)
    s.card(534, y, 472, 116, t2, sub2, ic2, tone='accent')
    s.arrow([(436, y + 58), (534, y + 58)])
s.arrow([(770, 218), (770, 196)])
s.card(1104, 100, 432, 130, 'PostgreSQL', ['Versions, jobs, credits'], 'database')
s.card(1104, 300, 432, 130, 'Private object storage', ['Assets and exports'], 'bucket')
s.arrow([(1006, 138), (1104, 160)])
s.arrow([(1006, 162), (1104, 350)])
s.arrow([(1006, 414), (1104, 190)])
s.arrow([(1006, 440), (1104, 380)])
s.group(40, 560, 1520, 290, 'Controls applied at these boundaries')
ctl = [('Release', ['Readiness, migrations,', 'named-revision rollback'], 'branch'),
       ('Jobs', ['Idempotency, retry,', 'cancellation'], 'check'),
       ('Spend', ['Credits, quotes, budgets,', 'provider stop'], 'tag'),
       ('Recovery', ['Backups, PITR,', 'restore rehearsal'], 'history'),
       ('Telemetry', ['Structured telemetry', 'and diagnostics'], 'activity')]
for i, (t, sub, ic) in enumerate(ctl):
    s.card(64 + i * 296, 614, 280, 140, t, sub, ic)
s.add(f'<path d="M800 556 V504" stroke="{BLUE2}" stroke-width="3" marker-end="url(#arrowBlue)"/>')
s.text(800, 822, 'Configured controls. Live operational proof is documented separately.', 16, 500, MUTED, 'middle')
s.save('08-scaling-failure-cost-controls.svg')
print('ok')
