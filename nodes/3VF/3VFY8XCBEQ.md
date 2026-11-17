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
We show that this rule is not an [[infinite descent|0EFYCFHYFG]], and that $S$ is not empty.

1. The set $S$ is not empty: $(2, 1)$ is in $S$, because $2 = 2 \cdot 1$. In fact $S = \{(2k, k) : k \ge 1\}$.
2. For $(x, y) = (2y, y)$ in $S$, the new pair $(y, y/2)$ satisfies the equation, because $y = 2 \cdot (y/2)$.
3. Its size is $y = x/2 < x$. So the rule lowers the size.
4. But a descent needs the new pair to lie in $S$, so $y/2$ must be a positive integer.
5. For $(x, y) = (2, 1)$ the new pair is $(1, \tfrac12)$, and $\tfrac12$ is not an integer. So the new pair is not in $S$.
6. The rule works only when $y$ is even. Starting from $(24, 12)$, it gives $(12, 6)$, then $(6, 3)$, and then it stops, because $3$ is odd.
7. So the chain of smaller solutions is finite, and there is no contradiction.

The rule fails the condition "each element of $S$ gives a smaller element of $S$".
This agrees with step 1: the equation has solutions, so no correct descent can exist.

## Remarks

1. Compare with $a^2 = 2b^2$, where the rule $(a, b) \mapsto (2b - a, a - b)$ always gives positive integers, and the descent proves that $\sqrt{2}$ is irrational.
2. The non-example shows that the check "the new object is again in the set" is the heart of a descent proof. A smaller object outside the set proves nothing.
3. The finite chain of step 6 is useful in its own right: it stops at a pair $(2k, k)$ with $k$ odd. This proves that each positive integer is $2^e$ times an odd number.

## Explanations

### L1 human

The pairs "a number and its half" are easy to find: $2$ and $1$, $4$ and $2$, $6$ and $3$.
From $6$ and $3$ we would like the smaller pair $3$ and one and a half.
But one and a half is not a whole number, so the smaller pair is not allowed.
The chain stops, and so it proves nothing.
A real descent must give whole numbers at every step.

### L2 human

We test the descent rule on several starting pairs.

1. Start at $(16, 8)$: the chain is $(16, 8)$, $(8, 4)$, $(4, 2)$, $(2, 1)$, and then $(1, \tfrac12)$ is not allowed.
2. Start at $(10, 5)$: the next pair $(5, \tfrac52)$ is not allowed at once.
3. Start at $(48, 24)$: the chain is $(48, 24)$, $(24, 12)$, $(12, 6)$, $(6, 3)$, and then it stops.
4. Each chain has finitely many pairs, and its length is the number of factors $2$ in $y$, plus one.

The typical use of this non-example is a check list for a descent proof: the new object must satisfy the equation, lie in the same set and be strictly smaller.
A trap is to check only the equation and the size, as in steps 2 and 3, and forget the integrality of step 4.
