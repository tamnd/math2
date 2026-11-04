---
tag: SAAGBV8XZ2
kind: proof
name: Proof of Cantor's intersection theorem
msc: [54D30]
proves: 0EZBG8SKJM
uses: [0CNQXVBHCX, 00R0X1WGPX, 0G5AV9Q4RR, 0P6PMJB4MA]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_intersection_theorem
    locator: Topological statement
---

## Proof

We argue by contradiction, with the complements of the sets $C_n$ as an open cover.

1. Let $X$ be a [[topological space|0CNQXVBHCX]]. Let $C_1 \supseteq C_2 \supseteq \cdots$ be nonempty [[compact|00R0X1WGPX]] [[closed|0G5AV9Q4RR]] subsets of $X$.
2. Assume that $\bigcap_{n \ge 1} C_n = \emptyset$. For $n \ge 1$, let $U_n = X \setminus C_n$. Each $U_n$ is open, because $C_n$ is closed.
3. Let $x \in C_1$. By step 2, $x$ is not in some $C_n$, so $x \in U_n$. Hence $C_1 \subseteq \bigcup_{n \ge 1} U_n$.
4. The set $C_1$ is compact. By [[compactness via open covers|0P6PMJB4MA]], there are finitely many indices $n_1, \ldots, n_p$ with $C_1 \subseteq U_{n_1} \cup \cdots \cup U_{n_p}$.
5. Since $C_1$ is nonempty, $p \ge 1$. Let $m = \max(n_1, \ldots, n_p)$.
6. For $n \le m$ we have $C_m \subseteq C_n$, so $U_n \subseteq U_m$. Hence $C_1 \subseteq U_m = X \setminus C_m$.
7. But $C_m \subseteq C_1$, so $C_m \subseteq X \setminus C_m$. This forces $C_m = \emptyset$.
8. This contradicts the hypothesis that $C_m$ is nonempty. So $\bigcap_{n \ge 1} C_n \ne \emptyset$.

## Idea

If the intersection were empty, the complements would form an open cover of the compact set $C_1$.
Because the sets are nested, a finite subcover reduces to a single complement $X \setminus C_m$, and that would make $C_m$ empty.
