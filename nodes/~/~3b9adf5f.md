---
tag: ~3b9adf5f
kind: definition
name: Iterated derivative
msc: [26B05]
defines: ~d233e1b1
uses: [~9e2dfc39, ~804b326a, ~ff1fb7d0]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Higher derivatives
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open and let $f \colon U \to \mathbb{R}^m$.
For an integer $k \ge 0$, let $L^k(\mathbb{R}^n; \mathbb{R}^m)$ be the space of $k$-linear maps from $(\mathbb{R}^n)^k$ to $\mathbb{R}^m$, with $L^0(\mathbb{R}^n; \mathbb{R}^m) = \mathbb{R}^m$.
The iterated derivatives are defined by recursion. First, $D^0 f = f$.
Suppose that $D^k f \colon U \to L^k(\mathbb{R}^n; \mathbb{R}^m)$ is defined on $U$ and is [[differentiable on U|~804b326a]].
Then $D^{k+1} f(a)$, for $a \in U$, is the $(k+1)$-linear map
$$D^{k+1} f(a)(v_1, v_2, \dots, v_{k+1}) = \big(D(D^k f)(a)(v_1)\big)(v_2, \dots, v_{k+1}).$$
Here $D(D^k f)(a)$ is the [[Fréchet derivative|~9e2dfc39]] of $D^k f$ at $a$, a linear map from $\mathbb{R}^n$ to $L^k(\mathbb{R}^n; \mathbb{R}^m)$.

## Remarks

For $k = 1$, $D^1 f = Df$. For $k = 2$, $D^2 f(a)(u, v)$ is the derivative of $x \mapsto Df(x)(v)$ at $a$ in the direction $u$.
On basis vectors, $D^2 f(a)(e_i, e_j) = \dfrac{\partial}{\partial x_i}\left(\dfrac{\partial f}{\partial x_j}\right)(a)$. In general, $D^k f(a)(e_{i_1}, \dots, e_{i_k})$ is a [[partial derivative of order k|~ff1fb7d0]].
For a real-valued $f$, the matrix of the bilinear map $D^2 f(a)$ is the [[Hessian matrix|~4b597766]].
If $f$ is of class $C^k$, then $D^k f(a)$ is a symmetric $k$-linear map, by the [[symmetry of second derivatives|~4384a49a]].

## Explanations

### L1 human

The first derivative takes one direction and gives a rate of change.
The second derivative takes two directions $u$ and $v$. It tells how the rate of change in direction $v$ itself changes as you move in direction $u$.
