---
tag: KB1JR1RAST
kind: proof
name: Proof that the order of a finite group is the index times the order of a subgroup
msc: [20D60]
proves: 04DC0SRN2K
uses: [G5S1M9, 0N0PXCTYA7, 05FD317V2W, 04QEBF8S49, 0DKMBWTD7P, 0SEX9F9J5Z]
sources:
  - url: https://proofwiki.org/wiki/Lagrange%27s_Theorem_(Group_Theory)
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Proof
---

## Proof

1. Let $G$ be a finite [[group|G5S1M9]] with identity $e$, and let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$.
2. Each $x \in G$ lies in its own [[left coset|05FD317V2W]] $xH$, since $x = xe$ and $e \in H$.
3. Claim: if two left cosets $xH$ and $yH$ have a common element, then $xH = yH$.
4. Let $z \in xH \cap yH$, so $z = xa = yb$ with $a, b \in H$. Then $y = xab^{-1}$.
5. For $h \in H$, $yh = x(ab^{-1}h)$, and $ab^{-1}h \in H$ because $H$ is a subgroup. So $yH \subseteq xH$.
6. Exchanging the roles of $x$ and $y$ gives $xH \subseteq yH$. So $xH = yH$, which proves the claim.
7. By steps 2 and 6, the distinct left cosets of $H$ are pairwise disjoint, and their union is $G$.
8. There are finitely many left cosets, since each is a subset of the finite set $G$. Let $C_1, \ldots, C_r$ be the distinct ones.
9. By the definition of the [[index|04QEBF8S49]], $r = [G : H]$.
10. Since [[cosets have the same cardinality as the subgroup|0DKMBWTD7P]], $\abs{C_i} = \abs{H}$ for each $i$.
11. By step 7, $\abs{G} = \abs{C_1} + \cdots + \abs{C_r} = r \abs{H}$. So the [[order|0SEX9F9J5Z]] of $G$ is $\abs{G} = [G : H] \cdot \abs{H}$.

## Idea

The left cosets of $H$ cut $G$ into disjoint pieces. Each piece is a copy of $H$ moved by a fixed element, so each has $\abs{H}$ elements. Counting the elements of $G$ piece by piece gives $[G : H]$ times $\abs{H}$.
