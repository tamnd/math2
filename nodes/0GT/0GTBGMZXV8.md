---
tag: 0GTBGMZXV8
kind: definition
name: Triple integral
msc: [26B15]
defines: 0698M7C7AX
uses: [0NKBMFC18R, 0JPCHTXWG0]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Mathematical definition
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Triple integral
---

## Definition

Let $B = [a_1, b_1] \times [a_2, b_2] \times [a_3, b_3]$ with $a_i < b_i$, and let $f \colon B \to \mathbb{R}$ be bounded.
Partition each interval $[a_i, b_i]$, and let $B_1, \dots, B_N$ be the resulting closed sub-boxes, with volumes $\Delta V_1, \dots, \Delta V_N$.
For points $p_k \in B_k$, the sum $S = \sum_{k=1}^{N} f(p_k) \, \Delta V_k$ is a Riemann sum of $f$.
The function $f$ is Riemann integrable on $B$ if there is $I \in \mathbb{R}$ with this property. For each $\varepsilon > 0$, there is $\delta > 0$ with $|S - I| < \varepsilon$ for all Riemann sums whose sub-boxes have diameter less than $\delta$.
Then $I$ is the triple integral of $f$ over $B$, written $\iiint_B f(x, y, z) \, dV$.

## Remarks

This is the case $n = 3$ of the multiple integral over a box. The case $n = 2$ is the [[double integral|0NKBMFC18R]].
For a bounded solid $E \subseteq B$, the integral over $E$ is the integral over $B$ of $f$ times the indicator function of $E$. The volume of $E$ is $\iiint_E 1 \, dV$, when this integral exists.
By [[Fubini's theorem|0R0T1VWH5X]], for continuous $f$ the triple integral equals an iterated integral. For example, $\iiint_{[0,1]^3} x y z \, dV = (1/2)^3 = 1/8$.

## Explanations

### L1 human

A triple integral adds up the values of $f$ over a solid, each weighted by the volume of a small piece.
If $f$ is a density, the triple integral is the total mass of the solid.
