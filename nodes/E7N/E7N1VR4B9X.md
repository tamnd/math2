---
tag: E7N1VR4B9X
kind: proof
name: Proof that compact Hausdorff spaces are normal
msc: [54D30]
proves: 0MQQQ5NA2S
uses: [0AJ646N339, 0QPHW703PV, 0MXB4CKHFW, 066HW6D9A7, 0P6PMJB4MA, 00R0X1WGPX, 0D5YHQGDJY, 0G5AV9Q4RR, 0CNQXVBHCX]
sources:
  - url: https://proofwiki.org/wiki/Compact_Hausdorff_Space_is_T4
---

## Proof

We first separate a point from a compact set, and then a compact set from a compact set.

1. Let $A, B \subseteq X$ be disjoint [[closed sets|0G5AV9Q4RR]]. The [[subspace topology|0D5YHQGDJY]] on $X$ as a subset of itself is its own topology, so $X$ is a [[compact set|00R0X1WGPX]] in $X$.
2. By [[closed subsets of compact sets are compact|066HW6D9A7]], $A$ and $B$ are compact.
3. Claim: if $C \subseteq X$ is compact and $x \notin C$, there are disjoint open $U \ni x$ and $V \supseteq C$. If $C = \varnothing$, take $U = X$ and $V = \varnothing$.
4. Let $C \ne \varnothing$. For each $c \in C$, we have $c \neq x$. Since $X$ is [[Hausdorff|0MXB4CKHFW]], choose disjoint open sets $U_c \ni x$ and $V_c \ni c$.
5. The open sets $V_c$, for $c \in C$, cover $C$. By [[compactness via open covers|0P6PMJB4MA]], there are $c_1, \ldots, c_n \in C$ with $C \subseteq V_{c_1} \cup \cdots \cup V_{c_n}$.
6. Let $U = U_{c_1} \cap \cdots \cap U_{c_n}$ and $V = V_{c_1} \cup \cdots \cup V_{c_n}$. Both are open by the axioms of a [[topology|0CNQXVBHCX]]. Also $x \in U$ and $C \subseteq V$.
7. If $z \in U \cap V$, then $z \in V_{c_k}$ for some $k$ and $z \in U_{c_k}$. This contradicts $U_{c_k} \cap V_{c_k} = \varnothing$. So $U \cap V = \varnothing$, and the claim holds.
8. Now separate $A$ and $B$. If $A = \varnothing$, take $U = \varnothing$ and $V = X$. Let $A \ne \varnothing$.
9. For each $a \in A$, we have $a \notin B$. Step 3 with $C = B$ gives disjoint open sets $U_a \ni a$ and $V_a \supseteq B$.
10. The open sets $U_a$, for $a \in A$, cover $A$. By compactness of $A$, there are $a_1, \ldots, a_m \in A$ with $A \subseteq U_{a_1} \cup \cdots \cup U_{a_m}$.
11. Let $U = U_{a_1} \cup \cdots \cup U_{a_m}$ and $V = V_{a_1} \cap \cdots \cap V_{a_m}$. Both are open, $A \subseteq U$ and $B \subseteq V$.
12. If $z \in U \cap V$, then $z \in U_{a_k}$ for some $k$ and $z \in V_{a_k}$, which contradicts $U_{a_k} \cap V_{a_k} = \varnothing$. So $U \cap V = \varnothing$.
13. Hence $X$ is [[normal|0AJ646N339]].

## Idea

The Hausdorff property separates two points. Compactness upgrades this, one finite cover at a time: first a point from a compact set, then a compact set from a compact set. Closed sets of a compact space are compact, so this separates any two disjoint closed sets.
