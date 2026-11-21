---
tag: 30AYM35BMY
kind: example
name: Lists of measurements as vectors in R^4
msc: ["15A03", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0QN3D80AWP]
uses: [0QN3D80AWP, 00EBGSR5NY]
sources:
  - url: https://en.wikipedia.org/wiki/Real_coordinate_space
    locator: lead section
  - url: https://understandinglinearalgebra.org/
    locator: Section 2.1
---

## Example

A shop records its sales of bread on four days, Monday to Thursday.
In week $1$ the sales are $x = (20, 18, 25, 22)$, and in week $2$ they are $y = (22, 16, 27, 20)$.
Both lists are [[vectors|00EBGSR5NY]] of $\mathbb{R}^4$, and we compute with them component by component.

1. The total sales of the two weeks are the sum:
   $$x + y = (20 + 22, \; 18 + 16, \; 25 + 27, \; 22 + 20) = (42, 34, 52, 42).$$
2. The mean of the two weeks is half of the sum, $\tfrac{1}{2}(x + y) = (21, 17, 26, 21)$.
3. The change from week $1$ to week $2$ is the difference, $y - x = (2, -2, 2, -2)$.
4. If each loaf gives a profit of $3$ units of money, the profit of week $1$ is the multiple $3x = (60, 54, 75, 66)$.

## Remarks

A vector of $\mathbb{R}^n$ need not be an arrow that you can draw.
The rules for the sum and for multiples are the same as in the plane, only with more components, and each component keeps its meaning: the first is always Monday.
That is why the order matters, and $(20, 18, 25, 22)$ and $(18, 20, 25, 22)$ are different vectors.
If the shop adds a fifth day, the vectors move to $\mathbb{R}^5$, and nothing else changes.

## Explanations

### L1 human

A vector can be a list of numbers, one number for each day.
Adding two lists means adding the numbers in the same position.
For example, $20$ loaves on Monday of week $1$ and $22$ on Monday of week $2$ make $42$ loaves.

### L2 human

The mean $\tfrac{1}{2}(x + y)$ is also the midpoint of $x$ and $y$ in $\mathbb{R}^4$.
The same formula gives the midpoint of a segment in the plane or in space, so a fact of geometry and a fact of bookkeeping are one computation.
Watch out: you can add only vectors with the same number of components, so $(1, 2) + (1, 2, 3)$ has no meaning.
