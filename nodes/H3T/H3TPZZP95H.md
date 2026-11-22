---
tag: H3TPZZP95H
kind: proof
name: Proof that short exact sequences of vector spaces split
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: grad
proves: 1GYTT98CC5
methods: [01XM7JEKHY]
uses: [0P9T8WHNMH, 04C3BAHV03, 0BJBYCGMWE, 8MCYV0P04T, 02WZB422CE]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_lemma
    locator: Proof
---

## Proof

We choose a complement of $\ker g$, show that $g$ maps it isomorphically onto $W$, and invert that isomorphism to get $s$.

1. Let $K = \operatorname{im} f$.
   By exactness at $V$ in the [[short exact sequence|8MCYV0P04T]], $K = \ker g$.
2. By the [[existence of complements|0P9T8WHNMH]], $K$ has a [[complement|04C3BAHV03]] $C$, so $V = K \oplus C$.
3. Let $h \colon C \to W$ be the restriction of $g$ to $C$.
   Its kernel is $C \cap \ker g = C \cap K = \{0\}$, so $h$ is injective, by [[injectivity and the kernel|0BJBYCGMWE]].
4. The map $h$ is onto.
   Given $w \in W$, pick $v \in V$ with $g(v) = w$, which exists because $g$ is onto, and write $v = k + c$ with $k \in K$ and $c \in C$.
   Then $h(c) = g(v) - g(k) = w - 0 = w$, since $g$ vanishes on $K = \ker g$.
5. So $h$ is an isomorphism.
   Let $\iota_C \colon C \to V$ be the inclusion, and put $s = \iota_C \circ h^{-1} \colon W \to V$.
   Then $g(s(w)) = h(h^{-1}(w)) = w$ for all $w$, so $g \circ s = \operatorname{id}_W$.
6. Now let $s$ be any linear map with $g \circ s = \operatorname{id}_W$, and define $\Phi \colon U \oplus W \to V$ on the [[external direct sum|02WZB422CE]] by $\Phi(u, w) = f(u) + s(w)$.
   It is linear, because $f$ and $s$ are linear.
7. The map $\Phi$ is injective.
   If $f(u) + s(w) = 0$, then applying $g$ gives $g(f(u)) + w = 0$, and $g(f(u)) = 0$ because $\operatorname{im} f = \ker g$, so $w = 0$.
   Then $f(u) = 0$, and $u = 0$ because $f$ is injective.
8. The map $\Phi$ is onto.
   For $v \in V$, the vector $v - s(g(v))$ satisfies $g\bigl(v - s(g(v))\bigr) = g(v) - g(v) = 0$.
   So it lies in $\ker g = \operatorname{im} f$, say $v - s(g(v)) = f(u)$, and then $v = \Phi(u, g(v))$.
9. So $\Phi$ is an isomorphism.
10. For the left inverse, let $\pi_U(u, w) = u$ and put $r = \pi_U \circ \Phi^{-1} \colon V \to U$.
    Then $r(f(u)) = \pi_U(\Phi^{-1}(\Phi(u, 0))) = \pi_U(u, 0) = u$, so $r \circ f = \operatorname{id}_U$.

## Idea

The map $g$ kills $\ker g$ and nothing else, so on a complement of $\ker g$ it is one-to-one, and it still reaches all of $W$.
Inverting $g$ on that complement gives a section $s$, a way to lift each vector of $W$ back into $V$.
Then every $v \in V$ splits as its lift $s(g(v))$ plus a remainder in $\ker g = \operatorname{im} f$, and that is the isomorphism with $U \oplus W$.

## Variants

One can build $s$ directly from a basis, without naming a complement.
Choose a basis $(w_j)_{j \in J}$ of $W$, pick $v_j \in V$ with $g(v_j) = w_j$, and let $s$ be the unique linear map with $s(w_j) = v_j$.
This uses that every vector space has a basis and that a linear map can be prescribed freely on a basis.
The span of the $v_j$ is then a complement of $\ker g$.

For modules over a ring the same argument shows that a short exact sequence splits whenever $\ker g$ has a complement, or whenever $W$ is a projective module.
