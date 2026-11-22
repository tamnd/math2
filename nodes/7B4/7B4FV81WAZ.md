---
tag: 7B4FV81WAZ
kind: proof
name: Proof that the span is the smallest subspace containing the set
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 2BX666XF68
methods: [0NTF6DMVAP, 0ASJVEFA9J, MKHVRNW68H]
uses: [0HR573CHNM, Z5XKYXTC0K, 0V33SPH7RR, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: Theorems
  - book: isbn:9783031410253
    locator: Section 2A
---

## Proof

We show that the combinations form a subspace, then show by induction that every subspace containing $S$ contains every combination.
Write $L = \operatorname{span}(S)$, the set of all finite linear combinations of vectors of $S$.

1. The empty combination, with $k = 0$, has value $0$, so $0 \in L$ and $L$ is nonempty.
2. Let $x = \sum_{i=1}^k a_i v_i$ and $y = \sum_{j=1}^l b_j w_j$ lie in $L$, with all $v_i, w_j \in S$, and let $c \in F$. By the distributive law and the compatibility axiom of the [[definition of a vector space|05EGHEQZAW]],
$$x + cy = \sum_{i=1}^k a_i v_i + \sum_{j=1}^l (c b_j) w_j.$$
3. The right side is a combination of the $k + l$ vectors $v_1, \dots, v_k, w_1, \dots, w_l$ of $S$, so $x + cy \in L$.
4. By the [[subspace test|Z5XKYXTC0K]] and steps 1 to 3, $L$ is a subspace of $V$.
5. For $v \in S$, the unit axiom gives $v = 1v$, a combination with $k = 1$. So $S \subseteq L$, and part 1 is proved.
6. For part 2, let $W$ be a subspace with $S \subseteq W$. We show by induction on $k$ that every combination $\sum_{i=1}^k a_i v_i$ with $v_i \in S$ lies in $W$.
7. For $k = 0$ the combination is $0$, and $0 \in W$ because $W$ is a subspace.
8. Assume that $x = \sum_{i=1}^{k} a_i v_i$ lies in $W$. Since $v_{k+1} \in S \subseteq W$ and $W$ is closed under scaling, $a_{k+1} v_{k+1} \in W$, and since $W$ is closed under addition, $x + a_{k+1} v_{k+1} \in W$.
9. By induction every element of $L$ lies in $W$, so $L \subseteq W$, and part 2 is proved.
10. For part 3, let $M$ be the intersection of all subspaces of $V$ that contain $S$. This family is nonempty, because $V$ belongs to it, so by the [[intersection theorem|0V33SPH7RR]] $M$ is a subspace that contains $S$.
11. By steps 4 and 5, $L$ is one of the subspaces in the family, so $M \subseteq L$.
12. By part 2 with $W = M$, we get $L \subseteq M$, so $L = M$, and part 3 is proved.
13. For part 4, take $S = \varnothing$. The only combination is the empty one, whose value is $0$, so $\operatorname{span}(\varnothing) = \{0\}$.

## Idea

Two facts do all the work.
First, a combination of combinations is again a combination, because you can multiply out and collect terms, so the span is closed under the operations.
Second, a subspace that holds the vectors of $S$ must hold every combination of them, one term at a time, which is the induction on the length.
The intersection of all subspaces containing $S$ is squeezed between these two facts, so it equals the span.

## Variants

One can take part 3 as the definition, as Mathlib does, and prove the description by combinations afterwards.
Then the intersection is a subspace by the intersection theorem, and it contains $L$ by the induction of steps 6 to 9.
For the reverse inclusion, one shows that $L$ is a subspace containing $S$, as in steps 1 to 5, so the intersection lies inside $L$.
The two routes use the same facts in a different order.
