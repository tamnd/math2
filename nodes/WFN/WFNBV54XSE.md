---
tag: WFNBV54XSE
kind: proof
name: Proof that the exterior derivative squares to zero
msc: ["58A10"]
proves: 0X308R2DBE
uses: [004FRCXH6M, 0S166D363M, 0QHTX7WQEY, 0NNQY8WCW6, 0TCBZMEYGN, 0SK90238BH, 0JEJJCB0EX, 02DTRYKGE8]
sources:
  - url: https://en.wikipedia.org/wiki/Exterior_derivative
    locator: In terms of axioms
---

## Proof

We expand $d(d\omega)$ in coordinates. The mixed second derivatives are symmetric, while the wedge symbols are antisymmetric, so the terms cancel in pairs.

1. Write $\partial_j = \partial / \partial x_j$. For a finite sequence $J = (j_1, \dots, j_m)$ of indices in $\set{1, \dots, n}$, let $e_J = dx_{j_1} \wedge \dots \wedge dx_{j_m}$, as in the definition of the [[wedge product|0S166D363M]]. It is $0$ if two indices are equal. Otherwise it is $\operatorname{sgn}(\sigma) \, dx_K$, where $K$ is the increasing rearrangement and $\sigma$ the sorting permutation.
2. Fact A: let $J$ have no repeated index, with $e_J = \varepsilon \, dx_K$. Then $e_{(l, J)} = \varepsilon \, e_{(l, K)}$ for each index $l$.
3. Proof of fact A. If $l$ occurs in $J$, then it occurs in $K$, and both sides are $0$. Otherwise, sort $(l, J)$ in two stages: first sort the last $m$ places, turning $J$ into $K$, then sort $(l, K)$.
4. The first stage has [[sign|0SK90238BH]] $\varepsilon$. The sign is multiplicative, because [[the sign is a homomorphism|0JEJJCB0EX]]. So the sign of sorting $(l, J)$ is $\varepsilon$ times the sign of sorting $(l, K)$, which is fact A.
5. Fact B: for indices $l, j$ and a sequence $I$, $e_{(l, j) I} = -e_{(j, l) I}$, where $(l, j) I$ means $(l, j, i_1, \dots, i_k)$. If there is a repeated index, both sides are $0$.
6. Proof of fact B without repeats. The two sequences differ by the [[transposition|02DTRYKGE8]] of the first two places. So their sorting permutations differ by a transposition, which has sign $-1$, and the homomorphism property gives the sign change.
7. Let $\omega = \sum_I f_I \, dx_I$ be a [[$k$-form|0QHTX7WQEY]] whose coefficients $f_I$ are of [[class $C^2$|0TCBZMEYGN]]. By the definition of the [[exterior derivative|004FRCXH6M]], and since $dx_j \wedge dx_I = e_{(j) I}$, we have $d\omega = \sum_I \sum_j \partial_j f_I \, e_{(j) I}$.
8. For $j \notin I$, write $e_{(j) I} = \varepsilon(j, I) \, dx_{K(j, I)}$ with $\varepsilon(j, I) = \pm 1$. For $j \in I$, $e_{(j) I} = 0$. Collecting terms gives $d\omega = \sum_K g_K \, dx_K$, where $g_K$ is the sum of $\varepsilon(j, I) \, \partial_j f_I$ over the pairs with $j \notin I$ and $K(j, I) = K$.
9. Each $g_K$ is a finite sum of first partial derivatives of $C^2$ functions, so it is $C^1$. So $d(d\omega)$ is defined, and $d(d\omega) = \sum_K \sum_l \partial_l g_K \, e_{(l) K}$.
10. Expanding $g_K$ by step 8 and regrouping the finite sum, $d(d\omega) = \sum_I \sum_{j \notin I} \sum_l \partial_l \partial_j f_I \, \varepsilon(j, I) \, e_{(l) K(j, I)}$.
11. By fact A, $\varepsilon(j, I) \, e_{(l) K(j, I)} = e_{(l, j) I}$. For $j \in I$ the sequence $(l, j) I$ has a repeated index, so $e_{(l, j) I} = 0$. Hence $d(d\omega) = \sum_I \sum_{j, l} \partial_l \partial_j f_I \, e_{(l, j) I}$.
12. Fix $I$. The terms with $j = l$ vanish, because $(l, l) I$ has a repeated index.
13. For $j \ne l$, take the two terms for $(j, l)$ and $(l, j)$. By fact B their sum is $(\partial_l \partial_j f_I - \partial_j \partial_l f_I) \, e_{(l, j) I}$.
14. By [[Schwarz's theorem|0NNQY8WCW6]] for the $C^2$ function $f_I$, $\partial_l \partial_j f_I = \partial_j \partial_l f_I$. So each such pair contributes $0$.
15. By steps 11 to 14, every term of $d(d\omega)$ cancels, and $d(d\omega) = 0$.

## Idea

Applying $d$ twice produces each second derivative $\partial_l \partial_j f$ together with $dx_l \wedge dx_j$. Swapping $l$ and $j$ leaves the derivative the same for $C^2$ functions but changes the sign of the wedge. So the terms cancel in pairs, and the diagonal terms vanish because $dx_l \wedge dx_l = 0$.
