---
tag: 77SJHGNFR8
kind: example
name: The polynomial x^2 - 2x + 2 is positive for every real x
msc: ["00A35", "26D05"]
topics: [958EF46EYJ]
audience: school
instance_of: [CX38X989TB]
uses: [CX38X989TB, XNCV97HTZ8, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_generalization
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Completing_the_square
    locator: lead section
---

## Example

Statement: for every [[real number|08J2M1JYAG]] $x$, $x^2 - 2x + 2 > 0$.
We [[prove the universal statement|CX38X989TB]] with a generic element.

1. Let $x$ be an arbitrary real number.
   We assume nothing else about $x$.
2. [[Complete the square|XNCV97HTZ8]]:
   $$x^2 - 2x + 2 = (x^2 - 2x + 1) + 1 = (x - 1)^2 + 1.$$
3. The square of a real number is never negative, so $(x - 1)^2 \ge 0$.
4. Add $1$ to both sides: $(x - 1)^2 + 1 \ge 1$.
5. By steps 2 and 4, $x^2 - 2x + 2 \ge 1 > 0$.
6. Step 1 put no condition on $x$, so steps 2 to 5 hold for each real number, and the statement holds for all real $x$.

Check: $x = 0$ gives $2$, $x = 1$ gives $1$, and $x = -3$ gives $9 + 6 + 2 = 17$.

## Remarks

The proof gives more than the statement asks.
The value is at least $1$, and it equals $1$ exactly when $(x - 1)^2 = 0$, that is, at $x = 1$.
So the bound $x^2 - 2x + 2 \ge 1$ is sharp, and the polynomial has its minimum $1$ at $x = 1$.

A change of the constant term changes the answer.
For $x^2 - 2x + c$ the same computation gives
$$x^2 - 2x + c = (x - 1)^2 + (c - 1),$$
so the polynomial is positive for every real $x$ exactly when $c > 1$.
For $c = 1$ it is $0$ at $x = 1$, and for $c < 1$ it is negative at $x = 1$.
A few checks cannot see this.
For $c = 0.5$, the values at $x = 0, 2, 3$ are $0.5$, $0.5$ and $3.5$, all positive, but the value at $x = 1$ is $-0.5$.

## Explanations

### L1 human

The claim is that $x^2 - 2x + 2$ is a positive number, whatever number $x$ is.
Try $x = 0$ and the value is $2$; try $x = 1$ and it is $1$; try $x = 5$ and it is $17$.
These tries do not cover all numbers.
The proof rewrites the expression as "a square plus $1$".
A square is never negative, so the sum is at least $1$ for every $x$.

### L2 human

The same method works for a polynomial in two variables: for all real $x$ and $y$, $x^2 + xy + y^2 \ge 0$.
Let $x$ and $y$ be arbitrary real numbers, and complete the square in $x$:
$$x^2 + xy + y^2 = \left(x + \frac{y}{2}\right)^2 + \frac{3}{4} y^2.$$
Check by expanding: $\left(x + \frac{y}{2}\right)^2 = x^2 + xy + \frac{1}{4} y^2$, and $\frac{1}{4} y^2 + \frac{3}{4} y^2 = y^2$.
Both terms on the right are at least $0$, so their sum is at least $0$.
The typical use is the one shown: an expression written as a sum of squares is non-negative for all values of its variables.
Watch out: "for $x = y = 1$ the value is $3 > 0$" proves nothing about all $x$ and $y$.
