---
tag: AEXJNRBASV
kind: concept
name: Semiconjugacy and factor map
msc: [37B02, 37C15]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_conjugacy
---

## Summary

A semiconjugacy from one dynamical system to another is a continuous surjection that intertwines the two maps.
The target system is then called a factor of the source, and the source an extension of the target.
The map itself is a factor map.
A factor is a simplified picture of the system that may forget some information.
Still, every orbit of the factor is the image of an orbit of the extension.
A semiconjugacy that is a homeomorphism is a [[topological conjugacy|HNXXAPQKG3]]; the same idea with measure-preserving maps gives factors in ergodic theory.

## Explanations

### L1 human

A factor map is like a blurry camera filming a system: it may merge different states, but it is faithful to the motion.
Watching the blurry film step by step is the same as filming each step of the real system.
For example, write a number in $[0, 1)$ in binary and shift the digits one place to the left.
Reading the digits as a number turns this shift into the doubling map $x \mapsto 2x \bmod 1$, so the doubling map is a factor of the shift.
