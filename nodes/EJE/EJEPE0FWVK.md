---
tag: EJEPE0FWVK
kind: proof
name: Proof of the second isomorphism theorem for vector spaces
msc: [15A03, 16D10]
topics: [QHKTJ89V6S]
audience: ug1
proves: 0APN65D6Y6
uses: [0MTBGVZ4XJ, 0V33SPH7RR, 0JMTY8MF54, 0BR3FY5Q8M, 0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 00YC1D652K]
sources:
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Proof

We apply the first isomorphism theorem to the map $U \to (U + W) / W$ that sends each $u$ to its coset.

1. The [[sum|0JMTY8MF54]] $U + W$ is a [[subspace|00YC1D652K]] of $V$ that contains $W$.
   It contains $0 = 0 + 0$, and it is closed under the operations, since $(u + w) + a(u' + w') = (u + au') + (w + aw')$.
   Each $w \in W$ equals $0 + w$, so $W \subseteq U + W$.
2. The [[intersection|0V33SPH7RR]] $U \cap W$ is a subspace of $U$.
   So both [[quotient spaces|0BR3FY5Q8M]] $U / (U \cap W)$ and $(U + W) / W$ are defined.
3. For $x, y \in U + W$, we have $x + W = y + W$ if and only if $x - y \in W$.
   If $x + W = y + W$, then $x = x + 0$ lies in $y + W$, so $x - y \in W$.
   If $x - y = w_0 \in W$, then $x + w = y + (w_0 + w)$ and $y + w = x + (w - w_0)$ for each $w \in W$, so the two cosets agree.
4. Define $\varphi \colon U \to (U + W) / W$ by $\varphi(u) = u + W$.
   By the definition of the operations on cosets, $\varphi(u + au') = (u + W) + a(u' + W) = \varphi(u) + a \varphi(u')$, so $\varphi$ is a [[linear map|0NRYHJPQG2]].
5. The map $\varphi$ is surjective.
   An element of $(U + W) / W$ has the form $(u + w) + W$ with $u \in U$ and $w \in W$.
   Since $(u + w) - u = w$ lies in $W$, step 3 gives $(u + w) + W = u + W = \varphi(u)$.
6. The zero vector of $(U + W) / W$ is $0 + W$, and step 3 shows that $\varphi(u) = 0 + W$ if and only if $u \in W$.
7. So the [[kernel|0S23E6YE83]] of $\varphi$ is $\{u \in U : u \in W\} = U \cap W$, and by step 5 the [[image|0WSFKKT6FF]] of $\varphi$ is all of $(U + W) / W$.
8. By the [[first isomorphism theorem|0MTBGVZ4XJ]], the map $U / \ker \varphi \to \im \varphi$, $u + \ker \varphi \mapsto \varphi(u)$, is well defined and is a linear isomorphism.
9. By step 7, this is the map $U / (U \cap W) \to (U + W) / W$, $u + (U \cap W) \mapsto u + W$.
   So this map is well defined and is a linear isomorphism, which is the statement.

## Idea

The proof rests on two observations.
First, every coset in $(U + W) / W$ already has a representative in $U$, because the $W$ part of $u + w$ can be dropped.
Second, two vectors of $U$ give the same coset of $W$ exactly when their difference lies in $W$, and so in $U \cap W$.
The first observation says that the map $u \mapsto u + W$ is onto, the second says that its kernel is $U \cap W$, and the first isomorphism theorem does the rest.

## Variants

One can also check the four properties of the map $u + (U \cap W) \mapsto u + W$ by hand, without the first isomorphism theorem.
It is well defined and injective because $u - u' \in U \cap W$ holds exactly when $u - u' \in W$, for $u, u' \in U$.
It is linear because the operations on both sides are computed on representatives, and it is onto by step 5.
In finite dimension, a third route compares dimensions: once the map is known to be injective, Grassmann's formula, proved by extending a basis of $U \cap W$, shows that both sides have dimension $\dim U - \dim (U \cap W)$.
