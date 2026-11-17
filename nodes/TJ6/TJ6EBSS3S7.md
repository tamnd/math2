---
tag: TJ6EBSS3S7
kind: example
name: The alternating group is the kernel of the sign
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0W88CEGQP1]
illustrates: [0C9ZKYSPYR]
uses: [02DKV69ZH0, 0JEJJCB0EX, 0Z5905Q73D, 0515A6D2Y1, 0W88CEGQP1]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Alternating_group
    locator: Basic properties
---

## Example

Let $n \ge 2$, and let $S_n$ be the [[symmetric group|0515A6D2Y1]].
Compose permutations from right to left: $\sigma\tau$ means first $\tau$, then $\sigma$.
Consider the [[sign|02DKV69ZH0]] $\operatorname{sgn} \colon S_n \to \{1, -1\}$, where $\{1, -1\}$ is a group under multiplication.

1. The sign is a homomorphism ([[sign is a homomorphism|0JEJJCB0EX]]).
2. A permutation has sign $1$ exactly when it is a product of an even number of transpositions.
3. So the [[kernel|0W88CEGQP1]] of $\operatorname{sgn}$ is the set of even permutations, the [[alternating group|0Z5905Q73D]] $A_n$.
4. For $n = 3$, we have $(1\,3)(1\,2) = (1\,2\,3)$, so $\operatorname{sgn}(1\,2\,3) = (-1)(-1) = 1$. In the same way $(1\,2)(1\,3) = (1\,3\,2)$.
5. So $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, and the three transpositions of $S_3$ are not in $A_3$.
6. By [[kernels are normal|0C9ZKYSPYR]], $A_n$ is a [[normal subgroup|0CB0DX5BVV]] of $S_n$.
7. The sign is surjective, because $\operatorname{sgn}(1\,2) = -1$. So $S_n/A_n \cong \{1, -1\}$, and $A_n$ has index $2$.

## Remarks

The example shows how a kernel gives a normal subgroup without any computation of conjugates.
For $n \ge 3$, the group $S_n$ is not abelian, so the normality of $A_n$ does not come from commutativity.
For $n = 2$, $A_2 = \{e\}$, and the sign is an isomorphism from $S_2$ to $\{1, -1\}$.
For $n = 1$, the group $S_1$ has only the identity, so the sign is not surjective and $A_1 = S_1$.
For $n \ge 2$ the order of $A_n$ is $n!/2$, by step 7 and the first isomorphism theorem.

## Explanations

### L1 human

Each shuffle of $n$ cards can be done by swapping two cards at a time.
For a given shuffle, the number of swaps is always even or always odd.
The sign records this parity as $1$ or $-1$.
The even shuffles are the ones that the sign sends to the identity $1$, so they form the kernel.

### L2 human

We compute the sign of $\sigma = (1\,2\,3\,4)$ in $S_4$, composed from right to left.

1. A check of each point gives $(1\,2\,3\,4) = (1\,4)(1\,3)(1\,2)$.
2. This is a product of three transpositions, so $\operatorname{sgn}(\sigma) = (-1)^3 = -1$.
3. So $\sigma \notin A_4$, but $\sigma^2 = (1\,3)(2\,4)$ has sign $1$ and lies in $A_4$.

The typical use is to show that some permutation cannot be reached by an even number of swaps.
The trap is the length of a cycle: a cycle of length $k$ has sign $(-1)^{k-1}$, so a $4$-cycle is odd and a $3$-cycle is even.
