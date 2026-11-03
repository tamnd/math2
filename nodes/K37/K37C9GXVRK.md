---
about:
- 0A6QZ367GX
kind: statement
msc:
- 34A30
name: Superposition for linear homogeneous systems
role: theorem
sources:
- locator: ch-systems.tex:1641
  url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L1641
tag: K37C9GXVRK
uses:
- 0A6QZ367GX
- 0CRMGPAH83
---

## Statement

Let $\vec{x}' = P\vec{x}$ be a homogeneous [[system of linear differential equations|0A6QZ367GX]], where $P$ is an $n \times n$ matrix of coefficients on an interval $I$.

1. If $\vec{x}_1, \dots, \vec{x}_k$ are solutions and $c_1, \dots, c_k$ are constants, then $c_1 \vec{x}_1 + \cdots + c_k \vec{x}_k$ is again a solution.
2. If $\vec{x}_1, \dots, \vec{x}_n$ are $n$ solutions that are [[linearly independent|0CRMGPAH83]], then every solution $\vec{x}$ has the form $c_1 \vec{x}_1 + \cdots + c_n \vec{x}_n$ for some constants $c_1, \dots, c_n$.

## Remarks

Part 1 follows from the linearity of differentiation and of multiplication by $P$.
Part 2 says that $n$ independent solutions span the whole solution space, so that space has dimension $n$.
