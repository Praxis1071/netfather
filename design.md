# NetFather UI Design Strategy

> Living visual and interaction standard for the GTK4 + Libadwaita desktop application.
> Scope: presentation, information hierarchy, interaction clarity, responsive layout, and accessibility.
> Non-goal: changing networking, scanning, policy, firewall, persistence, or other business logic.

## 1. Product direction

NetFather should feel like a native, trustworthy Linux network-control workspace: calm, precise, readable, and immediately understandable to both newcomers and experienced administrators. Prefer GNOME/Libadwaita conventions over web-dashboard styling or decorative effects.

### Experience principles

1. **Clarity before density** — show the most important state and next action first; move secondary detail into sections, expanders, or selection details.
2. **One primary action per view** — give the main task clear visual priority; keep secondary actions neutral.
3. **Progressive disclosure** — advanced scan, identity, policy, and diagnostic details remain available without dominating the initial view.
4. **Consistent patterns** — reuse page headers, section headings, status treatments, list rows, empty states, and action placement.
5. **Trustworthy feedback** — distinguish idle, running, success, warning, offline, and failure states with both text and semantic styling; never rely on color alone.
6. **Safe and reversible presentation** — destructive or high-impact actions must remain visually distinct and retain existing confirmation behavior.
7. **Native first** — use GTK4/Libadwaita widgets and system theme colors; avoid custom web-like controls and hard-coded light/dark palettes.

## 2. Visual system

### Surfaces and hierarchy
- Use the system window and view colors as the foundation.
- Reserve .card for related content groups, not every individual widget.
- Use boxed lists for repeated peer records; keep row structure regular.
- Keep elevation, borders, and shadows subtle. Avoid nested cards and excessive outlines.
- Keep content aligned to a shared page gutter and a readable maximum width.

### Spacing
- Follow a consistent 6-point rhythm where practical: 6, 12, 18, 24, 30, 36.
- Page outer margins: approximately 24–28 points on roomy desktop layouts; reduce on narrow windows.
- Related controls: 8–12 points apart. Separate sections: 18–24 points.
- Card padding: approximately 12–18 points. Avoid large empty gaps and cramped rows.

### Typography
- Prefer system typography and GTK semantic classes (title-1, title-2, heading, body, caption, dim-label).
- Use no more than a few clear levels per view: page title, section title, primary value, supporting description.
- Use weight and size sparingly; avoid all-caps, decorative fonts, and long unbroken technical strings.
- Use monospace only for values where character-by-character comparison matters (IP, MAC, ports, IDs).

### Color and status
- Respect Adwaita light, dark, high-contrast, and user accent settings.
- Prefer semantic GTK theme colors/classes (success, warning, error) rather than fixed hex values.
- Pair every status color with a readable label or icon/text cue.
- Reserve suggested-action styling for the single most important action in a view; destructive styling only for destructive actions.

## 3. Page composition

Every page should follow this order when applicable:
1. Page title and a short, plain-language explanation.
2. At-a-glance summary or current state.
3. Primary task/action.
4. Main content (list, table, metrics, topology, or form).
5. Selection-specific or advanced details.
6. History, diagnostics, and secondary information.

Do not force every page into an identical card layout. Choose the simplest native pattern that fits its content.

## 4. Page-specific direction

- **Dashboard:** prioritize current network state, key metrics, and the next useful action. Keep activity and secondary summaries visually subordinate.
- **Network Discovery:** make the primary scan action obvious; summarize selected scan mode and target; keep advanced options grouped and collapsible; provide clear progress, cancellation, empty, and completion states.
- **Devices:** present a scannable device list with concise online/offline/conflict indicators; keep detailed identity evidence and editing controls in a clearly separated detail area.
- **Network Topology:** emphasize the network relationships and legend; keep labels readable and prevent visual clutter; explain unavailable/unknown data explicitly.
- **Profiles:** make active/default state, profile purpose, and available actions easy to compare; group configuration details.
- **Rules:** make scope, action, schedule, enabled state, and next transition scannable; keep editing and preview distinct from the rule list.
- **Monitoring:** establish metric hierarchy and consistent units; align values and labels; make warning thresholds and unavailable readings understandable.
- **Events:** optimize for chronology and scanning; distinguish severity, timestamp, and event description without noisy decoration.
- **Settings and navigation:** out of scope for this pass; preserve their structure and behavior exactly.

## 5. Interaction and content

- Use concise, action-oriented labels and familiar language; explain specialist terms at the point of use.
- Keep labels visible; do not rely on placeholder text as the only label.
- Align related controls consistently and use suitable native controls.
- Show validation and operation feedback close to the affected control or content.
- Empty states should say what is empty and, where useful, what the user can do next.
- Loading states should preserve layout and communicate that work is in progress.
- Avoid showing raw exceptions or dense diagnostic output as the primary user-facing message.
- Preserve keyboard navigation, focus visibility, tooltips for icon-only controls, and screen-reader names.

## 6. Adaptive behavior

- Design for the narrowest supported window first, then enhance for wide desktop.
- Support at least the application's 360×480 minimum window and the GNOME desktop baseline around 1024×600.
- On narrow widths, stack columns, allow controls to wrap, and avoid fixed-width form rows.
- On wide widths, use grids only when each column remains comfortably readable; constrain long text.
- Never let a layout depend on the user manually resizing the window to reveal essential controls.

## 7. Implementation guardrails

- UI-only changes: do not modify service calls, task scheduling, scan options, state transitions, persistence, policy evaluation, firewall behavior, or data models.
- Do not alter sidebar, navigation, settings, or application window behavior without explicit approval.
- Reuse existing shared page primitives and CSS classes where possible; avoid page-specific CSS duplication.
- Preserve translations: all new user-visible strings must use tr().
- Keep GTK widget access on the GTK main thread; do not move UI work into background workers.
- Keep existing confirmation flows and accessibility semantics.
- Before editing any tracked UI file, save an immutable, byte-for-byte backup under backups/ on main.
- Work directly on main only. Never create or switch branches unless explicitly instructed.

## 8. Quality gates

For each page change:
1. Inspect the current page and its data/state dependencies.
2. Identify presentation-only improvements and explicitly exclude behavior changes.
3. Back up the exact current file before editing.
4. Make the smallest coherent change.
5. Run syntax/format checks and focused tests where available.
6. Run the full repository test suite / CI.
7. Review the diff for accidental backend, navigation, or settings changes.
8. Record completed work and remaining issues in this document.

## 9. Research references

- GNOME Human Interface Guidelines: https://developer.gnome.org/hig/
- Design principles: https://developer.gnome.org/hig/principles.html
- UI styling and general guidelines: https://developer.gnome.org/hig/guidelines.html
- Typography: https://developer.gnome.org/hig/guidelines/typography.html
- Scaling and adaptiveness: https://developer.gnome.org/hig/guidelines/adaptive.html
- Accessibility: https://developer.gnome.org/hig/guidelines/accessibility.html
- Boxed lists: https://developer.gnome.org/hig/patterns/containers/boxed-lists.html
- List and column views: https://developer.gnome.org/hig/patterns/containers/list-column-views.html
- Libadwaita adaptive layout and component guidance: https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/

These platform references are the source of truth for native GTK/Libadwaita conventions. This document translates them into NetFather-specific implementation constraints and page priorities.

## 10. Progress log

- 2026-11-15: Established shared page spacing, page title/subtitle classes, metric-card styling, semantic status colors, and boxed-list spacing on main. CI passed for Python 3.12, 3.13, 3.14, editable install, nftables integration, and GTK4 adaptive/lifecycle checks.
- 2026-11-15: Added immutable pre-change backups for Devices, Discovery, Topology, Profiles, and Rules under backups/ui-before-next-pass-2026-11-15/; refined their list hierarchy, status readability, details surfaces, and advanced-options presentation. No service or policy logic was intentionally changed.
- Next: inspect the rendered GTK pages and CI results; then review Dashboard, Monitoring, and Events for any remaining presentation gaps.