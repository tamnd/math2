---
tag: PA1B7DJ0C4
kind: definition
name: Round-off error
msc: [65G50]
defines: CPN6SD3BTV
uses: [5NPVX29Y0C, RTKRSC3KPH, JA3QXVF2B8]
sources:
  - url: https://en.wikipedia.org/wiki/Round-off_error
---

## Definition

Let $F$ be a set of [[floating-point numbers|RTKRSC3KPH]] and let $\mathrm{fl} \colon \R \to F$ be a [[rounding|5NPVX29Y0C]].
The *round-off error* of representing $x \in \R$ is $\mathrm{fl}(x) - x$, and for $x \ne 0$ its *relative round-off error* is $(\mathrm{fl}(x) - x)/x$.
Let an algorithm compute $y = f(x)$ in exact real arithmetic, and let it return $\hat y$ when each operation is done in floating-point arithmetic.
Then the round-off error of the computation is $\hat y - y$.

## Remarks

Example: with base $10$, precision $3$ and rounding to nearest, $\mathrm{fl}(2/3) = 0.667$, so the round-off error is $0.667 - 2/3 = 1/3000$ and the relative round-off error is $1/2000 = 0.0005$.
This is within the unit roundoff $u = \tfrac12 \cdot 10^{-2}$ of the system.
Non-example: replacing $e = \sum_{k \ge 0} 1/k!$ by $\sum_{k=0}^{5} 1/k!$ in exact arithmetic gives an error, but it is a truncation error, not a round-off error.
If $x$ lies in the range of normalized numbers and $\mathrm{fl}$ rounds to nearest, then $\abs{\mathrm{fl}(x) - x} \le u \abs{x}$, where $u = \tfrac12 \beta^{1-p}$ is the unit roundoff, see [[machine epsilon|JA3QXVF2B8]].
