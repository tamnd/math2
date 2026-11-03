---
kind: statement
name: General solution of a linear system with distinct real eigenvalues
role: theorem
msc:
  - 34A30
tag: CEHQN8GR2G
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L2325
    locator: ch-systems.tex:2325
uses:
  - 0VJF99CZ0Z
  - 0N6960W0BV
  - 0CRMGPAH83
  - 0HNMFG8F8K
about:
  - 08ZWFDJP3H
---

## Statement

Let $P$ be a constant real $n \times n$ matrix, and consider the [[homogeneous linear system with constant coefficients|0VJF99CZ0Z]] $\vec{x}' = P\vec{x}$.

Suppose $P$ has $n$ distinct real eigenvalues $\lambda_1, \dots, \lambda_n$.

Then there are [[eigenvectors|0N6960W0BV]] $\vec{v}_1, \dots, \vec{v}_n$ for these eigenvalues, and they are [[linearly independent|0CRMGPAH83]].

Moreover, the general solution of the system is

$$\vec{x}(t) = c_1 \vec{v}_1 e^{\lambda_1 t} + c_2 \vec{v}_2 e^{\lambda_2 t} + \cdots + c_n \vec{v}_n e^{\lambda_n t},$$

where $c_1, \dots, c_n$ are arbitrary constants.

## Remarks

The independence of the eigenvectors follows from [[eigenvectors with distinct eigenvalues are independent|0HNMFG8F8K]].

Each term $\vec{v}_k e^{\lambda_k t}$ solves the system, and independence makes these $n$ solutions a basis of the solution space. This is the simplest case of the [[eigenvalue method|08ZWFDJP3H]].
