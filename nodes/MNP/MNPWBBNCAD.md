---
tag: MNPWBBNCAD
kind: definition
name: Large deviations theory
msc: [60F10]
defines: Q702WCDQQ3
uses: [059TJN0NZ1, 0CQHFPGJ45, 140N2PQSTE, 0ZCK8DQYN1, 02BH3MCBQB, 0QF1MZ9FRG, 0T3RZQXDYD, 033RZ32T4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Large_deviations_theory
---

## Definition

Let $\mathcal{X}$ be a [[topological space|0CQHFPGJ45]] with its Borel $\sigma$-algebra.
Let $(\mu_n)_{n \ge 1}$ be a sequence of [[probability measures|059TJN0NZ1]] on $\mathcal{X}$, and let $I \colon \mathcal{X} \to [0, \infty]$ be a [[rate function|140N2PQSTE]].
For $A \subseteq \mathcal{X}$, write $I(A) = \inf_{x \in A} I(x)$, with $I(\emptyset) = \infty$.
The sequence $(\mu_n)$ satisfies the *large deviation principle* with rate function $I$ if both of the following hold.

1. For every [[closed set|0ZCK8DQYN1]] $F \subseteq \mathcal{X}$, $\displaystyle \limsup_{n \to \infty} \frac{1}{n} \log \mu_n(F) \le -I(F)$.
2. For every [[open set|02BH3MCBQB]] $G \subseteq \mathcal{X}$, $\displaystyle \liminf_{n \to \infty} \frac{1}{n} \log \mu_n(G) \ge -I(G)$.

## Remarks

Here $\log 0 = -\infty$.
A sequence of random elements $Z_n$ of $\mathcal{X}$ satisfies the principle when their laws do.
The factor $1/n$ is the speed; some applications use another speed $1/\varepsilon$ or $1/a_n$ with $a_n \to \infty$.
If $A$ is a Borel set whose interior $A^\circ$ and closure $\bar A$ satisfy $I(A^\circ) = I(\bar A)$, then $\frac{1}{n} \log \mu_n(A) \to -I(A)$.

Example: let $\mu_n$ be the normal law with mean $0$ and variance $1/n$ on $\R$, and let $I(x) = x^2/2$.
For an interval $[a, \infty)$ with $a > 0$, the Gaussian tail estimate gives $\frac{1}{n} \log \mu_n([a, \infty)) \to -a^2/2 = -I([a, \infty))$.
The same tail estimate gives both bounds for all closed and open sets, so $(\mu_n)$ satisfies the principle with this $I$.

Non-example: the same sequence does not satisfy the principle with $I(x) = x^2$.
The upper bound fails for the closed set $F = [1, \infty)$.
Indeed $\frac{1}{n} \log \mu_n(F) \to -1/2$, while $-I(F) = -1 < -1/2$.
