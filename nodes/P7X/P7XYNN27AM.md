---
tag: P7XYNN27AM
kind: definition
name: Isotonic regression
msc: [62G08, 62G05]
defines: JAFPWZDM95
uses: [0BYTQ4X1HC, 0WFF6AZPBP, 0K06X9QXDX]
sources:
  - url: https://en.wikipedia.org/wiki/Isotonic_regression
---

## Definition

Let $y_1, \dots, y_n \in \R$ be data observed at points $x_1 < x_2 < \dots < x_n$, and let $w_1, \dots, w_n > 0$ be weights.
The *isotonic regression* of $y$ is the vector $\hat y \in \R^n$ that minimises
$$\sum_{i=1}^{n} w_i (y_i - z_i)^2$$
over all $z \in \R^n$ with $z_1 \le z_2 \le \dots \le z_n$.

## Remarks

The set of non-decreasing vectors is a closed [[convex|0K06X9QXDX]] cone, so $\hat y$ is the projection of $y$ onto it for the weighted inner product, and it exists and is unique.
It has the min-max formula $\hat y_i = \max_{s \le i} \min_{t \ge i} \mathrm{Av}(s, t)$, where $\mathrm{Av}(s, t) = \sum_{k=s}^{t} w_k y_k / \sum_{k=s}^{t} w_k$.
The pool adjacent violators algorithm computes $\hat y$ in $O(n)$ steps: it merges adjacent blocks whose averages are out of order and replaces them by their weighted average.
The same definition works for any partial order on the index set, with $z_i \le z_j$ required whenever $i$ precedes $j$.

Example: $y = (1, 3, 2)$ with equal weights.
The pair $3, 2$ violates the order, and pooling gives $\hat y = (1, 2.5, 2.5)$, which is non-decreasing.
Its squared error is $0 + 0.25 + 0.25 = 0.5$.

Non-example: $z = (1, 3, 2)$ itself has error $0$ but it is not non-decreasing, so it is not admissible; the [[monotone|0WFF6AZPBP]] constraint is what makes $\hat y$ differ from $y$.
