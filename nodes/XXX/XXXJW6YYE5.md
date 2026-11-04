---
tag: XXXJW6YYE5
kind: proof
name: Proof of the finite intersection property characterisation of compactness
msc: [54D30]
proves: 00BWV5CKCF
uses: [0CNQXVBHCX, 00R0X1WGPX, 0G5AV9Q4RR, 01ZQQDCERP, 0P6PMJB4MA]
sources:
  - url: https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Compact_Topological_Space
---

## Proof

We pass to complements and use [[compactness via open covers|0P6PMJB4MA]]. We read "finitely many indices" as allowing none. For no index, the intersection $K \cap F_{i_1} \cap \cdots \cap F_{i_n}$ is $K$ itself.

1. Let $X$ be a [[topological space|0CNQXVBHCX]], let $K \subseteq X$, and let $(F_i)_{i \in I}$ be [[closed subsets|0G5AV9Q4RR]] of $X$. Let $U_i = X \setminus F_i$, an [[open set|01ZQQDCERP]].
2. Claim: for each $J \subseteq I$, $K \subseteq \bigcup_{j \in J} U_j$ holds if and only if $K \cap \bigcap_{j \in J} F_j = \emptyset$. For $J = \emptyset$, the empty union is $\emptyset$ and $K \cap \bigcap_{j \in \emptyset} F_j$ means $K$.
3. Proof of the claim: a point $x \in K$ lies outside $\bigcap_{j \in J} F_j$ if and only if $x \notin F_j$ for some $j \in J$. This means $x \in U_j$ for some $j \in J$. So each point of $K$ lies in $\bigcup_{j \in J} U_j$ if and only if no point of $K$ lies in $\bigcap_{j \in J} F_j$.
4. Assume $K$ is [[compact|00R0X1WGPX]]. Let $(F_i)$ satisfy $K \cap F_{i_1} \cap \cdots \cap F_{i_n} \ne \emptyset$ for all finitely many indices.
5. Suppose $K \cap \bigcap_{i \in I} F_i = \emptyset$. By step 2 with $J = I$, the open sets $U_i$ cover $K$.
6. By compactness via open covers, there are finitely many indices $i_1, \ldots, i_n$ with $K \subseteq U_{i_1} \cup \cdots \cup U_{i_n}$.
7. By step 2 with $J = \set{i_1, \ldots, i_n}$, this gives $K \cap F_{i_1} \cap \cdots \cap F_{i_n} = \emptyset$. This contradicts step 4.
8. So $K \cap \bigcap_{i \in I} F_i \ne \emptyset$, and $K$ has the property.
9. Now assume $K$ has the property. Let $(U_i)_{i \in I}$ be open sets of $X$ that cover $K$. Let $F_i = X \setminus U_i$, a closed set.
10. Suppose no finite subfamily of $(U_i)$ covers $K$. By step 2, $K \cap F_{i_1} \cap \cdots \cap F_{i_n} \ne \emptyset$ for all finitely many indices.
11. By the property, $K \cap \bigcap_{i \in I} F_i \ne \emptyset$. By step 2 with $J = I$, the sets $U_i$ do not cover $K$. This contradicts step 9.
12. So some finite subfamily of $(U_i)$ covers $K$. By compactness via open covers, $K$ is compact.

## Idea

Closed sets with an empty intersection inside $K$ are the same as open sets, their complements, that cover $K$.
So "every open cover has a finite subcover" turns into "if all finite intersections meet $K$, the whole intersection meets $K$".
