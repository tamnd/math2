---
tag: 743PKABTM8
kind: proof
name: Proof of the third isomorphism theorem for vector spaces
msc: [15A03, 16D10]
topics: [QHKTJ89V6S]
audience: ug1
proves: 07RB3EMBWW
uses: [0MTBGVZ4XJ, 0ZERJX6PH6, 0BR3FY5Q8M, 0N4F5FMQZW, 00YC1D652K, 0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF]
sources:
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Proof

We build a surjective linear map $V / W \to V / U$ with the universal property of the quotient, find its kernel, and apply the first isomorphism theorem.

1. For a subspace $X$ of $V$ and $x, y \in V$, we have $x + X = y + X$ if and only if $x - y \in X$.
   If $x + X = y + X$, then $x = x + 0$ lies in $y + X$, so $x - y \in X$.
   If $x - y = z_0 \in X$, then $x + z = y + (z_0 + z)$ and $y + z = x + (z - z_0)$ for each $z \in X$, so the two cosets agree.
2. In particular, $x + X$ is the zero vector $0 + X$ of $V / X$ exactly when $x \in X$.
3. The set $U / W = \{u + W : u \in U\}$ is a [[subspace|00YC1D652K]] of the [[quotient space|0BR3FY5Q8M]] $V / W$.
   It contains $0 + W$, and $(u + W) + a(u' + W) = (u + au') + W$ with $u + au' \in U$.
4. Let $\pi_U \colon V \to V / U$ be the [[quotient map|0N4F5FMQZW]], $\pi_U(v) = v + U$.
   It is a [[linear map|0NRYHJPQG2]] by the definition of the operations on $V / U$.
5. By step 2, the [[kernel|0S23E6YE83]] of $\pi_U$ is $U$, and $U$ contains $W$ by hypothesis.
6. By the [[universal property of the quotient|0ZERJX6PH6]], there is a linear map $\varphi \colon V / W \to V / U$ with $\varphi(v + W) = v + U$ for all $v \in V$.
7. The map $\varphi$ is surjective, since each $v + U$ equals $\varphi(v + W)$.
   So the [[image|0WSFKKT6FF]] of $\varphi$ is $V / U$.
8. The kernel of $\varphi$ contains $U / W$.
   For $u \in U$, step 2 gives $\varphi(u + W) = u + U = 0 + U$.
9. The kernel of $\varphi$ is contained in $U / W$.
   If $\varphi(v + W) = 0 + U$, then $v + U = 0 + U$, so $v \in U$ by step 2, and $v + W$ lies in $U / W$.
10. By the [[first isomorphism theorem|0MTBGVZ4XJ]], the map $(V / W) / \ker \varphi \to \im \varphi$, $(v + W) + \ker \varphi \mapsto \varphi(v + W)$, is well defined and is a linear isomorphism.
11. By steps 7 to 9, $\ker \varphi = U / W$ and $\im \varphi = V / U$, so this is the map $(V / W) / (U / W) \to V / U$, $(v + W) + U / W \mapsto v + U$.
    So this map is well defined and is a linear isomorphism, which is the statement.

## Idea

Since $W \subseteq U$, the cosets of $W$ are finer than the cosets of $U$: each coset $v + W$ lies inside the single coset $v + U$.
Sending $v + W$ to $v + U$ is therefore a well-defined map $V / W \to V / U$, and it is onto.
It sends $v + W$ to zero exactly when $v \in U$, so its kernel is $U / W$, and the first isomorphism theorem turns this into the isomorphism.

## Variants

One can skip the universal property and check by hand that $v + W \mapsto v + U$ is well defined.
If $v + W = v' + W$, then $v - v' \in W \subseteq U$, so $v + U = v' + U$ by step 1.
In finite dimension one can also finish by counting: the map of the theorem is onto, and both sides have dimension $\dim V - \dim U$ by the dimension of a quotient space, so it is an isomorphism.
