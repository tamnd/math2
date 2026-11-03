---
tag: E1P61VYRRD
kind: concept
name: Quantum Turing machine
msc: [68Q12, 68Q09, 81P68]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Turing_machine
same_as:
  wikidata: Q765620
  wikipedia: Quantum Turing machine
---

## Summary

A quantum Turing machine is a model of quantum computation built like a [[Turing machine|758EYCN27B]], whose configurations can be in superposition.
Its steps act on these superpositions by a [[unitary operator|MM0EJ2GDE4]], and a measurement at the end gives a random output.
David Deutsch proposed it in 1985, and Bernstein and Vazirani developed its complexity theory.
It defines the class [[BQP|VP21SFE7ZA]], and it is equivalent in power to uniform families of quantum circuits.

## Explanations

### L1 human

An ordinary Turing machine is in exactly one configuration at each moment.
A quantum Turing machine holds a weighted combination of configurations, with complex weights called amplitudes.
At each step every configuration spreads into several new ones, and weights of equal configurations add up, so they can reinforce or cancel.
When the machine stops one looks at it, and each outcome appears with probability equal to the squared size of its weight.
For example, a machine that turns a $0$ into the equal combination of $0$ and $1$ outputs each bit with probability $1/2$.
