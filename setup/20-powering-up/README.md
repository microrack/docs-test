# Powering Up

The Power Module is the heart of your MICRORACK system. It converts the input from your power adapter into the stable voltages required by your modules.

## Connecting the Power Module

1. **Identify the Power Rails:** Most breadboards have two sets of rails on the top and bottom. These will carry the +12V, +5V, GND, and -12V voltages.
2. **Insert the Power Module:** Place the Power Module at the far left or far right of your breadboard. Ensure the pins are firmly seated in the power rails.
3. **Check Orientation:** Ensure the Power Module's triangular notch is pointing towards the bottom of the breadboard.

## Power Supply Requirements

<!-- GAP: Confirm actual power supply specifications shipped with kits -->

| Parameter | Requirement |
|-----------|-------------|
| Voltage | DC (confirm voltage with your specific Power Module) |
| Polarity | Center-Positive (standard for most gear) |
| Current | Minimum 500mA recommended for small-medium setups |

> **Voltage Rails:** The system provides +12V, +5V, GND, and -12V to the breadboard rails. Modules use internal regulators as needed.

## The "Smoke Test"

1. Plug your power adapter into the Power Module.
2. Turn on the power switch (if applicable).
3. **Check the LEDs:** The Power Module should have indicator LEDs. If they light up, your system is ready!
4. If the LEDs do not light up, turn off the power immediately and check:
   - Power adapter is plugged in and working
   - Correct polarity
   - Power Module orientation (notch at bottom)

> **Tip:** One Power Module can power multiple breadboards if they are chained together. See the [Power & Expansion](../../ecosystem/20-power/) section for more details.

## What If Nothing Happens?

- **No LEDs:** Check power supply connection and polarity.
- **Module doesn't work:** Check orientation — notch should be at the bottom.
- **Intermittent power:** Ensure all pins are fully inserted into the breadboard.
