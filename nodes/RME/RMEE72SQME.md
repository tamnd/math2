---
tag: RMEE72SQME
kind: concept
name: Wave function collapse
msc: [81P15, 81P05]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_function_collapse
same_as:
  wikidata: Q842189
  wikipedia: Wave function collapse
---

## Summary

Wave function collapse is the rule of standard quantum mechanics for the state of a system right after a measurement.
If a measurement of an [[observable|DF5RN297GE]] gives a value $a$, the [[state|4NQN47A92F]] is replaced by its normalized projection onto the eigenspace of $a$.
It is a non-unitary update, unlike the time evolution given by the [[Schrödinger equation|EPZR6H2WJN]].
Its status as a physical process is a central question of the foundations of quantum theory.

## Explanations

### L1 human

Before a measurement, a quantum state can be a superposition of several possible outcomes.
The measurement gives one outcome, and the rule says the state then becomes the part of the old state that fits this outcome, rescaled to length one.
Picture a vector in the plane being dropped onto one axis and then stretched back to length one.
For a spin in the state $(\lvert\uparrow\rangle + \lvert\downarrow\rangle)/\sqrt{2}$, a spin measurement gives "up" with probability $1/2$, and after that the state is $\lvert\uparrow\rangle$.
A second measurement of the same spin then gives "up" again with certainty.
