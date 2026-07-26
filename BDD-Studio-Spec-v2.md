# Enterprise BDD Studio — Build Specification v2.0

> **Project:** Enterprise BDD Studio
> **Type:** Single-page HTML application (static, no backend)
> **Target:** GitHub Pages deployment
> **Audience:** Business Analysts, QA Engineers, Product Owners, Developers
> **Language:** Vanilla HTML5, CSS3, ES6+ JavaScript (zero dependencies)

---

## 1. Executive Summary

Build a **browser-based visual Gherkin editor** that allows BAs and testers to create, edit, visualize, simulate, and export BDD feature files. The app must feel **lively, modern, and professional**.

### Core Value Propositions
1. **Visual Editing** — WYSIWYG scenario builder
2. **Flow Visualization** — Auto-generated color-coded flowcharts
3. **Interactive Simulation** — Step-through with pass/fail marking
4. **Data-Driven Testing** — Examples tables with placeholder substitution
5. **Context Switching** — Pre-loaded domain templates
6. **Full Roundtrip** — Import/export `.feature` files
7. **Built-in Help** — Searchable help panel with indexed topics
8. **Zero Backend** — Pure client-side deployment

---

## 2. Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Markup | HTML5 | No build step |
| Styling | CSS3 custom properties | Dark theme, zero frameworks |
| Logic | Vanilla ES6+ | Zero dependencies |
| Storage | localStorage | Auto-save sessions |
| File I/O | FileReader / Blob | Import/export `.feature` |
| Clipboard | Clipboard API + fallback | Copy Gherkin |

---

## 3. Data Model

### 3.1 Application State
```javascript
appState = {
  context: string,           // "custom" | "ecommerce" | ...
  features: Feature[],
  activeFeatureId: string,
  mode: string,              // "edit" | "visual" | "simulate" | "gherkin"
  sim: {
    scenarioId: string,
    stepIndex: number,
    results: { [key]: "pass" | "fail" },
    exampleRowId: string     // selected data row
  }
}
```

### 3.2 Feature Object
```javascript
Feature = {
  id: string,
  name: string,
  desc: string,
  tags: string[],
  scenarios: Scenario[]
}
```

### 3.3 Scenario Object
```javascript
Scenario = {
  id: string,
  name: string,
  type: "scenario" | "scenario-outline",
  tags: string[],
  steps: Step[],
  examples: {
    headers: string[],
    rows: ExampleRow[]
  }
}
```

### 3.4 Step Object
```javascript
Step = {
  id: string,
  type: "given" | "when" | "then" | "and" | "but",
  text: string
}
```

### 3.5 Example Row Object
```javascript
ExampleRow = {
  id: string,
  cells: string[]
}
```

### 3.6 Context Templates
Pre-defined domain contexts with realistic scenarios and example data:
- `custom` — empty slate
- `ecommerce` — checkout, search, cart
- `banking` — transfers, balances
- `healthcare` — appointments
- `social` — posts, mentions
- `travel` — flights, bookings
- `saas` — onboarding, billing

---

## 4. UI Architecture

### 4.1 Layout (3-Panel)
```
+----------------------------------------------------------+
| HEADER (brand, help, context, import, export)           |
+----------+-----------------------------------------------+
|          | FEATURE META (title, description, tags)       |
| SIDEBAR  +-----------------------------------------------+
| (feature | TABS (Edit | Visual | Simulate | Gherkin)    |
|  list)   +-----------------------------------------------+
|          | MAIN CONTENT                                  |
+----------+-----------------------------------------------+
```

### 4.2 Help Panel (Slide-out)
- Right-side panel, 720px wide, slides in with animation
- Search bar at top filters topics in real-time
- Left nav: list of topics (Getting Started, Edit Mode, Examples, Visual Flow, Simulate, Gherkin View, Contexts, Tags, Shortcuts, FAQ)
- Right content: rendered HTML content for selected topic
- Overlay backdrop with blur
- Close via X button, overlay click, or Escape key

### 4.3 Color System (Dark Theme)
| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-primary` | `#0b0f19` | App background |
| `--bg-secondary` | `#111827` | Sidebar, header |
| `--bg-card` | `#151c2c` | Card surfaces |
| `--border` | `#1f2937` | Borders |
| `--text-primary` | `#f1f5f9` | Primary text |
| `--text-secondary` | `#94a3b8` | Secondary text |
| `--accent` | `#3b82f6` | Primary actions |
| `--success` | `#10b981` | Pass states |
| `--danger` | `#ef4444` | Fail states |
| `--given` | `#10b981` | Given steps |
| `--when` | `#3b82f6` | When steps |
| `--then` | `#f59e0b` | Then steps |
| `--and` | `#8b5cf6` | And steps |
| `--but` | `#ef4444` | But steps |

---

## 5. Feature Specifications

### 5.1 Sidebar
- New Feature button
- Load from file button (hidden file input)
- Feature list with hover delete
- Active state highlighting
- Auto-save indicator

### 5.2 Feature Meta Panel
- Title input (22px bold)
- Description textarea (As a / I want / So that)
- Tags as removable chips with add input

### 5.3 Edit Mode
**Scenario Cards:**
- Header: Type badge (clickable toggle SCENARIO/OUTLINE), name input, delete
- Step rows: Type badge (clickable cycle), text input, move up/down, delete
- Step toolbar: + Given, + When, + Then, + And, + But

**Examples Section (conditional):**
- Shown for Scenario Outlines or when examples exist
- Table with editable headers and cells
- Add/Remove columns
- Add/Delete rows
- If regular scenario has no examples, show "Add Examples Table" button (auto-converts to Outline)

### 5.4 Visual Flow Mode
- Vertical flowchart per scenario
- Color-coded nodes (Given=green, When=blue, Then=amber, And=purple, But=red)
- Gradient connectors between steps
- Hover lift animation
- Staggered entrance animation
- Examples table shown below flowchart if present

### 5.5 Simulate Mode
**Per Scenario:**
- Example picker dropdown (if examples exist) — select data row
- Step text shows substituted values: `<placeholder>` replaced with actual value, highlighted in blue
- Start / Prev / Next / Finish controls
- Current step: blue glow + pulse animation
- Pass (✓) / Fail (✕) buttons on active step
- Step states: Pending, Active, Pass (green), Fail (red)
- Summary bar: passed / failed / pending counts + active data set label

### 5.6 Gherkin View Mode
- Raw `.feature` content in `<pre>` block
- Copy button (clipboard)
- Download button (Blob + anchor)
- File naming: snake_case feature name + `.feature`

---

## 6. Import / Export

### 6.1 Import (Copy-Paste)
- Modal with textarea
- Parser handles: Feature, Scenario, Scenario Outline, Background, Examples tables, tags, all step keywords, comments
- Validation: null return shows error toast

### 6.2 Import (File Load)
- Hidden `<input type="file" accept=".feature,.txt">`
- FileReader reads as text
- Same parser as copy-paste

### 6.3 Export (Copy-Paste)
- Modal with read-only textarea
- Copy button with fallback

### 6.4 Export (Download)
- Blob generation
- Temporary anchor element

### 6.5 Gherkin Output Format
```gherkin
@tag1 @tag2
Feature: Feature Name
  As a role
  I want goal
  So that benefit

  @scenario-tag
  Scenario Outline: Scenario Name
    Given precondition with <placeholder>
    When action happens
    Then expected <result>

    Examples:
      | placeholder | result  |
      | value1      | success |
      | value2      | failure |
```

---

## 7. Help System

### 7.1 Trigger
- "?" button in header opens help panel

### 7.2 Panel Structure
- **Header**: "Help & Guide" title + close button
- **Search**: Input filters topics by title and keywords in real-time
- **Nav** (left, 220px): Topic list with active highlight, hidden items when filtered
- **Content** (right): HTML content of selected topic

### 7.3 Topics
1. **Getting Started** — Overview, quick start, first feature
2. **Edit Mode** — Adding steps, reordering, deleting, scenario types
3. **Examples & Data Tables** — Placeholders, columns, rows, simulation substitution
4. **Visual Flow** — Color coding, connectors, diagrams
5. **Simulate** — Walkthrough, pass/fail, example picker
6. **Gherkin View & Import/Export** — Copy, download, paste, file load
7. **Contexts & Templates** — Domain switching, pre-loaded examples
8. **Tags & Organization** — Feature tags, conventions
9. **Keyboard Shortcuts** — Supported keys
10. **FAQ & Troubleshooting** — Data storage, offline, collaboration, deployment

### 7.4 Search Behavior
- Real-time filtering as user types
- Matches against topic title and keywords field
- If active topic is filtered out, auto-select first visible topic
- Case-insensitive matching

---

## 8. Interactions & Animations

| Animation | Trigger | CSS Details |
|-----------|---------|-------------|
| `slideIn` | New step | opacity 0->1, translateX -8px->0, 0.3s |
| `popIn` | Visual node | opacity 0->1, scale 0.96->1, translateY 8px->0, 0.4s |
| `fadeIn` | Connectors | opacity 0->1, 0.3s |
| `pulse` | Active sim step | Box-shadow oscillation, 2s infinite |
| `modalIn` | Modal open | opacity 0->1, scale 0.95->1, translateY 10px->0, 0.3s |
| `toastIn` | Toast | opacity 0->1, translateX 20px->0, 0.3s |
| `helpSlideIn` | Help panel | translateX 100%->0, 0.35s cubic-bezier |

---

## 9. Persistence

### 9.1 localStorage
- Key: `rf_bdd_state_v2`
- Stores: features array + context string
- Auto-save on every mutation
- Load on init; fallback to E-Commerce context if empty/corrupt

---

## 10. Responsive Behavior

| Breakpoint | Behavior |
|------------|----------|
| > 768px | Full 3-panel layout |
| <= 768px | Sidebar 200px, title shrinks |
| <= 600px | (Future) Hamburger sidebar |

---

## 11. Accessibility

- Keyboard-focusable interactive elements
- Color + icon + text for all states
- Modal focus trap
- aria-label on icon buttons
- Sufficient contrast ratios

---

## 12. File Structure (GitHub Pages)

```
routeforge-bdd-studio/
├── index.html          # Single self-contained file
├── README.md           # Project description, usage guide
└── .github/
    └── workflows/
        └── pages.yml   # Optional: GitHub Actions
```

---

## 13. Testing Checklist

### Create & Edit
- [ ] Create new feature
- [ ] Edit title/desc/tags
- [ ] Add/remove/reorder steps
- [ ] Cycle step types
- [ ] Toggle scenario type
- [ ] Add/remove example columns
- [ ] Add/delete example rows
- [ ] Edit example cells

### Visual
- [ ] Flowcharts render correctly
- [ ] Examples table shown below flow

### Simulate
- [ ] Start simulation
- [ ] Pick example row from dropdown
- [ ] Verify placeholder substitution
- [ ] Mark pass/fail
- [ ] Prev/Next navigation
- [ ] Finish and summary

### Import/Export
- [ ] Paste Gherkin with Examples
- [ ] Load `.feature` file
- [ ] Download exports Examples correctly
- [ ] Copy to clipboard

### Help
- [ ] Open/close help panel
- [ ] Search filters topics
- [ ] Click topic switches content
- [ ] Auto-select on filter

---

## 14. Future Enhancements

1. Scenario Outlines with full Examples support (DONE in v2)
2. Background steps
3. Drag-and-drop reordering
4. Real-time collaborative editing
5. Dark/Light theme toggle
6. Mobile hamburger sidebar
7. Search/filter features in sidebar
8. Export visual diagrams to PNG/PDF
9. Cucumber/SpecFlow test runner integration
10. AI step suggestions

---

## 15. Performance & Security

- First paint: < 1s
- No external HTTP requests
- localStorage read/write: < 5ms
- Single HTML file < 100KB (excluding demo data)
- All data client-side, sandboxed to origin
- User input sanitized via textContent escaping

---

*End of Specification v2.0*
