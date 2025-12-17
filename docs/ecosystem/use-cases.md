# Use Cases

Explore common MICRORACK configurations and applications.

## Beginner Setups

### Drone Synthesizer

Create evolving ambient textures:

- 1× VCO (sound source)
- 1× VCF (tone shaping)
- 1× VCA (volume control)
- 1× LFO (modulation)

### Simple Monosynth

Classic synthesizer voice:

- 1× VCO
- 1× VCF
- 1× VCA
- 1× ADSR (envelope)
- 1× Jack Output

## Intermediate Setups

### Two-Voice Polysynth

Expanded capabilities:

- 2× VCO
- 2× VCF
- 2× VCA
- 2× ADSR
- 1× Mixer
- 1× MIDI-CV (ESP32)

### Effects Processor

Process external audio:

- 1× Jack Input
- 1× VCF
- 1× Delay
- 1× VCA
- 1× LFO
- 1× Jack Output

## Advanced Setups

### Generative System

Self-playing patches:

- 2× VCO
- 1× VCF
- 2× VCA
- 1× Step Sequencer
- 1× Sample & Hold
- 2× LFO
- 1× Noise

### Live Performance Rig

Stage-ready setup:

- 2× VCO
- 2× VCF
- 2× VCA
- 1× MIDI-CV
- 1× Mixer
- 1× Effects (Delay/Reverb)
- 1× Jack In/Out

## Integration Examples

### With Guitar

- Jack Input → VCF → Delay → Jack Output
- Use expression pedal for CV control

### With DAW

- MIDI from DAW → ESP32 → MICRORACK → Jack Output → Audio Interface
- Sync with DAW clock

### With Eurorack

- Rack Chassis adapter
- Level matching modules
- Shared power rail option

---

*See also: [Compatibility](/docs/ecosystem/compatibility) for connecting to other systems.*
