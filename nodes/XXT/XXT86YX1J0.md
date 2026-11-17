---
tag: XXT86YX1J0
kind: example
name: A5 is not a CLT group
msc: ["20D60", "20D06"]
topics: [1VHQWXC64D]
audience: ug2
not_instance_of:
  - target: Y9CB5P4YCS
    note: the order 60 of A5 is divisible by 30, but A5 has no subgroup of order 30
uses: [0Z5905Q73D, 0X1JXT47GA, 0B85S2V2DR, 03DEH43F4H, 0DTXBQPA2S, 0Z05VCBQ7Y, 3C53TD]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Existence of subgroups of given order
---

## Example

Let $A_5$ be the [[alternating group|0Z5905Q73D]] of the even permutations of $\{1, 2, 3, 4, 5\}$, with identity $e$.
Permutations compose from right to left.
The [[order|0B85S2V2DR]] of $A_5$ is $5!/2 = 60$, and $30$ divides $60$.
But $A_5$ has no [[subgroup|0X1JXT47GA]] of order $30$, so $A_5$ is not a [[CLT group|Y9CB5P4YCS]].

1. Assume that $H$ is a subgroup of $A_5$ of order $30$.
2. By [[Lagrange's theorem|3C53TD]], the [[index|0DTXBQPA2S]] of $H$ is $60/30 = 2$.
3. Thus $H$ has two [[left cosets|03DEH43F4H]]: $H$ itself, and $gH = A_5 \setminus H$ for each $g \notin H$.
4. Claim: $g^2 \in H$ for each $g \in A_5$. If $g \in H$, then $g^2 \in H$, because $H$ is a subgroup.
5. Let $g \notin H$, and assume that $g^2 \notin H$. Then $g^2 \in gH$ by step 3.
6. So $g^2 = gh$ for some $h \in H$. Then $g = h \in H$, a contradiction. This proves the claim.
7. Let $c$ be a [[cycle|0Z05VCBQ7Y]] of length $3$. Then $c^3 = e$, so $c = c^4 = (c^2)^2$ is a square.
8. Let $c$ be a cycle of length $5$. Then $c^5 = e$, so $c = c^6 = (c^3)^2$ is a square.
9. There are $\binom{5}{3} \cdot 2 = 20$ cycles of length $3$ in $A_5$.
10. There are $4! = 24$ cycles of length $5$ in $A_5$.
11. By steps 4 to 10, $H$ contains these $20 + 24 = 44$ elements, and also $e$.
12. Thus $|H| \ge 45 > 30$. This contradicts step 1.
13. Thus $A_5$ has no subgroup of order $30$, and $A_5$ is not CLT.

## Remarks

The example shows that the converse of Lagrange's theorem fails for a group of order $60$.
It also fails for [[the group $A_4$ of order $12$|0PDBVPP233]].
The proof is the same as for $A_4$: a subgroup of index $2$ contains all squares, and there are too many squares.
The group $A_5$ also has no subgroup of order $15$ or $20$, but these facts need other arguments.
The group $A_5$ is simple and not solvable, so it is also not CLT by the result that each CLT group is solvable.
The proof above does not use this result.

## Explanations

### L1 human

The group $A_5$ has $60$ elements, and $30$ divides $60$.
A subgroup with $30$ elements would be exactly half of the group.
Such a half must contain the square of each element.
But $45$ elements of $A_5$ are squares, and $45$ is more than half of $60$.

### L2 human

We count the squares in $A_5$ by the type of the element.

1. The elements of $A_5$ are $e$, $15$ products of two disjoint transpositions, $20$ $3$-cycles and $24$ $5$-cycles.
2. The sum is $1 + 15 + 20 + 24 = 60$, as it must be.
3. The square of a product of two disjoint transpositions is $e$.
4. The square of a $3$-cycle is a $3$-cycle, for example $(1\,2\,3)^2 = (1\,3\,2)$.
5. The square of a $5$-cycle is a $5$-cycle, for example $(1\,2\,3\,4\,5)^2 = (1\,3\,5\,2\,4)$.
6. By steps 7 and 8 of the example, each $3$-cycle and each $5$-cycle is a square.
7. Thus the set of squares has $1 + 20 + 24 = 45$ elements.

The typical use of the argument is to exclude subgroups of index $2$.
A trap is to think that a subgroup of index $2$ contains all elements of order $2$.
It contains all squares, and an element of order $2$ need not be a square.
