---
tag: CB1S5ZZFCK
kind: concept
name: Mori–Zwanzig formalism
msc: [82C03, 82C05, 82C31]
sources:
  - url: https://en.wikipedia.org/wiki/Mori–Zwanzig_formalism
same_as:
  wikidata: Q63966659
  wikipedia: Mori–Zwanzig formalism
---

## Summary

The Mori–Zwanzig formalism is an exact way to rewrite the dynamics of a large system as an equation for a few chosen variables.
One projects the dynamics onto the chosen variables; the rest of the system then appears as a memory term and a noise term.
The resulting equation has the form of a generalized Langevin equation.
It is the starting point for deriving Brownian motion, hydrodynamics and other coarse-grained descriptions from microscopic laws.

## Explanations

### L1 human

Suppose one only cares about the position of a heavy particle among billions of light molecules.
The molecules cannot be ignored, but their effect can be summarised.
The formalism splits that effect into two parts: a friction that depends on the particle's past, and a random-looking force.
For example, a heavy ball in a gas feels a drag and erratic kicks, and the formalism shows that both come from the same molecular collisions.
Nothing is approximated at this stage; approximations come later, for example by assuming the memory is short.
