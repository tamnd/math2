---
tag: QPH0JFF17Q
kind: example
name: S3 is a CLT group
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug2
instance_of: [Y9CB5P4YCS]
uses: [0515A6D2Y1, 0X1JXT47GA, 0B85S2V2DR, 0Z05VCBQ7Y, 02DTRYKGE8, 0Z5905Q73D]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Existence of subgroups of given order
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] of the permutations of $\{1, 2, 3\}$, with identity $e$.
Permutations compose from right to left.
The group $S_3$ has the six elements $e$, $(1\,2)$, $(1\,3)$, $(2\,3)$, $(1\,2\,3)$ and $(1\,3\,2)$, so its [[order|0B85S2V2DR]] is $6$.
The group $S_3$ is a [[CLT group|Y9CB5P4YCS]]: it has a [[subgroup|0X1JXT47GA]] of each order that divides $6$.

1. The divisors of $6$ are $1$, $2$, $3$ and $6$.
2. Order $1$: the subgroup $\{e\}$ has $1$ element.
3. Order $2$: the [[transposition|02DTRYKGE8]] $(1\,2)$ satisfies $(1\,2)^2 = e$. Thus $\{e, (1\,2)\}$ is a subgroup of order $2$.
4. Order $3$: let $c = (1\,2\,3)$, a [[cycle|0Z05VCBQ7Y]] of length $3$. Then $c^2 = (1\,3\,2)$ and $c^3 = e$.
5. Thus $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ is a subgroup of order $3$. It is the [[alternating group|0Z5905Q73D]] $A_3$.
6. Order $6$: the whole group $S_3$ is a subgroup of order $6$.
7. By steps 2 to 6, each divisor of $6$ is the order of a subgroup. Thus $S_3$ is CLT.

## Remarks

The example shows that a nonabelian group can be CLT.
The full list of subgroups of $S_3$ is $\{e\}$, the three subgroups $\{e, (1\,2)\}$, $\{e, (1\,3)\}$ and $\{e, (2\,3)\}$, then $A_3$ and $S_3$.
Thus $S_3$ has one subgroup of order $3$, but three subgroups of order $2$.
For $n = 4$, the group $S_4$ is also CLT, as [[this example|6WG1EF772J]] shows.
For $n \ge 5$, the group $S_n$ is not solvable, so it is not CLT.
The other group of order $6$ is the cyclic group $\mathbb{Z}/6\mathbb{Z}$, and it is also CLT.

## Explanations

### L1 human

The group $S_3$ is the set of the six ways to shuffle three cards.
The sizes $1$, $2$, $3$ and $6$ divide $6$, and each of them is the size of a subgroup.
The swap of the top two cards, with "do nothing", gives a subgroup of size $2$.
The three rotations of the three cards give a subgroup of size $3$.

### L2 human

We check one subgroup in detail, the subgroup $A_3$ of step 5.

1. The product of $(1\,2\,3)$ with itself sends $1 \mapsto 2 \mapsto 3$, $2 \mapsto 3 \mapsto 1$ and $3 \mapsto 1 \mapsto 2$.
2. Thus $(1\,2\,3)^2 = (1\,3\,2)$.
3. In the same way, $(1\,2\,3)(1\,3\,2) = e$ and $(1\,3\,2)^2 = (1\,2\,3)$.
4. Thus $A_3$ is closed under products. The inverse of $(1\,2\,3)$ is $(1\,3\,2)$, so $A_3$ is closed under inverses.

The typical use is a first check of the CLT definition on a small group.
A trap is to stop at the prime divisors $2$ and $3$.
Here the divisor $6$ is the whole group, so there is nothing more to check, but for $A_4$ the missing order is the divisor $6$.
