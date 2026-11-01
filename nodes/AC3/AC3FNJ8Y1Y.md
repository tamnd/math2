---
tag: AC3FNJ8Y1Y
kind: concept
name: Landau's constants
msc: [30C25, 30D20]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_analysis)
---

## Summary

Landau's constants are three numbers that measure how large a disc the image of a normalised holomorphic function on the unit disc must contain.
They are the Bloch constant $B$, the Landau constant $L$ and the univalent Landau constant $A$, and they satisfy $B \le L \le A$.
They are positive by [[Bloch's theorem|KW31KDX7TB]], but their exact values are open problems.

## Explanations

### L1 human

Take a holomorphic function $f$ on the unit disc with $f(0) = 0$ and $f'(0) = 1$.
Near $0$ it looks like the identity, so its image should contain some disc.
Landau's constant $L$ is the largest radius that works for every such $f$, the disc being anywhere in the image.
The Bloch constant $B$ asks in addition that the disc be covered exactly once, and $A$ restricts to injective $f$.
For the identity $f(z) = z$, the image is the unit disc itself, which contains discs of every radius below $1$.
