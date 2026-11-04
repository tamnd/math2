---
tag: H2YDWX0XJS
kind: proof
name: Proof of the first isomorphism theorem for linear maps
msc: [15A04, 16D10]
proves: 0MTBGVZ4XJ
uses: [0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 00YC1D652K, 0BR3FY5Q8M, 0BJBYCGMWE, 0B8T10CE7N]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Theorem 2
---

## Proof

We check in turn that $\bar T$ is well defined, linear, injective and surjective.

1. Let $K = \ker T$, the [[kernel|0S23E6YE83]] of the [[linear map|0NRYHJPQG2]] $T$. It is a [[subspace|00YC1D652K]] of $V$: $T(0) = 0$, and $T(u) = T(v) = 0$ gives $T(u + av) = 0$ for $a \in F$.
2. The [[image|0WSFKKT6FF]] $\im T$ is a subspace of $W$: it contains $T(0) = 0$, and $T(u) + a T(v) = T(u + av)$ lies in it.
3. For $x, y \in V$, we have $x + K = y + K$ if and only if $x - y \in K$. If $x + K = y + K$, then $x = x + 0 \in y + K$, so $x - y \in K$.
4. Conversely, if $x - y = k_0 \in K$, then $x + k = y + (k_0 + k)$ and $y + k = x + (k - k_0)$ for each $k \in K$. So $x + K = y + K$.
5. $\bar T$ is well defined. If $v + K = v' + K$, then $v - v' \in K$ by step 3, so $T(v) - T(v') = T(v - v') = 0$. Thus $T(v) = T(v')$.
6. Each value $T(v)$ lies in $\im T$, so $\bar T$ is a map from the [[quotient space|0BR3FY5Q8M]] $V / K$ to $\im T$.
7. $\bar T$ is linear. By the operations of $V / K$, $\bar T((u + K) + (v + K)) = \bar T((u + v) + K) = T(u + v) = T(u) + T(v)$. The last sum is $\bar T(u + K) + \bar T(v + K)$.
8. Likewise, for $a \in F$, $\bar T(a(v + K)) = \bar T(av + K) = T(av) = a\, T(v) = a\, \bar T(v + K)$.
9. $\bar T$ is surjective. Each element of $\im T$ is $T(v)$ for some $v \in V$, and $T(v) = \bar T(v + K)$.
10. The zero vector of $V / K$ is $0 + K$, since $(0 + K) + (v + K) = v + K$ for all $v \in V$.
11. $\bar T$ has trivial kernel. If $\bar T(v + K) = 0$, then $T(v) = 0$, so $v - 0 \in K$. By step 4, $v + K = 0 + K$.
12. By [[the kernel criterion|0BJBYCGMWE]], $\bar T$ is injective.
13. By steps 7 to 12, $\bar T$ is a bijective linear map, that is, a [[linear isomorphism|0B8T10CE7N]] from $V / \ker T$ onto $\im T$.

## Idea

Two vectors have the same image under $T$ exactly when they differ by an element of the kernel. So $T$ gives a well-defined map on cosets of the kernel, and this map can no longer merge distinct cosets. Its image is the image of $T$.
