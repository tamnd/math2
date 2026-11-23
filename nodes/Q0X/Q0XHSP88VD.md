---
tag: Q0XHSP88VD
kind: example
name: A cutting-planes refutation of the four clauses on two variables
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
instance_of: [KKCX2HQP2K]
uses: [KKCX2HQP2K, T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

Let $F$ be the CNF with the four [[clauses|T3SXVH3ZZC]] $x \vee y$, $x \vee \neg y$, $\neg x \vee y$ and $\neg x \vee \neg y$.
Each of the four assignments to $x$ and $y$ falsifies exactly one clause, so $F$ is unsatisfiable.
Here is a [[cutting-planes refutation|KKCX2HQP2K]] of $F$ with $9$ lines.

1. $x + y \geq 1$, the line of $x \vee y$.
2. $x - y \geq 0$, the line of $x \vee \neg y$, since $x + (1 - y) \geq 1$ is $x - y \geq 0$.
3. $2x \geq 1$, the sum of lines 1 and 2.
4. $x \geq \lceil 1/2 \rceil = 1$, by division of line 3 by $c = 2$.
5. $-x + y \geq 0$, the line of $\neg x \vee y$, since $(1 - x) + y \geq 1$ is $-x + y \geq 0$.
6. $-x - y \geq -1$, the line of $\neg x \vee \neg y$, since $(1 - x) + (1 - y) \geq 1$ is $-x - y \geq -1$.
7. $-2x \geq -1$, the sum of lines 5 and 6.
8. $-x \geq \lceil -1/2 \rceil = 0$, by division of line 7 by $c = 2$.
9. $0 \geq 1$, the sum of lines 4 and 8.

Check the two roundings.
In line 4, $1/2$ rounds up to $1$.
In line 8, $-1/2$ rounds up to $0$, since $0$ is the least integer that is at least $-1/2$.

The length of the refutation is $9$ lines.
Its rank is $1$, since no line depends on two divisions in a chain, and every number in it has absolute value at most $2$.

## Remarks

The division steps cannot be avoided.
The point $x = y = 1/2$ satisfies all four clause lines, which evaluate to $1 \geq 1$, $0 \geq 0$, $0 \geq 0$ and $-1 \geq -1$.
It also satisfies the Boolean axioms.
So every line derived by linear combination alone holds at this point, and none of them is $0 \geq 1$.
Line 4 is the first line that the point violates.

The refutation follows the [[resolution|6JSH907W5R]] refutation step by step.
Lines 1 to 4 resolve $x \vee y$ and $x \vee \neg y$ to the clause $x$, lines 5 to 8 give the clause $\neg x$, and line 9 resolves the two.
With $n$ variables and all $2^n$ clauses on them, the same pattern removes one variable at a time with one division by $2$ per resolution step.

## Explanations

### L1 human

Two switches $x$ and $y$ can each be on or off.
The four rules forbid each of the four combinations, so no setting works.
Cutting planes shows this with sums: the first two rules add up to "two times $x$ is at least $1$".
Since $x$ is $0$ or $1$, this forces $x = 1$.
The last two rules force $x = 0$ in the same way, and the two facts contradict each other.

### L2 human

The method is to add two lines so that one variable cancels, and then to divide.
Lines 5 and 6 cancel $y$:
$$(-x + y) + (-x - y) \geq 0 + (-1), \quad \text{that is,} \quad -2x \geq -1.$$
This says $x \leq 1/2$, and since $x$ is an integer, division by $2$ turns it into $x \leq 0$.
Watch out for the direction of rounding.
In the $\geq$ form the right side rounds up, so $-1/2$ becomes $0$ and not $-1$.
Rounding down to $-1$ would give $-x \geq -1$, a true but useless line.
