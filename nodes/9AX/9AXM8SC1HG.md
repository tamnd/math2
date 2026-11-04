---
tag: 9AXM8SC1HG
kind: proof
name: Proof of the third isomorphism theorem
msc: [20A05]
proves: 0TJ1V9DDPC
uses: [0W77CVBCHQ, 0YYWCNTPWR, 05FD317V2W, 0HV9Y7WG5R, 0Z424HK8CQ, 0C9ZKYSPYR, 0CXXJNG5B6]
sources:
  - url: https://proofwiki.org/wiki/Third_Isomorphism_Theorem/Groups
    locator: Proof 1
---

## Proof

We apply the first isomorphism theorem to the map $G/N \to G/K$, $gN \mapsto gK$.

1. Let $G$ be a group with identity $e$, and let $N \subseteq K$ be [[normal subgroups|0W77CVBCHQ]] of $G$. Both [[quotient groups|0YYWCNTPWR]] $G/N$ and $G/K$ exist.
2. Since $N \subseteq K$ and $N$ is normal in $G$, $N$ is normal in $K$. So $K/N = \{kN : k \in K\}$ is a subset of $G/N$.
3. We record a fact on [[left cosets|05FD317V2W]]. For $a \in G$, $aK = K$ holds exactly when $a \in K$.
4. Proof of step 3. If $aK = K$, then $a = ae \in K$. If $a \in K$, then $aK \subseteq K$ by closure, and each $m \in K$ equals $a(a^{-1}m) \in aK$.
5. Let $g, g' \in G$ with $gN = g'N$. Then $g' = g'e \in gN$, so $g' = gn$ with $n \in N \subseteq K$.
6. By step 4, $nK = K$. So $g'K = (gK)(nK) = (gK)K = gK$, using the operation of $G/K$ and that $K$ is its identity.
7. By steps 5 and 6, the formula $f(gN) = gK$ defines a map $f \colon G/N \to G/K$.
8. For $a, b \in G$, $f((aN)(bN)) = f((ab)N) = (ab)K = (aK)(bK) = f(aN) f(bN)$. So $f$ is a [[group homomorphism|0HV9Y7WG5R]].
9. Each element $gK$ of $G/K$ equals $f(gN)$. So $f$ is surjective.
10. Let $gN \in G/N$. By step 3, $f(gN) = K$ exactly when $g \in K$. So the [[kernel|0Z424HK8CQ]] of $f$ is the set of cosets $gN$ with $g \in K$.
11. A coset $gN$ with $g \in K$ lies in $K/N$. Conversely, each element $kN$ of $K/N$ has $k \in K$. So $\ker f = K/N$.
12. By [[the kernel is a normal subgroup|0C9ZKYSPYR]] and step 11, $K/N$ is a normal subgroup of $G/N$.
13. By the [[first isomorphism theorem|0CXXJNG5B6]], the map $(gN)(K/N) \mapsto f(gN) = gK$ is an isomorphism from $(G/N)/(K/N)$ onto $\operatorname{im} f$.
14. By step 9, $\operatorname{im} f = G/K$. Together with step 12, this proves the statement.

## Idea

Since $N$ lies in $K$, each coset of $N$ lies in one coset of $K$, so $gN \mapsto gK$ is well defined. This map is onto, and it kills exactly the cosets of $N$ that lie inside $K$, namely $K/N$. The first isomorphism theorem does the rest.
