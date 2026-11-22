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

The claim is that the equation $x^2 - 61y^2 = 1$ has no solution in positive integers.
Someone writes a program that checks, for each $y$ from $1$ to $10^6$, whether $61y^2 + 1$ is a perfect square.
It finds none, and the claim is offered as proved.

This is not a [[proof of impossibility|6F55216R53]], and in fact the claim is false.
A proof of impossibility must show that every candidate fails, and here the candidates are all pairs of positive integers.
The search covers only $y \leq 10^6$, so the pairs with $y > 10^6$ are never examined.
The equation is a [[Pell equation|0Z0NE3J6JX]], and its smallest solution in positive integers is
$$x = 1766319049, \qquad y = 226153980.$$
Check: $1766319049^2 - 61 \cdot 226153980^2 = 1$, which a computer confirms in exact integer arithmetic.
So the claim fails at a value of $y$ more than $200$ times the bound of the search.

## Remarks

The output of the search is correct: no solution has $y \leq 10^6$.
The error is only the step from "none found" to "none exists".

For a Pell equation $x^2 - dy^2 = 1$, with $d$ a positive integer that is not a square, a theorem guarantees a solution in positive integers for every such $d$.
The size of the smallest solution varies wildly with $d$.
For $d = 60$ it is $x = 31$, $y = 4$, since $961 - 960 = 1$, while for $d = 61$ the value of $x$ has ten digits.
Bhāskara II solved the case $d = 61$ in the twelfth century, and Pierre de Fermat proposed it as a challenge in 1657.

## Explanations

### L1 human

A computer tried a million values and found no solution.
That sounds convincing, but there are infinitely many values to try.
The first solution has a $y$ of about $226$ million, far beyond the million that were checked.
A search can find a solution, but a search that finds nothing proves nothing about the values it did not try.

### L2 human

Compare the search with a true impossibility proof for the nearby equation $x^2 - 61y^2 = 2$.
Any integer solution gives $x^2 \equiv 2 \pmod{61}$, so $2$ would have to be a square modulo $61$.
Since $61 \equiv 5 \pmod 8$, the second supplement to quadratic reciprocity says that $2$ is not a square modulo $61$.
You can also confirm this by listing the remainders of $0^2, 1^2, \ldots, 60^2$ on division by $61$ and seeing that $2$ is missing.
So $x^2 - 61y^2 = 2$ has no integer solution.
That finite list is a proof, because every integer $x$ has one of the $61$ remainders, so the list covers every candidate.
The lesson is that a finite check proves impossibility only when its finitely many cases cover all candidates.
Watch out: the failed search and the list of remainders are both finite, but only the second one covers everything.
