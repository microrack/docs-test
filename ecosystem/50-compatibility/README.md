# Compatibility

MICRORACK is designed to be a "bridge" between different modular formats and external equipment.

## Signal Level Reference

| Signal Type | MICRORACK Level | Notes |
|-------------|-----------------|-------|
| Audio (bipolar) | ±5V (10 Vpp) | Eurorack compatible |
| CV (unipolar) | 0 to +5V | Gates, envelopes, LFOs |
| Pitch CV | 1V/octave | Industry standard |
| Gate High | ≥ 3.5V | Logic threshold |
| Gate Low | ≤ 0.7V | Logic threshold |

---

## Modular Format Compatibility

### Eurorack

MICRORACK is signal-compatible with Eurorack systems:

| Aspect | MICRORACK | Eurorack | Compatibility |
|--------|-----------|----------|---------------|
| Audio signals | ±5V (10 Vpp) | ±5V typical | ✅ Direct |
| CV range | 0-5V / ±5V | ±5V or wider | ✅ Compatible |
| Pitch CV | 1V/octave | 1V/octave | ✅ Direct |
| Connector | Pin headers | 3.5mm jacks | Use **mod-jacket** |
| Power | ±12V, +5V | ±12V | Separate systems |

> **Interfacing:** Use the **mod-jacket** module to convert between MICRORACK pin headers and standard 3.5mm patch cables.

### AE Modular

Developed in partnership with **Tangible Waves**, MICRORACK shares design philosophy with AE Modular:

- **Pin Pitch:** Both systems use 2.54mm (0.1") spacing
- **Signal Levels:** Directly compatible without level shifting
- **Shared Chassis:** AE Modular chassis can accommodate MICRORACK modules

<!-- GAP: Confirm AE Modular chassis availability status -->

### Other Modular Formats

| Format | Compatibility | Method |
|--------|--------------|--------|
| Moog/1V-oct | ✅ Good | Same pitch CV standard |
| Korg MS (Hz/V) | ⚠️ Partial | Requires Hz/V to V/oct converter |
| Buchla | ⚠️ Partial | Different signal levels, needs conversion |

---

## External Equipment Integration

### MIDI Keyboards & Controllers

The **mod-midi** module provides comprehensive MIDI integration:

| Feature | Specification |
|---------|---------------|
| Input | MIDI TRS Type-A |
| Outputs | Pitch CV (1V/oct), Gate (0-3.3V) |
| Display | 128×64 OLED with oscilloscope mode |
| Controls | Rotary encoder + push buttons |

**Compatible devices:**
- MIDI keyboards (any manufacturer)
- MIDI controllers and pad controllers
- Digital drum kits (via MIDI out)
- DAWs (via USB-MIDI interface)
- Hardware sequencers with MIDI output

### Electroacoustic Instruments

Connect electric guitars, basses, violins, and electronic wind instruments via **mod-in-63**:

| Feature | Specification |
|---------|---------------|
| Input | 6.3mm (1/4") jack |
| Gain Range | -∞ to +60 dB |
| Channels | Stereo (L/R splitting) |
| DC Block | Switchable (CV mode available) |
| Pull-up | +5V available |

**Compatible instruments:**
- Electric guitar (passive or active pickups)
- Electric bass
- Electronic violin/cello
- Electronic wind instruments (EWI, etc.)
- Line-level synthesizers and drum machines

> **Tip:** The high gain range (+60 dB) makes **mod-in-63** suitable for passive single-coil pickups without a separate preamp.

### Acoustic Instruments & Vocals

Process live sound through your modular system:

| Source | Connection Method |
|--------|-------------------|
| **Dynamic mics** | Direct to **mod-in-63** (use gain control) |
| **Condenser mics** | External preamp with 48V phantom → **mod-in-63** |
| **Piezo pickups** | Direct to **mod-in-63** (high-Z input) |
| **Contact mics** | Direct to **mod-in-63** |

> **Note:** MICRORACK does not provide 48V phantom power. The +5V pull-up on **mod-in-63** is suitable for some electret/piezo preamp circuits, but not condenser mics.

### FX Pedals & External Processors

Create hybrid analog/digital signal chains:

**Send/Return Loop:**
1. **mod-out-35** or **mod-out-63** → Pedal input
2. Pedal output → **mod-in-63**
3. Adjust levels as needed (synth signals are typically hotter than guitar level)

**Compatible gear:**
- Guitar/bass effects pedals
- Multi-effects processors
- Studio outboard gear
- Drum machines (audio and MIDI sync)

> **Level Matching:** Synthesizer signals (±5V) are louder than guitar pedal expectations (~1V). Use the gain control on **mod-in-63** to prevent clipping.

### Other Synthesizers

Connect to semi-modular, desktop, and vintage synthesizers:

| Connection Type | MICRORACK Module | Notes |
|-----------------|------------------|-------|
| CV/Gate (3.5mm) | **mod-jacket** | 0-5V compatible |
| Audio (3.5mm) | **mod-jacket** | ±5V signals |
| Audio (6.3mm) | **mod-in-63** / **mod-out-63** | Line level |
| MIDI | **mod-midi** | DIN or TRS Type-A |

**Example integrations:**
- Use MICRORACK as an effects processor for your Minilogue
- Sequence MICRORACK VCOs from your Keystep
- Mix MICRORACK outputs with your Volca series
- Use Eurorack oscillators as sound sources for MICRORACK filters

---

## Tested Devices

<!-- GAP: Community-contributed compatibility list -->

We're building a list of tested compatible devices. Have you connected something interesting to MICRORACK?

**[Add your device to the list →](https://github.com/microrack/docs/edit/main/ecosystem/compatibility.md)**

| Category | Device | Status | Notes |
|----------|--------|--------|-------|
| MIDI Controller | — | — | Contributions welcome |
| Guitar | — | — | Contributions welcome |
| Microphone | — | — | Contributions welcome |
| Synthesizer | — | — | Contributions welcome |
| Drum Machine | — | — | Contributions welcome |

---

*Have questions about connecting specific gear? Ask on the [Forum](https://forum.microrack.org).*
