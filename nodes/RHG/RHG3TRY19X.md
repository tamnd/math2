---
tag: RHG3TRY19X
kind: definition
name: Poincaré asymptotic series
msc: [41A60, "30E15", "34E05"]
defines: 2HVC5G0H5K
uses: [BJQTEPEZ9G, XEGB8Y44GG]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Definition

Let $D$ be a subset of $\C$ that is unbounded, for example a sector or a ray, and let $f \colon D \to \C$.
A formal series $\sum_{n \ge 0} a_n z^{-n}$ with complex coefficients is a *Poincaré asymptotic series* of $f$ as $z \to \infty$ in $D$ if for every $N \ge 0$
$$z^N \Big( f(z) - \sum_{n=0}^{N} a_n z^{-n} \Big) \to 0 \quad \text{as } z \to \infty \text{ in } D.$$
This is written $f(z) \sim \sum_{n \ge 0} a_n z^{-n}$.
It is the [[asymptotic expansion|BJQTEPEZ9G]] of $f$ in the [[asymptotic scale|XEGB8Y44GG]] $\varphi_n(z) = z^{-n}$.

## Remarks

An equivalent condition is that $f(z) - \sum_{n=0}^{N} a_n z^{-n} = O(z^{-N-1})$ for every $N$.
The coefficients are determined by $f$: $a_0 = \lim f(z)$ and $a_N = \lim z^N \big( f(z) - \sum_{n<N} a_n z^{-n} \big)$.
The same definition with $(z - z_0)^n$ in place of $z^{-n}$ gives Poincaré series at a finite point $z_0$.

Example: $f(z) = \frac{1}{z - 1}$ on $D = (2, \infty)$ has $f(z) \sim \sum_{n \ge 1} z^{-n}$.
Check: $f(z) - \sum_{n=1}^{N} z^{-n} = \frac{z^{-N}}{z - 1}$, and $z^N$ times this is $\frac{1}{z - 1} \to 0$.

Non-example: $f(z) = \sin z$ on $D = (0, \infty)$ has no Poincaré asymptotic series, because $a_0 = \lim_{z \to \infty} \sin z$ does not exist.

The function $e^{-z}$ on $(0, \infty)$ has the zero series, like the function $0$, so the series does not determine the function.
