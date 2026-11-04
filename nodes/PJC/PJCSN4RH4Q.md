---
tag: PJCSN4RH4Q
kind: proof
name: Proof that closed subsets of compact sets are compact
msc: [54D30]
proves: 066HW6D9A7
uses: [0CNQXVBHCX, 00R0X1WGPX, 0G5AV9Q4RR, 0P6PMJB4MA, 01ZQQDCERP]
sources:
  - url: https://proofwiki.org/wiki/Closed_Subspace_of_Compact_Space_is_Compact
---

## Proof

We add the complement of $F$ to a cover of $F$ and use compactness of $K$.

1. Let $X$ be a [[topological space|0CNQXVBHCX]], let $K \subseteq X$ be [[compact|00R0X1WGPX]], and let $F \subseteq K$ be [[closed|0G5AV9Q4RR]] in $X$.
2. Let $(U_i)_{i \in I}$ be [[open sets|01ZQQDCERP]] of $X$ with $F \subseteq \bigcup_{i \in I} U_i$.
3. The set $V = X \setminus F$ is open, because $F$ is closed.
4. Let $x \in K$. If $x \in F$, then $x$ lies in some $U_i$. If $x \notin F$, then $x \in V$. So the sets $U_i$ together with $V$ cover $K$.
5. By [[compactness via open covers|0P6PMJB4MA]], finitely many of these sets cover $K$. So there are $i_1, \ldots, i_n \in I$ with $K \subseteq U_{i_1} \cup \cdots \cup U_{i_n} \cup V$.
6. Let $x \in F$. Then $x \in K$, so $x$ lies in one of the sets in step 5. But $x \notin V$, so $x \in U_{i_j}$ for some $j$.
7. So $F \subseteq U_{i_1} \cup \cdots \cup U_{i_n}$. Each cover of $F$ by open sets of $X$ has a finite subcover.
8. By compactness via open covers, $F$ is compact.

## Idea

The complement of $F$ is open and covers everything in $K$ outside $F$.
Adding it to a cover of $F$ gives a cover of $K$. A finite subcover of $K$, with the complement removed, still covers $F$.
