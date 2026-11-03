---
tag: GN6WHHGBAE
kind: proof
name: Proof of Extension of Lagrange's theorem
msc: [20D60]
proves: VAF6B01Q8W
sources:
  - wikipedia: en:31150@r1321322691
    locator: Lagrange's theorem (group theory), section Extension
    note: adopted
    mention: wikipedia://en/31150#DANC
    sections: [Proof]
---

## Proof

Let $S$ be a set of coset representatives for $K$ in $H$, so $H = \bigsqcup_{s \in S} sK$ (disjoint union), and $|S|=[H:K]$. For any $a \in G$, left-multiplication-by-$a$ is a bijection $G \to G$, so $aH = \bigsqcup_{s \in S} asK$. Thus each left coset of $H$ decomposes into $[H:K]$ left cosets of $K$. Since $G$ decomposes into $[G:H]$ left cosets of $H$, each of which decomposes into $[H:K]$ left cosets of $K$, the total number $[G:K]$ of left cosets of $K$ in $G$ is $[G:H][H:K]$.
