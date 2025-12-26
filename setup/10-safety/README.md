# Safety & Orientation

MICRORACK is designed to be a safe and robust platform for experimentation. Following a few simple rules will ensure your modules live a long and happy life.

## The "Look for the Notch" Rule

Every MICRORACK module has a distinct **triangular cutout (notch)** at the bottom of the PCB. This is your orientation guide.

| Correct | Incorrect |
|---------|-----------|
| Notch at **bottom** | Notch at top |
| Power pins align with rails | Module won't work |
| Module functions normally | No damage, just no function |

### How to Check

1. Hold the module with the components facing you
2. Look for the triangular notch (60 mil / 1.52mm deep)
3. The notch should point toward the **bottom** of your breadboard (usually the side closest to you)
4. Insert the module so the power pins seat firmly in the power rails

> **FYI:** If you accidentally plug a module in backwards, don't panic! MICRORACK modules include **reverse polarity protection** — they simply won't work until you flip them around. No smoke, no damage.

## Electrical Safety

### Voltage Levels

MICRORACK operates on low voltage (±12V, +5V DC). It is safe to touch the modules while powered.

| Safety Aspect | Status |
|---------------|--------|
| Shock hazard | ✅ None (low voltage) |
| Module touch-safe | ✅ Yes |
| Reverse insertion | ✅ Protected |

### Avoid Short Circuits

- Don't drop metal objects (loose wires, paperclips) onto the powered breadboard
- This can short the power rails and potentially damage your power supply
- If you hear a "pop" or see smoke, disconnect power immediately

### Hot-Swapping

While MICRORACK modules are designed to tolerate hot-swapping:

| Approach | Recommendation |
|----------|----------------|
| **Best practice** | Power off before adding/removing modules |
| **Acceptable** | Careful insertion with power on |
| **Avoid** | Rapid or careless module swapping while powered |

> **Why?** Hot-swapping can cause brief voltage transients. Modules are protected, but powering off first is always safer.

## Handling Modules

### Pin Headers

- The male pin headers on the underside are robust but can bend
- If pins get bent, gently straighten them with needle-nose pliers
- Avoid forcing bent pins into the breadboard

### Static Electricity

Like all electronics, modules can be sensitive to static discharge:

- Touch a grounded metal object before handling modules (especially in dry environments)
- Store modules in anti-static bags when not in use
- Avoid handling modules on carpet or synthetic surfaces

## Quick Safety Checklist

Before powering on:

- ☐ All modules inserted with **notch at bottom**
- ☐ Power Module firmly seated in power rails
- ☐ No loose wires or metal objects on the breadboard
- ☐ Power supply connected and correct polarity

## Still Unsure?

If you're worried about a specific connection or orientation:

- **Post a photo:** [Forum Safety Section](https://forum.microrack.org/c/support) — get quick confirmation from experienced users
- **Check the specs:** [Mechanical Specification](https://specs.microrack.org/mechanical/) for detailed diagrams
