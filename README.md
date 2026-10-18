# Frauenkompass

Statische Landing Page (Seite im Aufbau) für Sara Emanuela Casellini-Machado Sousa, Fachärztin für Gynäkologie, Liechtenstein. Gestaltung nach dem Frauenraum-CI (Burgundy, Sand, Rose, Copper-Gradient, Playfair Display + Inter).

Kein Build-Schritt. `index.html` direkt öffnen oder als statische Seite deployen (z.B. Vercel, Netlify).

## Dateien

- `index.html`: Landing Page mit News-Anmeldung
- `datenschutz.html`: Datenschutzerklärung (DSGVO/EWR + DSG Liechtenstein)
- `impressum.html`: Impressum nach ECG
- `assets/`: Stylesheet, Symbol, Favicons, lokal eingebundene Schriften (keine Google-Fonts-Abrufe)

## Offen vor dem Livegang

1. Betreiberin ist stellvertretend die CM Ventures Anstalt, Duxgass 2, 9494 Schaan. Gelb markierte Stellen (`class="todo"`) suchen.
2. E-Mail-Adresse und Domain: Domain frauenkompass.ch (oder .li) sichern, Platzhalter `kontakt@frauenkompass.ch` bei Bedarf anpassen (auch `KONTAKT_EMAIL` in `index.html`).
3. Newsletter-Dienst wählen (z.B. Brevo, EU-Hosting) und dessen Formular-URL als `ENDPOINT` in `index.html` setzen. Bis dahin öffnet das Formular ein vorbereitetes Mail. Double-Opt-in im Dienst aktivieren. Name des Dienstes in `datenschutz.html` Punkt 4 eintragen.
4. Hosting: NEXEUM Digital Services GmbH, Vaduz (eingetragen). Klären, wo die Server stehen und ob ein AV-Vertrag besteht.
5. Impressum: Ärztekammer und Aufsichtsbehörde. Facharzttitel (Schweiz) gegenprüfen.
6. Datenschutz und Impressum vor dem Livegang juristisch gegenlesen lassen. Die Texte sind ein Entwurf, keine Rechtsberatung.
