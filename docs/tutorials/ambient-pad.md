---
title: Ambient Pad Tutorial
description: Create a lush, evolving pad sound with MICRORACK
---

# Ambient Pad Tutorial

Create a beautiful, evolving pad sound perfect for ambient and atmospheric music.

## Required Modules

- 2× VCO (Voltage Controlled Oscillator)
- 1× VCF (Voltage Controlled Filter)
- 1× VCA (Voltage Controlled Amplifier)
- 2× ADSR (Envelope Generator)
- 1× LFO (Low Frequency Oscillator)

## Step 1: Dual Oscillator Setup

Create a thick sound with two detuned oscillators:

```
VCO1 ─┐
      ├─→ VCF → VCA → Output
VCO2 ─┘
```

1. Patch both VCO outputs to VCF input (use mixer if needed)
2. Set both to sawtooth waves
3. Tune VCO2 slightly sharp (+5 to +10 cents)

## Step 2: Oscillator Settings

### VCO1
- **Waveform**: Sawtooth
- **Octave**: 0 (middle range)
- **Tuning**: Specification (A = 440Hz)

### VCO2
- **Waveform**: Sawtooth
- **Octave**: 0
- **Tuning**: Slightly detuned (+5 to +10 cents)

## Step 3: Filter Configuration

- **Cutoff**: 10-11 o'clock (darker than full open)
- **Resonance**: Low (1-2 o'clock)
- **Filter Type**: Low-pass

## Step 4: Filter Envelope (ADSR1)

Create slow, evolving filter movement:

- Patch ADSR1 to VCF cutoff CV
- **Attack**: 1-2 seconds
- **Decay**: 1-2 seconds
- **Sustain**: 50-70%
- **Release**: 2-3 seconds

## Step 5: Amplitude Envelope (ADSR2)

Shape the overall dynamics:

- Patch ADSR2 to VCA CV input
- **Attack**: 500ms-1s (slow fade in)
- **Decay**: 1 second
- **Sustain**: 70-80%
- **Release**: 2-3 seconds (long tail)

## Step 6: Add Movement with LFO

Create evolving modulation:

- Patch LFO to VCF cutoff (use attenuator or moderate amount)
- **Waveform**: Triangle or sine
- **Rate**: Very slow (0.1-0.3 Hz, ~3-10 second cycles)
- **Amount**: Subtle (adjust to taste)

## Step 7: Fine Tuning

1. Play a chord and hold
2. Listen for pleasant beating between oscillators
3. Adjust detuning if needed
4. Fine-tune filter cutoff for desired darkness
5. Adjust LFO amount for subtle movement

## Variations

- **Brighter pad**: Increase filter cutoff, add resonance
- **More movement**: Increase LFO rate or amount
- **Thicker sound**: Add third oscillator, octave up or down
- **Stereo width**: Pan oscillators left/right

## Enhancement Ideas

If you have additional modules:

- **Reverb**: Add for space and depth
- **Chorus**: Enhance stereo width and richness
- **Second LFO**: Modulate oscillator pitch slightly
- **Delay**: Create rhythmic echoes

## Troubleshooting

- **Too busy**: Reduce LFO amount or slow it down
- **Too thin**: Increase detuning or add oscillators
- **Harsh**: Lower filter cutoff or reduce resonance
- **Not evolving enough**: Increase LFO amount or vary envelope times

## Tips for Live Performance

- Record variations with different chord progressions
- Experiment with different oscillator intervals (octaves, fifths)
- Try different waveform combinations
- Layer multiple pad patches for richness

Congratulations! You've created a complex, evolving sound. Experiment with the parameters to make it your own.
