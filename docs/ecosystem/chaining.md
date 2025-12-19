# Chaining

Connect multiple breadboards to expand your MICRORACK system.

## Why Chain?

As your module collection grows, you may need more space:

- Add specialized sections (oscillators, effects, sequencing)
- Create separate performance and studio setups
- Maintain organized patch layouts

## Connection Methods

### Power Rail Jumpers

Connect power rails between breadboards:

```
Breadboard A          Breadboard B
+9V ──────────────────+9V
GND ──────────────────GND
-9V ──────────────────-9V (if used)
```

Use short, thick wire (22AWG or larger) to minimize voltage drop.

### Signal Patching

Connect modules across breadboards with Specification patch cables:

- Keep cables organized
- Use color coding for signal types
- Consider cable management clips

## Multiple Breadboard Layouts

### Side by Side

Most common arrangement:

- Place breadboards adjacent
- Short signal paths
- Shared workspace

### Stacked

For compact setups:

- Use risers between levels
- Consider cable routing
- Good for performance

### Distributed

For studio installations:

- Breadboards in different locations
- Longer cable runs
- Use buffered signals for long runs

## Power Distribution

For larger systems:

| Breadboards | Power Approach |
|-------------|----------------|
| 2-3 | Daisy-chain from single PSU |
| 4-6 | Star distribution from central PSU |
| 7+ | Multiple PSUs, isolated sections |

## Tips

1. **Measure current draw** before expanding
2. **Use decoupling capacitors** on each breadboard
3. **Test power at far ends** of the chain
4. **Label cables** for easy troubleshooting

---

*See also: [Power](/docs/ecosystem/power) for detailed power requirements.*
