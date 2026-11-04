---
tag: FJ6SNYBX9X
kind: proof
name: Proof that a continuous image of a compact set is compact
msc: [54D30]
proves: 0K9AAJ8G51
uses: [0P6PMJB4MA, 0SY9ECQ19Q, 0FGCFY1AZX, 0Q3F20XB0A, 00R0X1WGPX]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Functions and compact spaces
---

## Proof

We check the open cover condition for $f(K)$ directly.

1. Let $(V_i)_{i \in I}$ be a family of open subsets of $Y$ with $f(K) \subseteq \bigcup_{i \in I} V_i$.
2. By [[compactness via open covers|0P6PMJB4MA]], it is enough to find finitely many indices $i_1, \ldots, i_n$ with $f(K) \subseteq V_{i_1} \cup \cdots \cup V_{i_n}$.
3. For each $i \in I$, let $U_i = f^{-1}(V_i)$ be the [[preimage|0FGCFY1AZX]]. Since $f$ is [[continuous|0SY9ECQ19Q]], each $U_i$ is open in $X$.
4. Let $x \in K$. Then $f(x)$ is in the [[image|0Q3F20XB0A]] $f(K)$, so $f(x) \in V_i$ for some $i$ by step 1. Thus $x \in U_i$.
5. So $(U_i)_{i \in I}$ is a family of open subsets of $X$ whose union contains $K$.
6. The set $K$ is [[compact|00R0X1WGPX]]. By [[compactness via open covers|0P6PMJB4MA]], there are indices $i_1, \ldots, i_n$ with $K \subseteq U_{i_1} \cup \cdots \cup U_{i_n}$.
7. Let $y \in f(K)$, and write $y = f(x)$ with $x \in K$. By step 6, $x \in U_{i_k}$ for some $k$, so $y = f(x) \in V_{i_k}$.
8. Hence $f(K) \subseteq V_{i_1} \cup \cdots \cup V_{i_n}$. By step 2, $f(K)$ is compact in $Y$.

## Idea

Pull the cover of $f(K)$ back along $f$. Continuity makes the pulled back sets open, and they cover $K$. A finite part of them covers $K$, and the matching sets cover $f(K)$.
