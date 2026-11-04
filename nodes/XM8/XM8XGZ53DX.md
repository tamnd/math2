---
tag: XM8XGZ53DX
kind: proof
name: Proof that a product of compact sets is compact by the tube lemma
msc: [54D30]
proves: 09ZKE5XQ74
uses: [0P6PMJB4MA, 0Z57EC6YX3, 06EX0FHBTF, 0CNQXVBHCX]
sources:
  - url: https://en.wikipedia.org/wiki/Tube_lemma
    locator: Proof
---

## Proof

We use the open cover condition and the tube lemma argument.

1. Let $(W_j)_{j \in J}$ be open subsets of $X \times Y$ with $K \times L \subseteq \bigcup_{j \in J} W_j$. By [[compactness via open covers|0P6PMJB4MA]], we must cover $K \times L$ by finitely many $W_j$.
2. If $K$ or $L$ is empty, then $K \times L$ is empty, and the empty subfamily covers it. From now on let $K$ and $L$ be nonempty.
3. Let $(x, y) \in K \times L$, and choose $j(x, y) \in J$ with $(x, y) \in W_{j(x, y)}$.
4. The sets $U \times V$ with $U$ open in $X$ and $V$ open in $Y$ form a [[basis|06EX0FHBTF]] of the [[product topology|0Z57EC6YX3]]. So there are open $U_{x, y} \subseteq X$ and $V_{x, y} \subseteq Y$ with $(x, y) \in U_{x, y} \times V_{x, y} \subseteq W_{j(x, y)}$.
5. Fix $x \in K$. The open sets $V_{x, y}$, for $y \in L$, cover $L$, since $y \in V_{x, y}$.
6. Since $L$ is compact, there are $y_1, \ldots, y_m \in L$ with $L \subseteq V_{x, y_1} \cup \cdots \cup V_{x, y_m}$. Here $m \ge 1$, because $L$ is nonempty.
7. Let $T_x = U_{x, y_1} \cap \cdots \cap U_{x, y_m}$. It is open in $X$ by the axioms of a [[topology|0CNQXVBHCX]], and it contains $x$.
8. Let $J_x = \set{j(x, y_1), \ldots, j(x, y_m)}$, a finite subset of $J$. Claim: $T_x \times L \subseteq \bigcup_{j \in J_x} W_j$. Let $(a, b) \in T_x \times L$. By step 6, $b \in V_{x, y_k}$ for some $k$.
9. Also $a \in T_x \subseteq U_{x, y_k}$. So $(a, b) \in U_{x, y_k} \times V_{x, y_k} \subseteq W_{j(x, y_k)}$ by step 4. This proves the claim.
10. The open sets $T_x$, for $x \in K$, cover $K$. Since $K$ is compact, there are $x_1, \ldots, x_p \in K$ with $K \subseteq T_{x_1} \cup \cdots \cup T_{x_p}$.
11. Let $(a, b) \in K \times L$. Then $a \in T_{x_l}$ for some $l$, so $(a, b) \in T_{x_l} \times L$.
12. By step 8, $(a, b) \in W_j$ for some $j \in J_{x_l}$.
13. So the sets $W_j$ with $j$ in the finite set $J_{x_1} \cup \cdots \cup J_{x_p}$ cover $K \times L$. By step 1, $K \times L$ is compact.

## Idea

For a fixed $x$, the slice $\set{x} \times L$ is a copy of the compact set $L$, so finitely many basic boxes cover it. Their first factors meet in an open set $T_x$, which gives a whole tube $T_x \times L$ covered by finitely many sets. Compactness of $K$ then needs only finitely many tubes.
