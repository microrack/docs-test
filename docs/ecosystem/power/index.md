# Power

MICRORACK modules require proper power distribution for reliable operation.

## Power Requirements

### Voltage

- **Primary**: +9V DC
- **Optional**: -9V DC (for modules requiring bipolar operation)
- **Ground**: Common ground reference

### Current

| Setup Size | Typical Current | Recommended PSU |
|------------|-----------------|-----------------|
| Small (5-10 modules) | 100-200mA | 500mA |
| Medium (10-20 modules) | 200-400mA | 1A |
| Large (20+ modules) | 400mA+ | 2A |

## Power Supply Options

### USB Power

For small setups:

- USB power bank (5V boosted to 9V)
- Computer USB port with voltage converter
- Portable and convenient

### Wall Adapter

For permanent setups:

- 9V DC center-positive adapter
- 1A minimum recommended
- Regulated output preferred

### Breadboard Power Module

Dedicated power distribution:

- Mounts on breadboard power rails
- Provides stable regulated power
- LED power indicator

## Power Distribution

### Using Power Rails

Specification breadboards include power rails along the sides:

1. Connect power supply to rail at one end
2. Modules draw power from rail connections
3. Ensure adequate gauge for current flow

### Best Practices

- Use decoupling capacitors (100nF) near modules
- Star ground when possible for complex setups
- Avoid long power runs for high-current modules

---

*See also: [Chaining](/docs/ecosystem/chaining) for connecting multiple breadboards.*
