---
tag: 2ZM39HSFTQ
kind: statement
role: theorem
name: Kirszbraun theorem
msc: [26B35, 54C20, 46C05]
uses: [0AW1E6YTJY, 0QVNCJXRY3]
about: [0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Kirszbraun_theorem
same_as:
  wikidata: Q4454954
  wikipedia: Kirszbraun theorem
---

## Statement

Let $n, m \ge 1$, let $S \subseteq \R^n$ be any subset, and let $L \ge 0$.
Give $\R^n$ and $\R^m$ the Euclidean norm.
Let $f \colon S \to \R^m$ satisfy the [[Lipschitz condition|0AW1E6YTJY]] $\norm{f(x) - f(y)} \le L \norm{x - y}$ for all $x, y \in S$.
Then there is a map $F \colon \R^n \to \R^m$ with $F = f$ on $S$ and $\norm{F(x) - F(y)} \le L \norm{x - y}$ for all $x, y \in \R^n$.

## Remarks

The point is that the extension keeps the same Lipschitz constant $L$.
For $m = 1$ this follows from the [[McShane–Whitney extension|MV7ADC2DEH]].
Extending each coordinate separately for $m \ge 2$ only gives the constant $\sqrt{m} \, L$.
The theorem holds more generally for maps from a subset of one Hilbert space to another Hilbert space.
It can fail for norms that do not come from an [[inner product|0QVNCJXRY3]].
One proof first extends $f$ to one extra point, which reduces to a statement about intersections of balls in Euclidean space, and then uses Zorn's lemma or a compactness argument.

## Explanations

### L1 human

A Lipschitz map does not stretch distances by more than a factor $L$.
If such a map is given only on part of space, one can fill in the rest without stretching any more.
This is easy for real-valued maps, but for vector-valued maps it needs the geometry of Euclidean space.

### L2 human

The theorem is a basic tool in geometric measure theory, where Lipschitz maps are often defined on irregular sets.
It lets one assume that a Lipschitz map is defined on all of $\R^n$, and then apply results such as [[Rademacher's theorem|QEY26RT19R]].
The key geometric step is about balls.
Take two families of balls with the same radii, where the distances between centres in the second family are at most those in the first.
If the first family has a common point, then so does the second.
