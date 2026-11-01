---
tag: KW31KDX7TB
kind: statement
role: theorem
name: Bloch's theorem
msc: [30D20, 30C25]
uses: [0DG0Z72CQD, 8G5ABXRK85, 0PVG1CRAJN, AC3FNJ8Y1Y]
about: [AC3FNJ8Y1Y]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_analysis)
same_as:
  wikidata: Q266291
  wikipedia: Bloch's theorem (complex analysis)
---

## Statement

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the [[unit disc|8G5ABXRK85]].
There is an absolute constant $b > 0$ with the following property.
Let $f \colon \mathbb{D} \to \C$ be any [[holomorphic|0DG0Z72CQD]] function with $f'(0) = 1$.
Then there is an open set $\Omega \subseteq \mathbb{D}$ such that $f$ is [[injective|0PVG1CRAJN]] on $\Omega$ and $f(\Omega)$ is an open disc of radius $b$.

## Remarks

The supremum of all such $b$ is the Bloch constant $B$, one of [[Landau's constants|AC3FNJ8Y1Y]].
Lars Ahlfors proved $B \ge \sqrt{3}/4$, and it is known that $B < 0.472$; the exact value is unknown.
One proof first replaces $f$ by $f(rz)/r$ for some $r < 1$, so that $f$ is holomorphic on the closed disc.
Then one picks a point where $(1 - \abs{z}^2)\abs{f'(z)}$ is maximal and rescales around it, which gives a function whose derivative is bounded on a disc of fixed size.
A bounded derivative with $\abs{f'(0)} = 1$ forces $f$ to be injective on a smaller disc of explicit radius, and the image of that disc contains a disc of explicit radius.
The theorem gives a short proof of [[Picard's little theorem|R2PHM118NG]].
The normalisation $f'(0) = 1$ is needed: the functions $f(z) = \varepsilon z$ only cover discs of radius $\varepsilon$.

## Explanations

### L1 human

Take any holomorphic function on the unit disc whose derivative at the centre is $1$.
Its image may fold over itself in a complicated way.
Bloch's theorem says that, somewhere inside the image, there is always a round disc of a fixed size that is covered exactly once.
The size of this disc does not depend on the function.

### L2 human

The theorem is a covering theorem with no assumption of injectivity on $f$.
For injective $f$, the [[Koebe quarter theorem|WX0HMW4GT7]] gives much more: a disc of radius $1/4$ around $f(0)$.
Bloch's theorem is scale invariant in the right way, so applying it to $f(rz)$ with large $r$ shows that a nonconstant entire function covers schlicht discs of every radius.
This is the key step in the proof of Picard's little theorem by Bloch's method.
