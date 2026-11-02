---
tag: VVT27RB46B
kind: statement
role: theorem
name: q-binomial theorem
msc: [33D15, 05A30]
uses: [Y1X8ZZQ7VM, EB4N9RQR51]
about: [EB4N9RQR51, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_binomial_coefficient
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
---

## Statement

Let $a, q, z \in \C$ with $\abs{q} < 1$ and $\abs{z} < 1$.
Then
$$\sum_{n=0}^{\infty} \frac{(a; q)_n}{(q; q)_n} z^n = \frac{(az; q)_\infty}{(z; q)_\infty},$$
where $(\cdot\,; q)_n$ and $(\cdot\,; q)_\infty$ are [[q-Pochhammer symbols|Y1X8ZZQ7VM]].
In the notation of [[basic hypergeometric series|EB4N9RQR51]], ${}_1\phi_0(a; -; q, z) = \frac{(az; q)_\infty}{(z; q)_\infty}$.

## Remarks

Proof idea: let $f(z) = \sum_n c_n z^n$ be the left side, with $c_n = \frac{(a; q)_n}{(q; q)_n}$.
Comparing the coefficients of $z^n$ on both sides, with $c_n (1 - q^n) = c_{n-1} (1 - a q^{n-1})$, gives $(1 - z) f(z) = (1 - az) f(qz)$.
Iterating this functional equation gives $f(z) = \frac{(az; q)_N}{(z; q)_N} f(q^N z)$, and $f(q^N z) \to f(0) = 1$ as $N \to \infty$.
Special cases: $a = 0$ gives $\sum_n \frac{z^n}{(q; q)_n} = \frac{1}{(z; q)_\infty}$, and replacing $a$ by $a/b$ and $z$ by $bz$ and letting $b \to 0$ gives $\sum_n \frac{(-1)^n q^{\binom{n}{2}} a^n z^n}{(q; q)_n} = (az; q)_\infty$.
With $a = q^{-N}$ and $z$ replaced by $-q^N z$, one obtains the finite form $\prod_{k=0}^{N-1} (1 + q^k z) = \sum_{k=0}^{N} q^{\binom{k}{2}} \binom{N}{k}_q z^k$ with the [[Gaussian binomial coefficients|YS09Z1YNEK]].
The hypothesis $\abs{z} < 1$ is needed for $a \notin \set{1, q^{-1}, q^{-2}, \dots}$, since the series then has radius of convergence $1$.

## Explanations

### L1 human

The binomial series says $\sum_n \binom{-a}{n} (-z)^n = (1 - z)^{-a}$.
The $q$-binomial theorem is its $q$-analogue: the power $(1 - z)^{-a}$ becomes a ratio of two infinite products.
Letting $q \to 1$ with $a$ replaced by $q^{a}$ recovers the [[binomial theorem|0EHWPWGHB2]] for real exponents.

### L2 human

This is the simplest summation formula for basic hypergeometric series, and many others follow from it.
Together with the case $a = 0$ it gives Euler's two expansions of $1/(z; q)_\infty$ and $(z; q)_\infty$, which are generating functions for partitions into parts of a given kind.
Its bilateral extension is [[Ramanujan's 1psi1 summation|RK6DCJVJCR]].
