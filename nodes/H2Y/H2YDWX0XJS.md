---
tag: H2YDWX0XJS
kind: proof
name: Proof of the first isomorphism theorem for vector spaces
msc: [15A04, 16D10]
topics: [QHKTJ89V6S]
audience: ug1
proves: 0MTBGVZ4XJ
uses: [0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 00YC1D652K, 0BR3FY5Q8M, 0BJBYCGMWE, 0B8T10CE7N]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Theorem 2
---

## Proof

We check in turn that $\bar T$ is well defined, linear, surjective and injective.
Write $K = \ker T$ for the [[kernel|0S23E6YE83]] of the [[linear map|0NRYHJPQG2]] $T$.

1. The kernel $K$ is a [[subspace|00YC1D652K]] of $V$.
   It contains $0$, since $T(0) = 0$, and if $T(u) = T(v) = 0$ and $a \in F$, then $T(u + av) = T(u) + a T(v) = 0$.
2. The [[image|0WSFKKT6FF]] $\im T$ is a subspace of $W$.
   It contains $T(0) = 0$, and $T(u) + a T(v) = T(u + av)$ lies in it.
3. For $x, y \in V$, if $x + K = y + K$, then $x - y \in K$.
   Indeed $x = x + 0$ lies in $x + K = y + K$, so $x = y + k$ for some $k \in K$.
4. Conversely, if $x - y = k_0 \in K$, then $x + K = y + K$.
   For each $k \in K$ we have $x + k = y + (k_0 + k)$ and $y + k = x + (k - k_0)$, and $k_0 + k$ and $k - k_0$ lie in $K$.
5. The map $\bar T$ is well defined.
   If $v + K = v' + K$, then $v - v' \in K$ by step 3, so $T(v) - T(v') = T(v - v') = 0$.
   Hence $T(v) = T(v')$, and the value $\bar T(v + K) = T(v)$ does not depend on the representative.
6. Each value $T(v)$ lies in $\im T$, so $\bar T$ is a map from the [[quotient space|0BR3FY5Q8M]] $V / K$ to $\im T$.
7. The map $\bar T$ is additive.
   By the definition of addition in $V / K$ and the linearity of $T$,
   $$\bar T\big((u + K) + (v + K)\big) = \bar T\big((u + v) + K\big) = T(u + v) = T(u) + T(v) = \bar T(u + K) + \bar T(v + K).$$
8. The map $\bar T$ respects scalars.
   For $a \in F$,
   $$\bar T\big(a(v + K)\big) = \bar T(av + K) = T(av) = a\, T(v) = a\, \bar T(v + K).$$
9. The map $\bar T$ is surjective.
   Each element of $\im T$ is $T(v)$ for some $v \in V$, and $T(v) = \bar T(v + K)$.
10. The zero vector of $V / K$ is $0 + K$, since $(0 + K) + (v + K) = v + K$ for all $v \in V$.
11. The kernel of $\bar T$ is zero.
    If $\bar T(v + K) = 0$, then $T(v) = 0$, so $v - 0 \in K$, and step 4 gives $v + K = 0 + K$.
12. By [[the kernel criterion for injectivity|0BJBYCGMWE]], step 11 shows that $\bar T$ is injective.
13. By steps 7 to 12, $\bar T$ is a bijective linear map, that is, a [[linear isomorphism|0B8T10CE7N]] from $V / \ker T$ onto $\im T$.

## Idea

Two vectors have the same image under $T$ exactly when their difference lies in the kernel.
Read from left to right, this says that $T$ takes one value on each coset of the kernel, so $\bar T$ is well defined.
Read from right to left, it says that different cosets get different values, so $\bar T$ is injective.
Linearity comes for free from the way the operations on cosets are defined, and surjectivity onto the image holds by the definition of the image.

## Variants

The [[universal property of the quotient|0ZERJX6PH6]] gives a shorter route.
Since $T$ vanishes on $\ker T$, it factors as $T = \bar T \circ \pi$ through the quotient map $\pi \colon V \to V / \ker T$, and this settles well-definedness and linearity at once.
It then remains to check steps 9 to 12.
In finite dimension one can also argue by dimensions: once injectivity is known, the [[dimension of a quotient space|0SXDQ6TN00]] and the rank-nullity theorem, in its proof by extending a basis of the kernel, show that $V / \ker T$ and $\im T$ have the same dimension, so the injective map $\bar T$ is onto.
