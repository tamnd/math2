---
tag: X1P48KQFXQ
kind: definition
name: Anosov diffeomorphism
msc: [37D20]
defines: RCQH8P6DPQ
uses: [NY9MCZXY6N, 0Z1Y7JHGBR, 0QPHW703PV]
sources:
  - url: https://en.wikipedia.org/wiki/Anosov_diffeomorphism
---

## Definition

Let $M$ be a [[compact|0QPHW703PV]] Riemannian manifold and let $f \colon M \to M$ be a $C^1$ [[diffeomorphism|0Z1Y7JHGBR]].
Then $f$ is an *Anosov diffeomorphism* if $M$ itself is a [[hyperbolic set|NY9MCZXY6N]] of $f$.
That is, there is a $Df$-invariant splitting $T_x M = E^s_x \oplus E^u_x$ for all $x \in M$, and there are constants $C > 0$ and $0 < \lambda < 1$.
For all $n \ge 0$, they satisfy $\norm{Df^n v} \le C\lambda^n \norm{v}$ for $v \in E^s$ and $\norm{Df^{-n} v} \le C\lambda^n\norm{v}$ for $v \in E^u$.

## Remarks

The property does not depend on the choice of Riemannian metric, since $M$ is compact.
Example: let $A$ be a $2 \times 2$ integer matrix with $\det A = \pm 1$ and no eigenvalue of modulus $1$, and let $f_A$ be the induced map of the torus $\R^2/\Z^2$.
Then $Df_A = A$ at every point, and the eigenlines of $A$ give $E^s$ and $E^u$ with $C = 1$ after a linear change of metric.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ the eigenvalues are $(3 \pm \sqrt5)/2$, which gives [[Arnold's cat map|BSCZN8Y1AN]].
Non-example: for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ the map $f_A$ is a diffeomorphism of the torus, but both eigenvalues equal $1$, so no direction is contracted and the condition fails.
All known Anosov diffeomorphisms are, up to topological conjugacy, hyperbolic automorphisms of tori, nilmanifolds or infranilmanifolds; whether this is always the case is an open question.
