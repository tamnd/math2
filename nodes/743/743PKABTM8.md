---
tag: 743PKABTM8
kind: proof
name: Proof of the third isomorphism theorem for vector spaces
msc: [15A03, 16D10]
proves: 07RB3EMBWW
uses: [0MTBGVZ4XJ, 0ZERJX6PH6, 0BR3FY5Q8M, 0N4F5FMQZW, 00YC1D652K, 0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF]
sources:
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Proof

We build the map $V / W \to V / U$ with the universal property and apply the first isomorphism theorem.

1. For a subspace $X$ of $V$ and $x, y \in V$, we have $x + X = y + X$ if and only if $x - y \in X$. If $x + X = y + X$, then $x = x + 0 \in y + X$, so $x - y \in X$.
2. Conversely, if $x - y = z_0 \in X$, then $x + z = y + (z_0 + z)$ and $y + z = x + (z - z_0)$ for each $z \in X$. So $x + X = y + X$.
3. In particular, the zero vector $0 + X$ of $V / X$ equals $x + X$ exactly when $x \in X$.
4. Let $U / W = \{u + W : u \in U\}$. It is a [[subspace|00YC1D652K]] of the [[quotient space|0BR3FY5Q8M]] $V / W$. It contains $0 + W$, and $(u + W) + a(u' + W) = (u + au') + W$ with $u + au' \in U$.
5. Let $\pi_U \colon V \to V / U$ be the [[quotient map|0N4F5FMQZW]], $\pi_U(v) = v + U$. It is a [[linear map|0NRYHJPQG2]] by the operations of $V / U$.
6. By step 3, the [[kernel|0S23E6YE83]] of $\pi_U$ is $U$, which contains $W$.
7. By the [[universal property of the quotient|0ZERJX6PH6]], there is a linear map $\varphi \colon V / W \to V / U$ with $\varphi(v + W) = v + U$ for all $v \in V$.
8. $\varphi$ is surjective, since each $v + U$ equals $\varphi(v + W)$. So the [[image|0WSFKKT6FF]] of $\varphi$ is $V / U$.
9. The kernel of $\varphi$ is $U / W$. If $u \in U$, then $\varphi(u + W) = u + U = 0 + U$ by step 3.
10. Conversely, let $\varphi(v + W) = 0 + U$. Then $v \in U$ by step 3, so $v + W \in U / W$.
11. By the [[first isomorphism theorem|0MTBGVZ4XJ]], the map $(V / W)/\ker \varphi \to \im \varphi$, $(v + W) + \ker \varphi \mapsto \varphi(v + W)$, is well defined and a linear isomorphism.
12. By steps 8 to 10, this is the map $(V / W)/(U / W) \to V / U$, $(v + W) + U/W \mapsto v + U$. So this map is well defined and a linear isomorphism.

## Idea

Since $W \subseteq U$, cosets of $W$ are finer than cosets of $U$, so each coset $v + W$ lies in a single coset $v + U$. This gives a surjective map $V / W \to V / U$. It sends $v + W$ to zero exactly when $v \in U$, so its kernel is $U / W$.
