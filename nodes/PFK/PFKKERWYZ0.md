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

Claim: for every group $G$ and all subgroups $H$ and $K$ of $G$, the [[union|0X1GSWNBN1]] $H \cup K$ is a [[subgroup|0X1JXT47GA]] of $G$.
We give a [[counterexample|0ED72CTBNP]].

1. Let $G = \mathbb{Z}$ with addition, $H = 2\mathbb{Z}$, the even integers, and $K = 3\mathbb{Z}$, the multiples of $3$.
2. $H$ is a subgroup: it contains $0$, and sums and negatives of even integers are even. In the same way $K$ is a subgroup.
3. $2 \in H$ and $3 \in K$, so $2$ and $3$ are in $H \cup K$.
4. Their sum $5$ is not even and not a multiple of $3$, so $5 \notin H \cup K$.
5. A subgroup is closed under the group operation, so $H \cup K$ is not a subgroup. The claim is false.

## Remarks

The [[intersection|0ZNMMA9TF5]] of two subgroups is always a subgroup, and a student who knows this may expect the same for unions.
The counterexample shows that the two operations behave differently.

The claim becomes true under an extra hypothesis: $H \cup K$ is a subgroup if and only if $H \subseteq K$ or $K \subseteq H$.
So any counterexample must use two subgroups, neither contained in the other, as $2\mathbb{Z}$ and $3\mathbb{Z}$ are.
The smallest group with a counterexample is the Klein four-group $\{e, a, b, ab\}$, with $H = \{e, a\}$ and $K = \{e, b\}$: the product $ab$ is not in $H \cup K$.

## Explanations

### L1 human

Take all even numbers and all multiples of $3$, and put them in one bag.
The bag contains $2$ and $3$.
But $2 + 3 = 5$ is neither even nor a multiple of $3$, so $5$ is not in the bag.
Adding two numbers from the bag can leave the bag.
That one sum shows that the bag is not closed under addition.

### L2 human

We prove the corrected statement: if $H \cup K$ is a subgroup of $G$, then $H \subseteq K$ or $K \subseteq H$.

1. Suppose, for a contradiction, that $H \not\subseteq K$ and $K \not\subseteq H$.
2. Choose $h \in H$ with $h \notin K$, and $k \in K$ with $k \notin H$.
3. Since $H \cup K$ is a subgroup, $hk \in H \cup K$.
4. If $hk \in H$, then $k = h^{-1}(hk) \in H$, which contradicts step 2.
5. If $hk \in K$, then $h = (hk)k^{-1} \in K$, which contradicts step 2.
6. Both cases are impossible, so $H \subseteq K$ or $K \subseteq H$.

The typical use: a counterexample points to the missing hypothesis, and the proof of the corrected statement shows why the counterexample works.

A trap: in step 2, the elements must be chosen outside the other subgroup.
The elements $2$ and $3$ of the example work because $2 \notin 3\mathbb{Z}$ and $3 \notin 2\mathbb{Z}$.
