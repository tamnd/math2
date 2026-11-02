---
tag: CBZ20SS8RQ
kind: statement
role: theorem
name: Riesz decomposition theorem
msc: [31B05, 31A05]
uses: [Z1MHMGFNFW, PR8KWEA3MH, 0DEB0JMN0W, BSJ8X2XRN9, 02BH3MCBQB, X4V2S56YQQ]
about: [Z1MHMGFNFW, PR8KWEA3MH]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $u$ be [[subharmonic|Z1MHMGFNFW]] on $\Omega$ and not identically $-\infty$ on any connected component.
Let $\mu$ be the [[Riesz measure|PR8KWEA3MH]] of $u$, so $\mu = \Delta u$ in the sense of distributions.
Let
$$E(x) = \frac{1}{2\pi} \log\abs{x} \ (n = 2), \qquad E(x) = -\frac{\abs{x}^{2-n}}{(n-2)\,\omega_n} \ (n \ge 3),$$
where $\omega_n$ is the area of the unit sphere in $\R^n$, so that $\Delta E = \delta_0$.
Let $U$ be an open set whose closure is compact and contained in $\Omega$.
Then there is a [[harmonic function|0DEB0JMN0W]] $h$ on $U$ such that
$$u(x) = \int_U E(x - y)\, d\mu(y) + h(x) \qquad \text{for all } x \in U.$$

## Remarks

Proof idea: the measure $\mu$ restricted to $U$ is finite, so $p(x) = \int_U E(x - y)\, d\mu(y)$ is subharmonic on $\R^n$ and $\Delta p = \mu$ on $U$ in the sense of distributions.
Then $\Delta(u - p) = 0$ on $U$ as a distribution, and Weyl's lemma makes $u - p$ equal, almost everywhere, to a harmonic function $h$.
Both $u$ and $p + h$ are subharmonic, and two subharmonic functions that agree almost everywhere agree everywhere, since each is the limit of its ball averages.

Example: for $u(z) = \log\abs{z}$ on $\C$, $\mu = 2\pi\delta_0$, so $\int E(z - w)\, d\mu(w) = \log\abs{z}$ and $h = 0$.
Let $f$ be a polynomial with leading coefficient $c$ and zeros $a_1, \dots, a_k$ listed with multiplicity.
Then $\log\abs{f(z)} = \sum_j \log\abs{z - a_j} + \log\abs{c}$ on all of $\C$, which has the same form, with the constant $h = \log\abs{c}$ as harmonic part.

A global form holds on a domain $\Omega$ with a Green function $G$, normalised by $-\Delta G(\cdot, y) = \delta_y$.
Let $u$ be a [[superharmonic|X4V2S56YQQ]] function on $\Omega$ that has a subharmonic minorant.
Then $u$ is the sum of the Green potential of the measure $-\Delta u$ and the greatest harmonic minorant of $u$.

## Explanations

### L1 human

Every subharmonic function is, locally, the potential of some charge distribution plus a harmonic function.
The charge distribution is its Riesz measure, and the harmonic part is the "smooth background".
So subharmonic functions are exactly the negatives of potentials of positive charges, up to harmonic corrections.

### L2 human

The theorem reduces many questions about subharmonic functions to questions about measures and their potentials.
For $\log\abs{f}$ with $f$ holomorphic it is the analytic form of factoring $f$ through its zeros, as in Jensen's formula and the Hadamard factorisation of entire functions.
In the global form on Green domains, it identifies the positive superharmonic functions with zero greatest harmonic minorant, the potentials, with Green potentials of measures.
