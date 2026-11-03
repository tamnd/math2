---
tag: N8E0GVVWG1
kind: concept
name: Fourier transform on a nonabelian group
msc: ["43A30", "22D10"]
specializes: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_harmonic_analysis
---

## Summary

The Fourier transform on a nonabelian [[locally compact group|AHV05ZBCYW]] sends a function on the group to a family of operators.
There is one operator for each irreducible [[unitary representation|74BPYJNZTM]].
For an abelian group the irreducible unitary representations are characters and the operators are numbers.
One then gets back the [[Fourier transform on locally compact abelian groups|VHN5VW5Q92]].
It turns convolution into composition of operators.
The [[Plancherel theorem for groups|DH3PYQJXH0]] and the [[Plancherel measure|QESEAKKABM]] describe how it preserves the $L^2$ norm.

## Explanations

### L1 human

On the real line the Fourier transform tests a function against each wave $e^{i \xi x}$ and records one number per frequency.
On a nonabelian group the role of the waves is played by the irreducible unitary representations, which are often matrices or operators rather than numbers.
So the transform records one operator per representation.
For a finite group, a function $f$ on $G$ gives the matrix $\sum_{g} f(g) \pi(g)^*$ for each irreducible representation $\pi$.
For the symmetric group $S_3$ this gives two numbers, for the two one-dimensional representations, and one $2 \times 2$ matrix.
