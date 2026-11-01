---
tag: TRGBJYPBXH
kind: statement
role: theorem
name: Sato–Tate conjecture
msc: [11G05, 11F80, 11K06]
uses: [427N6S6QQW, D3HEJTVY7G, 7Y26317GJ0, 0ZXZ82FTX2]
about: [427N6S6QQW]
sources:
  - url: https://en.wikipedia.org/wiki/Sato%E2%80%93Tate_conjecture
same_as:
  wikidata: Q2993331
  wikipedia: Sato–Tate conjecture
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over $\Q$ without [[complex multiplication|D3HEJTVY7G]].
For each prime $p$ of good reduction for $E$, let $\tilde{E}$ be the reduction of $E$ modulo $p$, a curve over the [[finite field|0ZXZ82FTX2]] $\F_p$.
Let $a_p = p + 1 - \#\tilde{E}(\F_p)$.
Let $\theta_p \in [0, \pi]$ be the angle with $a_p = 2\sqrt{p} \cos \theta_p$; it exists by [[Hasse's theorem|7Y26317GJ0]].
Then for all $0 \le \alpha \le \beta \le \pi$,
$$\lim_{x \to \infty} \frac{\#\set{p \le x : p \text{ good}, \ \alpha \le \theta_p \le \beta}}{\#\set{p \le x : p \text{ good}}} = \frac{2}{\pi} \int_\alpha^\beta \sin^2 \theta \, d\theta.$$

## Remarks

In words, the angles $\theta_p$ are equidistributed with respect to the measure $\frac{2}{\pi} \sin^2 \theta \, d\theta$ on $[0, \pi]$.
This is the image of the Haar measure of $\mathrm{SU}(2)$ under the map that sends a matrix with eigenvalues $e^{\pm i\theta}$ to $\theta$.
The conjecture was formulated independently by Mikio Sato and John Tate around 1960.
Tate showed that it follows from the meromorphic continuation and non-vanishing on $\mathrm{Re}(s) \ge 1$ of the symmetric power $L$-functions $L(\mathrm{Sym}^m E, s)$ for all $m \ge 1$.
Clozel, Harris, Shepherd-Barron and Taylor proved it for curves with multiplicative reduction at some prime, in work published in 2008.
Barnet-Lamb, Geraghty, Harris and Taylor removed this condition in 2011, using potential automorphy of the symmetric powers.
The hypothesis of no complex multiplication is necessary.
For a CM curve, $a_p = 0$ for the good primes that are inert in the CM field, which are half of all primes.
So $\theta_p = \pi/2$ for these primes, and the limit distribution is different.

## Explanations

### L1 human

For each prime, the number of points of an elliptic curve modulo $p$ is close to $p + 1$, with an error that is at most $2\sqrt{p}$ in size.
Rescaled to an angle between $0$ and $\pi$, this error looks random as $p$ varies.
The theorem says exactly how it is distributed: angles near $\pi/2$ are most common, and angles near $0$ and $\pi$ are rare, with density proportional to $\sin^2 \theta$.

### L2 human

The proof is a major application of automorphy lifting theorems in the [[Langlands program|J9T2M084W5]].
The statement generalises, through the notion of Sato–Tate group, to other motives and to modular forms.
For example, it is also known for non-CM holomorphic newforms of weight at least $2$.
