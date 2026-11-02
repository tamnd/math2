---
tag: A67HV2KCHR
kind: definition
name: Birkhoff's axioms
msc: [51M05, 51F05]
defines: 6BB0KD6752
uses: [08J2M1JYAG, 0MP9BCF6DP, 0GJAJC6TNZ, 0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff%27s_axioms
---

## Definition

Let $\Pi$ be a set of points with a family of subsets called lines and a distance function $d \colon \Pi \times \Pi \to \R$.
For a point $O$, the rays from $O$ carry a measure: $\angle AOB$ denotes the angle of the rays $OA$ and $OB$.
*Birkhoff's axioms* are the following four postulates.

1. Line measure: the points of each [[line|0MP9BCF6DP]] $\ell$ can be put in bijection with the [[real numbers|08J2M1JYAG]], $A \mapsto x_A$, so that $\abs{x_A - x_B} = d(A, B)$ for all $A, B \in \ell$.
2. Point and line: through two distinct points there is exactly one line.
3. Angle measure: the rays from each point $O$ can be put in bijection with $\R / 2\pi\Z$. Then $\angle AOB$ is the difference of the numbers of $OA$ and $OB$. Moreover, as $B$ moves continuously on a line not through $O$, the number of the ray $OB$ varies continuously.
4. Similarity: let $ABC$ and $A'B'C'$ be [[triangles|0CTNFGYMM2]] and $k > 0$ such that $d(A', B') = k\, d(A, B)$, $d(A', C') = k\, d(A, C)$ and $\angle B'A'C' = \pm \angle BAC$. Then $d(B', C') = k\, d(B, C)$, $\angle C'B'A' = \pm \angle CBA$ and $\angle A'C'B' = \pm \angle ACB$.

## Remarks

Example: $\R^2$ with the usual distance and the polar angle of rays satisfies all four postulates.
The similarity postulate holds there because a similarity of ratio $k$ maps one triangle onto the other.
Non-example: the sphere with great circles as lines and the great-circle distance fails postulate 2, since there are infinitely many great circles through two antipodal points.
The axioms of [[angles|0GJAJC6TNZ]] are those of a protractor, and the axioms of lines are those of a ruler.
The four postulates determine the Euclidean plane up to isometry.
