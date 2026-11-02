---
tag: 1GVF19KFAK
kind: statement
role: theorem
name: Enriques–Kodaira classification
msc: [14J10, 32J15]
uses: [KFTECAATKG, ZW00Q0SAGR, W05VYY4HBR, 5NK10NGY13, Q3V566R6K2, Y30JE2DC6Y, VSC3F53DX4, SV4CK2XP8M, R7W03TXRS9, WJ5WRGG5DE, QXHMMQX1D7]
about: [KFTECAATKG, ZW00Q0SAGR]
sources:
  - url: https://en.wikipedia.org/wiki/Enriques%E2%80%93Kodaira_classification
same_as:
  wikidata: Q2584390
  wikipedia: Enriques–Kodaira classification
---

## Statement

Let $S$ be a smooth projective [[algebraic surface|KFTECAATKG]] over $\C$ that is minimal, meaning that it contains no smooth rational curve $E$ with $E^2 = -1$.
Let $\kappa(S)$ be its [[Kodaira dimension|ZW00Q0SAGR]] and $K_S$ its [[canonical divisor|W05VYY4HBR]].
Then exactly one of the following holds.

1. $\kappa(S) = -\infty$, and $S$ is the projective plane $\mathbb{P}^2$ or a [[ruled surface|5NK10NGY13]] $\mathbb{P}(\mathcal{E}) \to C$ over a smooth projective curve $C$.
2. $\kappa(S) = 0$, and $S$ is a [[K3 surface|Q3V566R6K2]], an [[Enriques surface|Y30JE2DC6Y]], an [[abelian surface|R7W03TXRS9]] or a bielliptic surface. In each case $12 K_S \sim 0$.
3. $\kappa(S) = 1$, and $S$ is an [[elliptic surface|VSC3F53DX4]].
4. $\kappa(S) = 2$, and $S$ is a [[surface of general type|SV4CK2XP8M]].

Moreover, every smooth projective surface is obtained from a minimal one by finitely many blow-ups of points, and if $\kappa(S) \ge 0$ this minimal model is unique.

## Remarks

The reduction to minimal surfaces uses [[Castelnuovo's contraction theorem|WJ5WRGG5DE]]: a smooth rational curve with self-intersection $-1$ can be blown down to a smooth point, which lowers the second Betti number.
For each value of $\kappa$, the finer classification uses the invariants $q = h^1(\mathcal{O}_S)$, $p_g = h^0(K_S)$, the plurigenera $P_n = h^0(nK_S)$, and the Chern numbers $K_S^2$ and $c_2(S)$.
[[Castelnuovo's rationality criterion|QXHMMQX1D7]] is the key step for $\kappa = -\infty$.
Kodaira extended the classification to all compact complex surfaces, which adds non-algebraic classes such as surfaces of class VII and Kodaira surfaces.
Bombieri and Mumford extended it to algebraically closed fields of positive characteristic, where new classes appear in characteristics $2$ and $3$.
Example: a smooth quartic surface in $\mathbb{P}^3$ has $K_S = 0$ by adjunction and lands in case 2 as a K3 surface.
A smooth quintic surface has $K_S$ ample and lands in case 4.

## Explanations

### L1 human

Every complex algebraic surface can be simplified, by collapsing certain special curves, to a minimal surface.
The classification sorts minimal surfaces into four families according to how fast the number of sections of powers of the canonical bundle grows.
The first three families are known in detail; the last one, the surfaces of general type, is by far the largest and is not classified in detail.

### L2 human

The classification is the two-dimensional model of the minimal model program.
In dimension one, curves split by genus into $g = 0$, $g = 1$ and $g \ge 2$, which matches $\kappa = -\infty, 0, 1$; for surfaces there is one more class.
The invariants that tell the classes apart are birational invariants, so they can be computed on any smooth model.
Results like the Bogomolov–Miyaoka–Yau inequality constrain the invariants of the last class.
