---
tag: 4KTBRP27P6
kind: statement
role: theorem
name: Siegel's theorem on integral points
msc: [11G30, 11D45, 14G05]
uses: [MWBDFS2KJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Siegel%27s_theorem_on_integral_points
same_as:
  wikidata: Q7510553
  wikipedia: Siegel's theorem on integral points
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$.
Let $C$ be a smooth projective geometrically irreducible curve over $K$ of genus $g \ge 1$.
Let $f$ be a nonconstant rational function on $C$ defined over $K$.
Then the set $\set{P \in C(K) : P \text{ is not a pole of } f \text{ and } f(P) \in \mathcal{O}_K}$ is finite.

## Remarks

Equivalently, an affine curve of genus at least $1$ over $K$, embedded in affine space, has only finitely many points with coordinates in $\mathcal{O}_K$.
For genus $0$ the same conclusion holds when $f$ has at least three distinct poles over $\overline{K}$.
The hypothesis $g \ge 1$ is necessary: the Pell equation $x^2 - 2y^2 = 1$ defines a curve of genus $0$ with infinitely many integral points, here $f = x$ has only two poles.
Example: for each integer $k \ne 0$, the Mordell equation $y^2 = x^3 + k$ defines an elliptic curve, so it has only finitely many solutions with $x, y \in \Z$.
The proof combines the weak Mordell–Weil theorem for the Jacobian with a Diophantine approximation theorem of Thue–Siegel type, now usually Roth's theorem; it is not effective in general.
Siegel proved the theorem in 1929.

## Explanations

### L1 human

A curve of genus at least one can have infinitely many rational points, but only finitely many of them have integer coordinates.
For instance, $y^2 = x^3 + k$ has only finitely many integer solutions for each fixed nonzero $k$.

### L2 human

The theorem applies to [[elliptic curves|427N6S6QQW]], where rational points may be infinite in number by [[Mordell's theorem|BZHGKN6Q3K]] but integral points are finite.
Baker's method in transcendence theory later gave effective bounds in many cases, such as Mordell's equation and [[Thue equations|3Q6CFPQZDF]].
For genus at least $2$, [[Faltings's theorem|H0DB07WM20]] gives the stronger statement that even rational points are finite.
