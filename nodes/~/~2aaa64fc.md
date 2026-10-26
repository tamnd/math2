---
tag: ~2aaa64fc
kind: statement
role: proposition
name: Parallelogram law
msc: [46C05]
uses: [~9375149a]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: The parallelogram law in inner product spaces
same_as:
  wikidata: Q919125
  wikipedia: Parallelogram law
---

## Statement

Let $V$ be an inner product space over $\R$ or $\C$, with the [[induced norm|~0470436a]] $\norm{\cdot}$.
Then, for all $x, y \in V$,
$$\norm{x + y}^2 + \norm{x - y}^2 = 2 \norm{x}^2 + 2 \norm{y}^2.$$

## Remarks

The proof expands both squares with the inner product; the mixed terms cancel.
By the Jordan–von Neumann theorem, a norm comes from an inner product if and only if it satisfies this law.
The norm $\abs{x_1} + \abs{x_2}$ on $\R^2$ fails it for $x = (1, 0)$ and $y = (0, 1)$, so it comes from no inner product.

## Explanations

### L1 human

In a parallelogram, the squares of the two diagonals add up to the squares of the four sides.
The vectors $x + y$ and $x - y$ are the diagonals of the parallelogram with sides $x$ and $y$.
In a rectangle, both diagonals have the same length, and this is the Pythagorean theorem twice.
