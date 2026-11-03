---
tag: 9QXBBQWH0T
kind: definition
name: Bent function
msc: ["06E30", 94A60, 94A55]
defines: BBDDJMX1CB
uses: [0X05GS525E, K784BA2WHV, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Bent_function
---

## Definition

Let $n \ge 1$ and let $f \colon \F_2^n \to \F_2$ be a [[Boolean function|0X05GS525E]].
For $a, x \in \F_2^n$ write $a \cdot x = a_1 x_1 + \cdots + a_n x_n \in \F_2$.
The [[Walsh–Hadamard transform|K784BA2WHV]] of $f$ is the function
$$W_f(a) = \sum_{x \in \F_2^n} (-1)^{f(x) + a \cdot x}, \qquad a \in \F_2^n.$$
The function $f$ is *bent* if $\abs{W_f(a)} = 2^{n/2}$ for every $a \in \F_2^n$.

## Remarks

By Parseval's identity $\sum_a W_f(a)^2 = 2^{2n}$, so $2^{n/2}$ is the smallest possible value of $\max_a \abs{W_f(a)}$.
Since $W_f(a)$ is an integer, $2^{n/2}$ must be an integer, so bent functions exist only for even $n$.
Equivalently, $f$ is bent when its Hamming distance to every affine function is $2^{n-1} \pm 2^{n/2 - 1}$, the largest possible nonlinearity $2^{n-1} - 2^{n/2-1}$.

Example: $n = 2$ and $f(x_1, x_2) = x_1 x_2$.
Then $W_f(0,0) = 1 + 1 + 1 - 1 = 2$, $W_f(1, 0) = 1 + 1 - 1 + 1 = 2$, $W_f(0, 1) = 2$ by symmetry, and $W_f(1, 1) = 1 - 1 - 1 - 1 = -2$.
All have absolute value $2 = 2^{2/2}$, so $f$ is bent.
More generally $x_1 x_2 + x_3 x_4 + \cdots + x_{n-1} x_n$ is bent for even $n$.

Non-example: $n = 2$ and the linear function $f(x) = x_1$.
Then $W_f(1, 0) = 4$ and $W_f(a) = 0$ for $a \ne (1, 0)$, so $\abs{W_f}$ is not constant and $f$ is not bent.

Rothaus introduced the name in 1976.
