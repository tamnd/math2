---
tag: RJWXAX4ENN
kind: proof
name: Proof of the universal property of the quotient space
msc: [15A04]
proves: 0ZERJX6PH6
uses: [0BR3FY5Q8M, 0N4F5FMQZW, 0NRYHJPQG2, 0S23E6YE83]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Theorem 3
---

## Proof

We define $\bar T$ on cosets, check that this makes sense, and then prove uniqueness.

1. For $x, y \in V$, we have $x + W = y + W$ if and only if $x - y \in W$. If $x + W = y + W$, then $x = x + 0 \in y + W$, so $x - y \in W$.
2. Conversely, if $x - y = w_0 \in W$, then $x + w = y + (w_0 + w)$ and $y + w = x + (w - w_0)$ for each $w \in W$. So $x + W = y + W$.
3. Existence. Define $\bar T(v + W) = T(v)$ for $v \in V$. This is well defined: if $v + W = v' + W$, then $v - v' \in W$ by step 1.
4. Since $W \subseteq \ker T$, the [[kernel|0S23E6YE83]], we get $T(v) - T(v') = T(v - v') = 0$. So $T(v) = T(v')$.
5. $\bar T$ is additive. By the operations of the [[quotient space|0BR3FY5Q8M]], $\bar T((u + W) + (v + W)) = \bar T((u + v) + W) = T(u + v) = T(u) + T(v)$.
6. $\bar T$ is homogeneous. For $a \in F$, $\bar T(a(v + W)) = \bar T(av + W) = T(av) = a\, T(v)$. So $\bar T$ is a [[linear map|0NRYHJPQG2]].
7. For $v \in V$, the [[quotient map|0N4F5FMQZW]] gives $\pi(v) = v + W$. So $(\bar T \circ \pi)(v) = \bar T(v + W) = T(v)$, and $\bar T \circ \pi = T$.
8. Uniqueness. Let $S \colon V / W \to U$ be a linear map with $S \circ \pi = T$.
9. Every element of $V / W$ has the form $v + W = \pi(v)$ for some $v \in V$. For it, $S(v + W) = S(\pi(v)) = T(v) = \bar T(v + W)$.
10. So $S = \bar T$. Hence $\bar T$ is the only linear map with $\bar T \circ \pi = T$, and it is given by $\bar T(v + W) = T(v)$.

## Idea

A map on cosets is defined through representatives, so it only makes sense if all representatives of a coset give the same value. They differ by elements of $W$, which $T$ sends to $0$. Uniqueness holds because the quotient map hits every coset.
