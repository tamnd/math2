---
tag: 8YB9F8JDYY
kind: definition
name: Gini coefficient
msc: [91B82, 62P20]
defines: 22JK76F1SW
uses: [JEZ26SAXT1, 0PNRKMRC55, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Gini_coefficient
---

## Definition

Let $X$ be a non-negative [[random variable|0PNRKMRC55]] with finite positive [[mean|0WQNRCNY3M]] $\mu$, and let $L$ be its [[Lorenz curve|JEZ26SAXT1]].
The *Gini coefficient* of $X$ is
$$G = 1 - 2 \int_0^1 L(p) \, dp.$$
Equivalently, if $Y$ is an independent copy of $X$, then
$$G = \frac{\mathbb{E} \abs{X - Y}}{2 \mu}.$$
For values $x_1, \dots, x_n \ge 0$ with positive mean $\bar x$, taken with equal weights, this reads
$$G = \frac{1}{2 n^2 \bar x} \sum_{i=1}^n \sum_{j=1}^n \abs{x_i - x_j}.$$

## Remarks

Example: for incomes $1, 2, 3, 4$, the mean is $\bar x = 5/2$.
The six differences $\abs{x_i - x_j}$ with $i < j$ sum to $10$, so the double sum is $20$ and $G = 20/(2 \cdot 16 \cdot 5/2) = 1/4$.
The area under the Lorenz polygon is $3/8$ by the trapezoid rule, and $1 - 2 \cdot 3/8 = 1/4$ agrees.

Non-example: if all values are $0$, the hypothesis $\mu > 0$ fails and the Gini coefficient is not defined.

Always $0 \le G \le 1$, with $G = 0$ exactly when $X$ is almost surely constant.
For $n$ values the largest possible value is $(n - 1)/n$, reached when one value is positive and the others are $0$.
The coefficient does not change when all values are multiplied by the same positive number.
