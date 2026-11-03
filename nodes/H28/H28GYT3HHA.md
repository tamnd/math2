---
tag: H28GYT3HHA
kind: concept
name: FTCS scheme
msc: [65M06, "80M20", 35K05]
specializes: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/FTCS_scheme
same_as:
  wikidata: Q5427183
  wikipedia: FTCS scheme
---

## Summary

The FTCS scheme, for "forward time, centred space", is the simplest [[finite difference method|X7HYEBA5SA]] for the [[heat equation|VP2HN86VAG]].
It replaces the time derivative by a forward difference and the second space derivative by a centred difference.
So each new value is computed explicitly from three old ones.
It is first-order accurate in time and second-order accurate in space.
It is stable only under the condition $\alpha \Delta t / \Delta x^2 \le 1/2$, which forces very small time steps on fine grids.
See the [[definition|G87YVCE8Z5]].

## Explanations

### L1 human

Divide a rod into small cells and keep a temperature for each cell.
At each time step, every cell moves its temperature a little toward the average of its two neighbours.
This is exactly what heat conduction does: a cell colder than its neighbours warms up, and a hotter one cools down.
If the time step is too long, a cell overshoots past the average, the errors flip sign and grow, and the computation blows up.
The rule $\alpha \Delta t / \Delta x^2 \le 1/2$ says how short the time step must be.
