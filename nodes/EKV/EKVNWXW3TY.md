---
tag: EKVNWXW3TY
kind: proof
name: Proof that the continuous image of a connected set is connected
msc: [54D05]
proves: 0EPD87YVG8
uses: [0R37DFJKFW, 0D939CMME7, 0D5YHQGDJY, 0SY9ECQ19Q, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Theorems
---

## Proof

We argue by contradiction, and pull a splitting of $f(S)$ back to $S$.

1. Recall that a subset is [[connected|0R37DFJKFW]] when it is a [[connected space|0D939CMME7]] in the [[subspace topology|0D5YHQGDJY]]. The open sets of $f(S)$ are the sets $f(S) \cap U$ with $U$ open in $Y$.
2. Suppose that $f(S)$ is not connected. Then there are open $U, V \subseteq Y$ such that $U' = f(S) \cap U$ and $V' = f(S) \cap V$ are nonempty and disjoint, with $U' \cup V' = f(S)$.
3. Let $P = S \cap f^{-1}(U)$ and $Q = S \cap f^{-1}(V)$, with [[preimages|0FGCFY1AZX]] taken under $f$. Since $f$ is [[continuous|0SY9ECQ19Q]], $f^{-1}(U)$ and $f^{-1}(V)$ are open in $X$. So $P$ and $Q$ are open in $S$.
4. $P$ is nonempty. Take $y \in U'$. Then $y = f(s)$ for some $s \in S$, and $s \in P$. In the same way, $Q$ is nonempty.
5. $P$ and $Q$ are disjoint. If $s \in P \cap Q$, then $f(s) \in f(S) \cap U \cap V = U' \cap V'$, which is empty.
6. $P \cup Q = S$. For $s \in S$, $f(s) \in f(S) = U' \cup V'$, so $f(s) \in U$ or $f(s) \in V$. Thus $s \in P$ or $s \in Q$.
7. So $P$ and $Q$ split $S$, and $S$ is not connected. This contradicts the hypothesis, so $f(S)$ is connected.

## Idea

Continuity means that preimages of open sets are open. So a splitting of the image into two open pieces pulls back to a splitting of $S$, which cannot exist.
