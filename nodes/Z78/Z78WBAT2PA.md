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

We check three equations over $\mathbb{R}$ against the definition of a [[linear equation|0Q3ZT8J05R]], and we confirm the answer with a test on the solutions.

1. In $xy = 1$, the term $xy$ is a product of two unknowns, not a constant times one unknown. So the equation is not linear.
2. In $x^2 + y = 1$, the term $x^2$ is a power of an unknown. So the equation is not linear.
3. In $\sin x + y = 0$, the term $\sin x$ is not of the form $ax$ with $a$ constant. So the equation is not linear.
4. A test for $xy = 1$: the points $(1, 1)$ and $(-1, -1)$ are solutions, but their midpoint $(0, 0)$ gives $0 \cdot 0 = 0 \ne 1$.
5. A test for $x^2 + y = 1$: the points $(1, 0)$ and $(-1, 0)$ are solutions, but their midpoint $(0, 0)$ gives $0 + 0 \ne 1$.

## Remarks

The midpoint test works because a linear left side $L$ treats averages well:
$$L\big(\tfrac12 (s + t)\big) = \tfrac12 \big(L(s) + L(t)\big).$$
So if $L(s) = b$ and $L(t) = b$, the midpoint also gives $b$.
For a linear equation over $\mathbb{R}$, the solution set even contains the whole line through any two of its solutions.
A curved solution set, such as the hyperbola $xy = 1$ or the parabola $x^2 + y = 1$, fails this at once.

## Explanations

### L1 human

The graph of $xy = 1$ is a curve with two branches, and the graph of $x^2 + y = 1$ is a parabola.
Neither graph is a straight line, and that is a quick sign that these equations are not linear.

### L2 human

To decide whether an equation is linear, first move all terms with unknowns to the left side and expand every bracket.
Then check that each term is a constant, or a constant times exactly one unknown to the first power.
Watch out: some equations change type when you expand.
The equation $(x + 1)^2 = x^2 + y$ looks nonlinear, but expanding gives $x^2 + 2x + 1 = x^2 + y$, which is the linear equation $2x - y = -1$.
