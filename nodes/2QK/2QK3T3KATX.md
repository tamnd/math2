---
tag: 2QK3T3KATX
kind: statement
role: theorem
name: MacWilliams identity
msc: [94B05]
uses: [E85KREWV60, JA3DP8NM0A, K8ZHAQAK2B]
about: [JA3DP8NM0A]
sources:
  - url: https://en.wikipedia.org/wiki/Enumerator_polynomial
---

## Statement

Let $C$ be a [[linear code|E85KREWV60]] of length $n$ over the finite field $\F_q$, and let $C^\perp$ be its [[dual code|JA3DP8NM0A]].
For a linear code $D$ of length $n$, let its weight enumerator be the polynomial
$$W_D(x, y) = \sum_{c \in D} x^{n - \mathrm{wt}(c)} y^{\mathrm{wt}(c)},$$
where $\mathrm{wt}(c)$ is the [[Hamming weight|K8ZHAQAK2B]] of $c$.
Then
$$W_{C^\perp}(x, y) = \frac{1}{\abs{C}} \, W_C\big(x + (q - 1)y, \; x - y\big).$$

## Remarks

The proof is a discrete Fourier argument on the group $\F_q^n$.
For a nontrivial additive character $\chi$ of $\F_q$, the sum $\sum_{c \in C} \chi(u \cdot c)$ equals $\abs{C}$ if $u \in C^\perp$ and $0$ otherwise.
Summing the function $u \mapsto x^{n - \mathrm{wt}(u)} y^{\mathrm{wt}(u)}$ against this indicator and computing its Fourier transform coordinate by coordinate gives the identity.
Example: for the binary code $C = \set{000, 111}$, $W_C = x^3 + y^3$, and the identity gives
$$\tfrac{1}{2}\big((x + y)^3 + (x - y)^3\big) = x^3 + 3xy^2,$$
which is the weight enumerator of $C^\perp = \set{000, 011, 101, 110}$.
The identity holds for linear codes.
For a nonlinear code, the same transform of its distance distribution still has nonnegative coefficients, and this is the basis of the linear programming bound.

## Explanations

### L1 human

The weight enumerator counts how many codewords have each number of nonzero symbols.
The MacWilliams identity says that these counts for a linear code fix the counts for its dual code, by an explicit formula.
So one can learn the weights of a huge dual code from the weights of a small code without listing the dual.

### L2 human

The identity is a finite form of the Poisson summation formula, applied to the subgroup $C$ of $\F_q^n$ and its annihilator $C^\perp$.
It is used to compute weight distributions, for instance of Hamming codes from those of their small duals, the simplex codes.
For a self-dual code, $W_C$ is invariant under the substitution in the identity, and this invariance strongly restricts the possible weight enumerators, as in Gleason's theorem.
The nonnegativity of the transformed distance distribution gives Delsarte's linear programming bound on the size of codes.
