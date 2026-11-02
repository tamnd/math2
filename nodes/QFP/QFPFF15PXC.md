---
tag: QFPFF15PXC
kind: statement
role: theorem
name: Poles of the gamma function
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0NSD1TPHR0, 066E7PJCYE, 0PHN07KVQT]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$.
The [[poles|066E7PJCYE]] of $\Gamma$ are exactly the points $z = -n$ with $n \in \set{0, 1, 2, \ldots}$.
Each of them is a simple pole, and the [[residue|0PHN07KVQT]] of $\Gamma$ at $-n$ is
$$\operatorname{Res}_{z = -n} \Gamma(z) = \frac{(-1)^n}{n!}.$$

## Remarks

Iterating the functional equation gives $\Gamma(z) = \dfrac{\Gamma(z + n + 1)}{z (z + 1) \cdots (z + n)}$ near $z = -n$.
The numerator is holomorphic at $-n$ with value $\Gamma(1) = 1$, and only the factor $z + n$ of the denominator vanishes there, to first order.
So the pole is simple, and the residue is $1/\big((-n)(-n + 1) \cdots (-1)\big) = (-1)^n/n!$.
Away from these points $\Gamma$ is holomorphic, see [[holomorphy of the gamma function|ZKJF80DTNB]].
For example, near $z = 0$ one has $\Gamma(z) = \frac{1}{z} - \gamma + O(z)$, where $\gamma$ is the [[Euler–Mascheroni constant|00C5P9JZBK]].

## Explanations

### L1 human

The gamma function blows up at $0$ and at every negative integer.
Near each such point it behaves like a constant divided by the distance to the point, and the constants $1, -1, \tfrac12, -\tfrac16, \ldots$ are $(-1)^n/n!$.

### L2 human

The residues explain contour integral formulas such as the Mellin–Barnes integrals, where closing the contour to the left picks up the poles of $\Gamma$ and produces power series.
For instance, summing the residues of $\Gamma(s) x^{-s}$ at $s = -n$ gives $\sum_n (-1)^n x^n / n! = e^{-x}$.
The fact that the poles are simple and $\Gamma$ has no zeros makes $1/\Gamma$ an entire function with simple zeros.
