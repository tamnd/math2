---
tag: KJBM9C3RF3
kind: example
name: A set of three permutations that is not a transversal of a subgroup of order two in S3
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: grad
not_instance_of:
  - target: QQVCDZX300
    note: "the set has 3 elements, the index of H, but it has no element in H and two elements in one left coset and in one right coset"
uses: [0515A6D2Y1, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, QQVCDZX300, 0DTXBQPA2S]
sources:
  - url: https://en.wikipedia.org/wiki/Transversal_(combinatorics)
    locator: Examples
---

## Example

Let $G = S_3$ be the [[symmetric group|0515A6D2Y1]], and compose permutations from right to left.
Let $H = \{e, (1\,2)\}$, a [[subgroup|0X1JXT47GA]] of [[index|0DTXBQPA2S]] $3$.
Let $S = \{(1\,2\,3), (1\,3\,2), (2\,3)\}$.
We show that $S$ is neither a left nor a right [[transversal|QQVCDZX300]] of $H$.

1. The [[left cosets|03DEH43F4H]] of $H$ are $H$, $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$.
2. Both $(1\,3\,2)$ and $(2\,3)$ lie in $(2\,3)H$, and no element of $S$ lies in $H$. So $S$ is not a left transversal.
3. The [[right cosets|0NE1DK7H4T]] of $H$ are $H$, $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ and $H(2\,3) = \{(2\,3), (1\,2\,3)\}$.
4. Both $(1\,2\,3)$ and $(2\,3)$ lie in $H(2\,3)$, and no element of $S$ lies in $H$. So $S$ is not a right transversal.

Thus $S$ has the right number of elements, but it is not a transversal of either kind.

## Remarks

A set with $[G : H]$ elements is a left transversal exactly when it meets each left coset.
Equivalently, no two of its elements lie in the same left coset.
The set $S$ fails both tests.

The set $S$ is the complement of $\{e, (1\,2), (1\,3)\}$, and it misses the coset $H$ entirely.
If we replace $(1\,3\,2)$ by $e$, we get $\{e, (1\,2\,3), (2\,3)\}$, which is a left transversal.

## Explanations

### L1 human

A transversal must take one element from each piece.
Here the set has three elements and there are three pieces, so the count is right.
But two elements come from the same piece, and one piece gets nothing.
So the set is not a transversal.

### L2 human

We test whether two elements $a$ and $b$ lie in the same left coset of $H$.

1. They lie in the same left coset exactly when $a^{-1}b \in H$.
2. For $a = (2\,3)$ and $b = (1\,3\,2)$, we compute $a^{-1}b = (2\,3)(1\,3\,2)$.
3. This product sends $1 \mapsto 3 \mapsto 2$, $2 \mapsto 1 \mapsto 1$ and $3 \mapsto 2 \mapsto 3$, so it is $(1\,2)$.
4. Thus $a^{-1}b \in H$, and $a$ and $b$ lie in the same left coset.

The typical use is a quick test of a candidate transversal without a list of all cosets.
A trap is to count elements only.
The count $[G : H]$ is necessary, but it is not sufficient.
