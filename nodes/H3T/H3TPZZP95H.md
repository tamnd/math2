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

1. Let $K = \operatorname{im} f$. By exactness at $V$ in the [[short exact sequence|8MCYV0P04T]], $K = \ker g$.
2. By the [[existence of complements|0P9T8WHNMH]], $K$ has a [[complement|04C3BAHV03]] $C$, so $V = K \oplus C$.
3. Let $h = g|_C \colon C \to W$. Its kernel is $C \cap \ker g = C \cap K = \{0\}$, so $h$ is injective by [[injectivity and the kernel|0BJBYCGMWE]].
4. $h$ is surjective: for $w \in W$, pick $v$ with $g(v) = w$, since $g$ is surjective. Write $v = k + c$ with $k \in K$ and $c \in C$. Then $g(c) = g(v) - g(k) = w - 0 = w$.
5. So $h$ is an isomorphism. Let $s = \iota_C \circ h^{-1} \colon W \to V$, where $\iota_C$ is the inclusion of $C$. Then $g(s(w)) = h(h^{-1}(w)) = w$, so $g \circ s = \operatorname{id}_W$.
6. Let $\Phi \colon U \oplus W \to V$, $\Phi(u, w) = f(u) + s(w)$, on the [[external direct sum|02WZB422CE]]. It is linear, since $f$ and $s$ are.
7. $\Phi$ is injective: if $f(u) + s(w) = 0$, then applying $g$ gives $0 + w = 0$, so $w = 0$. Then $f(u) = 0$, and $u = 0$ since $f$ is injective.
8. $\Phi$ is surjective: for $v \in V$, the vector $v - s(g(v))$ satisfies $g(v - s(g(v))) = g(v) - g(v) = 0$. So it lies in $\ker g = \operatorname{im} f$, say $v - s(g(v)) = f(u)$. Then $v = \Phi(u, g(v))$.
9. So $\Phi$ is an isomorphism.
10. For the left inverse: define $r \colon V \to U$ by $r = \pi_U \circ \Phi^{-1}$, where $\pi_U(u, w) = u$. Then $r(f(u)) = \pi_U(u, 0) = u$.

## Idea

A complement of $\ker g$ is mapped isomorphically onto $W$ by $g$.
Inverting this isomorphism gives a section, and the section together with $f$ fills $V$ without overlap.

## Variants

- One can construct $s$ directly from a basis: choose a basis $(w_j)$ of $W$, pick $v_j$ with $g(v_j) = w_j$, and define $s(w_j) = v_j$. This uses that bases exist and that linear maps can be defined freely on a basis.
- For modules, the same argument shows that a short exact sequence splits whenever $\ker g$ has a complement, or whenever $W$ is a projective module.
