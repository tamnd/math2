---
tag: REER3CG7DS
kind: definition
name: Fatou set
msc: [37F10]
defines: C0N0XGC6GK
uses: [0XDK9CGYKJ, 0J78KBPFZB, JTVWRXXAKM, AYVTR2ES5B, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Julia_set
---

## Definition

Let $f \colon \hat{\C} \to \hat{\C}$ be a [[rational function|0XDK9CGYKJ]] of degree at least $2$ on the [[Riemann sphere|0J78KBPFZB]] $\hat{\C}$.
Let $f^n$ be its $n$-th [[iterate|AYVTR2ES5B]].
A point $z \in \hat{\C}$ belongs to the *Fatou set* $F(f)$ if the following holds.
There is an [[open|02BH3MCBQB]] neighbourhood $U$ of $z$ such that $\set{f^n|_U : n \ge 0}$ is a [[normal family|JTVWRXXAKM]].
Normality refers to maps into $\hat{\C}$ with the spherical metric.
So every sequence in the family has a subsequence that converges locally uniformly on $U$, possibly to the constant $\infty$.
A connected component of $F(f)$ is a *Fatou component*.

## Remarks

By definition $F(f)$ is open.
Example: for $f(z) = z^2$, the open unit disc lies in $F(f)$, since there $f^n(z) = z^{2^n} \to 0$ locally uniformly.
Non-example: $z = 1$ is not in $F(z^2)$; every neighbourhood of $1$ contains points tending to $0$ and points tending to $\infty$, so no subsequence of iterates has a continuous limit there.
The Fatou set is completely invariant: $z \in F(f)$ if and only if $f(z) \in F(f)$.
The same definition with $\C$ in place of $\hat{\C}$ is used for transcendental entire functions.
