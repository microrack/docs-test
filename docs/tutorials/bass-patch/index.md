---
title: Bass Patch Tutorial
description: Create a powerful bass sound with MICRORACK
---

# Bass Patch Tutorial

Learn to create a punchy, powerful bass sound perfect for electronic music.

## Required Modules

- 1× VCO (Voltage Controlled Oscillator)
- 1× VCF (Voltage Controlled Filter)
- 1× VCA (Voltage Controlled Amplifier)
- 1× ADSR (Envelope Generator)

## Step 1: Basic Signal Path

Connect the modules in this order:

```
VCO → VCF → VCA → Output
```

1. Patch VCO output to VCF input
2. Patch VCF output to VCA input
3. Patch VCA output to mixer or speakers

## Step 2: VCO Settings

- **Waveform**: Sawtooth (for rich harmonics)
- **Octave**: -1 or -2 (for bass range)
- **Tuning**: Adjust to taste (typically C1 or C2)

## Step 3: VCF Configuration

- **Cutoff**: Start at 12 o'clock, adjust to taste
- **Resonance**: 2-3 o'clock (moderate boost)
- **Filter Type**: Low-pass (if selectable)

## Step 4: Envelope Setup

Create two envelope connections:

### Filter Envelope
- Patch ADSR output to VCF cutoff CV input
- **Attack**: Very short (almost instant)
- **Decay**: 200-400ms
- **Sustain**: 0 (for punchy sound)
- **Release**: Short (100-200ms)

### Amplitude Envelope
- Patch ADSR output to VCA CV input
- **Attack**: Very short
- **Decay**: 300-500ms
- **Sustain**: 40-60% (if held notes desired)
- **Release**: Short to medium

## Step 5: Fine Tuning

1. Play a note and listen
2. Adjust filter cutoff for desired brightness
3. Tweak resonance for character (don't overdo it)
4. Adjust envelope decay times for punch vs. sustain balance

## Variations

- **Harder bass**: Increase resonance, shorter decay
- **Softer bass**: Lower resonance, longer attack
- **Wobble bass**: Add LFO to filter cutoff
- **Sub bass**: Use sine wave, less filtering

## Troubleshooting

- **Too thin**: Lower the octave or increase filter cutoff
- **Too muddy**: Reduce low frequencies or increase cutoff decay
- **Not punchy enough**: Shorten envelope times
- **Clicking sounds**: Increase attack time slightly

## Next Steps

Try the [Ambient Pad Tutorial](./ambient-pad) to learn multi-oscillator patches!
