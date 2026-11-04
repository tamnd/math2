---
tag: G24TND9BXB
kind: proof
name: Proof that compact subsets of a Hausdorff space are closed
msc: [54D30]
proves: 0MYFJVMN7M
uses: [0CNQXVBHCX, 0MXB4CKHFW, 00R0X1WGPX, 0P6PMJB4MA, 0G5AV9Q4RR, 01ZQQDCERP]
sources:
  - url: https://proofwiki.org/wiki/Compact_Subspace_of_Hausdorff_Space_is_Closed
    locator: Proof 1
---

## Proof

We show that the complement of $K$ is open, by separating each outside point from $K$.

1. Let $X$ be a [[Hausdorff space|0MXB4CKHFW]] and let $K$ be a [[compact|00R0X1WGPX]] subset of $X$.
2. If $K = \emptyset$, then $X \setminus K = X$ is open, and $K$ is [[closed|0G5AV9Q4RR]]. So assume $K \ne \emptyset$.
3. Fix $y \in X \setminus K$. For each $x \in K$ we have $x \ne y$. By the Hausdorff property, choose [[open sets|01ZQQDCERP]] $U_x \ni x$ and $V_x \ni y$ with $U_x \cap V_x = \emptyset$.
4. The sets $U_x$ with $x \in K$ are open and cover $K$. By [[compactness via open covers|0P6PMJB4MA]], there are $x_1, \ldots, x_n \in K$ with $K \subseteq U_{x_1} \cup \cdots \cup U_{x_n}$, and $n \ge 1$.
5. Let $V_y = V_{x_1} \cap \cdots \cap V_{x_n}$. A [[topology|0CNQXVBHCX]] is closed under finite intersections, so $V_y$ is open. Also $y \in V_y$.
6. Let $z \in K$. By step 4, $z \in U_{x_j}$ for some $j$. Since $U_{x_j} \cap V_{x_j} = \emptyset$ and $V_y \subseteq V_{x_j}$, we get $z \notin V_y$.
7. So $V_y \subseteq X \setminus K$ for each $y \in X \setminus K$.
8. Hence $X \setminus K = \bigcup_{y \in X \setminus K} V_y$, a union of open sets. It is open by the axioms of a topology.
9. Thus $K$ is closed in $X$.

## Idea

Each point outside $K$ can be separated from each point of $K$ by disjoint open sets.
Compactness lets us use only finitely many of these separations, and a finite intersection of open sets is still open. This gives an open neighbourhood of the outside point that misses $K$.
