---
tag: Z78WBAT2PA
kind: example
name: Equations that are not linear
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0Q3ZT8J05R
    note: each equation contains a product, a power or a function of an unknown
uses: [0Q3ZT8J05R]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_equation
    locator: lead section
---

## Example

We check three equations over $\R$ against the definition of a [[linear equation|0Q3ZT8J05R]].

1. In $xy = 1$, the term $xy$ is a product of two unknowns, not a constant times one unknown. So the equation is not linear.
2. In $x^2 + y = 1$, the term $x^2$ is a power of an unknown. So the equation is not linear.
3. In $\sin x + y = 0$, the term $\sin x$ is not of the form $a x$ with $a$ constant. So the equation is not linear.
4. A test for $xy = 1$: the solutions $(1, 1)$ and $(-1, -1)$ have midpoint $(0, 0)$, which is not a solution. For a linear equation, the midpoint of two solutions is always a solution.
5. A test for $x^2 + y = 1$: the solutions $(1, 0)$ and $(-1, 0)$ have midpoint $(0, 0)$, and $0 + 0 \ne 1$.

## Remarks

The midpoint test in steps 4 and 5 works because a linear left side $L$ satisfies $L(\tfrac12(s + t)) = \tfrac12 (L(s) + L(t))$.
So the solution set of a linear equation over $\R$ contains the whole line through any two of its points.

## Explanations

### L1 human

The graph of $xy = 1$ is a curve with two branches, and the graph of $x^2 + y = 1$ is a parabola.
Neither graph is a straight line.
That is a quick sign that these equations are not linear.

### L2 human

To decide whether an equation is linear, follow these steps.

1. Move all terms with unknowns to the left side.
2. Expand any brackets.
3. Check that each term is a constant, or a constant times exactly one unknown to the first power.

A trap: $(x + 1)^2 = x^2 + y$ looks nonlinear, but after expanding it becomes $2x - y = -1$, which is linear.
