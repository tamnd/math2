---
tag: JFVZP694ST
kind: proof
name: Proof of the inclusion–exclusion principle by counting each element
msc: [05A05]
proves: 0FF7726C7P
uses: [0EE2V3CHFK, 0BFMR2FQ8B, 0PQQGFAWSH, 0F8YBHF2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Inclusion–exclusion_principle
    locator: Proof of main statement
---

## Proof

We count how often each element is counted on the right side, a form of [[double counting|0F8YBHF2W3]].

1. Let $A_1, \dots, A_n$ be finite sets, and let $U = \bigcup_{i=1}^{n} A_i$. Then $U$ is the union of the pairwise disjoint sets $A_i \setminus (A_1 \cup \dots \cup A_{i-1})$. Each is a subset of the finite set $A_i$, so the [[rule of sum|0EE2V3CHFK]] shows that $U$ is finite.
2. Let $\mathcal{I}$ be the set of nonempty subsets $I \subseteq \set{1, \dots, n}$. For $I \in \mathcal{I}$, let $A_I = \bigcap_{i \in I} A_i$. Then $A_I \subseteq U$.
3. For $x \in U$ and $I \in \mathcal{I}$, let $e(x, I) = 1$ if $x \in A_I$, and $e(x, I) = 0$ otherwise.
4. For each $I \in \mathcal{I}$, the set $A_I$ is the disjoint union of the singletons $\set{x}$ with $x \in A_I$. So the [[rule of sum|0EE2V3CHFK]] gives $|A_I| = \sum_{x \in U} e(x, I)$.
5. Let $R$ be the right side of the statement. By step 4, and by exchanging two finite sums,
$$R = \sum_{I \in \mathcal{I}} (-1)^{|I| + 1} \sum_{x \in U} e(x, I) = \sum_{x \in U} c(x), \qquad c(x) = \sum_{I \in \mathcal{I}} (-1)^{|I| + 1} e(x, I).$$
6. Fix $x \in U$. Let $J = \set{i : x \in A_i}$ and $m = |J|$. Since $x \in U$, $J$ is nonempty, so $m \ge 1$.
7. For $I \in \mathcal{I}$, we have $x \in A_I$ exactly when $x \in A_i$ for all $i \in I$, that is, when $I \subseteq J$.
8. So $c(x)$ is the sum of $(-1)^{|I| + 1}$ over the nonempty subsets $I$ of $J$.
9. By the [[number of $k$-element subsets|0BFMR2FQ8B]], $J$ has $\binom{m}{k}$ subsets with $k$ elements. Grouping the subsets by size gives
$$c(x) = \sum_{k=1}^{m} (-1)^{k+1} \binom{m}{k}.$$
10. Since $m \ge 1$, the [[alternating sum of binomial coefficients|0PQQGFAWSH]] gives $\sum_{k=0}^{m} (-1)^k \binom{m}{k} = 0$.
11. The term with $k = 0$ there is $\binom{m}{0} = 1$. So $\sum_{k=1}^{m} (-1)^k \binom{m}{k} = -1$, and by step 9, $c(x) = 1$.
12. By steps 5 and 11, $R = \sum_{x \in U} 1 = |U|$. This is the claimed formula $\left| \bigcup_{i=1}^{n} A_i \right| = \sum_{I \in \mathcal{I}} (-1)^{|I| + 1} |A_I|$.

## Idea

Expand each $|A_I|$ as a sum over its elements and collect the contributions of one element $x$. If $x$ lies in exactly $m \ge 1$ of the sets, the signs add up to $\binom{m}{1} - \binom{m}{2} + \dots$, which is $1$ because $(1 - 1)^m = 0$. So every element of the union is counted exactly once.
