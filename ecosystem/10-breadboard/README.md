# Breadboard Architecture

The breadboard is the "canvas" of the MICRORACK system. Understanding how it works is key to building complex patches and expanding your system.

## How Breadboards Work

A standard breadboard consists of:

| Component | Description |
|-----------|-------------|
| **Terminal Strips** | The main area where modules are inserted. Organized in vertical columns of 5 connected points. |
| **Power Rails** | The horizontal rows at the top and bottom (marked with + and – or red and blue lines). |
| **Center Gap** | The divider that separates the two halves of the terminal strips. |

### Recommended Breadboard Sizes

| Size | Contact Points | Modules | Best For |
|------|----------------|---------|----------|
| **830-point** | 830 | 8-12 | Standard setups |
| **400-point** | 400 | 4-6 | Portable/compact rigs |

<!-- GAP: Confirm which breadboard model is shipped with starter kits -->

## Bridging the Gap

Many standard breadboards have a **split in the power rails** halfway across the board. This can interrupt power flow in larger systems.

**The MICRORACK Solution:** Every MICRORACK module is designed to bridge the power rails. When you insert a module:

1. It draws power from the rails on its left side
2. It passes power through to the rails on its right side
3. Power flows continuously left-to-right, even across rail gaps

> **Tip:** If you're using a breadboard with a physical gap in the power rails, simply place a MICRORACK module over the gap to "bridge" the power to the other side.

## Module Placement

### Orientation Rules

- **Vertical Alignment:** Modules must be placed vertically to align power pins with the rails
- **The Notch:** Always ensure the triangular notch is at the **bottom** of the module
- **Power Pins:** Located at the bottom corners — they connect to the breadboard power rails

### Spacing

- Modules can be placed side-by-side with no gap
- Leave gaps between modules for custom circuits or prototyping
- The terminal strip area above modules is available for patching and experimentation

### Pin Layout

Per the MICRORACK Mechanical Specification:

| Position | Rail |
|----------|------|
| Bottom-left corners | GND, V12- |
| Top-left corners | V12+, V5+ |
| Bottom-right corners | GND, V12- |
| Top-right corners | V12+, V5+ |

> **Safe Design:** If you accidentally insert a module backwards, it simply won't work — MICRORACK modules include reverse polarity protection and won't be damaged.
