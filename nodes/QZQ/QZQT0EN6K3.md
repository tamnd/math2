---
tag: QZQT0EN6K3
kind: example
name: The sum of k over 2 to the k by a power series
msc: ["00A35", "40A05"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [8NJ0VN9Z97]
uses: [8NJ0VN9Z97, 0MZB06ST2B, 0TJ8QBJX5K]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_series
    locator: lead section
---

## Example

We compute
$$S = \sum_{k=1}^{\infty} \frac{k}{2^k} = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \cdots$$
by [[generalization|8NJ0VN9Z97]]: the number $\frac{1}{2}$ becomes a variable $x$.

1. We generalize.
   Let $g(x) = \sum_{k=1}^{\infty} k x^k$, a [[power series|0MZB06ST2B]], so that $S = g\left(\frac{1}{2}\right)$.
2. We find a known relative, the geometric series:
   $$\sum_{k=0}^{\infty} x^k = \frac{1}{1 - x}, \qquad |x| < 1.$$
3. We use the new tool.
   By [[term-by-term differentiation|0TJ8QBJX5K]], valid inside the radius of convergence $1$,
   $$\sum_{k=1}^{\infty} k x^{k-1} = \frac{1}{(1 - x)^2}, \qquad |x| < 1.$$
4. We multiply by $x$, which gives $g(x) = \frac{x}{(1 - x)^2}$ for $|x| < 1$.
5. We specialize to $x = \frac{1}{2}$:
   $$S = \frac{1/2}{(1/2)^2} = 2.$$

Check with partial sums: they are $0.5$, $1$, $1.375$, $1.625$ and $1.78125$, and the first $10$ terms add to $\frac{509}{256} \approx 1.988$.

## Remarks

The given series has no variable, so we could not differentiate it.
The general series $g(x)$ is a function, and its link to the geometric series is a derivative.
The same family gives $\sum_{k=1}^{\infty} \frac{k}{3^k} = g\left(\frac{1}{3}\right) = \frac{3}{4}$, and a second differentiation gives
$$\sum_{k=1}^{\infty} k^2 x^k = \frac{x(1 + x)}{(1 - x)^3}, \qquad |x| < 1.$$

A direct proof also exists.
The sum of the first $n$ terms is $2 - \frac{n + 2}{2^n}$, which induction proves and which tends to $2$.
The generalization found the value without any need to guess this formula.

## Explanations

### L1 human

Write the sum as a staircase of rows.
The first row is $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$, the second row is $\frac{1}{4} + \frac{1}{8} + \cdots$, the third is $\frac{1}{8} + \cdots$, and so on.
The term $\frac{3}{8}$ of the sum appears as one $\frac{1}{8}$ in each of the first three rows.
The rows add to $1$, $\frac{1}{2}$, $\frac{1}{4}$ and so on, and these add to $2$.
The power series method gives the same $2$ by a calculation that works for every base.

### L2 human

We use the generalization once more for $T = \sum_{k=1}^{\infty} \frac{k^2}{2^k}$.
Differentiate $\sum k x^k = \frac{x}{(1 - x)^2}$ term by term:
$$\sum_{k=1}^{\infty} k^2 x^{k-1} = \frac{1 + x}{(1 - x)^3}.$$
Multiply by $x$ and put $x = \frac{1}{2}$:
$$T = \frac{\frac{1}{2} \cdot \frac{3}{2}}{\frac{1}{8}} = 6.$$
Check: the first $20$ terms add to $6 - \frac{486}{2^{20}} \approx 5.9995$.

This is the typical use: a factor $k$ in the terms points to a derivative of $x^k$.
Watch out for the range: the formula $\frac{x}{(1 - x)^2}$ holds only for $|x| < 1$, and at $x = 2$ it gives $2$, while the series $\sum k \, 2^k$ diverges.
