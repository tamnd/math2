---
tag: Y1E9SJC3Y0
kind: statement
role: theorem
name: Carleson–Sjölin theorem
msc: [42B15, 42B08, 42B20]
uses: [AFS2DCWCD3, RAGR38Q40B, SASP14MA1Z]
about: [AFS2DCWCD3]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean
    locator: Bochner–Riesz conjecture
---

## Statement

Let $\delta > 0$ and $1 \le p \le \infty$.
Let $S^\delta$ be the [[Bochner–Riesz operator|AFS2DCWCD3]] of order $\delta$ on $\R^2$, the operator with multiplier $(1 - \abs{\xi}^2)_+^\delta$.
Then $S^\delta$ is bounded on $L^p(\R^2)$ if and only if
$$\Big| \frac{1}{p} - \frac{1}{2} \Big| < \frac{1 + 2\delta}{4}.$$
In particular, $S^\delta$ is bounded on $L^p(\R^2)$ for every $\delta > 0$ and every $4/3 \le p \le 4$.

## Remarks

Lennart Carleson and Per Sjölin proved the sufficiency of the condition in 1972.
The necessity holds in every dimension $n$.
The kernel of $S^\delta$ decays like $\abs{x}^{-(n + 1)/2 - \delta}$ with oscillation, and it lies in $L^p$ only when $1/p - 1/2 < (1 + 2\delta)/(2n)$.
Boundedness of $S^\delta$ on $L^p$ forces its kernel into $L^p$.
Since $S^\delta$ is self-adjoint, boundedness on $L^p$ is equivalent to boundedness on $L^{p'}$, and this gives the other half of the condition.
The proof of sufficiency decomposes the multiplier into pieces near the circle $\abs{\xi} = 1$ and uses an $L^4$ estimate for oscillatory integrals whose phase has curved level sets.

Example: for $\delta = 1/4$ the condition reads $\abs{1/p - 1/2} < 3/8$, that is $8/7 < p < 8$.
Without $\delta > 0$ the result fails: for $\delta = 0$, [[Fefferman's ball multiplier theorem|4A5MJY4XPV]] shows that $S^0$ is bounded only on $L^2(\R^2)$.

The same condition in dimension $n$, namely $\abs{1/p - 1/2} < (1 + 2\delta)/(2n)$, is the Bochner–Riesz conjecture; the theorem settles it for $n = 2$, while it is open for $n \ge 3$.

## Explanations

### L1 human

In the plane, rebuilding a function from its frequencies by a sharp round cut fails in every $L^p$ norm except $L^2$.
This theorem says that fading the frequencies out with any tiny amount of smoothness, any $\delta > 0$, already works for all $p$ between $4/3$ and $4$.
It also gives the exact range of $p$ for each $\delta$.

### L2 human

The theorem is the two-dimensional case of the Bochner–Riesz problem, and its proof has the same structure as the two-dimensional case of the [[restriction conjecture|9CE11G48JY]].
For $\delta > 0$ and $4/3 \le p \le 4$, it gives $L^p$ convergence of the Bochner–Riesz means $S^\delta_R f \to f$ for $f \in L^p(\R^2)$.
In higher dimensions, the [[Stein–Tomas restriction theorem|ZZVWHNFY6F]] gives a partial range, and the full range is open.
