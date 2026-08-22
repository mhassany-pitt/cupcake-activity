# Cupcake Programming Activities Format

This repository defines and demonstrates the declarative **YAML format and JSON Schema** used by the **Cupcake** platform for authoring, exchanging, and rendering interactive programming learning activities.

---

## 🎯 Activity Types

Cupcake supports a diverse suite of programming activity formats. This repository introduces the specification and sample files, starting with **Worked Examples**.

### 1. Worked Example (`worked-example`)

A **Worked Example** provides step-by-step instructional code walkthroughs. It links human-readable explanations directly to specific source code snippets, explains control flow and syntax, and demonstrates sample runtime executions (console outputs, `stdin`, `stdout`, and `stderr`).

🔗 **Live Online Demo:**  
[Open Sample Worked Example on Cupcake Web](https://adapt2.sis.pitt.edu/cupcake/#/activities/sample-py-bank-account/worked-example.yaml)

---

## 📂 Repository Structure

```
.
├── schemas/
│   └── worked-example_0.1.0.json       # JSON Schema definition for worked-example activities
├── samples/
│   ├── worked-example.yaml             # Example activity configuration (YAML format)
│   └── main.py                         # Target source code referenced by the activity
├── viewer/
│   └── index.html                      # Standalone, interactive HTML viewer for the activity
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
| `source` | `string` | Relative path to the underlying program file (e.g. `main.py`) |
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

### 1. `samples/worked-example.yaml`

```yaml
$schema: https://learning-contents.org/schemas/worked-example/0.1.0
source: main.py
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

### 2. `samples/main.py`

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

## 💻 Standalone Viewer

A zero-dependency standalone HTML/JS viewer is provided under [`viewer/index.html`](viewer/index.html).

### Running the Local Viewer

Because the viewer loads the sample YAML and Python files via `fetch()`, serve the directory using any static HTTP server:

```bash
# Using Python 3 built-in HTTP server:
python3 -m http.server 8000
```

Then visit [http://localhost:8000/viewer/](http://localhost:8000/viewer/) in your web browser.

---

## 🔗 Online Interactive Demo

Experience the full-featured Cupcake activity viewer in action:  
👉 **[Cupcake Worked Example Demo](https://adapt2.sis.pitt.edu/cupcake/#/activities/sample-py-bank-account/worked-example.yaml)**
