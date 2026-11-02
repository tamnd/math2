---
tag: 8GRA22YEMB
kind: definition
name: Multidimensional Z-transform
msc: [44A55, 44A30]
defines: A7NF067M7N
uses: [5FY0JQGHYZ, 1P8WX3EGHF, 0GXMPDNYX3]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_transform
---

## Definition

Let $n \ge 1$ and let $x \colon \Z^n \to \C$ be a sequence, written $x[k]$ for $k = (k_1, \dots, k_n)$.
The *$n$-dimensional Z-transform* of $x$ is the function
$$X(z_1, \dots, z_n) = \sum_{k \in \Z^n} x[k]\, z_1^{-k_1} \cdots z_n^{-k_n},$$
defined at those $(z_1, \dots, z_n) \in (\C \setminus \set{0})^n$ where the series converges absolutely.
This set is its [[region of convergence|1P8WX3EGHF]].

## Remarks

For $n = 1$ this is the bilateral [[Z-transform|5FY0JQGHYZ]].
The series is a [[Laurent series|0GXMPDNYX3]] in several variables.
Absolute convergence at $(z_1, \dots, z_n)$ depends only on $(\abs{z_1}, \dots, \abs{z_n})$.

Example: $x[k_1, k_2] = a^{k_1} b^{k_2}$ for $k_1, k_2 \ge 0$ and $x[k] = 0$ otherwise, with $a, b \in \C$.
The sum is a product of two geometric series, and $X(z_1, z_2) = \frac{1}{(1 - a z_1^{-1})(1 - b z_2^{-1})}$ for $\abs{z_1} > \abs{a}$ and $\abs{z_2} > \abs{b}$.

Non-example: $x[k] = 1$ for all $k \in \Z^2$ has an empty region of convergence.
For every $z$, choose signs $\epsilon_1, \epsilon_2 \in \set{1, -1}$ with $\abs{z_j}^{-\epsilon_j} \ge 1$ for $j = 1, 2$.
Then the infinitely many terms with $k_j = \epsilon_j m_j$, $m_1, m_2 \ge 0$, all have absolute value at least $1$, so the series diverges.
