---
tag: SHSXQ98PHB
kind: definition
name: Julia set
msc: [37F10]
defines: 5M4S7P04GR
uses: [C0N0XGC6GK, 0XDK9CGYKJ, 0J78KBPFZB]
sources:
  - url: https://en.wikipedia.org/wiki/Julia_set
---

## Definition

Let $f \colon \hat{\C} \to \hat{\C}$ be a [[rational function|0XDK9CGYKJ]] of degree at least $2$ on the [[Riemann sphere|0J78KBPFZB]] $\hat{\C}$.
Let $F(f)$ be the [[Fatou set|C0N0XGC6GK]] of $f$.
The *Julia set* of $f$ is the complement $J(f) = \hat{\C} \setminus F(f)$.
So a point $z$ lies in $J(f)$ if and only if the iterates $f^n$, $n \ge 0$, form a normal family on no open neighbourhood of $z$.

## Remarks

Example: for $f(z) = z^2$, $J(f)$ is the unit circle.
On $\abs{z} < 1$ the iterates $z^{2^n}$ tend to $0$ locally uniformly, and on $\abs{z} > 1$ they tend to $\infty$, so both regions lie in $F(f)$.
Every neighbourhood of a point with $\abs{z} = 1$ contains points whose orbits tend to $0$ and points whose orbits tend to $\infty$.
So a limit of a subsequence of iterates would be discontinuous there, and the point is in $J(f)$.
Non-example: $z = 1/2$ is not in $J(z^2)$, because the disc $\abs{z} < 3/4$ lies in the Fatou set.
For degree at least $2$, $J(f)$ is nonempty, compact and perfect, it satisfies $f^{-1}(J(f)) = J(f)$, and it is the closure of the set of repelling periodic points.
The same definition, with $\C$ in place of $\hat{\C}$, is used for transcendental entire functions.
