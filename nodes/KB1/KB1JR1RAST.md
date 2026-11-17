---
tag: KB1JR1RAST
kind: proof
name: Proof that the order of G equals the index times the order of H
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
proves: 04DC0SRN2K
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0DTXBQPA2S, 0DKMBWTD7P, 0B85S2V2DR, 0HTGB13FE2, 0GG9TVW90M, 0EBACQFAZW]
methods: [0NTF6DMVAP]
sources:
  - url: https://proofwiki.org/wiki/Lagrange%27s_Theorem_(Group_Theory)
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Proof
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.

First we show that two [[left cosets|03DEH43F4H]] are equal or disjoint.

1. Each $x \in G$ lies in its own left coset $xH$, since $x = xe$ and $e \in H$.
2. Let $z \in xH \cap yH$. Then $z = xa = yb$ with $a, b \in H$, so $y = xab^{-1}$.
3. For $h \in H$, we get $yh = x(ab^{-1}h)$. Here $ab^{-1}h \in H$, because $H$ is a subgroup. So $yH \subseteq xH$.
4. We exchange the roles of $x$ and $y$ and get $xH \subseteq yH$. Thus $xH = yH$.
5. By steps 1 to 4, the distinct left cosets are pairwise disjoint, and their union is $G$.

Part 1: $G$ is finite.

6. Each left coset is a subset of the finite set $G$, so there are finitely many distinct left cosets. Call them $C_1, \ldots, C_r$.
7. By the definition of the [[index|0DTXBQPA2S]], $r = [G : H]$.
8. By the [[lemma on the size of cosets|0DKMBWTD7P]], $|C_i| = |H|$ for each $i$.
9. By step 5, $|G| = |C_1| + \cdots + |C_r|$. By step 8, this sum is $r \cdot |H|$.
10. Thus $|G| = [G : H] \cdot |H|$, and $[G : H] = |G| / |H|$.

Part 2: $G$ is arbitrary.

11. By the [[axiom of choice|0HTGB13FE2]], choose a set $R \subseteq G$ that contains exactly one element of each left coset.
12. The map $r \mapsto rH$ from $R$ to $G/H$ is a [[bijection|0GG9TVW90M]], by the choice of $R$. Thus $|R| = [G : H]$.
13. Define $F \colon R \times H \to G$ by $F(r, h) = rh$.
14. The map $F$ is surjective. Let $x \in G$, and let $r$ be the element of $R$ in $xH$. Then $xH = rH$ by step 4, so $x = rh$ for some $h \in H$.
15. The map $F$ is injective. Let $rh = r'h'$. Then $rh$ lies in $rH$ and in $r'H$, so $rH = r'H$ by step 4.
16. The set $R$ meets each coset once, so $r = r'$. We cancel $r$ in $rh = rh'$ and get $h = h'$.
17. Thus $F$ is a bijection, and $|G| = |R \times H|$.
18. By the definition of the product of [[cardinal numbers|0EBACQFAZW]], $|R \times H| = |R| \cdot |H|$.
19. By steps 12, 17 and 18, $|G| = [G : H] \cdot |H|$ as cardinal numbers.

This proves both parts of the statement.

## Idea

The left cosets of $H$ cut $G$ into disjoint pieces, and each piece has $|H|$ elements.
For a finite group we add the sizes of the pieces.
For an infinite group we pick one representative in each piece, and each element of $G$ is then a unique product of a representative and an element of $H$.

## Variants

Part 1 is a special case of part 2, because for finite sets the product of cardinals is the ordinary product.
Part 1 needs no choice, since there are only finitely many cosets.
Another proof of part 1 uses the [[orbit-stabiliser theorem|0E2HSCKZ6C]] for the action of $G$ on $G/H$.
