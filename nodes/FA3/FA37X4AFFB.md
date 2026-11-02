---
tag: FA37X4AFFB
kind: statement
role: theorem
name: Classification of Fatou components
msc: [37F10, 37F50]
uses: [C0N0XGC6GK, 0XDK9CGYKJ, T75CZ5H47N, KNDYA9T8ZK, HZX6Q514X8, C9FDR4BGMG]
about: [C0N0XGC6GK]
sources:
  - url: https://en.wikipedia.org/wiki/Classification_of_Fatou_components
same_as:
  wikidata: Q4223035
  wikipedia: Classification of Fatou components
---

## Statement

Let $f \colon \hat{\C} \to \hat{\C}$ be a [[rational function|0XDK9CGYKJ]] of degree at least $2$.
Let $U$ be a component of the [[Fatou set|C0N0XGC6GK]] of $f$ with $f^p(U) = U$ for some $p \ge 1$, and let $g = f^p$.
Then exactly one of the following holds.

1. Attracting case: $U$ contains a fixed point $z_0$ of $g$ with $\abs{g'(z_0)} < 1$, and $g^n \to z_0$ locally uniformly on $U$.
2. Parabolic case: $\partial U$ contains a fixed point $z_0$ of $g$ with $g'(z_0) = 1$, and $g^n \to z_0$ locally uniformly on $U$.
3. Siegel case: $U$ is a [[Siegel disc|KNDYA9T8ZK]].
4. Herman case: $U$ is a [[Herman ring|HZX6Q514X8]].

## Remarks

In the first two cases $z_0$ is a [[periodic point|T75CZ5H47N]] of $f$, and the superattracting case $g'(z_0) = 0$ is included in the first case.
In the last two cases $g$ restricted to $U$ is conformally conjugate to an irrational rotation of a disc or of a round annulus.
The proof uses the theory of normal families: limits of subsequences of $g^n$ on $U$ are either constant, giving the first two cases, or not, giving the last two.
For $f(z) = z^2$, the unit disc is an attracting component with $z_0 = 0$.
For $f(z) = z + z^2$, the fixed point $0$ has multiplier $1$ and lies on the boundary of a parabolic component.
By [[Sullivan's theorem|C9FDR4BGMG]] every Fatou component is eventually periodic, so these four types describe the long-run behaviour on the whole Fatou set.

## Explanations

### L1 human

A periodic piece of the Fatou set can behave in only four ways.
Its points can be sucked into a fixed point inside it, or creep towards a fixed point on its edge.
Or the piece can be a disc or a ring on which the map simply turns, like a wheel by an irrational angle.
Nothing else can happen.

### L2 human

The theorem is the starting point for describing the Fatou set of any rational map.
Attracting and parabolic cycles each attract at least one critical point.
So a map of degree $d$ has at most $2d - 2$ such cycles, the number of its critical points counted with multiplicity.
Siegel discs and Herman rings are rotation domains; their boundaries lie in the closure of the critical orbits.
Polynomials have no Herman rings, so for them only three cases occur.
