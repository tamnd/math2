---
tag: WJ5WRGG5DE
kind: statement
role: theorem
name: Castelnuovo's contraction theorem
msc: ["14E05", 14J26]
uses: [KFTECAATKG, C4KGYAFPN7, 4HV4WTAX9P, ZT9A6JK8QF, 0PF6TM8TWT]
about: [KFTECAATKG, C4KGYAFPN7]
sources:
  - url: https://en.wikipedia.org/wiki/Enriques%E2%80%93Kodaira_classification
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] and let $X$ be a smooth projective [[surface|KFTECAATKG]] over $k$.
Let $E \subset X$ be a curve with $E \cong \mathbb{P}^1$ and self-[[intersection number|4HV4WTAX9P]] $E \cdot E = -1$.
Then there are a smooth projective surface $Y$, a point $p \in Y$ and a morphism $f \colon X \to Y$ with the following property.
The morphism $f$ is isomorphic to the [[blow-up|C4KGYAFPN7]] of $Y$ at $p$, with exceptional curve $E$.

## Remarks

The idea of the proof is to choose a very ample divisor $H$ on $X$ with $H^1(X, \mathcal{O}_X(H)) = 0$, put $m = H \cdot E$, and use the linear system $\abs{H + mE}$.
It has degree $0$ on $E$, so it contracts $E$ to a point, and a computation of sections shows that the image surface is smooth at that point.
Example: a smooth cubic surface over $k$ contains $27$ lines, each a $(-1)$-curve, and contracting six disjoint lines among them gives $\mathbb{P}^2$.
The condition $E \cdot E = -1$ cannot be weakened to $E \cdot E < 0$.
A smooth rational curve with $E \cdot E = -2$ can sometimes be contracted, but the image point is then singular, an $A_1$ singularity.

## Explanations

### L1 human

Blowing up a point of a smooth surface creates a new curve, a copy of the projective line with self-intersection $-1$.
The theorem says the converse: any such curve comes from a blow-up and can be blown down.
So the curves of this kind are exactly the traces left by blowing up.

### L2 human

The theorem is the basic step of the minimal model program for surfaces.
Contracting $(-1)$-curves one at a time lowers the Picard number, so the process stops, at a surface with no $(-1)$-curves.
So every smooth projective surface is obtained from a surface without $(-1)$-curves by finitely many blow-ups of points.
The surfaces without $(-1)$-curves are then sorted by the Enriques–Kodaira classification.
