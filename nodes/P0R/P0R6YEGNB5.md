---
tag: P0R6YEGNB5
kind: statement
role: theorem
name: Schwarz reflection principle
msc: [30B40, "30E25"]
uses: [0DG0Z72CQD, 0VDD7W0EKZ, 0BJV24C4SY, 097KNJFJ7V]
about: [0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_reflection_principle
same_as:
  wikidata: Q4378892
  wikipedia: Schwarz reflection principle
---

## Statement

Let $\Omega \subseteq \C$ be an open set that is symmetric with respect to the real axis: $\bar z \in \Omega$ for each $z \in \Omega$.
Let $\Omega^+ = \set{z \in \Omega : \operatorname{Im} z > 0}$ and $\sigma = \Omega \cap \R$.
Let $f$ be continuous on $\Omega^+ \cup \sigma$, [[holomorphic|0DG0Z72CQD]] on $\Omega^+$, and real-valued on $\sigma$.
Define $F(z) = f(z)$ for $z \in \Omega^+ \cup \sigma$ and $F(z) = \overline{f(\bar z)}$ for $z \in \Omega$ with $\operatorname{Im} z < 0$.
Then $F$ is holomorphic on $\Omega$.

## Remarks

Proof idea: $F$ is holomorphic on $\Omega \setminus \R$, since $z \mapsto \overline{f(\bar z)}$ satisfies the Cauchy–Riemann equations when $f$ does.
$F$ is continuous on $\Omega$, because $f$ is real on $\sigma$, so the two definitions agree there.
The integral of $F$ over each small triangle in $\Omega$ is $0$: for triangles meeting $\R$, approximate by triangles slightly off the axis.
[[Morera's theorem|0VDD7W0EKZ]] then gives that $F$ is holomorphic.
Example: $f(z) = e^{z}$ on the upper half-plane is real on $\R$, and its reflection is $\overline{e^{\bar z}} = e^{z}$, as expected.
The hypothesis that $f$ is real on $\sigma$ is needed: $f(z) = i$ is continuous up to $\R$ but its reflection is $-i$ below the axis, which is not even continuous.
By a Möbius transformation the same principle holds for reflection across a circle, with $\bar z$ replaced by the inverse point.

## Explanations

### L1 human

If a holomorphic function on the upper half-plane takes real values on the real axis, it extends to the lower half-plane by mirror symmetry.
The value at the mirror point $\bar z$ is the complex conjugate of the value at $z$.
The two halves fit together into one holomorphic function.

### L2 human

The reflection principle is a basic tool of [[analytic continuation|0M3YQJ81NB]].
It is used to extend conformal maps whose boundary goes to a line or a circle, as for the Schwarz–Christoffel formula.
It also shows that a conformal map between domains bounded by analytic arcs extends across those arcs.
There is a version for harmonic functions that vanish on a line, which is the main step in some proofs.
