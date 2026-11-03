---
tag: N1NX5VFS56
kind: concept
name: Luenberger observer
msc: [93B53, 93C05]
specializes: [TQ7E9S194T]
sources:
  - url: https://en.wikipedia.org/wiki/State_observer
---

## Summary

The Luenberger observer is the standard [[state observer|TQ7E9S194T]] for a linear system.
It is a copy of the system model driven by the known input.
The copy is corrected by a gain $L$ times the difference between the measured output and the predicted output.
The estimation error then obeys $e' = (A - LC)e$, and the gain is chosen to make this error decay.
Combined with [[full state feedback|AWDQ3ES2S3]] of the estimate, it gives an output feedback controller.
The closed-loop eigenvalues are then those of the state feedback and those of the observer.

## Explanations

### L1 human

The observer runs a simulation of the system next to the real one.
Whenever the simulated measurement differs from the real measurement, the simulation is nudged in a direction that reduces the difference.
The gain $L$ says how hard to nudge each internal variable.
For a cart with measured position, this lets the simulation learn the correct speed within a few time constants.
