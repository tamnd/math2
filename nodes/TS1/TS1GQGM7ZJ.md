---
tag: TS1GQGM7ZJ
kind: definition
name: Gauss sum
msc: [11T24, 11L05]
defines: EQ6A3ZN48K
uses: [0ZXZ82FTX2, 0JYTG5K9Y4, 0YV2CKP2AV, 0JTC045NNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss_sum
---

## Definition

Let $F$ be a [[finite field|0ZXZ82FTX2]] with $q$ elements.
A *multiplicative character* of $F$ is a [[group homomorphism|0JYTG5K9Y4]] $\chi \colon F^\times \to \C^\times$; it is extended to $F$ by $\chi(0) = 0$.
An *additive character* of $F$ is a group homomorphism $\psi \colon (F, +) \to \C^\times$.
The *Gauss sum* of $\chi$ and $\psi$ is
$$g(\chi, \psi) = \sum_{a \in F} \chi(a) \psi(a).$$

## Remarks

The most common case is $F = \Z/p\Z$ for a prime $p$ and $\psi(a) = \zeta^a$ with $\zeta = e^{2\pi i/p}$; one then writes $g(\chi) = \sum_{a=1}^{p-1} \chi(a) \zeta^a$.
If $\chi$ and $\psi$ are both nontrivial, then $\abs{g(\chi, \psi)} = \sqrt{q}$.

Example: let $p = 3$ and let $\chi$ be the [[Legendre symbol|0JTC045NNZ]] modulo $3$, so $\chi(1) = 1$ and $\chi(2) = -1$.
Then $g(\chi) = \zeta - \zeta^2 = i\sqrt{3}$, and $g(\chi)^2 = -3$, in line with the general rule $g(\chi)^2 = \left(\frac{-1}{p}\right) p$ for the quadratic character.

Non-example: the sum $\sum_{a \in \Z/p\Z} \chi(a) e^{2\pi i a^2/p}$ is not a Gauss sum in this sense, because $a \mapsto e^{2\pi i a^2/p}$ is not additive, so it is not an additive character.

For a [[Dirichlet character|7XB5VJKDPG]] $\chi$ modulo $n$ one defines in the same way $g(\chi) = \sum_{a \bmod n} \chi(a) e^{2\pi i a/n}$.
