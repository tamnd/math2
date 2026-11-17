---
tag: NAQDKVNJCR
kind: example
name: A failed search for a solution of x^2 - 61y^2 = 1
msc: ["00A35", "11D09"]
topics: [958EF46EYJ]
audience: ug1
not_instance_of:
  - target: 6F55216R53
    note: checking all y up to 10^6 leaves the other values of y unchecked, and the equation does have a solution with y = 226153980
uses: [6F55216R53, 0Z0NE3J6JX]
sources:
  - url: https://en.wikipedia.org/wiki/Pell%27s_equation
    locator: lead section
---

## Example

Claim: the equation $x^2 - 61y^2 = 1$ has no solution in positive integers.
Someone writes a program that checks, for each $y$ from $1$ to $10^6$, whether $61y^2 + 1$ is a perfect square.
It finds none, and the claim is offered as proved.

This is not a [[proof of impossibility|6F55216R53]], and the claim is false.
We check the condition that fails.

1. A proof of impossibility must show that every candidate fails. Here the candidates are all pairs of positive integers.
2. The search covers only $y \leq 10^6$. The pairs with $y > 10^6$ are not checked.
3. The equation is a [[Pell's equation|0Z0NE3J6JX]], and its smallest positive solution is $x = 1766319049$, $y = 226153980$.
4. Check: $1766319049^2 - 61 \cdot 226153980^2 = 1$. So the claim fails, at a value of $y$ more than $200$ times the bound of the search.

## Remarks

The result of the search is correct: no solution has $y \leq 10^6$.
The error is only in the step from "none found" to "none exists".

For Pell's equations $x^2 - dy^2 = 1$, with $d$ a positive integer that is not a square, a theorem guarantees a solution in positive integers for every such $d$.
The size of the smallest solution varies a lot with $d$: for $d = 60$ it is $x = 31$, $y = 4$, and for $d = 61$ it has ten digits.
Bhāskara II solved the case $d = 61$ in the twelfth century, and Pierre de Fermat proposed it as a challenge in 1657.

## Explanations

### L1 human

A computer tried a million values and found no solution.
That sounds convincing, but there are infinitely many values to try.
The first solution has a $y$ of about $226$ million, far beyond the million that were checked.
A search can find a solution, but a search that finds nothing proves nothing about the values it did not try.

### L2 human

We compare the search with a real impossibility proof for a nearby equation, $x^2 - 61y^2 = 2$.

1. Reduce modulo $61$: any solution gives $x^2 \equiv 2 \pmod{61}$.
2. The remainders of the squares $0^2, 1^2, \ldots, 60^2$ on division by $61$ can be listed, and one checks whether $2$ appears.
3. Since $61 \equiv 5 \pmod 8$, the number $2$ is not a square modulo $61$; this follows from the second supplement to quadratic reciprocity.
4. So $x^2 - 61y^2 = 2$ has no integer solution. Here the finite check in step 2 covers all integers $x$, because every integer has one of the $61$ remainders.

The typical use: a finite check is a proof only when the finitely many cases cover all candidates, as remainders do.

A trap: the search in the example and the check in step 2 are both finite, but only the second one covers every candidate.
