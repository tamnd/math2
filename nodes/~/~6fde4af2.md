---
tag: ~6fde4af2
kind: proof
name: Proof that the span is the smallest subspace containing the set
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: ~13840ba2
methods: [0NTF6DMVAP, 0ASJVEFA9J, MKHVRNW68H]
uses: [0HR573CHNM, ~3900ae4c, 0V33SPH7RR, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: Theorems
  - book: isbn:9783031410253
    locator: Section 2A
---

## Proof

Write $L = \operatorname{span}(S)$, the set of all finite linear combinations of vectors of $S$.

1. (Part 1) The empty combination, with $k = 0$, has value $0$. So $0 \in L$, and $L$ is nonempty.
2. Let $x = \sum_{i=1}^k a_i v_i$ and $y = \sum_{j=1}^l b_j w_j$ be in $L$, with $v_i, w_j \in S$, and let $c \in F$.
3. By axioms 5 and 7 of the [[definition|05EGHEQZAW]], $x + cy = \sum_{i=1}^k a_i v_i + \sum_{j=1}^l (c b_j) w_j$.
4. This is a combination of the $k + l$ vectors $v_1, \dots, v_k, w_1, \dots, w_l$ of $S$, so $x + cy \in L$.
5. By the [[subspace test|~3900ae4c]] and steps 1 to 4, $L$ is a subspace.
6. For $v \in S$, we have $v = 1v$ by axiom 6, which is a combination with $k = 1$. So $S \subseteq L$.
7. (Part 2) Let $W$ be a subspace with $S \subseteq W$. We show by induction on $k$ that each combination $\sum_{i=1}^k a_i v_i$ with $v_i \in S$ lies in $W$.
8. Base $k = 0$: the empty combination is $0$, which lies in $W$.
9. Step: assume $x = \sum_{i=1}^{k} a_i v_i \in W$. Then $x + a_{k+1} v_{k+1} \in W$, because $v_{k+1} \in S \subseteq W$ and $W$ is closed under scaling and addition.
10. By induction, $L \subseteq W$. This proves part 2.
11. (Part 3) Let $M$ be the intersection of all subspaces that contain $S$. The family is nonempty, because $V$ is in it. By [[the intersection theorem|0V33SPH7RR]], $M$ is a subspace, and $S \subseteq M$.
12. By step 5 and step 6, $L$ is one of the subspaces in the family, so $M \subseteq L$.
13. By part 2 applied to $W = M$, we have $L \subseteq M$. So $L = M$.
14. (Part 4) For $S = \varnothing$, the only combination is the empty one, with value $0$. So $\operatorname{span}(\varnothing) = \set{0}$.

## Idea

Combinations of combinations are combinations, so the span is closed.
Closure of any subspace that contains $S$ forces it to contain every combination, by induction on the length.
