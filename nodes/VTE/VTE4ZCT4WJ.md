---
tag: VTE4ZCT4WJ
kind: concept
name: Chemical master equation
msc: [60J28, "92E20", 80A30]
specializes: [VHQA7XPMQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Master_equation
---

## Summary

The chemical master equation is the [[master equation|VHQA7XPMQ4]] of a well-mixed chemical system in which molecules are counted one by one.
Its unknowns are the probabilities $P(x, t)$ that the vector of molecule numbers equals $x$ at time $t$.
It is the forward equation of a [[continuous-time Markov chain|TWQFE0FZZS]] on the lattice of molecule counts.
The jump rates of this chain are the propensities of the reactions.
It is the stochastic counterpart of the deterministic [[rate equations|TTH05RV6SW]], and it matters when some species are present in small numbers, as in living cells.

## Explanations

### L1 human

When only a few molecules of a species are present, their number jumps up and down at random times instead of changing smoothly.
The chemical master equation tracks the whole probability distribution of these numbers over time.
For the decay $A \to \emptyset$ starting from $N$ molecules, each molecule disappears independently after an exponential waiting time.
Then the number left at time $t$ is binomial with $N$ trials and success probability $e^{-ct}$, where $c$ is the decay rate per molecule.
Its mean $N e^{-ct}$ matches the deterministic first-order rate equation.
