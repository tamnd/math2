---
tag: WHHMJERDFG
kind: definition
name: Integral current
msc: [49Q15, 28A75]
defines: EG4AJVEFT2
uses: [360H7MD9RD, 7N0GFMW05R, Q1TGZK8RN6]
sources:
  - url: https://en.wikipedia.org/wiki/Current_(mathematics)
---

## Definition

Let $0 \le m \le n$, and let $T$ be an $m$-dimensional [[current|360H7MD9RD]] on $\R^n$, with mass $\mathbf{M}(T)$ and boundary $\partial T$.
The current $T$ is *integer multiplicity rectifiable* if there are:

1. an $\mathcal{H}^m$-measurable countably $m$-[[rectifiable set|7N0GFMW05R]] $S \subseteq \R^n$, where $\mathcal{H}^m$ is the [[Hausdorff measure|Q1TGZK8RN6]];
2. a locally $\mathcal{H}^m$-integrable function $\theta \colon S \to \set{1, 2, 3, \dots}$;
3. an $\mathcal{H}^m$-measurable map $\xi$ that assigns to $\mathcal{H}^m$-almost every $x \in S$ a unit simple $m$-vector $\xi(x)$ orienting the approximate tangent space of $S$ at $x$;

such that $T(\omega) = \int_S \ip{\omega(x)}{\xi(x)} \, \theta(x) \, d\mathcal{H}^m(x)$ for every smooth compactly supported $m$-form $\omega$.
The current $T$ is an *integral current* if it is integer multiplicity rectifiable, has compact support, satisfies $\mathbf{M}(T) < \infty$, and, when $m \ge 1$, satisfies $\mathbf{M}(\partial T) < \infty$.

## Remarks

By the boundary rectifiability theorem of Federer and Fleming, the boundary of an integral current is again an integral current.
Federer's original definition asks instead that $T$ and $\partial T$ be rectifiable currents, and the two definitions agree by that theorem.
The integral $0$-currents are the finite sums $\sum_i a_i \delta_{p_i}$ with $a_i \in \Z$.

Example: let $D$ be the closed unit disc in $\R^2 \subseteq \R^3$, oriented by $e_1 \wedge e_2$.
Then $[\![D]\!](\omega) = \int_D \omega$ is an integral $2$-current: take $S = D$, $\theta = 1$, $\xi = e_1 \wedge e_2$.
Its mass is $\pi$, and its boundary is the circle, of mass $2\pi$.

Non-example: in $\R$, let $T = \sum_{k \ge 1} [\![I_k]\!]$, where $I_k = [1/(2k + 1), 1/(2k)]$ is oriented by $e_1$.
It is integer multiplicity rectifiable with compact support in $[0, 1]$ and $\mathbf{M}(T) = \sum_k \frac{1}{2k(2k + 1)} < \infty$.
But $\partial T$ is a sum of infinitely many unit point masses, so $\mathbf{M}(\partial T) = \infty$ and $T$ is not an integral current.

## Explanations

### L1 human

An integral current is integration over an oriented rectifiable set with positive integer multiplicities, with finite area and finite boundary length.
