---
tag: 1Q99SE2FDY
kind: proof
name: Proof of the extension property for partial automorphisms of finite graphs
msc: ["03C15", "05C25"]
topics: [ZS8X8KS54R]
audience: research
proves: TA9KGWV9NM
uses: [00C0BR7D7H, 0EREPBVG2G, DSQ17TNW1C, 0F7QKGJS6B]
methods: [01XM7JEKHY, 0NTF6DMVAP]
sources:
  - book: isbn:9780521587136
---

## Proof

We give an explicit [[construction|01XM7JEKHY]].
Let $G$ have vertex set $V$ with $\lvert V \rvert = n$, and fix a linear order on $V$.
All arithmetic on labels is modulo $2$.

### The graph $H$

1. A vertex of $H$ is a pair $(a, f)$ with $a \in V$ and $f \colon V \setminus \set{a} \to \set{0, 1}$.
2. Join $(a, f)$ and $(b, g)$ when $a \ne b$ and $f(b) + g(a) = 1$.
3. The condition is symmetric in the two pairs, so $H$ is a [[graph|00C0BR7D7H]] with $n 2^{n-1}$ vertices.

### Two kinds of automorphisms

4. For a permutation $\sigma$ of $V$, let $\alpha_\sigma(a, f) = (\sigma a, f \circ \sigma^{-1})$.
5. Then $f \circ \sigma^{-1}(\sigma b) + g \circ \sigma^{-1}(\sigma a) = f(b) + g(a)$, so $\alpha_\sigma$ is an [[automorphism|DSQ17TNW1C]].
6. For a map $t$ from $2$-subsets of $V$ to $\set{0, 1}$, let $\tau_t(a, f) = (a, f')$ with $f'(b) = f(b) + t(\set{a, b})$.
7. Then $f'(b) + g'(a) = f(b) + g(a) + 2 t(\set{a, b}) = f(b) + g(a)$, so $\tau_t$ is an automorphism.

### The embedding of $G$

8. For $v \in V$, let $f_v(w) = 1$ if $v < w$ and $v \sim w$ in $G$, and $f_v(w) = 0$ otherwise.
9. Let $e(v) = (v, f_v)$. For $v < w$, $f_v(w) + f_w(v) = f_v(w)$, which is $1$ exactly when $v \sim w$.
10. So $e$ is an isomorphism of $G$ onto an [[induced subgraph|0EREPBVG2G]] of $H$.

### Extending a partial isomorphism

11. Let $p \colon A \to B$ be an [[isomorphism|0F7QKGJS6B]] of induced subgraphs of $G$, and extend $p$ to a permutation $\sigma$ of $V$.
12. Then $\alpha_\sigma(e(a)) = (p(a), f_a \circ \sigma^{-1})$ for $a \in A$.
13. For $a \in A$ and $y \ne p(a)$, set $t(\set{p(a), y}) = f_{p(a)}(y) + f_a(\sigma^{-1} y)$. Set $t = 0$ on pairs disjoint from $B$.
14. If $y = p(a')$ with $a' \in A$, the pair $\set{p(a), p(a')}$ gets two definitions. Their sum is $[p(a) \sim p(a')] + [a \sim a']$ by step 9.
15. This sum is $0$ because $p$ preserves edges, so the two definitions agree and $t$ is well defined.
16. By step 13, $\tau_t(\alpha_\sigma(e(a))) = (p(a), f_{p(a)}) = e(p(a))$ for every $a \in A$.
17. So $\tau_t \circ \alpha_\sigma$ is an automorphism of $H$ extending $p$, and $H$ works for all $p$ at once.

## Idea

Each vertex of $H$ carries a label for every potential neighbor, and adjacency is the parity of two labels.
Permuting $V$ moves vertices, and flipping both labels on a pair keeps the parity, so the edge relation is preserved.
The partial isomorphism fixes the parity on pairs inside $B$, which is exactly the consistency needed to choose the flips.

## Variants

Hrushovski's original argument and the later proofs by Herwig and by Herwig and Lascar use different constructions, which extend to other relational classes.
The construction above uses that graphs have a single binary symmetric relation, so that adjacency can be coded by a parity.
