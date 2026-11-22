---
tag: PFKKERWYZ0
kind: example
name: The union of two subgroups need not be a subgroup
msc: ["00A35", "20A05"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [0ED72CTBNP]
uses: [0ED72CTBNP, 0X1JXT47GA, 0X1GSWNBN1]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Basic properties of subgroups
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
---

## Example

The claim is: for every group $G$ and all subgroups $H$ and $K$ of $G$, the [[union|0X1GSWNBN1]] $H \cup K$ is a [[subgroup|0X1JXT47GA]] of $G$.
We refute it with a [[counterexample|0ED72CTBNP]] in the integers.

1. Let $G = \mathbb{Z}$ with addition, let $H = 2\mathbb{Z}$ be the even integers, and let $K = 3\mathbb{Z}$ be the multiples of $3$.
2. $H$ is a subgroup, because it contains $0$ and the sum and the negative of even integers are even.
   For the same reason, $K$ is a subgroup.
3. We have $2 \in H$ and $3 \in K$, so $2$ and $3$ both lie in $H \cup K$.
4. Their sum is $5$, which is not even and not a multiple of $3$, so $5 \notin H \cup K$.
5. A subgroup is closed under the group operation, so $H \cup K$ is not a subgroup, and the claim is false.

## Remarks

The [[intersection|0ZNMMA9TF5]] of two subgroups is always a subgroup, so it is natural to expect the same of unions.
The counterexample shows that the two operations behave differently.

The claim becomes true with one extra hypothesis: $H \cup K$ is a subgroup if and only if $H \subseteq K$ or $K \subseteq H$.
So every counterexample must use two subgroups, neither inside the other, as $2\mathbb{Z}$ and $3\mathbb{Z}$ are.
In each group of order at most $3$, and in the cyclic group of order $4$, the subgroups form a chain, so these groups have no counterexample.
The smallest group with one is the Klein four-group $\{e, a, b, ab\}$, with $H = \{e, a\}$ and $K = \{e, b\}$, since the product $ab$ lies in neither.

## Explanations

### L1 human

Take all even numbers and all multiples of $3$, and put them in one bag.
The bag contains $2$ and $3$.
But $2 + 3 = 5$ is neither even nor a multiple of $3$, so $5$ is not in the bag.
Adding two numbers from the bag can leave the bag.
That one sum shows that the bag is not closed under addition.

### L2 human

Why must a counterexample use two subgroups that are not nested?
We prove the corrected statement: if $H \cup K$ is a subgroup of $G$, then $H \subseteq K$ or $K \subseteq H$.
Suppose that $H \not\subseteq K$ and $K \not\subseteq H$, and choose $h \in H$ with $h \notin K$ and $k \in K$ with $k \notin H$.
Since $H \cup K$ is a subgroup, the product $hk$ lies in $H$ or in $K$.
If $hk \in H$, then
$$k = h^{-1}(hk) \in H,$$
which contradicts the choice of $k$.
If $hk \in K$, then $h = (hk)k^{-1} \in K$, which contradicts the choice of $h$.
Both cases are impossible, so one subgroup contains the other.
In the example, $h = 2$ and $k = 3$ play these roles, because $2 \notin 3\mathbb{Z}$ and $3 \notin 2\mathbb{Z}$.
So a counterexample points to the missing hypothesis, and the proof of the corrected statement explains why the counterexample works.
