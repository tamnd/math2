---
tag: 5NEJPXA6N4
kind: statement
role: theorem
name: Congruence criteria for triangles
msc: [51M04, 51F20]
uses: [093EDENVA1, 0CTNFGYMM2, 0GJAJC6TNZ, 0NPPGHQNXQ]
about: [093EDENVA1]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_(geometry)
---

## Statement

Let $ABC$ and $A'B'C'$ be [[triangles|0CTNFGYMM2]] in the Euclidean plane.
Write $XY$ for the [[distance|0NPPGHQNXQ]] between points $X$ and $Y$, and $\angle A$ for the [[angle|0GJAJC6TNZ]] $\angle BAC$, and so on.
The triangles are [[congruent|093EDENVA1]] under $A \mapsto A'$, $B \mapsto B'$, $C \mapsto C'$ in each of these cases.

1. Side-side-side: $AB = A'B'$, $BC = B'C'$ and $CA = C'A'$.
2. Side-angle-side: $AB = A'B'$, $AC = A'C'$ and $\angle A = \angle A'$.
3. Angle-side-angle: $\angle A = \angle A'$, $AB = A'B'$ and $\angle B = \angle B'$.
4. Angle-angle-side: $\angle A = \angle A'$, $\angle B = \angle B'$ and $BC = B'C'$.

## Remarks

The [[side-side-side criterion|0BRBYRK6PA]] has its own node.
For side-angle-side, the [[law of cosines|060ZVZBV3E]] gives $BC^2 = AB^2 + AC^2 - 2 \, AB \cdot AC \cos \angle A$, so $BC = B'C'$, and case 1 applies.
Angle-angle-side reduces to angle-side-angle, because the [[angle sum|05MDKQBEAF]] gives $\angle C = \angle C'$.
For angle-side-angle, the law of sines then fixes the two other sides.

Two other patterns are not criteria.
Side-side-angle fails: $AB = 2$, $BC = \sqrt{2}$ and $\angle A = 30^\circ$ fit two triangles.
By the law of sines $\sin \angle C = \frac{1}{\sqrt{2}}$, so $\angle C = 45^\circ$ or $\angle C = 135^\circ$.
Angle-angle-angle fails: triangles with equal angles are [[similar|0YF6QXXWB5]], but they can have different sizes.

## Explanations

### L1 human

These rules say how little you need to know about a triangle to pin it down.
Three sides are enough, and so are two sides with the angle between them, or one side with two angles.
Each rule says that two triangles that agree in these pieces are copies of each other.

### L2 human

In Euclid's Elements these are early propositions of Book I, and in Hilbert's axioms a form of side-angle-side is taken as an axiom.
The criteria are the main tool of synthetic proofs: one shows two segments or angles are equal by fitting them into congruent triangles.
Over the reals, each criterion follows from the law of cosines or the law of sines.
