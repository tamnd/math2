---
tag: 0TCBZMEYGN
kind: statement
role: proposition
name: C^k function characterised by continuous derivatives
msc: [26B05]
uses: [0EY05Z9RPN, 02RSXVM1ZN]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothness
    locator: Multivariate differentiability classes
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}^m$, and let $k \ge 1$ be an integer.
Say that $f$ is of class $C^k$ on $U$ when the following is true for each component $f_j$ and each $r \le k$. Each [[partial derivative|02RSXVM1ZN]] $\partial^r f_j / \partial x_{i_r} \cdots \partial x_{i_1}$ of order $r$ exists on $U$ and is continuous on $U$.
Then $f$ is of class $C^k$ on $U$ if and only if these two conditions hold.

1. For each $r$ with $0 \le r \le k$, the [[iterated derivative|0EY05Z9RPN]] $D^r f$ exists on $U$ and is continuous on $U$.
2. For each $r$ with $0 \le r < k$, the map $D^r f$ is differentiable on $U$.

## Remarks

So in finite dimensions, $C^k$ means $k$ times continuously differentiable, in either the sense of partial derivatives or the sense of Fréchet derivatives.
A function is of class $C^\infty$, or smooth, when it is of class $C^k$ for each $k$.
Each polynomial in $x_1, \dots, x_n$ is of class $C^\infty$ on $\mathbb{R}^n$. The function $x \mapsto \|x\|$ is of class $C^\infty$ on $\mathbb{R}^n \setminus \{0\}$, but it is not differentiable at $0$.

## Explanations

### L1 human

There are two ways to count derivatives: one variable at a time with partial derivatives, or all variables at once with total derivatives.
For functions on open subsets of $\mathbb{R}^n$, both ways give the same classes $C^1, C^2, \dots$, as long as you also ask for continuity.
