---
tag: 0YF0VXKXGB
kind: definition
name: Jacobian matrix
msc: [26B10]
defines: 047NDTEPCV
uses: [09EGC6F8PT, 0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant
    locator: Jacobian matrix
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, let $f = (f_1, \dots, f_m) \colon U \to \mathbb{R}^m$, and let $a \in U$.
Suppose that each [[partial derivative|09EGC6F8PT]] $\partial f_i / \partial x_j$ exists at $a$, for $1 \le i \le m$ and $1 \le j \le n$.
The Jacobian matrix of $f$ at $a$ is the $m \times n$ matrix
$$J_f(a) = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1}(a) & \cdots & \dfrac{\partial f_1}{\partial x_n}(a) \\ \vdots & \ddots & \vdots \\ \dfrac{\partial f_m}{\partial x_1}(a) & \cdots & \dfrac{\partial f_m}{\partial x_n}(a) \end{pmatrix},$$
whose entry in row $i$ and column $j$ is $\partial f_i / \partial x_j (a)$.
Other notations are $Df(a)$, $f'(a)$ and $\dfrac{\partial (f_1, \dots, f_m)}{\partial (x_1, \dots, x_n)}$.

## Remarks

If $f$ is [[differentiable|0135XZZQ8M]] at $a$, then $Df(a)(h) = J_f(a) \, h$ for each column vector $h \in \mathbb{R}^n$.
Row $i$ of $J_f(a)$ is the transpose of the [[gradient|0ABK9V9Y64]] of $f_i$ at $a$. For $m = 1$, the Jacobian matrix is the gradient written as a row.
For the polar map $f(r, \theta) = (r \cos \theta, r \sin \theta)$, the Jacobian matrix is $\begin{pmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{pmatrix}$.
For $m = n$, its determinant is the [[Jacobian determinant|0ZCSMYHTBP]].

## Explanations

### L1 human

The Jacobian matrix lists how each output changes with each input: one row for each output, one column for each input.
It is the multivariable form of the derivative. It turns a small step $h$ in the input into the approximate step $J_f(a) h$ in the output.
