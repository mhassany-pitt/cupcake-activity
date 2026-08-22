# Cupcake Programming Activities Format

This repository defines and demonstrates the declarative **YAML format and JSON Schema** used by the **Cupcake** platform for authoring, exchanging, and rendering interactive programming learning activities.

---

## 🎯 Activity Types

Cupcake supports a diverse suite of programming activity formats. This repository introduces the specification and sample files, starting with **Worked Examples**.

### 1. Worked Example (`worked-example`)

A **Worked Example** provides step-by-step instructional code walkthroughs. It links human-readable explanations directly to specific source code snippets, explains control flow and syntax, and demonstrates sample runtime executions (console outputs, `stdin`, `stdout`, and `stderr`).

🔗 **Interactive Demo:**  
[Open demo/index.html](demo/index.html) or serve locally at `http://localhost:8000/demo/`.

---

## 📂 Repository Structure

```
.
├── schemas/
│   └── worked-example_0.1.0.json            # JSON Schema definition for worked-example activities
├── demo/
│   ├── index.html                           # Interactive demo page
│   ├── bank-account.worked-example.yaml     # Activity configuration (YAML format)
│   └── bank-account.py                      # Target source code referenced by the activity
├── viewer/
│   └── cupcake-activity-we.js               # Standalone single-file Web Component bundle
└── README.md
```

---

## 📐 Specification & Format Overview

A Cupcake activity YAML file defines metadata, pedagogy, runtime environment, source code references, and interactive elements.

### Top-Level Properties

| Field | Type | Description |
| :--- | :--- | :--- |
| `$schema` | `string` | URL / identifier of the JSON Schema (e.g. `https://learning-contents.org/schemas/worked-example/0.1.0`) |
| `id` | `string` | Unique identifier for the activity |
| `title` | `string` | Human-readable title |
| `description`| `string` | Brief overview or educational objective |
| `source` | `string` | Relative path to the underlying program file (e.g. `bank-account.py`) |
| `license` | `string` | Content license (e.g. `MIT`) |
| `locale` | `string` | IETF language tag (e.g. `en-US`) |
| `authors` | `array` | List of author objects with `first`, `last`, `email`, and `affiliation` |
| `pedagogy` | `object` | Pedagogical attributes: `activity`, `difficulty` (`novice`, `intermediate`, `advanced`), `prereq_topics`, and `topics` |
| `runtime` | `object` | Target execution environment: `language` (e.g. `python`) and `version` |
| `statement` | `string` | Markdown-supported activity prompt / background statement |
| `executions` | `array` | Sample execution scenarios showcasing expected console output, `stdin`, `stdout`, and status |
| `elements` | `array` | Interactive overlay elements (e.g., snippet explanations with matching locations) |

---

## 🔍 Example: Bank Account Management

### 1. `demo/bank-account.worked-example.yaml`

```yaml
$schema: https://learning-contents.org/schemas/worked-example/0.1.0
source: bank-account.py
license: MIT
locale: en-US
id: we_bank_account
title: Bank Account Management
description: Learn how to use classes and methods to manage a bank account in Python.
authors:
  - first: Jone
    last: Doe
    email: jone.doe@example.com
    affiliation: University of John Doe
pedagogy:
  activity: worked-example
  difficulty: novice
  prereq_topics: []
  topics:
    - classes
    - state
runtime:
  language: python
  version: 3
statement: |
  This worked example demonstrates how the `BankAccount` class manages state. We'll examine:
  1. Class constructor (`__init__`)
  2. Deposit method (`deposit`)
  3. Withdrawal method (`withdraw`)
executions:
  - title: Bob's Account
    stdin: []
    stdout: |-
      Deposited 100
      Withdrew 50
      Balance: 250
    console: |-
      Deposited 100
      Withdrew 50
      Balance: 250
    status: pass
elements:
  - type: explanation
    location:
      snippet: "def __init__(self, owner, balance):"
    explanations:
      - body: |
          The constructor initializes the account owner and an optional starting balance. In Python, this is written as:
          ```python
          def __init__(self, owner, balance):
              self.owner = owner
              self.balance = balance
          ```
          The parameter `balance` defaults to `0` if not provided.
      - body: |
          ...
  - type: explanation
    location:
      snippet: "if 0 < amount and amount <= self.balance:"
    explanations:
      - body: |
          This condition validates that the withdrawal transaction is correct: it checks if the `amount` is greater than `0` and is less than or equal to the current `self.balance`.
```

### 2. `demo/bank-account.py`

```python
class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
      print(f"Deposited {amount}")
    return self.balance

  def withdraw(self, amount):
    if 0 < amount and amount <= self.balance:
      self.balance = self.balance - amount
      print(f"Withdrew {amount}")
    else:
      print("Insufficient funds")
    return self.balance

account = BankAccount("Bob", 200)
account.deposit(100)
account.withdraw(50)
print(f"Balance: {account.balance}")
```

---

## 💻 Web Component Viewer

The worked example viewer is exported directly from `cupcake-web` as a **single-file standalone Web Component** (`<cupcake-worked-example>`) located at [`viewer/cupcake-activity-we.js`](viewer/cupcake-activity-we.js). All CSS, polyfills, CodeMirror, and markdown dependencies are inlined into this single file.

### Running the Local Demo

Because the demo loads the YAML and Python files via `fetch()`, serve the repository with any static server:

```bash
# From the repository root:
python3 -m http.server 8000
```

Then open [http://localhost:8000/demo/](http://localhost:8000/demo/) in your web browser.

### Embedding the Web Component

Embedding only requires importing the single JS bundle and instantiating the tag:

```html
<!-- 1. Single JS bundle (styles and polyfills bundled) -->
<script src="viewer/cupcake-activity-we.js" type="module"></script>
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>

<!-- 2. Web Component element -->
<cupcake-worked-example id="workedExample"></cupcake-worked-example>

<!-- 3. Provide YAML & source code -->
<script>
  customElements.whenDefined('cupcake-worked-example').then(async () => {
    const [yamlText, pythonCode] = await Promise.all([
      fetch('demo/bank-account.worked-example.yaml').then(r => r.text()),
      fetch('demo/bank-account.py').then(r => r.text())
    ]);

    const el = document.getElementById('workedExample');
    el.task = jsyaml.load(yamlText);
    el.sourceCode = pythonCode;
  });
</script>
```

---

## 🔗 Interactive Demo

Experience the interactive Worked Example viewer in action:

- **Live GitHub Pages Demo:** [https://mhassany-pitt.github.io/cupcake-activity/demo/](https://mhassany-pitt.github.io/cupcake-activity/demo/)
- **Local Preview via Local Server:**
  ```bash
  python3 -m http.server 8000
  ```
  Then open [http://localhost:8000/demo/](http://localhost:8000/demo/) in your browser.


