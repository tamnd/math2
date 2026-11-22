---
tag: RJWXAX4ENN
kind: proof
name: Proof of the universal property of the quotient space
msc: [15A04]
topics: [QHKTJ89V6S]
audience: ug1
proves: 0ZERJX6PH6
uses: [0BR3FY5Q8M, 0N4F5FMQZW, 0NRYHJPQG2, 0S23E6YE83]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Theorem 3
---

## Proof

We define $\bar T$ on cosets through representatives, check that this makes sense and is linear, prove uniqueness, and then compute the kernel and the image.

1. For $x, y \in V$, we have $x + W = y + W$ if and only if $x - y \in W$.
   If $x + W = y + W$, then $x = x + 0 \in y + W$, so $x = y + w$ for some $w \in W$, and $x - y = w \in W$.
   Conversely, if $x - y = w_0 \in W$, then $x + w = y + (w_0 + w)$ and $y + w = x + (w - w_0)$ for each $w \in W$, so $x + W = y + W$.
2. Existence.
   We set $\bar T(v + W) = T(v)$ for $v \in V$, and we check that this does not depend on $v$.
   If $v + W = v' + W$, then $v - v' \in W$ by step 1.
3. Since $W \subseteq \ker T$, the [[kernel|0S23E6YE83]] of $T$, we get $T(v) - T(v') = T(v - v') = 0$.
   So $T(v) = T(v')$, and $\bar T$ is well defined.
4. The map $\bar T$ is additive, by the operations of the [[quotient space|0BR3FY5Q8M]] and the linearity of $T$:
   $$\bar T\bigl((u + W) + (v + W)\bigr) = \bar T\bigl((u + v) + W\bigr) = T(u + v) = T(u) + T(v).$$
5. The map $\bar T$ is homogeneous: for $a \in F$,
   $$\bar T\bigl(a(v + W)\bigr) = \bar T(av + W) = T(av) = a\, T(v).$$
   So $\bar T$ is a [[linear map|0NRYHJPQG2]].
6. For $v \in V$, the [[quotient map|0N4F5FMQZW]] gives $\pi(v) = v + W$.
   So $(\bar T \circ \pi)(v) = \bar T(v + W) = T(v)$, and $\bar T \circ \pi = T$.
7. Uniqueness.
   Let $S \colon V / W \to U$ be a linear map with $S \circ \pi = T$.
   Every element of $V / W$ has the form $v + W = \pi(v)$ for some $v \in V$, and for it
   $$S(v + W) = S(\pi(v)) = T(v) = \bar T(v + W).$$
   So $S = \bar T$.
8. The kernel.
   A coset $v + W$ lies in $\ker \bar T$ exactly when $T(v) = 0$, that is, when $v \in \ker T$.
   So $\ker \bar T$ is the set of cosets $v + W$ with $v \in \ker T$, which is the subspace $\ker T / W$ of $V / W$.
9. The image.
   The values of $\bar T$ are the values $T(v)$ for $v \in V$, so $\operatorname{im} \bar T = \operatorname{im} T$.

## Idea

A map on cosets is defined through representatives, so it makes sense only if all representatives of a coset give the same value.
Two representatives differ by an element of $W$, and $T$ sends that element to $0$, so they do give the same value.
Linearity is inherited from $T$, because the operations on cosets are the operations on representatives.
Uniqueness holds because the quotient map reaches every coset, so a map on $V / W$ is fixed by what it does after $\pi$.

## Variants

When $V$ is finite-dimensional, one can prove existence with a complement $C$ of $W$.
The map $C \to V / W$, $c \mapsto c + W$, is an isomorphism, and $\bar T$ is the inverse of this map followed by the restriction of $T$ to $C$.
This proof is less direct, since the definition of $\bar T$ then depends on the choice of $C$ until uniqueness shows that it does not.
