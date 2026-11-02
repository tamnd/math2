---
tag: XXXSST2DR5
kind: definition
name: Spectrum of an operator
msc: [47A10]
defines: BMKATJ802A
uses: [06GZ956657, 03TM135G0N, CPAD5W1CGW, 0XPX5NC67E, VM7B38PA87]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
---

## Definition

Let $X$ be a complex [[Banach space|06GZ956657]], let $I$ be its identity map, and let $T \colon X \to X$ be a [[continuous linear map|03TM135G0N]].
The *spectrum* of $T$ is the set
$$\sigma(T) = \set{\lambda \in \C : T - \lambda I \text{ is not invertible}},$$
where invertible means [[invertible as a bounded operator|CPAD5W1CGW]].

## Remarks

By the bounded inverse theorem, $\lambda \in \sigma(T)$ if and only if $T - \lambda I$ is not bijective.
If $X \ne \set{0}$, then $\sigma(T)$ is a nonempty compact subset of the closed disc $\set{\lambda : \abs{\lambda} \le \norm{T}}$.
For $X = \C^n$, $\sigma(T)$ is the [[spectrum of the matrix|0XPX5NC67E]] of $T$, its set of eigenvalues.

Example: let $D(x_n) = (x_n / n)$ on $\ell^2$.
For $\lambda \notin \set{1/n : n \ge 1} \cup \set{0}$, the numbers $1/(1/n - \lambda)$ are bounded, so the diagonal operator with these entries is a bounded inverse of $D - \lambda I$.
Each $1/n$ is an eigenvalue, and $D$ is not surjective, so $\sigma(D) = \set{1/n : n \ge 1} \cup \set{0}$.

Non-example: the number $2$ is not in $\sigma(D)$, since $\abs{1/(1/n - 2)} \le 1$ for all $n$, so $D - 2I$ has a bounded inverse.

For a [[closed operator|VM7B38PA87]] $T$ with domain $D(T)$, $\lambda$ is outside $\sigma(T)$ when $T - \lambda I \colon D(T) \to X$ is bijective with bounded inverse.
The spectrum is then closed, but it can be empty or unbounded.
