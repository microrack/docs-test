# Power Distribution

MICRORACK uses a standardized power distribution system to ensure all modules receive the correct voltages.

## The Power Rails

The system relies on four power rails distributed through the breadboard:

| Rail | Voltage | Color | Purpose |
|------|---------|-------|---------|
| **V12+** | +12V | Red | Positive supply for analog circuits |
| **V5+** | +5V | — | Auxiliary supply for digital logic & LEDs |
| **GND** | 0V | Black | Common ground reference |
| **V12-** | -12V | Blue | Negative supply for bipolar signals |

> **Note:** The V5+ rail is intended for powering digital logic and LED indicators only. Do not use it as a voltage reference — modules should derive local regulated supplies internally.

## Current Limits

While breadboard rails are convenient, they have physical limits:

- **Maximum per rail:** 100 mA per individual power rail (per MICRORACK Specification)
- **Voltage tolerance:** ±10% on all power rails
- **Ripple:** Up to 200 mV peak-to-peak is acceptable

### Typical Module Consumption

| Module | Power Consumption |
|--------|-------------------|
| mod-vco | 732 mW |
| mod-midi | 660 mW |
| mod-in-63 | 348 mW |
| mod-jacket | 24 mW |

<!-- GAP: Power consumption data needed for remaining modules -->

## Power Flow

Power flows from the **Power Module** through the breadboard rails. Each MICRORACK module acts as a "repeater," passing power from left to right through its power pins. This ensures continuous power distribution even across breadboard rail gaps.

## Hot-Swap Considerations

MICRORACK modules are designed to tolerate hot-swapping, but transient voltage spikes may occur when inserting modules with power on. For best practice, power off before adding or removing modules.

## Troubleshooting Power

- **Dim LEDs:** Too many modules on one rail, or underpowered supply.
- **Noise/Whining:** Check that your Power Module is firmly seated and you're using a quality regulated DC adapter.
- **No Power:** Verify power supply polarity and that the adapter meets voltage/current requirements.

<!-- GAP: Confirm actual power supply specs (voltage, current, polarity) shipped with kits -->

---

## Expanding Your System

One of the greatest strengths of MICRORACK is its scalability. You can start with a single breadboard and grow into a massive wall of sound.

### Connecting Multiple Breadboards

To expand your system, you can physically connect multiple breadboards using their built-in interlocking tabs.

#### Power Rail Jumpers

To share power between breadboards, connect each power rail:

| Rail | From Board A | To Board B |
|------|--------------|------------|
| V12+ | +12V rail | +12V rail |
| V5+ | +5V rail | +5V rail |
| GND | Ground rail | Ground rail |
| V12- | -12V rail | -12V rail |

> **Wire Gauge:** Use short, thick jumper wires (22AWG or larger) to minimize voltage drop across long power runs.

### Distributed Power

For very large systems (3+ breadboards), we recommend using a dedicated **Power Module** for every two breadboards to ensure voltage stability and prevent current overload on the rails.

### Planning Your Expansion

| System Size | Breadboards | Power Modules | Notes |
|-------------|-------------|---------------|-------|
| Starter | 1 | 1 | Up to ~10 modules |
| Medium | 2 | 1 | Chain power rails |
| Large | 3-4 | 2 | One per 2 boards |
| Studio | 5+ | 3+ | Consider star grounding |

<!-- GAP: Confirm recommended max modules per Power Module based on current draw -->
