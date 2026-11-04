---
tag: EJEPE0FWVK
kind: proof
name: Proof of the second isomorphism theorem for vector spaces
msc: [15A03, 16D10]
proves: 0APN65D6Y6
uses: [0MTBGVZ4XJ, 0V33SPH7RR, 0JMTY8MF54, 0BR3FY5Q8M, 0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 00YC1D652K]
sources:
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Proof

We apply the first isomorphism theorem to the map $U \to (U + W)/W$ that sends $u$ to its coset.

1. The [[sum|0JMTY8MF54]] $U + W$ is a [[subspace|00YC1D652K]] of $V$ that contains $W$. Indeed $0 = 0 + 0$, and $(u + w) + a(u' + w') = (u + au') + (w + aw')$. Each $w \in W$ equals $0 + w \in U + W$.
2. By [[the intersection of subspaces|0V33SPH7RR]], $U \cap W$ is a subspace of $U$. So both [[quotient spaces|0BR3FY5Q8M]] $U / (U \cap W)$ and $(U + W)/W$ are defined.
3. For $x, y \in U + W$, we have $x + W = y + W$ if and only if $x - y \in W$. If $x + W = y + W$, then $x = x + 0 \in y + W$, so $x - y \in W$.
4. Conversely, if $x - y = w_0 \in W$, then $x + w = y + (w_0 + w)$ and $y + w = x + (w - w_0)$ for each $w \in W$. So $x + W = y + W$.
5. Define $\varphi \colon U \to (U + W)/W$ by $\varphi(u) = u + W$. By the operations of the quotient, $\varphi(u + au') = (u + W) + a(u' + W)$, so $\varphi$ is a [[linear map|0NRYHJPQG2]].
6. $\varphi$ is surjective. Let $(u + w) + W$ be an element of $(U + W)/W$, with $u \in U$ and $w \in W$. Since $(u + w) - u = w \in W$, step 4 gives $(u + w) + W = u + W = \varphi(u)$.
7. The zero vector of $(U + W)/W$ is $0 + W$. By steps 3 and 4, $\varphi(u) = 0 + W$ if and only if $u \in W$.
8. So the [[kernel|0S23E6YE83]] of $\varphi$ is $\{u \in U : u \in W\} = U \cap W$. By step 6, the [[image|0WSFKKT6FF]] of $\varphi$ is $(U + W)/W$.
9. By the [[first isomorphism theorem|0MTBGVZ4XJ]], the map $U / \ker \varphi \to \im \varphi$, $u + \ker \varphi \mapsto \varphi(u)$, is well defined and a linear isomorphism.
10. By step 8, this is the map $U / (U \cap W) \to (U + W)/W$, $u + (U \cap W) \mapsto u + W$. So this map is well defined and a linear isomorphism.

## Idea

Every coset in $(U + W)/W$ already has a representative in $U$, because the $W$ part can be dropped. Two vectors of $U$ give the same coset exactly when their difference lies in $U \cap W$. The first isomorphism theorem turns these two facts into the isomorphism.
