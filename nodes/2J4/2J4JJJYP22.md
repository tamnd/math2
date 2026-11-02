---
tag: 2J4JJJYP22
kind: concept
name: Homology of a chain complex
msc: [18G35]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_(mathematics)
---

## Summary

The homology of a [[chain complex|WQ82C0M3QB]] $(C_\bullet, d)$ is the sequence of objects $H_n(C) = \ker d_n / \im d_{n+1}$.
It measures the failure of the complex to be [[exact|JB7ZBFBA9C]]: $H_n(C) = 0$ exactly when the complex is exact at $C_n$.
Each [[chain map|HTK9WQZJ1G]] induces maps on homology, so homology is a functor.
The homology of the singular chain complex of a space is its [[singular homology|M0Q5CFJ7ZH]].
The same construction gives [[simplicial homology|C6J40QF82R]], group homology and derived functors.

## Explanations

### L1 human

In a chain complex, every element in the image of $d_{n+1}$ is killed by $d_n$.
The elements killed by $d_n$ are called cycles, and those in the image of $d_{n+1}$ are called boundaries.
Homology is "cycles modulo boundaries": it collects the cycles that are not explained by a boundary.
In topology, a loop around a hole is a cycle that is not the boundary of any surface, and it gives a nonzero homology class.
For the complex $0 \to \Z \xrightarrow{2} \Z \to 0$ in degrees $1$ and $0$, the homology is $0$ in degree $1$ and $\Z/2\Z$ in degree $0$.
