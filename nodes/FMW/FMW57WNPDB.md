---
tag: FMW57WNPDB
kind: concept
name: Pontryagin dual
msc: [43A40, 22B05]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Summary

The Pontryagin dual of a locally compact abelian group $G$ is the group $\widehat{G}$ of continuous characters of $G$, with the compact-open topology.
It is again a locally compact abelian group.
The dual is the domain of the Fourier transform on $G$, and the Pontryagin duality theorem says that the dual of $\widehat{G}$ is $G$ again.

## Explanations

### L1 human

The dual group lists all the ways the group can "vibrate": each element of the dual is a wave on $G$.
For the circle, the waves are $e^{in\theta}$ with $n$ an integer, so the dual of the circle is $\Z$.
For the integers, the waves are $n \mapsto z^n$ with $\abs{z} = 1$, so the dual of $\Z$ is the circle.
For the real line, the waves are $x \mapsto e^{i\xi x}$ with $\xi$ real, so $\R$ is its own dual.
Fourier series and the Fourier transform are the cases $G = $ circle and $G = \R$ of one theory built on this dual.
