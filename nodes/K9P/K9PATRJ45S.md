---
tag: K9PATRJ45S
kind: proof
name: Proof that a countable intersection of dense open sets in a Baire space is dense
msc: ["54E52"]
proves: 0X2T63GFQQ
uses: [0CNQXVBHCX, 0D5KR33H7X, 0D198GPMTJ, 0DRKT1QJR7, 0SHC6Z304Z, 0C38S0KMJK, 0HAZEFH137, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_space
    locator: Definition
---

## Proof

We pass to complements and use the definition of a Baire space.

1. Let $X$ be a [[Baire space|0D5KR33H7X]], and let $U_n$ be open and [[dense|0D198GPMTJ]] in $X$ for each $n \in \N$. Let $F_n = X \setminus U_n$, a [[closed set|0G5AV9Q4RR]].
2. Fix $n$, and let $V$ be an open set with $V \subseteq F_n$. Then $V \cap U_n = \emptyset$, so $U_n \subseteq X \setminus V$.
3. The set $X \setminus V$ is closed. Since the [[closure is the smallest closed superset|0SHC6Z304Z]], $\overline{U_n} \subseteq X \setminus V$.
4. Since $U_n$ is dense, $\overline{U_n} = X$. So $X \subseteq X \setminus V$, which gives $V = \emptyset$.
5. The [[interior|0C38S0KMJK]] $\operatorname{int} F_n$ is an open subset of $F_n$, because the [[interior is the largest open subset|0HAZEFH137]]. By steps 2 to 4, $\operatorname{int} F_n = \emptyset$.
6. Since $X$ is a Baire space, $\operatorname{int} \bigcup_n F_n = \emptyset$.
7. Let $D = \bigcap_n U_n$. A point lies outside $D$ if and only if it lies outside some $U_n$. So $X \setminus D = \bigcup_n F_n$.
8. Let $\overline{D}$ be the [[closure|0DRKT1QJR7]] of $D$. By the same statement as in step 3, it is closed and contains $D$. So $X \setminus \overline{D}$ is open.
9. Since $D \subseteq \overline{D}$, we get $X \setminus \overline{D} \subseteq X \setminus D = \bigcup_n F_n$.
10. By steps 8 and 9, and since the interior is the largest open subset, $X \setminus \overline{D} \subseteq \operatorname{int} \bigcup_n F_n = \emptyset$.
11. So $\overline{D} = X$, and $\bigcap_n U_n$ is dense in $X$.

## Idea

The complement of a dense open set is a closed set with empty interior.
The Baire property says a countable union of such sets has empty interior. Taking complements again, the intersection of the open sets is dense.
