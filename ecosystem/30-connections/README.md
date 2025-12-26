# Connections & Patching

Patching is where the magic happens. MICRORACK uses a simple, color-coded system to make signal routing intuitive.

## The Pin Header Standard

Instead of bulky patch cables, MICRORACK uses standard **2.54mm male pin headers** for all inputs and outputs. This allows you to use:

| Cable Type | Description |
|------------|-------------|
| **Standard Jumper Wires** | Cheap and widely available from electronics suppliers |
| **MICRORACK Patch Cables** | High-quality, flexible cables designed for the system |
| **Breadboard Wire Kits** | Pre-cut lengths in various colors |

> **Tip:** For firmer connections (especially for frequently-used interfaces), double-row male pin headers can be used per the mechanical specification.

## Color Coding

MICRORACK follows a strict color-coding standard for pin headers:

| Color | Function | Description |
|-------|----------|-------------|
| **Blue** | **Input** | Audio or CV signals entering a module |
| **Red** | **Output** | Audio or CV signals leaving a module |
| **Black** | **Utility / GND** | Ground, clock sync, power extension, stylus voltage |

### I/O Placement Convention

Per the MICRORACK specification, inputs are typically placed on the **left side** and outputs on the **right side** of modules, at the top edge of the board.

## Patching Best Practices

### Basic Rules

- **Outputs to Inputs:** Always connect a Red pin (Output) to a Blue pin (Input)
- **Never connect two Outputs:** Connecting two Red pins together can cause electrical contention

### Splitting Signals (Mults)

To send one output to multiple inputs:

1. Use "stackable" jumper wires that allow multiple connections
2. Use a small breadboard area to create a passive mult
3. Connect multiple wires to the same output pin (up to 2-3 destinations)

> **Note:** Per the electrical specification, each signal should have at least two output pins that duplicate the signal. This makes it easier to patch one signal to multiple destinations.

### Input Summing

Many MICRORACK modules sum multiple inputs together:

- Each input typically has 2+ pins that are summed internally
- You can connect multiple sources to create complex modulation
- This is useful for mixing CV signals (e.g., LFO + envelope → filter cutoff)

## Improve Cable Management

- Keep cables tidy to avoid accidentally pulling modules out
- Use consistent color coding for different signal types (audio vs CV vs gate)
- Write complex patches down to recall them later

The color coding makes it easy to trace signals: follow Red to Blue connections through your patch.

---

## Module Chaining

MICRORACK modules can be chained together in various ways to create complex signal paths.

### Signal Patching Across Breadboards

Signals can be patched between breadboards just as easily as within a single board. For long runs, we recommend:

- Keeping the boards physically close together
- Using shielded cables for sensitive audio signals
- Maintaining the color-coding convention (Red output → Blue input)

### Chaining Techniques

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **Serial** | Output → Input → Output → Input | Effects chains, filters in series |
| **Parallel** | One output to multiple inputs | Modulation distribution, audio splitting |
| **Feedback** | Output looped back to earlier input | Self-oscillation, complex timbres |

### Clock & Gate Chaining

For sequenced and rhythmic patches:

- Use **Black (Utility)** pins for clock signals
- Chain clock from master sequencer/clock module to all slaves
- Gate signals follow the same Red → Blue convention as audio

> **Tip:** When building large patches across multiple breadboards, sketch your signal flow on paper first. This helps plan module placement and minimize cable lengths.
