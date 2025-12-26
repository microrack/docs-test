# Use Cases

Not sure where to start? Here are common configurations for the MICRORACK system, from beginner to advanced.

---

## Beginner Configurations

### 1. The Beginner Monosynth
*A classic subtractive synthesizer voice.*

| Module | Function |
|--------|----------|
| mod-vco | Sound source (oscillator) |
| mod-vcf | Tone shaping (filter) |
| mod-vca | Volume control |
| mod-env | Envelope for dynamics |
| mod-out-35 | Audio output |

**Patch it:** VCO → VCF → VCA → Output. Use ENV to control VCA for plucky sounds.

**Learn:** Basic synthesis signal flow, subtractive synthesis concepts.

---

### 2. The Ambient Drone Rig
*Evolving, atmospheric textures.*

| Module | Function |
|--------|----------|
| mod-vco ×2 | Dual oscillators for thickness |
| mod-vcf | Filtering overtones |
| mod-delay | Space and atmosphere |
| mod-vco (LFO mode) ×2 | Slow modulation sources |

**Patch it:** Detune VCOs slightly. Use LFOs to slowly modulate filter cutoff and delay time.

**Learn:** Modulation, beating frequencies, ambient sound design.

---

## Intermediate Configurations

### 3. The Guitar FX Processor
*Turn your synth into a pedalboard.*

| Module | Function |
|--------|----------|
| mod-in-63 | Guitar input (high impedance) |
| mod-vcf | Resonant filter sweeps |
| mod-sat | Analog distortion/saturation |
| mod-delay | Tape-style echoes |
| mod-out-63 | To amp or audio interface |

**Patch it:** Guitar → mod-in-63 → mod-vcf → mod-sat → mod-delay → mod-out-63.

**Learn:** Processing external audio, gain staging, effect chains.

---

### 4. The DAW Companion
*Integrate analog warmth into your digital workflow.*

| Module | Function |
|--------|----------|
| mod-midi | MIDI-to-CV from your DAW |
| mod-vco | Analog oscillator |
| mod-vcf | Analog filter |
| mod-out-35 | Back into audio interface |

**Patch it:** MIDI from DAW → mod-midi pitch/gate → mod-vco → mod-vcf → mod-out-35 → audio interface.

**Learn:** Hybrid workflows, MIDI-CV integration, recording analog.

---

### 5. The Generative System
*A synth that plays itself.*

| Module | Function |
|--------|----------|
| mod-vco | Sound source |
| mod-vcf | Tone shaping |
| mod-seq | 4-step sequencer |
| mod-noise | Random/S&H source |
| mod-clk | Clock source |
| mod-vco (LFO mode) | Additional modulation |

**Patch it:** Clock → Sequencer. Sequencer CV → VCO pitch. Noise → S&H → Filter cutoff.

**Learn:** Generative music, randomness, self-playing patches.

---

## Advanced Configurations

### 6. The Vocal Transformer
*Process your voice through analog circuits.*

| Module | Function |
|--------|----------|
| mod-in-63 | Mic input (via preamp) |
| mod-vcf | Formant-like filtering |
| mod-delay | Vocal doubling/effects |
| mod-vco (LFO mode) | Filter modulation |
| mod-out-63 | To PA or interface |

**Requires:** External mic preamp with phantom power (for condenser mics).

**Patch it:** Mic → Preamp → mod-in-63 → mod-vcf → mod-delay → mod-out-63.

**Learn:** Live vocal processing, performance setup.

---

### 7. Hybrid Drum Setup
*Digital triggers, analog sounds.*

| Module | Function |
|--------|----------|
| mod-midi | Trigger from e-drums or DAW |
| mod-noise | Noise source for snares/hats |
| mod-vcf | Shaping noise bursts |
| mod-env | Snappy envelope for drums |
| mod-vca | Dynamics |

**Patch it:** MIDI gate → mod-env → mod-vca. mod-noise → mod-vcf → mod-vca.

**Learn:** Drum synthesis, envelope shapes, trigger-based patches.

---

### 8. Acoustic-to-Modular (Piezo)
*Turn any object into a controller.*

| Module | Function |
|--------|----------|
| mod-in-63 | Piezo pickup input |
| mod-env | Envelope follower mode |
| mod-vcf | Modulated by envelope |
| mod-vco | Sound source |

**Patch it:** Piezo → mod-in-63 → mod-env (follower) → mod-vcf CV. Tap the surface to control filter.

**Learn:** Envelope following, acoustic/electronic hybrid, found sound.

---

### 9. The Pedalboard Expansion
*MICRORACK as a custom analog effect.*

| Module | Function |
|--------|----------|
| mod-in-63 | From pedalboard send |
| mod-vcf | Modulatable filter |
| mod-sat | Saturation/distortion |
| mod-out-63 | To pedalboard return |

**Patch it:** Guitar chain send → mod-in-63 → mod-vcf → mod-sat → mod-out-63 → chain return.

**Learn:** Parallel effects, pedalboard integration, analog character.

---

## Share Your Setup!

Have you created a unique patch or custom configuration? We want to see it!

- **Post on the Forum:** [Share your use cases](https://forum.microrack.org/c/use-cases) with the community
- **Tag us on Instagram:** [@microrack.synth](https://instagram.com/microrack.synth)
- **Submit to the docs:** [Edit this page on GitHub](https://github.com/microrack/docs)
