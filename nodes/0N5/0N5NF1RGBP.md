---
tag: 0N5NF1RGBP
kind: definition
name: Wronskian
msc: [34A30]
defines: 0KC1NMG90B
sources:
  - url: https://en.wikipedia.org/wiki/Wronskian
    locator: Definition
---

## Definition

Let $I$ be an interval and let $f_1, \dots, f_n : I \to \mathbb{R}$ be $n - 1$ times differentiable functions.
The Wronskian of $f_1, \dots, f_n$ is the function $W(f_1, \dots, f_n) : I \to \mathbb{R}$ given by
$$W(f_1, \dots, f_n)(x) = \det \begin{pmatrix} f_1(x) & f_2(x) & \cdots & f_n(x) \\ f_1'(x) & f_2'(x) & \cdots & f_n'(x) \\ \vdots & \vdots & \ddots & \vdots \\ f_1^{(n-1)}(x) & f_2^{(n-1)}(x) & \cdots & f_n^{(n-1)}(x) \end{pmatrix}.$$

## Remarks

For two functions, $W(f, g) = f g' - f' g$.
Example: $W(\cos, \sin) = \cos^2 + \sin^2 = 1$.
The [[Wronskian test|0MHE4B1QCQ]] uses $W$ to decide whether solutions of a linear equation are linearly independent.

## Explanations

### L1 human

The rows of the matrix are the functions, then their first derivatives, and so on.
The determinant measures whether the vectors of starting data of the functions are independent at the point $x$.
