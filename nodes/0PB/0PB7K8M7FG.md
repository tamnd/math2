---
tag: 0PB7K8M7FG
kind: definition
name: Linear differential equation of order n
msc: [34A30]
defines: 0QQRP17Z7S
uses: [0P97V20RW7, 09M2RDB61G, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: Basic terminology
---

## Definition

Let $n \ge 1$, let $I$ be an open [[interval|0Q1D85B8G6]], and let $a_0, \dots, a_{n-1}, b : I \to \mathbb{R}$ be continuous functions.
The linear differential equation of order $n$ with these coefficients and right side $b$ is the equation
$$y^{(n)} + a_{n-1}(x)\, y^{(n-1)} + \dots + a_1(x)\, y' + a_0(x)\, y = b(x)$$
for an unknown $n$ times differentiable function $y : I \to \mathbb{R}$.
With the operator $L y = y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_0 y$, the equation is $L y = b$.

## Remarks

The map $L$ is linear: $L(c_1 y_1 + c_2 y_2) = c_1 L y_1 + c_2 L y_2$ for constants $c_1, c_2$.
An equation $a_n(x) y^{(n)} + \dots + a_0(x) y = b(x)$ with continuous $a_n$ and no zero of $a_n$ on $I$ takes this form after division by $a_n$.
The equation is [[homogeneous|0EQZSAB9EC]] if $b = 0$. The case $n = 1$ is the [[linear first-order equation|0Z3YKRQZ48]].
For each $x_0 \in I$ and each $(c_0, \dots, c_{n-1}) \in \mathbb{R}^n$, there is exactly one solution on all of $I$ with $y^{(k)}(x_0) = c_k$ for $k = 0, \dots, n-1$.

## Explanations

### L1 human

In a linear equation, the unknown $y$ and its derivatives appear only to the first power, each multiplied by a function of $x$.
For example, $y'' + x y' + y = \cos x$ is linear, but $y'' + y^2 = 0$ is not.
Linear equations have a rich theory, because sums and multiples of solutions behave well.
