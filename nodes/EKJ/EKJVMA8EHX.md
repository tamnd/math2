---
tag: EKJVMA8EHX
kind: proof
name: Proof that the number of conjugates of a subgroup is the index of its normaliser
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
proves: PVQC3S10D2
uses: [0YGN3VAA0D, 0H11ZPX4ND, 03DEH43F4H, 0DTXBQPA2S, 0GG9TVW90M]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy of subgroups and general subsets
---

## Proof

Let $G$ be a group, let $H \le G$, and write $N = N_G(H)$ for the [[normaliser|0YGN3VAA0D]] of $H$.
For $g \in G$, write $c_g(x) = gxg^{-1}$, and $c_g(S) = gSg^{-1}$ for a subset $S$ of $G$.

1. $c_k(c_g(x)) = kgxg^{-1}k^{-1} = c_{kg}(x)$ for all $k, g, x \in G$. So $c_k \circ c_g = c_{kg}$, also on subsets.
2. $c_e$ is the identity map, so $c_{g^{-1}} \circ c_g = c_e$ by step 1. So $c_g$ is a bijection of $G$ with inverse $c_{g^{-1}}$.
3. $N$ is a subgroup of $G$. It contains $e$, because $c_e$ is the identity map.
4. If $g, k \in N$, then $c_{gk}(H) = c_g(c_k(H)) = c_g(H) = H$, by step 1. So $gk \in N$.
5. If $g \in N$, then $c_{g^{-1}}(H) = c_{g^{-1}}(c_g(H)) = c_e(H) = H$, by step 1. So $g^{-1} \in N$.
6. Let $g, k \in G$. Apply the bijection $c_{k^{-1}}$ of step 2 to both sides of $gHg^{-1} = kHk^{-1}$.
7. By step 1, $gHg^{-1} = kHk^{-1}$ holds exactly when $c_{k^{-1}g}(H) = H$, that is, when $k^{-1}g \in N$.
8. If $k^{-1}g = n \in N$, then $g = kn$ and $gN = k(nN) = kN$, because $nN = N$ for $n$ in the subgroup $N$.
9. If $gN = kN$, then $g = ge \in kN$, so $g = kn$ with $n \in N$, and $k^{-1}g = n \in N$.
10. By steps 7, 8 and 9, $gHg^{-1} = kHk^{-1}$ holds exactly when $gN = kN$.
11. Define $\Phi(gN) = gHg^{-1}$ on the [[left cosets|03DEH43F4H]] of $N$. The direction "if" of step 10 shows that $\Phi$ is well defined.
12. The direction "only if" of step 10 shows that $\Phi$ is injective.
13. Each [[conjugate subgroup|0H11ZPX4ND]] of $H$ has the form $gHg^{-1} = \Phi(gN)$. So $\Phi$ is surjective.
14. So $\Phi$ is a [[bijection|0GG9TVW90M]] from the left cosets of $N$ to the conjugates of $H$.
15. The number of left cosets of $N$ is the [[index|0DTXBQPA2S]] $[G : N]$. So $H$ has exactly $[G : N]$ conjugates.

## Idea

Two elements $g$ and $k$ move $H$ to the same place exactly when $k^{-1}g$ does not move $H$ at all.
The elements that do not move $H$ form the normaliser.
So the conjugates of $H$ correspond to the cosets of the normaliser.

## Variants

The proof is the orbit-stabiliser theorem for the action of $G$ on its subgroups by conjugation.
With the [[orbit-stabiliser theorem|0E2HSCKZ6C]] as a known result, steps 6 to 15 reduce to one line: the orbit of $H$ is the set of its conjugates, and the stabiliser is $N$.
