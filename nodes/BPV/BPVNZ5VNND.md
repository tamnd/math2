---
tag: BPVNZ5VNND
kind: example
name: A left coset of {e, (1 2)} in S3 that is not a right coset of it
msc: ["20B30"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [03DEH43F4H]
not_instance_of:
  - target: 0NE1DK7H4T
    note: the set {(1 3), (1 2 3)} is a left coset of H = {e, (1 2)} but not a right coset of H
uses: [0515A6D2Y1, 09H9Y0Q11W, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: First example
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Example

Let $G = S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$, with permutations composed from right to left.
Let $H = \{e, (1\,2)\}$, a [[subgroup|0X1JXT47GA]] of order $2$.
Let $C = (1\,3)H$.

1. By the definition of a [[left coset|03DEH43F4H]], $C = \{(1\,3)e, (1\,3)(1\,2)\}$.
2. We compute $(1\,3)(1\,2)$. The map $(1\,2)$ acts first. Then $1 \mapsto 2 \mapsto 2$, $2 \mapsto 1 \mapsto 3$ and $3 \mapsto 3 \mapsto 1$. Thus $(1\,3)(1\,2) = (1\,2\,3)$.
3. So $C = \{(1\,3), (1\,2\,3)\}$.
4. The [[right cosets|0NE1DK7H4T]] of $H$ are $H$, $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ and $H(2\,3) = \{(2\,3), (1\,2\,3)\}$. Here $(1\,2)(1\,3) = (1\,3\,2)$ and $(1\,2)(2\,3) = (1\,2\,3)$, by the same method as step 2.
5. The set $C$ is not equal to any of these three sets. Thus $C$ is a left coset of $H$ but not a right coset of $H$.

## Remarks

The example is the mirror image of the [[right coset that is not a left coset|M9F4BWH6EN]].
The two partitions of $S_3$ differ because $H$ is not [[normal|0CB0DX5BVV]].
The set $C$ is a right coset of the conjugate subgroup $K = (1\,3)H(1\,3) = \{e, (2\,3)\}$.
Indeed $K(1\,3) = \{(1\,3), (2\,3)(1\,3)\} = \{(1\,3), (1\,2\,3)\} = C$.
In general, $gH = (gHg^{-1})g$, so each left coset of $H$ is a right coset of a conjugate of $H$.

## Explanations

### L1 human

Take the six ways to arrange three objects, and the subgroup $H$ of the two moves "do nothing" and "swap $1$ and $2$".
Do the swap first and then the move $(1\,3)$.
This gives the left coset $(1\,3)H$.
If you do the swap after the move $(1\,3)$, you get a different pair of moves.

### L2 human

We test whether $C = \{(1\,3), (1\,2\,3)\}$ is a right coset of $H$.

1. A right coset that contains $(1\,3)$ is equal to $H(1\,3)$, because each element of a coset is a representative.
2. We computed $H(1\,3) = \{(1\,3), (1\,3\,2)\}$.
3. This set is not $C$, because $(1\,2\,3) \neq (1\,3\,2)$.
4. So $C$ is not a right coset of $H$.

The typical use of step 1 is a fast test: to check if a set is a coset, compute the coset of one of its elements and compare.
A trap is to conclude that $C$ is not a coset of any subgroup.
It is a right coset of the subgroup $\{e, (2\,3)\}$.
