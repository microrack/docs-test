# Powering Up

## Breadboard

A breadboard is the base platform where you will build your MICRORACK system. It distributes power and provides mechanical support for all your modules.

> Compatible full-size 830 tie-point breadboards are included in every MICRORACK Kit and widely available online or at local electronics stores.

![Breadboard](breadboard.png)

MICRORACK modules use only the **Horizontal Power Rails** located on the top and bottom of the breadboard; these rails provide power to all your modules.

For more details on breadboards check out the [Breadboard](../../ecosystem/10-breadboard/) page.

## Power Module

The Power Module is the fundamental utility module in MICRORACK System. It converts the power from your source to stable voltages required by modules and expands power connection to other breadboards. [More details](../../ecosystem/20-power/)

## Output Module

The Output Module is the main audio output interface for your MICRORACK system. It provides a standard 3.5mm headphone jack and a volume control knob. [More details](../../ecosystem/30-output/)

## Connecting the power

![Power Up](power-up.png)

1. **Identify the Power Rails:** Most breadboards have two sets of rails on the top and bottom. These will carry the voltages to all your modules.
2. **Insert the Power Module First:** Place the Power Module anywhere on your breadboard. Ensure all pins are firmly seated in the power rails.
3. **Check Orientation:** Ensure the triangular notch is pointing towards you.
4. **Plug your power adapter** into the Power Module.
5. **Check the LEDs:** The Power Module should have indicator LEDs. If they light up, your system is ready!

> **Tip:** One Power Module can power multiple breadboards if they are chained together. See the [Power & Expansion](../../ecosystem/20-power/) section for more details.

### Hot-Swapping

While MICRORACK modules are designed to tolerate hot-swapping **the best practice is to power off** your setup before rearranging.

**It is okay** to add or remove modules while everything is powered on but requires an extra bit of caution.

## Quick Checklist

Before powering on:

- ☐ All modules inserted with **notch at bottom**
- ☐ Power Module firmly seated in power rails
- ☐ Volume turned down on Output Module
- ☐ No loose wires or metal objects on the breadboard
- ☐ Power supply has correct interface (Type-C or DC Jack), voltage rating (5V-12V) and polarity (Center-Positive)

## What If Nothing Happens?

- **No LEDs:** Check power supply connection and polarity.
- **Module doesn't work:** Check orientation — notch should be at the bottom.
- **Intermittent power:** Ensure all pins are fully inserted into the breadboard.
