---
tag: QQW1AWRFZH
kind: definition
name: Condition number
msc: [15A12, 65F35]
defines: AB3S6MHJ8X
uses: [0EB9N0S33C, 54T6Y6DSY4, 06EKW1AKXF, 09VMDSRXWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Condition_number
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, let $n \ge 1$, and let $\norm{\cdot}$ be a submultiplicative [[matrix norm|54T6Y6DSY4]] on $\mathbb{K}^{n \times n}$.
Let $A$ be an [[invertible|0EB9N0S33C]] $n \times n$ matrix over $\mathbb{K}$.
The *condition number* of $A$ with respect to $\norm{\cdot}$ is
$$\kappa(A) = \norm{A} \, \norm{A^{-1}}.$$

## Remarks

By convention, $\kappa(A) = \infty$ when $A$ is not invertible.
If $\norm{\cdot}$ is an [[operator norm|06EKW1AKXF]], then $\kappa(A) \ge \norm{A A^{-1}} = \norm{I} = 1$.
For the operator norm of the Euclidean norm, $\kappa_2(A) = \sigma_{\max} / \sigma_{\min}$, the ratio of the largest and smallest [[singular values|09VMDSRXWJ]].
If $Ax = b$ with $b \ne 0$ and $A(x + \delta x) = b + \delta b$, then $\norm{\delta x} / \norm{x} \le \kappa(A) \, \norm{\delta b} / \norm{b}$ for the operator norm of a vector norm.
Example: $A = \begin{pmatrix} 1 & 0 \\ 0 & 10^{-3} \end{pmatrix}$ has $\norm{A}_2 = 1$ and $\norm{A^{-1}}_2 = 10^{3}$, so $\kappa_2(A) = 10^3$.
Non-example: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ is not invertible, so the formula does not apply.
