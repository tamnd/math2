---
tag: H1WNVN5V7F
kind: concept
name: Character of an abelian group
msc: [43A40]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Summary

A character of an abelian group is a group homomorphism from the group to the circle group of complex numbers of absolute value $1$.
The characters of a group form a group under pointwise multiplication, the character group.
Characters are the "pure waves" of Fourier analysis on groups: every reasonable function on the group is built from them.

## Explanations

### L1 human

A character labels each element of the group by a point on the unit circle, so that adding elements multiplies the labels.
On the cyclic group $\Z/n\Z$, the map $k \mapsto e^{2\pi i k/n}$ is a character: going once around the group goes once around the circle.
More generally $k \mapsto e^{2\pi i jk/n}$ is a character for each $j$, and these are all of them.
On the real line, the maps $x \mapsto e^{i\xi x}$ for real $\xi$ are the continuous characters, and they are the waves used in the Fourier transform.
