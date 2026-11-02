---
tag: T942SHWSSF
kind: definition
name: Divided differences
msc: [65D05, 41A05, 39A70]
defines: N5ZHV4HWDC
uses: [0EPAT51DXQ, 04C5ZBG1WT, SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Divided_differences
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] and let $f$ be a [[function|0EPAT51DXQ]] from a subset of $K$ to $K$.
Let $x_0, \dots, x_n$ be pairwise distinct points of its domain.
The *divided differences* of $f$ are defined by recursion on the number of points:

1. $f[x_i] = f(x_i)$ for each $i$;
2. for $k \ge 1$ and $0 \le i \le n - k$,
$$f[x_i, \dots, x_{i+k}] = \frac{f[x_{i+1}, \dots, x_{i+k}] - f[x_i, \dots, x_{i+k-1}]}{x_{i+k} - x_i}.$$

## Remarks

The value $f[x_0, \dots, x_n]$ is a symmetric function of the points: it does not depend on their order.
It has the closed form
$$f[x_0, \dots, x_n] = \sum_{j=0}^{n} \frac{f(x_j)}{\prod_{k \ne j} (x_j - x_k)}.$$
It is the coefficient of $x^n$ in the [[interpolation polynomial|SS1YMS2NPC]] of $f$ at $x_0, \dots, x_n$.
For a real function $f$ with enough derivatives, the definition extends to repeated points by continuity; for example $f[x, x] = f'(x)$.

Example: for $f(x) = x^2$ and the points $0, 1, 3$: $f[0, 1] = 1$, $f[1, 3] = \frac{9 - 1}{2} = 4$, and $f[0, 1, 3] = \frac{4 - 1}{3 - 0} = 1$.
This is the leading coefficient of $x^2$, as expected.

Non-example: the recursion cannot be applied to the list $1, 1$ of repeated points, because the denominator $x_1 - x_0$ is $0$.
