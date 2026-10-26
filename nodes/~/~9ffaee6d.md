---
tag: ~9ffaee6d
kind: statement
role: theorem
name: The characteristic function determines the distribution
aliases: [uniqueness-theorem-for-characteristic-functions, levy-inversion-formula]
msc: ["60E10"]
uses: [~d6b5de2f, ~e6cf98ca, ~d33bcb6a]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)
    locator: Inversion formula
---

## Statement

Let $X$ and $Y$ be real random variables with [[characteristic functions|~d6b5de2f]] $\varphi_X$ and $\varphi_Y$.
If $\varphi_X(t) = \varphi_Y(t)$ for all $t \in \mathbb{R}$, then $X$ and $Y$ have the same [[law|~e6cf98ca]].

## Remarks

The proof uses the Lévy inversion formula. For real $a < b$ that are continuity points of the [[cumulative distribution function|~d33bcb6a]] $F_X$,
$$F_X(b) - F_X(a) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^{T} \frac{e^{-ita} - e^{-itb}}{it} \, \varphi_X(t) \, dt.$$
If $\int |\varphi_X(t)| \, dt < \infty$, then $X$ has the continuous density $f_X(x) = \frac{1}{2\pi} \int e^{-itx} \varphi_X(t) \, dt$.
The same result holds for random vectors in $\mathbb{R}^n$, with $\varphi_X(t) = E[e^{i \langle t, X \rangle}]$.

## Explanations

### L1 human

Two different distributions cannot have the same characteristic function.
So, to identify a distribution, it is enough to compute its characteristic function and recognize it.
