---
tag: 7M4QNPXBT3
kind: proof
name: Proof of side-side-side congruence with orthonormal frames
msc: [51M04]
proves: 0BRBYRK6PA
uses: [093EDENVA1, 02HPP5VCZH, 0CTNFGYMM2, 0AFNNTRTJE, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 0CRMGPAH83, 0RW9TNNT87, 0S9GGTR0EX, 0Y85GYEGSF, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Uniqueness of vector realizations
---

## Proof

The direction "only if" is immediate. For "if", we build the isometry from two orthonormal frames.

1. Suppose that the triangles are [[congruent|093EDENVA1]]. Then there is an [[isometry|02HPP5VCZH]] $f$ of $\R^n$ with $f(A) = A'$, $f(B) = B'$ and $f(C) = C'$.
2. So $d(A', B') = d(f(A), f(B)) = d(A, B)$, and in the same way $d(B', C') = d(B, C)$ and $d(C', A') = d(C, A)$. This proves "only if".
3. For "if", assume the three equalities. Let $u = B - A$, $v = C - A$, $u' = B' - A'$ and $v' = C' - A'$. With the [[Euclidean distance|0NPPGHQNXQ]] and the [[length|0XKBKGTCPC]], the hypotheses say $\norm{u} = \norm{u'}$, $\norm{v} = \norm{v'}$ and $\norm{u - v} = \norm{u' - v'}$.
4. The [[dot product|0S52TNNTH9]] is bilinear and symmetric, so $u \cdot v = \frac{1}{2} \left( \norm{u}^2 + \norm{v}^2 - \norm{u - v}^2 \right)$. The same holds for $u'$ and $v'$. By step 3, $u \cdot v = u' \cdot v'$.
5. Every difference of two vertices of $ABC$ lies in the span of $u$ and $v$. Since $A$, $B$, $C$ are not [[collinear|0AFNNTRTJE]], this span has dimension $2$. So $u$ and $v$ are [[linearly independent|0CRMGPAH83]], and $n \geq 2$. The same holds for $u'$ and $v'$.
6. Let $e_1 = u / \norm{u}$, let $\lambda = v \cdot e_1$, and let $h = v - \lambda e_1$. Then $h \neq 0$, since otherwise $v$ is a multiple of $u$, against step 5.
7. We have $e_1 \cdot h = \lambda - \lambda = 0$ and $\norm{h}^2 = \norm{v}^2 - 2 \lambda^2 + \lambda^2 = \norm{v}^2 - \lambda^2$. Let $e_2 = h / \norm{h}$. Then $(e_1, e_2)$ is an [[orthonormal family|0RW9TNNT87]].
8. In the same way let $e_1' = u' / \norm{u'}$, $\lambda' = v' \cdot e_1'$, $h' = v' - \lambda' e_1'$ and $e_2' = h' / \norm{h'}$. Then $(e_1', e_2')$ is an orthonormal family and $\norm{h'}^2 = \norm{v'}^2 - \lambda'^2$.
9. By steps 3 and 4, $\lambda = (u \cdot v) / \norm{u} = (u' \cdot v') / \norm{u'} = \lambda'$. With step 3 and steps 7 and 8, also $\norm{h} = \norm{h'}$.
10. Each orthonormal family of $\R^n$ [[extends to an orthonormal basis|0Y85GYEGSF]]. Let $(e_1, \dots, e_n)$ and $(e_1', \dots, e_n')$ be [[orthonormal bases|0S9GGTR0EX]] that extend the two families.
11. Let $T$ be the [[linear map|0NRYHJPQG2]] of $\R^n$ with $T(e_i) = e_i'$ for each $i$. It exists because a linear map can take any values on a basis.
12. For $x = \sum_i x_i e_i$, orthonormality gives $\norm{T(x)}^2 = \norm{\sum_i x_i e_i'}^2 = \sum_i x_i^2 = \norm{x}^2$. So $T$ preserves lengths.
13. Let $f(x) = A' + T(x - A)$. By linearity, $f(x) - f(y) = T(x - y)$. By step 12, $d(f(x), f(y)) = d(x, y)$ for all $x, y$. So $f$ is an isometry.
14. We have $f(A) = A'$. Also $f(B) = A' + T(u) = A' + \norm{u} \, e_1' = A' + \norm{u'} \, e_1' = A' + u' = B'$.
15. By steps 6 and 7, $v = \lambda e_1 + \norm{h} \, e_2$. So $T(v) = \lambda e_1' + \norm{h} \, e_2' = \lambda' e_1' + \norm{h'} \, e_2' = \lambda' e_1' + h' = v'$, by step 9.
16. Thus $f(C) = A' + T(v) = A' + v' = C'$.
17. By steps 13, 14 and 16, $f$ is an isometry that maps $A$, $B$, $C$ to $A'$, $B'$, $C'$. So the triangles are congruent.

## Idea

The three side lengths fix the lengths of the edge vectors $u$, $v$ from $A$ and their dot product. These numbers fix the coordinates of $u$ and $v$ in an orthonormal frame adapted to them. A linear isometry that carries one frame to the other, followed by a translation, carries one triangle to the other.
