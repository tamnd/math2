---
tag: 3VFY8XCBEQ
kind: example
name: The pairs with x = 2y do not descend
msc: ["00A35", "11D04"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: 0EFYCFHYFG
    note: the smaller pair (y, y/2) is not always a pair of positive integers, so the descent leaves the set of solutions and stops
uses: [0EFYCFHYFG, 08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: lead section
---

## Example

Let $S$ be the set of pairs $(x, y)$ of positive integers with $x = 2y$.
Consider the rule $(x, y) \mapsto (y, y/2)$, with the size $x$.
The rule lowers the size and keeps the equation, and still it is not an [[infinite descent|0EFYCFHYFG]].
We check each condition.

1. The set $S$ is not empty: $(2, 1) \in S$, because $2 = 2 \cdot 1$.
   In fact $S = \{ (2k, k) : k \ge 1 \}$.
2. For $(x, y) = (2y, y)$ in $S$, the new pair $(y, y/2)$ satisfies the equation, because $y = 2 \cdot (y/2)$.
3. Its size is $y = x/2 < x$, so the rule lowers the size.
4. A descent also needs the new pair to lie in $S$, so $y/2$ must be a positive integer.
5. For $(x, y) = (2, 1)$ the new pair is $(1, \tfrac12)$, and $\tfrac12$ is not an integer, so the new pair is not in $S$.
6. The rule stays in $S$ only while $y$ is even.
   From $(24, 12)$ it gives $(12, 6)$, then $(6, 3)$, and then it stops, because $3$ is odd.
7. So each chain of smaller solutions is finite, and there is no contradiction.

The rule fails the condition "each element of $S$ gives a smaller element of $S$".
This agrees with step 1: the equation has solutions, so no correct descent can exist.

## Remarks

The non-example shows the heart of every descent proof: the new object must lie in the same set, inside the natural numbers.
A smaller object outside the set proves nothing.
Compare the equation $a^2 = 2b^2$ in positive integers.
There the rule $(a, b) \mapsto (2b - a, a - b)$ always gives positive integers, since $b < a < 2b$, and the descent proves that $\sqrt{2}$ is irrational.

The finite chain is useful in its own right.
It stops at a pair $(2k, k)$ with $k$ odd, so it writes the starting $y$ as a power of $2$ times an odd number.
For $(24, 12)$ the chain stops at $(6, 3)$, and indeed $12 = 2^2 \cdot 3$.

## Explanations

### L1 human

Pairs of the form "a number and its half" are easy to find: $2$ and $1$, $4$ and $2$, $6$ and $3$.
From $6$ and $3$ we would like the smaller pair $3$ and one and a half.
But one and a half is not a whole number, so the smaller pair is not allowed.
The chain stops, and so it proves nothing.
A real descent must give whole numbers at every step.

### L2 human

We run the rule from three starting pairs.
From $(16, 8)$ the chain is $(16, 8)$, $(8, 4)$, $(4, 2)$, $(2, 1)$, and then $(1, \tfrac12)$ is not allowed.
From $(10, 5)$ the next pair $(5, \tfrac52)$ is not allowed at once.
From $(48, 24)$ the chain is $(48, 24)$, $(24, 12)$, $(12, 6)$, $(6, 3)$, and then it stops.
Each chain is finite, and its number of pairs is the number of factors $2$ in $y$, plus one.

Check: $8 = 2^3$ gives $4$ pairs, $5$ has no factor $2$ and gives $1$ pair, and $24 = 2^3 \cdot 3$ gives $4$ pairs.
The typical use of this non-example is a checklist for a descent proof: the new object must satisfy the equation, lie in the same set and be strictly smaller.
Watch out: checking only the equation and the size, as in steps 2 and 3, misses the integrality of step 4.
