---
tag: MRH07WB74D
kind: proof
name: Proof that the number of Sylow subgroups divides the index
msc: [20D20]
proves: 0M3PYJ3TSE
uses: [0JWZX6FKSH, 0AT1ZSNM25, 09ZJ6CAK7S, 04DC0SRN2K, 04QEBF8S49]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Proof of the Sylow theorems
---

## Proof

1. Let $N = N_G(P)$ be the [[normaliser|0AT1ZSNM25]] of $P$ in $G$. It is a subgroup of $G$: if $gPg^{-1} = P$ and $hPh^{-1} = P$, then $(gh)P(gh)^{-1} = P$ and $g^{-1}Pg = P$.
2. For $x \in P$ we have $xPx^{-1} = P$, because $P$ is a subgroup. So $P \subseteq N \subseteq G$.
3. By the [[index formula|04DC0SRN2K]] for $P$ in $G$, for $N$ in $G$, and for $P$ in $N$, we get $|G| = [G : P]\,|P|$, $|G| = [G : N]\,|N|$ and $|N| = [N : P]\,|P|$.
4. Combining these, $[G : P]\,|P| = [G : N]\,[N : P]\,|P|$. Dividing by $|P| \geq 1$ gives $[G : P] = [G : N] \cdot [N : P]$.
5. By the [[formula for the number of Sylow subgroups|09ZJ6CAK7S]], $n_p = [G : N]$.
6. So $[G : P] = n_p \cdot [N : P]$, where $[N : P]$ is a positive integer. Hence $n_p$ divides the [[index|04QEBF8S49]] $[G : P]$.

## Idea

The number $n_p$ is the index of the normaliser of $P$. The normaliser sits between $P$ and $G$, and indices multiply along a chain of subgroups. So $n_p$ is a factor of $[G : P]$.
