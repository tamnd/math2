---
tag: ACWQ5B20KG
kind: proof
name: Proof of the uniqueness of finite fields of a given order
msc: ["12E20"]
proves: 010PKCQPXP
uses: [08RTDHX1SK, 0H5WWC8RZX, 0VPFBAY7MW, 0ZMYX7GMH0, 0EBZ3G455G, 0GK1WB9R98, 0N5QW9K7MH, 06K7SARZKR, 0NFEG48RDR, 00X2A9G9W3, 0QWR8WTZEW, 0KJVQV3E0F, 0ZN39QDTP9]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Proof

We follow the source, but we build the isomorphism from a generator of $F^\times$. This avoids identifying the two prime subfields by hand.

1. Let $F$ and $F'$ be [[finite fields|08RTDHX1SK]] with $\abs{F} = \abs{F'} = q$. By the [[prime power theorem|0H5WWC8RZX]], $q = p^n$ and $q = p'^{n'}$, where $p$ and $p'$ are the characteristics.
2. By unique factorisation of $q$ into primes, $p = p'$ and $n = n'$.
3. Let $P$ and $P'$ be the [[prime subfields|0VPFBAY7MW]] of $F$ and $F'$. As in the prime power theorem, the maps $\Z \to P$, $k \mapsto k \cdot 1$, and $\Z \to P'$ are surjective ring homomorphisms with kernel $p\Z$.
4. By the [[first isomorphism theorem|0ZMYX7GMH0]], both $P$ and $P'$ are isomorphic to $\Z/p\Z$. So $\iota \colon P \to P'$, $k \cdot 1 \mapsto k \cdot 1$, is a ring isomorphism.
5. Applying $\iota$ to the coefficients gives a ring isomorphism $P[x] \to P'[x]$, written $g \mapsto g^\iota$. It preserves degrees and fixes $x^q - x$.
6. By the [[cyclicity of $F^\times$|0EBZ3G455G]], there is $\alpha \in F$ that generates $F^\times$. Every nonzero element of $F$ is a power of $\alpha$, so $F = P(\alpha)$.
7. Let $g$ be the [[minimal polynomial|0GK1WB9R98]] of $\alpha$ over $P$. Then $\deg g = [P(\alpha) : P] = [F : P] = n$, by the [[degree of a simple extension|0N5QW9K7MH]] and the prime power theorem.
8. Since $\alpha^q = \alpha$ by [[the equation $x^q = x$|0QWR8WTZEW]], the polynomial $g$ [[divides|06K7SARZKR]] $x^q - x$. Write $x^q - x = g h$ with $h \in P[x]$ of degree $q - n$.
9. Applying $\iota$ gives $x^q - x = g^\iota h^\iota$ in $P'[x]$. Every $b \in F'$ is a root of $x^q - x$ by the same result. So $g^\iota(b) h^\iota(b) = 0$ for each of the $q$ elements $b \in F'$.
10. The polynomial $h^\iota$ is nonzero of degree $q - n < q$, so it has [[fewer than $q$ roots|0KJVQV3E0F]] in $F'$. So $g^\iota(\beta) = 0$ for some $\beta \in F'$.
11. The polynomial $g$ is monic and [[irreducible|0NFEG48RDR]]. The isomorphism of step 5 preserves factorisations and degrees, so $g^\iota$ is monic and [[irreducible|00X2A9G9W3]] in $P'[x]$.
12. The minimal polynomial of $\beta$ over $P'$ divides $g^\iota$. By step 11 it equals $g^\iota$.
13. By the [[structure of simple extensions|0ZN39QDTP9]], $F = P(\alpha) \cong P[x]/(g)$ and $P'(\beta) \cong P'[x]/(g^\iota)$. The isomorphism of step 5 maps the ideal $(g)$ onto $(g^\iota)$, so it induces $P[x]/(g) \cong P'[x]/(g^\iota)$.
14. Composing, we get a ring isomorphism $\sigma \colon F \to P'(\beta)$. So $P'(\beta)$ has $q$ elements.
15. Since $P'(\beta) \subseteq F'$ and $\abs{F'} = q$, we get $P'(\beta) = F'$. So $\sigma$ is an isomorphism from $F$ onto $F'$.

## Idea

Both fields are generated over their copy of $\F_p$ by a single element. The minimal polynomial of a generator of $F$ divides $x^q - x$, and $x^q - x$ vanishes on all of $F'$. So that polynomial also has a root in $F'$, and the two simple extensions it defines are isomorphic.
