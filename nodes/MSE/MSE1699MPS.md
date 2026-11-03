---
tag: MSE1699MPS
kind: definition
name: Modal analysis
msc: [70J10, 70J50]
defines: D14DP6XQJ6
uses: [WZGRC78VDB, 0FK17N4DKA, 0QQCG3JWJ4, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_analysis
---

## Definition

Let $M$ and $K$ be real [[symmetric|0N28QN4CYA]] $n \times n$ matrices with $M$ [[positive definite|0QQCG3JWJ4]], and consider the forced linear system
$$M \ddot x + K x = f(t),$$
with a continuous force $f \colon \R \to \R^n$.
Let $v_1, \ldots, v_n$ be a basis of $\R^n$ and $\lambda_1, \ldots, \lambda_n$ real numbers with
$$K v_k = \lambda_k M v_k, \qquad v_j^T M v_k = \delta_{jk};$$
the $v_k$ are the mode shapes of the [[normal modes|WZGRC78VDB]].
*Modal analysis* is the change of variables $x(t) = \sum_{k=1}^n \eta_k(t) \, v_k$; the functions $\eta_k$ are the *modal coordinates*, and they satisfy the decoupled equations
$$\ddot \eta_k + \lambda_k \eta_k = v_k^T f(t), \qquad k = 1, \ldots, n.$$

## Remarks

Such a basis exists by [[simultaneous diagonalisation|0FK17N4DKA]] of the symmetric matrices $M$ and $K$, with $M$ positive definite.
The decoupled equations follow by substituting $x$ into the system and multiplying on the left by $v_k^T$.
If $K$ is positive semidefinite, $\lambda_k = \omega_k^2 \ge 0$ with natural frequencies $\omega_k$.
With a damping matrix $C$, the equations decouple in the same way when $v_j^T C v_k = 0$ for $j \ne k$, for example for proportional damping $C = \alpha M + \beta K$.

Example: $M = I_2$, $K = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, $v_1 = \frac{1}{\sqrt 2}(1, 1)$, $v_2 = \frac{1}{\sqrt 2}(1, -1)$, $\lambda_1 = 1$, $\lambda_2 = 3$.
The modal coordinates $\eta_1 = (x_1 + x_2)/\sqrt 2$ and $\eta_2 = (x_1 - x_2)/\sqrt 2$ satisfy $\ddot \eta_1 + \eta_1 = (f_1 + f_2)/\sqrt 2$ and $\ddot \eta_2 + 3 \eta_2 = (f_1 - f_2)/\sqrt 2$.

Non-example: the standard basis $e_1, e_2$ in the same system is not a basis of mode shapes, since $K e_1 = (2, -1)^T$ is not a multiple of $e_1$.
In these coordinates the equations stay coupled.
