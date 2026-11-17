---
tag: 6VFF2TTXYZ
kind: example
name: The left cosets of a subgroup of order two in S3
msc: ["20B30"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [564VVAQTNR, 03DEH43F4H]
illustrates: [3C53TD]
uses: [0515A6D2Y1, 09H9Y0Q11W, 0X1JXT47GA, 564VVAQTNR, 03DEH43F4H, 05FD317V2W, 3C53TD, 0DKMBWTD7P, 08QMKTWF9T]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: First example
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$, with permutations composed from right to left.
Let $H = \{e, (1\,2)\}$, a [[subgroup|0X1JXT47GA]] of order $2$.

1. We compute $(1\,3)(1\,2)$. The map $(1\,2)$ acts first: $1 \mapsto 2 \mapsto 2$, $2 \mapsto 1 \mapsto 3$, $3 \mapsto 3 \mapsto 1$. So $(1\,3)(1\,2) = (1\,2\,3)$.
2. In the same way, $(2\,3)(1\,2) = (1\,3\,2)$, $(1\,2\,3)(1\,2) = (1\,3)$ and $(1\,3\,2)(1\,2) = (2\,3)$.
3. The [[left cosets|03DEH43F4H]] are $eH = (1\,2)H = \{e, (1\,2)\}$, then $(1\,3)H = (1\,2\,3)H = \{(1\,3), (1\,2\,3)\}$, and $(2\,3)H = (1\,3\,2)H = \{(2\,3), (1\,3\,2)\}$.
4. Each of the $6$ elements of $S_3$ is in exactly one of these cosets. So they form a [[partition|08QMKTWF9T]] of $S_3$.
5. Each coset has $2$ elements, as the [[lemma on the size of cosets|0DKMBWTD7P]] states. Thus $6 = 3 \cdot 2$, as [[Lagrange's theorem|3C53TD]] states.

## Remarks

The example shows that each coset has several names: $(1\,3)H$ and $(1\,2\,3)H$ are the same set.
The right cosets of $H$ are different sets, because $H$ is not normal in $S_3$.
For example, $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ is not a left coset of $H$.
If we replace $H$ by $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, there are only $2$ left cosets, and they are also the right cosets.

## Explanations

### L1 human

Put three books on a shelf.
There are $6$ ways to arrange them.
Group the arrangements in pairs: an arrangement and the one you get by first swapping books $1$ and $2$.
You get $3$ pairs, and each arrangement is in exactly one pair.

### L2 human

We test whether $(1\,3)$ and $(1\,2\,3)$ lie in the same left coset.

1. Two elements $a$, $b$ lie in the same left coset if and only if $a^{-1}b \in H$.
2. Here $a^{-1} = (1\,3)$, because a transposition is its own inverse.
3. We compute $a^{-1}b = (1\,3)(1\,2\,3)$. The map $(1\,2\,3)$ acts first: $1 \mapsto 2 \mapsto 2$, $2 \mapsto 3 \mapsto 1$, $3 \mapsto 1 \mapsto 3$. So $a^{-1}b = (1\,2)$.
4. Since $(1\,2) \in H$, the two elements lie in the same left coset, which agrees with step 3 of the example.

The typical use of the test in step 1 is to decide coset membership without listing the cosets.
A trap is to use $ab^{-1}$ instead of $a^{-1}b$, which is the test for right cosets.
