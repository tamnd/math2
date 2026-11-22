---
tag: KGFAG81ZNC
kind: proof
name: Proof of the linear dependence lemma
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: H75GS7QVPB
methods: [0NTF6DMVAP, 0J0XBKG64S, MKHVRNW68H]
uses: [0EVHJFTG9Z, 0HR573CHNM, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2A
---

## Proof

We solve a dependence relation for its last vector with a nonzero coefficient, and then substitute that expression wherever the vector appears.

1. For part 1, the family is [[dependent|0EVHJFTG9Z]], so there are $a_1, \dots, a_m \in F$, not all $0$, with $a_1 v_1 + \dots + a_m v_m = 0$.
2. Let $k$ be the largest index with $a_k \ne 0$. The coefficients after $a_k$ are $0$, so $a_1 v_1 + \dots + a_k v_k = 0$.
3. Since $F$ is a field and $a_k \ne 0$, the inverse $a_k^{-1}$ exists. Subtract $a_k v_k$ from both sides and multiply by $-a_k^{-1}$:
$$v_k = \sum_{i < k} (-a_k^{-1} a_i) v_i.$$
4. So $v_k \in \operatorname{span}(v_1, \dots, v_{k-1})$. For $k = 1$ the sum is empty, and step 3 says $v_1 = 0$.
5. For part 2, write $v_k = \sum_{i < k} b_i v_i$. A combination of the $v_i$ with $i \ne k$ is a combination of all the $v_i$ with coefficient $0$ for $v_k$, so the span without $v_k$ lies inside the [[span|0HR573CHNM]] of all of them.
6. For the other inclusion, let $w = \sum_{i=1}^m c_i v_i$. Substitute the expression for $v_k$ and collect terms by the axioms of a [[vector space|05EGHEQZAW]]:
$$w = \sum_{i < k} (c_i + c_k b_i) v_i + \sum_{i > k} c_i v_i.$$
7. The right side does not use $v_k$, so $w$ lies in the span without $v_k$, and the two spans are equal.
8. For part 3, assume first that the family is dependent. Part 1 gives $v_k$ in the span of $v_1, \dots, v_{k-1}$, and this span lies inside the span of all $v_i$ with $i \ne k$.
9. Conversely, assume $v_j = \sum_{i \ne j} b_i v_i$. Then $\sum_{i \ne j} b_i v_i + (-1) v_j = 0$, and the coefficient of $v_j$ is $-1 \ne 0$, so this relation is nontrivial and the family is dependent.
10. For part 4, assume $c_1 v_1 + \dots + c_m v_m + c v = 0$. Suppose, for a contradiction, that $c \ne 0$.
11. Then, as in step 3, $v = \sum_i (-c^{-1} c_i) v_i$ lies in $\operatorname{span}(v_1, \dots, v_m)$, which contradicts the hypothesis. So $c = 0$.
12. The relation becomes $c_1 v_1 + \dots + c_m v_m = 0$, and the independence of $(v_1, \dots, v_m)$ gives $c_1 = \dots = c_m = 0$.
13. All coefficients are $0$, so $(v_1, \dots, v_m, v)$ is independent.

## Idea

A dependence relation is an equation among the vectors, and in a field you can solve it for any vector whose coefficient is not zero.
Choosing the last such vector gives an expression in terms of the earlier ones, which is part 1.
Substituting that expression removes the vector from every combination, which is part 2.
Part 4 runs the same idea backward: a relation with a nonzero coefficient on the new vector would put the new vector in the old span.

## Variants

Part 4 can be proved in contrapositive form.
Suppose $(v_1, \dots, v_m, v)$ is dependent; by part 1 some vector of it lies in the span of the earlier ones.
That vector cannot be one of $v_1, \dots, v_m$, since then $(v_1, \dots, v_m)$ would be dependent by part 3, so it is $v$, and $v \in \operatorname{span}(v_1, \dots, v_m)$.
Part 1 can also be proved by induction on $m$: if $(v_1, \dots, v_{m-1})$ is already dependent, use the induction hypothesis, and otherwise part 4 in contrapositive form puts $v_m$ in the span of the earlier vectors.
