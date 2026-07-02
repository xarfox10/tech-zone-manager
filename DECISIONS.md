# TECH ZONE Manager - Decisions

## Decision #001

Everything sold is treated as an Item.

Status:
✅ Accepted

Reason:

The store sells:

- Products
- Repairs
- Services
- Labor
- Installation
- Second-hand items

---

## Decision #002

Barcode is optional.

Status:
✅ Accepted

Reason:

Many services and custom jobs do not have barcodes.

---

## Decision #003

Every important action commits immediately.

Status:
✅ Accepted

Reason:

Brownouts are common.

---

## Decision #004

SQLite will be the primary database.

Status:
✅ Accepted

Reason:

Fast, lightweight, offline, portable.

---

## Decision #005

Keyboard-first workflow.

Status:
✅ Accepted

Reason:

Cashiers should rarely need the mouse.

## Decision  #006

Product Philosophy

- One product = one identity.
- Stock updates should never erase previous purchase history.
- Inventory history will record supplier, invoice number, quantity, unit cost, and received date.
- Dashboard focuses on operational awareness.
- Reports focus on accounting, history, and compliance.