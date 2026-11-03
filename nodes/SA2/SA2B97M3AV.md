---
tag: SA2B97M3AV
kind: proof
name: Proof that cyclic groups of the same order are isomorphic
msc: [20A05]
proves: 0736AXH2ME
uses: [0B85Q41RP6, 0YT586TKXF, 0SEX9F9J5Z, 0JPYSD5E0B, 031M8HX7DA, 0F5QC101Q7, 00DRK90Z6K, 085PND4KNT]
sources:
  - url: https://proofwiki.org/wiki/Cyclic_Groups_of_Same_Order_are_Isomorphic
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Section 4
---

## Proof

1. Let $G$ and $H$ be [[cyclic groups|0B85Q41RP6]] of the same [[order|0SEX9F9J5Z]]. Let $g$ generate $G$ and $h$ generate $H$. Write $e$ for the identity of each group.
2. So $G = \langle g \rangle = \set{g^k : k \in \Z}$ and $H = \set{h^k : k \in \Z}$, by the definition of the [[cyclic subgroup|0YT586TKXF]].
3. By [[the order of a cyclic subgroup|031M8HX7DA]], $g$ has finite [[order|0JPYSD5E0B]] $n$ exactly when $G$ is finite, and then $|G| = n$. The same holds for $h$ and $H$.
4. Since $|G| = |H|$, there are two cases. Either $g$ and $h$ both have the same finite order $n$, or both have infinite order.
5. Claim: for all $a, b \in \Z$, $g^a = g^b$ if and only if $h^a = h^b$.
6. By the [[laws of exponents|00DRK90Z6K]], $g^a = g^{a-b}g^b$. So $g^a = g^b$ if and only if $g^{a-b} = e$, by cancelling $g^b$ on the right. The same holds for $h$.
7. In the finite case, $g^{a-b} = e$ if and only if $n$ divides $a - b$, by [[the divisibility criterion for powers|0F5QC101Q7]]. The same holds for $h$, so the claim follows.
8. In the infinite case, the powers $g^k$ for $k \in \Z$ are distinct, by the order of a cyclic subgroup. So $g^a = g^b$ if and only if $a = b$. The same holds for $h$, so the claim follows.
9. Define $\varphi \colon G \to H$ by $\varphi(g^k) = h^k$. By the "only if" part of step 5, $\varphi(x)$ does not depend on the choice of $k$ with $x = g^k$.
10. By the "if" part of step 5, $h^a = h^b$ implies $g^a = g^b$. So $\varphi$ is injective.
11. Each element of $H$ is $h^k = \varphi(g^k)$ for some $k$. So $\varphi$ is surjective.
12. Let $x = g^a$ and $y = g^b$. By the laws of exponents, $xy = g^{a+b}$. So $\varphi(xy) = h^{a+b} = h^a h^b = \varphi(x)\varphi(y)$.
13. So $\varphi$ is a bijection that preserves products, a [[group isomorphism|085PND4KNT]]. Hence $G$ and $H$ are isomorphic.

## Idea

Each element of a cyclic group is a power of the generator. The only question is when two exponents give the same element, and this depends only on the order of the group. So "send $g^k$ to $h^k$" is a well-defined bijection, and it preserves products because exponents add.
