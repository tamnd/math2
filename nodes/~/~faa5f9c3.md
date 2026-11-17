---
tag: ~faa5f9c3
kind: example
name: Minimising a sum of squares term by term
msc: ["00A35", "26A06"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: ~8b9406d8
    note: the two terms share the variable x, so the partial results (minimisers x = 1 and x = 3) cannot be recombined into a minimiser of the sum
uses: [~8b9406d8, XNCV97HTZ8]
sources:
  - url: https://en.wikipedia.org/wiki/Completing_the_square
    locator: lead section
---

## Example

Problem: find the minimum of $f(x) = (x - 1)^2 + (x - 3)^2$ over all real $x$.
A naive [[decomposition|~8b9406d8]] splits $f$ into its two terms and minimises each one alone.
We follow it and see why the recombination fails.

1. The term $(x - 1)^2$ has its minimum $0$ at $x = 1$.
2. The term $(x - 3)^2$ has its minimum $0$ at $x = 3$.
3. The two partial answers ask for two different values of the same variable $x$. No single $x$ gives both minima, so the partial results cannot be combined.
4. Adding the minima gives $0 + 0 = 0$, but $f(x) = 0$ would need $x = 1$ and $x = 3$ at once, so $0$ is not attained.

The correct solution treats $f$ as a whole.

1. Expand: $f(x) = 2x^2 - 8x + 10$.
2. [[Complete the square|XNCV97HTZ8]]: $f(x) = 2(x - 2)^2 + 2$.
3. So $f(x) \geq 2$ for all $x$, with equality exactly at $x = 2$.

The minimum is $2$, at $x = 2$, and neither partial answer is the minimiser.

## Remarks

The decomposition fails because the pieces are coupled: both terms depend on the same variable.
If the variables are separate, the same idea works.
The function $g(x, y) = (x - 1)^2 + (y - 3)^2$ has its minimum $0$ at $(1, 3)$, found term by term.

The sum of the partial minima is still useful as a lower bound.
In general, $\min (u + v) \geq \min u + \min v$, and here the bound $0$ is below the true minimum $2$.

The midpoint $x = 2$ of the partial answers is the minimiser here only because the two terms have equal weight.
For $h(x) = (x - 1)^2 + 4(x - 3)^2 = 5x^2 - 26x + 37$, the minimum is at $x = \frac{13}{5} = 2.6$, with value $3.2$.
In general, $\sum w_i (x - a_i)^2$ has its minimum at the weighted mean $\frac{\sum w_i a_i}{\sum w_i}$.

## Explanations

### L1 human

Two friends live at kilometre $1$ and kilometre $3$ of a straight road, and they want to meet.
Each friend would like the meeting point to be at home.
Asking each friend alone gives two answers that cannot both be used.
The problem has one meeting point for both, so it must be solved as one problem.
With the cost measured as the sum of the squared distances, the best point is kilometre $2$.

### L2 human

We test whether a problem can be split into independent parts.

1. Write the objective as a sum $u + v$ of simpler pieces.
2. List the variables of each piece. If $u$ depends only on $x$ and $v$ only on $y$, the minimum of $u + v$ is $\min u + \min v$, attained at the pair of minimisers.
3. If the pieces share a variable, as here, the partial minimisers may disagree, and step 2 fails.
4. Then solve the coupled problem as a whole, here by completing the square, and use $\min u + \min v$ only as a lower bound.

The typical use: an objective is a sum of terms in separate variables, and each term is minimised alone.

A trap: the partial answers $1$ and $3$ suggest the answer $2$, which is correct here by the symmetry of the weights; with weights $1$ and $4$ the same guess is wrong.
