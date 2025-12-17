# VCA — Voltage Controlled Amplifier

The VCA controls the volume of audio signals based on control voltage, essential for creating dynamic sounds.

## Overview

The MICRORACK VCA provides:

- Linear and exponential response options
- Unity gain at maximum CV
- Clean signal path
- Low noise design

## Specifications

| Parameter | Value |
|-----------|-------|
| Response | Linear / Exponential |
| Gain range | 0 to unity (0dB) |
| Input level | 5Vpp max |
| Output level | 5Vpp max |
| THD | < 0.1% |
| Current draw | 8mA |

## Inputs

- **IN**: Audio input signal
- **CV**: Control voltage input (0-5V)

## Outputs

- **OUT**: Amplified audio output

## Controls

- **GAIN**: Initial gain level (offset)
- **CV AMT**: CV input attenuator

## Response Curves

### Linear

- Volume change proportional to CV
- Best for controlling CV signals
- Used for AM/ring modulation effects

### Exponential

- Matches human perception of loudness
- Natural-sounding amplitude envelopes
- Best for audio signals

## Patching Examples

### Basic Amplitude Envelope

```
VCO → VCA IN
ADSR → VCA CV
VCA OUT → OUTPUT
```

### Tremolo

```
VCO → VCA IN
LFO → VCA CV
VCA OUT → OUTPUT
```

### Velocity Sensitivity (with MIDI)

```
VCO → VCA IN
MIDI VELOCITY → VCA CV
VCA OUT → VCF
```

## Tips

- Use the GAIN control to set a minimum volume
- Chain VCAs for more dynamic range control
- Linear mode is useful for CV processing and AM synthesis
- Exponential mode sounds more natural for musical applications

---

*See also: [ADSR](/docs/modules/adsr), [LFO](/docs/modules/lfo)*
