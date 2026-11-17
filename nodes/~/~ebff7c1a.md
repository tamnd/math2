---
tag: ~ebff7c1a
kind: proof
name: Proof of Poincaré's theorem on subgroups of finite index
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug2
proves: ~e932864a
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0DTXBQPA2S, 0ZTGMDNVTB, 0AZG100DKH, 0JYTG5K9Y4, 0W88CEGQP1, 0C9ZKYSPYR, 0CXXJNG5B6, 0PCKBBMEXC, 3C53TD, 0ZQJ7KEFQ5]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Finite index
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H$ and $K$ be [[subgroups|0X1JXT47GA]] of $G$.
For a subgroup $L$, let $G/L$ be the set of [[left cosets|03DEH43F4H]] of $L$, so that $[G : L] = |G/L|$ is the [[index|0DTXBQPA2S]].
We use the coset criterion: $aL = bL$ if and only if $a^{-1}b \in L$.

Part 1.
Assume that $[G : H]$ and $[G : K]$ are finite.

1. Let $I = H \cap K$. It is a subgroup of $G$, because the [[intersection of subgroups is a subgroup|0ZTGMDNVTB]].
2. Define $\varphi \colon G/I \to G/H \times G/K$ by $\varphi(gI) = (gH, gK)$.
3. The map $\varphi$ is well defined. If $gI = g'I$, then $g^{-1}g' \in I$ by the coset criterion.
4. Then $g^{-1}g' \in H$ and $g^{-1}g' \in K$, because $I \subseteq H$ and $I \subseteq K$. Thus $gH = g'H$ and $gK = g'K$.
5. The map $\varphi$ is injective. Assume that $gH = g'H$ and $gK = g'K$.
6. By the coset criterion, $g^{-1}g' \in H$ and $g^{-1}g' \in K$. Thus $g^{-1}g' \in I$, and $gI = g'I$.
7. An injective map into a finite set has a finite domain of at most the same size.
8. Thus $[G : I] = |G/I| \le |G/H| \cdot |G/K| = [G : H] \cdot [G : K]$.

Part 2.
Assume that $[G : H] = n$ is finite, and let $X = G/H$.

9. For $g \in G$, define $\lambda_g \colon X \to X$ by $\lambda_g(aH) = gaH$.
10. The map $\lambda_g$ is well defined. If $aH = bH$, then $(ga)^{-1}(gb) = a^{-1}b \in H$, so $gaH = gbH$.
11. For $g, g' \in G$, we have $\lambda_g(\lambda_{g'}(aH)) = gg'aH = \lambda_{gg'}(aH)$. Also $\lambda_e$ is the identity map of $X$.
12. By step 11, $\lambda_{g^{-1}}$ is the inverse map of $\lambda_g$. Thus $\lambda_g$ is a permutation of $X$.
13. By steps 11 and 12, $\lambda \colon G \to \operatorname{Sym}(X)$, $g \mapsto \lambda_g$, is a [[group homomorphism|0JYTG5K9Y4]]. This is the [[action on left cosets|0AZG100DKH]].
14. The set $X$ has $n$ elements, so $\operatorname{Sym}(X)$ has [[order $n!$|0PCKBBMEXC]].
15. Let $N$ be the [[kernel|0W88CEGQP1]] of $\lambda$. It is a normal subgroup of $G$, because [[each kernel is normal|0C9ZKYSPYR]].
16. The subgroup $N$ is contained in $H$. If $g \in N$, then $gH = \lambda_g(H) = H$, so $g \in H$ by the coset criterion.
17. The subgroup $N$ is the core of $H$. Indeed, $g \in N$ means $gaH = aH$ for each $a \in G$.
18. By the coset criterion, this means $a^{-1}ga \in H$ for each $a$, that is, $g \in aHa^{-1}$ for each $a$.
19. By the [[first isomorphism theorem|0CXXJNG5B6]], the quotient group $G/N$ is isomorphic to the image $\lambda(G)$.
20. The image $\lambda(G)$ is a subgroup of $\operatorname{Sym}(X)$. Thus $[G : N] = |G/N| = |\lambda(G)|$ is finite.
21. By [[Lagrange's theorem|3C53TD]] for $\operatorname{Sym}(X)$, the order $|\lambda(G)|$ divides $n!$. Thus $[G : N]$ divides $n!$.
22. By the [[tower law|0ZQJ7KEFQ5]] for $N \le H \le G$, we have $[G : N] = [G : H] \cdot [H : N] = n \cdot [H : N]$.
23. Here $[H : N]$ is finite, because $[G : N]$ is finite. Thus $n$ divides $[G : N]$.

This proves both parts of Poincaré's theorem.

## Idea

For part 1, a coset of $H \cap K$ is fixed by the pair of cosets of $H$ and of $K$ that contain it.
Thus the cosets of $H \cap K$ inject into the pairs, and there are at most $[G : H] \cdot [G : K]$ of them.
For part 2, the group permutes the $n$ cosets of $H$.
The elements that fix every coset form a normal subgroup inside $H$, and the quotient by it is a group of permutations of $n$ objects.

## Variants

Part 1 also follows from the [[orbit-stabiliser theorem|0E2HSCKZ6C]].
The group $G$ acts on $G/H \times G/K$, and the stabiliser of the point $(H, K)$ is $H \cap K$.
Thus $[G : H \cap K]$ is the size of the orbit of $(H, K)$, which is at most $[G : H] \cdot [G : K]$.
Part 1 for $n$ subgroups of finite index follows by induction, with the bound $\prod_i [G : H_i]$.
