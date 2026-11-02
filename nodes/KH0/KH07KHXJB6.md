---
tag: KH07KHXJB6
kind: definition
name: Unique ergodicity
msc: [37A25, 37B05]
defines: NZZE9KCAD8
uses: [0VKD1TP7F3, 0TVJZYB6SH, DYR1QFNGNJ, 059TJN0NZ1, B232EZ1FMB, 1DHZ81S0YE]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodicity
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]] [[metric space|0VKD1TP7F3]] and let $T \colon X \to X$ be a continuous map.
A [[Borel|DYR1QFNGNJ]] [[probability measure|059TJN0NZ1]] $\mu$ on $X$ is $T$-[[invariant|B232EZ1FMB]] if $\mu(T^{-1}A) = \mu(A)$ for every Borel set $A \subseteq X$.
The map $T$ is *uniquely ergodic* if there is exactly one $T$-invariant Borel probability measure on $X$.

## Remarks

By the [[Krylov–Bogolyubov theorem|1DHZ81S0YE]] the set of invariant Borel probability measures is never empty, so unique ergodicity asks that it has a single element.

Example: let $X = \R/\Z$, let $\alpha$ be irrational and let $T(x) = x + \alpha \bmod 1$.
If $\mu$ is invariant, its Fourier coefficients $\hat\mu(h) = \int e^{-2\pi i h x} \, d\mu(x)$ satisfy $\hat\mu(h) = e^{-2\pi i h \alpha} \hat\mu(h)$.
For $h \ne 0$ the factor $e^{-2\pi i h \alpha}$ is not $1$, so $\hat\mu(h) = 0$.
A measure on the circle is determined by its Fourier coefficients, so $\mu$ is Lebesgue measure, and $T$ is uniquely ergodic.

Non-example: the doubling map $T(x) = 2x \bmod 1$ on $\R/\Z$ is continuous and fixes $0$.
Both the point mass at $0$ and Lebesgue measure are invariant, so $T$ is not uniquely ergodic.

Equivalent form: $T$ is uniquely ergodic if and only if, for every continuous $f \colon X \to \R$, the averages $\frac{1}{N} \sum_{n=0}^{N-1} f(T^n x)$ converge uniformly in $x$ to a constant.
The constant is then $\int f \, d\mu$ for the unique invariant measure $\mu$.
