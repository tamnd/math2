---
tag: NYTQ2BY74G
kind: statement
role: theorem
name: Lee–Yang theorem
msc: [82B20, 82B26, 30C15]
uses: [R0KGM32QN6]
about: [R0KGM32QN6, BH3ZRF72H1]
sources:
  - url: https://en.wikipedia.org/wiki/Lee%E2%80%93Yang_theorem
same_as:
  wikidata: Q6516611
  wikipedia: Lee–Yang theorem
---

## Statement

Let $\Lambda$ be a finite set with $\abs{\Lambda} = N$, and let $J_{ij} = J_{ji} \ge 0$ for $i \ne j$ in $\Lambda$ (ferromagnetic couplings).
For $h \in \C$, let
$$Z(h) = \sum_{\sigma \in \set{-1, +1}^\Lambda} \exp\Big( \sum_{\set{i, j} \subseteq \Lambda} J_{ij} \sigma_i \sigma_j + h \sum_{i \in \Lambda} \sigma_i \Big)$$
be the partition function of the [[Ising model|R0KGM32QN6]] on $\Lambda$ in a uniform external field $h$.
Then $Z(h) = e^{N h} P(e^{-2h})$ for a polynomial $P$ of degree $N$, and every zero $z$ of $P$ satisfies $\abs{z} = 1$.
Equivalently, every zero of $Z$ in the complex $h$-plane lies on the imaginary axis.

## Remarks

The factorization holds because $\sum_i \sigma_i = N - 2m$, where $m$ is the number of minus spins, so each term is $e^{Nh}$ times a power $z^m$ of $z = e^{-2h}$.
One proves the stronger multivariable statement: with a separate variable $z_i$ for each site, the polynomial has no zeros when all $\abs{z_i} < 1$.
This is shown by building the system one site or bond at a time, using the Asano contraction, which preserves the absence of zeros in the product of unit discs.
The symmetry $\sigma \mapsto -\sigma$ gives $z^N P(1/z) = P(z)$, which rules out zeros with $\abs{z} > 1$ too.
The hypothesis $J_{ij} \ge 0$ is needed: for antiferromagnetic couplings the zeros can leave the unit circle.

Example: for one site, $Z(h) = e^h + e^{-h} = e^h (1 + e^{-2h})$, and the only zero $z = -1$ lies on the unit circle.

## Explanations

### L1 human

The partition function encodes all the thermodynamics of a finite magnet, and its complex zeros signal where the free energy can stop being smooth.
Lee and Yang proved in 1952 that for ferromagnetic Ising models these zeros all lie on a circle in the variable $e^{-2h}$.
In the infinite-volume limit, the free energy is then analytic in $h$ away from $h = 0$.
So a ferromagnet can only have a phase transition at zero magnetic field.

### L2 human

The theorem is the start of the theory of [[Lee–Yang zeros|BH3ZRF72H1]], where phase transitions appear as zeros pinching the real axis in the limit.
It extends to many other spin models, including some continuous spins, and was greatly generalized by the theory of stable polynomials.
It also gives correlation inequalities and the analyticity of the magnetization in $h$ for $\operatorname{Re} h \ne 0$.
The density of zeros on the circle determines the free energy, much as charges determine an electrostatic potential.
