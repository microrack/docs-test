# Your First Patch

Let's make some noise! This "Hello World" patch will guide you through the basics of signal flow in MICRORACK.

---

## Step 1: The Drone (VCO → Output)

**Goal:** Hear your first sound — a continuous tone.

### What You Need
- 1× VCO (Voltage Controlled Oscillator)
- 1× Output Module (mod-out-35 or mod-out-63)
- 1× Patch cable (jumper wire)
- Headphones or speakers

### Instructions

1. **Insert the VCO:** Place your VCO module into the breadboard (notch at bottom)
2. **Insert the Output Module:** Place an Output module nearby
3. **Connect the Signal:**
   - Find the **Red pin** (Output) on the VCO
   - Find the **Blue pin** (Input) on the Output module
   - Connect them with a patch cable
4. **Listen:** Plug in your headphones and turn up the volume

**Result:** You should hear a steady tone. Try turning the **Pitch** knob on the VCO to change the frequency.

> **Tip:** The VCO has multiple outputs (saw, triangle, square). Each has a different timbre — try connecting different ones!

---

## Step 2: Subtractive Synthesis (VCO → VCF → Output)

**Goal:** Shape the tone using a filter.

### What You Need
- Previous setup, plus:
- 1× VCF (Voltage Controlled Filter)

### Instructions

1. **Insert the VCF:** Place it between the VCO and Output module
2. **Re-route the Patch:**
   - VCO Output (Red) → VCF Input (Blue)
   - VCF Output (Red) → Output Module Input (Blue)
3. **Tweak:** Turn the **Cutoff** knob on the VCF

**Result:** The sound gets brighter (cutoff up) or darker (cutoff down) as you filter out frequencies.

> **Try this:** Turn up the **Resonance** knob for a more aggressive, "singing" filter sound.

---

## Step 3: Adding Modulation (LFO → VCF)

**Goal:** Make the filter move automatically.

### What You Need
- Previous setup, plus:
- 1× LFO (Low Frequency Oscillator) — or use mod-vco in LFO mode

### Instructions

1. **Insert the LFO:** Place it anywhere on the breadboard
2. **Connect the Modulation:**
   - LFO Output (Red) → VCF CV Input (Blue)
3. **Adjust:** Set the LFO to a slow speed (0.5-2 Hz)

**Result:** The filter cutoff now moves up and down automatically, creating a "wah-wah" or sweeping effect.

> **Experiment:** Try different LFO waveforms (if available) — triangle for smooth sweeps, square for abrupt changes.

---

## Signal Flow Summary

```
┌─────┐      ┌─────┐      ┌─────┐      ┌────────┐
│ VCO │─Red──│ VCF │─Red──│ VCA │─Red──│ Output │──► 🎧
└─────┘      └──┬──┘      └──┬──┘      └────────┘
                │            │
           Blue │       Blue │
                │            │
            ┌───┴───┐    ┌───┴───┐
            │  LFO  │    │  ENV  │
            └───────┘    └───────┘
```

**Remember:** Red (Output) always connects to Blue (Input).

---

## What's Next?

### Add More Modules

| Module | What It Does |
|--------|--------------|
| **mod-env** | Add attack/decay/sustain/release shaping |
| **mod-vca** | Control volume with CV |
| **mod-delay** | Add echo and space |
| **mod-seq** | Create melodic sequences |

### Explore Use Cases

Check out the [Use Cases](../../ecosystem/60-use-cases/) section for complete patch ideas:
- Ambient drones
- Guitar effects processing
- Generative music
- MIDI integration

---

## Congratulations!

You've just built your first modular synthesizer patch. From here, the possibilities are endless.

- **Learn more:** Explore the [Modules](../../modules/) section
- **Get inspired:** Browse the [Forum](https://forum.microrack.org/c/patches)
- **Share:** Post your first patch on [Instagram](https://instagram.com/microrack.synth) with #MICRORACK
