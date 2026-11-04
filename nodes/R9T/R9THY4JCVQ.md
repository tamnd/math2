---
tag: R9THY4JCVQ
kind: proof
name: Proof of angle-angle similarity with the law of sines
msc: [51M04]
proves: 0NZVJYZVTZ
uses: [0YF6QXXWB5, 0GJAJC6TNZ, 05MDKQBEAF, 0PASQ34GHG, 0NPPGHQNXQ, 0CTNFGYMM2, 08WFZP6P89, 0BRBYRK6PA, 02HPP5VCZH]
sources:
  - url: https://en.wikipedia.org/wiki/Similarity_(geometry)
    locator: Similar triangles
---

## Proof

We get the third angle from the angle sum, and then the ratio of the sides from the law of sines.

1. Let $\alpha = \angle BAC$, $\beta = \angle CBA$ and $\gamma = \angle ACB$, and let $\alpha'$, $\beta'$, $\gamma'$ be the corresponding [[angles|0GJAJC6TNZ]] of $A'B'C'$. By hypothesis $\alpha = \alpha'$ and $\beta = \beta'$.
2. By the [[angle sum of a triangle|05MDKQBEAF]], $\gamma = \pi - \alpha - \beta = \pi - \alpha' - \beta' = \gamma'$.
3. Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$, with the [[Euclidean distance|0NPPGHQNXQ]] $d$. Let $a'$, $b'$, $c'$ be the same distances in $A'B'C'$.
4. By the [[law of sines|0PASQ34GHG]] in $ABC$, there is a number $k$ with $a = k \sin \alpha$, $b = k \sin \beta$ and $c = k \sin \gamma$. Here $k = a / \sin \alpha$.
5. By the law of sines in $A'B'C'$ and steps 1 and 2, there is a number $k'$ with $a' = k' \sin \alpha$, $b' = k' \sin \beta$ and $c' = k' \sin \gamma$.
6. The vertices of a [[triangle|0CTNFGYMM2]] are distinct, so $a, a' > 0$. The quotient $a / \sin \alpha$ in the law of sines is defined, so $\sin \alpha \neq 0$. Since $\alpha \in [0, \pi]$, where the [[sine|08WFZP6P89]] is nonnegative, $\sin \alpha > 0$. So $k > 0$ and $k' = a' / \sin \alpha > 0$.
7. Let $r = k' / k > 0$. By steps 4 and 5, $a' = r a$, $b' = r b$ and $c' = r c$.
8. This says $d(B', C') = r \, d(B, C)$, $d(C', A') = r \, d(C, A)$ and $d(A', B') = r \, d(A, B)$.
9. Let $A'' = A' / r$, $B'' = B' / r$ and $C'' = C' / r$. Scaling by $1 / r$ keeps points non-collinear, so $A''B''C''$ is a triangle.
10. Scaling by $1 / r$ divides each distance by $r$. By step 8, $A''B''C''$ has the same side lengths as $ABC$.
11. By [[side-side-side congruence|0BRBYRK6PA]], there is an [[isometry|02HPP5VCZH]] $f$ of $\R^n$ with $f(A) = A''$, $f(B) = B''$ and $f(C) = C''$.
12. Let $g(x) = r f(x)$. Then $g$ maps $A$, $B$, $C$ to $A'$, $B'$, $C'$, and $d(g(x), g(y)) = r \, d(x, y)$ for all $x, y$.
13. So $A'B'C'$ is a copy of $ABC$, scaled by $r$ after a rigid motion. Hence the triangles are [[similar|0YF6QXXWB5]] with the ratio $r$.

## Idea

Two angles fix the third, because the three add up to $\pi$. The law of sines then says that the sides are proportional to the sines of the opposite angles. Equal angles give equal sines, so the sides of the two triangles are proportional with one common factor. Side-side-side congruence then turns this into a scaling after a rigid motion.
