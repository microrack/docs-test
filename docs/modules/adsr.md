# ADSR — Envelope Generator

The ADSR envelope generator creates time-varying control voltages that shape sound dynamics over time.

## Overview

The MICRORACK ADSR provides:

- Full ADSR stages
- Gate and trigger inputs
- Adjustable stage times
- LED indicator

## Specifications

| Parameter | Value |
|-----------|-------|
| Attack time | 1ms - 10s |
| Decay time | 1ms - 10s |
| Sustain level | 0 - 100% |
| Release time | 1ms - 10s |
| Output range | 0 - 5V |
| Current draw | 6mA |

## Inputs

- **GATE**: Gate input (>2.5V triggers envelope)
- **TRIG**: Trigger input (retriggers attack)

## Outputs

- **ENV**: Envelope output (0-5V)
- **INV**: Inverted envelope output (5V-0V)

## Controls

- **A**: Attack time
- **D**: Decay time
- **S**: Sustain level
- **R**: Release time

## Envelope Stages

### Attack

Time for the envelope to rise from 0 to maximum when gate goes high.

### Decay

Time for the envelope to fall from maximum to the sustain level.

### Sustain

Level held while the gate remains high (not a time parameter).

### Release

Time for the envelope to fall from sustain level to 0 when gate goes low.

## Patching Examples

### Classic Synth Voice

```
KEYBOARD GATE → ADSR GATE
ADSR ENV → VCA CV
ADSR ENV → VCF CV
```

### Plucky Sound

- Short Attack (fully CCW)
- Short Decay (9 o'clock)
- No Sustain (fully CCW)
- Short Release (9 o'clock)

### Pad Sound

- Medium Attack (12 o'clock)
- Medium Decay (12 o'clock)
- High Sustain (3 o'clock)
- Long Release (3 o'clock)

### Percussive

- Instant Attack
- Short Decay
- Zero Sustain
- Ignore Release (no gate hold)

## Tips

- Use INV output for ducking effects
- Combine with VCA for amplitude control
- Combine with VCF for filter sweeps
- Multiple ADSRs can control different parameters for complex sounds

---

*See also: [VCA](/docs/modules/vca), [LFO](/docs/modules/lfo)*
