---
tag: 2AKFNAGF1N
kind: definition
name: Positive linear operator
msc: [47B65, 41A36, 46A40]
defines: AQDXWH4812
uses: [000AYPA9AJ, 0QV2JS9RJ3, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_linear_operator
---

## Definition

Let $X$ and $Y$ be real [[vector spaces|000AYPA9AJ]], each with a preorder $\le$, such as a [[partial order|0QV2JS9RJ3]], compatible with the vector operations.
Compatible means that $x \le y$ implies $x + z \le y + z$ and $tx \le ty$ for all vectors $z$ and all real $t \ge 0$.
A [[linear map|0NRYHJPQG2]] $L \colon X \to Y$ is a *positive linear operator* if $x \ge 0$ implies $L x \ge 0$ for every $x \in X$.

## Remarks

Equivalently, $L$ is monotone: $x \le y$ implies $L x \le L y$, since $L y - L x = L(y - x)$.

Example: on $C[0, 1]$ with the pointwise order $f \le g$ when $f(x) \le g(x)$ for all $x$, the Bernstein operator
$$B_n f(x) = \sum_{k=0}^{n} \binom{n}{k} x^k (1 - x)^{n-k} f(k/n)$$
is positive, because all weights $\binom{n}{k} x^k (1 - x)^{n-k}$ are nonnegative on $[0, 1]$.

Non-example: differentiation $D \colon C^1[0, 1] \to C[0, 1]$ is linear but not positive.
The function $f(x) = 1 - x$ satisfies $f \ge 0$, while $D f = -1 < 0$.

For a compact Hausdorff space $K$ and a positive linear operator $L \colon C(K) \to C(K)$ with the uniform norm, $L$ is bounded with $\norm{L} = \norm{L 1}$.
Indeed $-\norm{f} \cdot 1 \le f \le \norm{f} \cdot 1$ gives $\abs{L f} \le \norm{f} \, L 1$.
A positive linear functional is the case $Y = \R$; on $C(K)$ these are the integrals against finite positive measures.
