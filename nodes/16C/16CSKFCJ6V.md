---
tag: 16CSKFCJ6V
kind: proof
name: Proof of the codimension bound for an intersection of subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug2
proves: G7DHT62D9F
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0MTBGVZ4XJ, 06HN47VPTH, 0QW084460E, 0SVR29SV1V, 0J0SK5FF4M, 0MM085RX00]
sources:
  - url: https://en.wikipedia.org/wiki/Codimension
    locator: Additivity of codimension and dimension counting
---

## Proof

We embed $V / (U \cap W)$ into the product $V / U \times V / W$ and compare dimensions, and then we find when the embedding is onto.

1. Define $\varphi \colon V \to V / U \times V / W$ by $\varphi(v) = (v + U, v + W)$.
   It is linear, because both [[quotient maps|0J0SK5FF4M]] are linear and the [[product|0MM085RX00]] has componentwise operations.
2. The condition $\varphi(v) = 0$ means $v + U = U$ and $v + W = W$, that is, $v \in U$ and $v \in W$.
   So $\ker \varphi = U \cap W$.
3. By the [[first isomorphism theorem|0MTBGVZ4XJ]], $V / (U \cap W) \cong \operatorname{im} \varphi$.
4. By the [[dimension of a direct product|06HN47VPTH]], the space $V / U \times V / W$ has finite dimension $\operatorname{codim} U + \operatorname{codim} W$.
5. The image $\operatorname{im} \varphi$ is a subspace of this product.
   By the [[dimension of a subspace|0QW084460E]], it is finite-dimensional, $\dim \operatorname{im} \varphi \le \operatorname{codim} U + \operatorname{codim} W$, and equality holds exactly when $\varphi$ is onto.
6. By step 3,
$$\operatorname{codim}(U \cap W) = \dim\bigl(V / (U \cap W)\bigr) = \dim \operatorname{im} \varphi \le \operatorname{codim} U + \operatorname{codim} W.$$
   This proves that $U \cap W$ has finite codimension and that the inequality holds.
7. By step 5, it remains to show that $\varphi$ is onto if and only if $U + W = V$.
8. Assume $U + W = V$, and let a pair $(a + U, b + W)$ be given.
   Write $a - b = u + w$ with $u \in U$ and $w \in W$, and put $v = a - u$.
   Then $v = b + w$ as well, because $a - u = b + w$ is the same equation as $a - b = u + w$.
9. So $v - a = -u \in U$ and $v - b = w \in W$.
   Hence $\varphi(v) = (a + U, b + W)$, and $\varphi$ is onto.
10. Conversely, assume that $\varphi$ is onto, and let $x \in V$.
    Choose $v$ with $\varphi(v) = (x + U, 0 + W)$.
11. Then $x - v \in U$ and $v \in W$.
    So $x = (x - v) + v$ lies in $U + W$, and $U + W = V$.
12. By steps 5 to 11, equality holds in the inequality if and only if $U + W = V$.

## Idea

A vector of $V$ gives two pieces of data, its coset modulo $U$ and its coset modulo $W$.
Two vectors give the same data exactly when they differ by an element of $U \cap W$, so $V / (U \cap W)$ sits inside $V / U \times V / W$.
The dimension of the product bounds the codimension.
The bound is reached when every pair of cosets comes from one vector, and that is the case when $U + W = V$, in the same way as in the Chinese remainder theorem.

## Variants

In finite dimension there is a shorter route.
[[Grassmann's formula|06HTJNCMPA]] gives $\dim(U \cap W) = \dim U + \dim W - \dim(U + W)$, and subtracting both sides from $\dim V$ gives the exact formula $\operatorname{codim}(U \cap W) = \operatorname{codim} U + \operatorname{codim} W - \operatorname{codim}(U + W)$.
Since $\operatorname{codim}(U + W) \ge 0$, with equality exactly when $U + W = V$, both parts of the statement follow.

The same argument with the map $V \to \prod_{i=1}^{k} V / U_i$ proves the bound $\operatorname{codim} \bigcap_i U_i \le \sum_i \operatorname{codim} U_i$ for $k$ subspaces.
