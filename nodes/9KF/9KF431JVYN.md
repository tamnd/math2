---
tag: 9KF431JVYN
kind: statement
role: theorem
name: Existence of the radius of convergence of a power series
msc: [30B10]
uses: [0VP56B4EMX, 0660QX1VPR, 0YBDSJARWN]
about: [0N288P2TB5]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-power-ser.tex#L132
    locator: ch-power-ser.tex:132
---

## Statement

Let $\sum_{n=0}^\infty a_n (x - x_0)^n$ be a real [[power series|0VP56B4EMX]] with center $x_0$.
Then there is a number $\rho \in [0, \infty]$ with two properties.

1. The series [[converges absolutely|0YBDSJARWN]] at every $x$ with $|x - x_0| < \rho$.
2. The series diverges at every $x$ with $|x - x_0| > \rho$.

This $\rho$ is the [[radius of convergence|0660QX1VPR]]. The value $\rho = \infty$ means that the series converges at every real $x$.

## Remarks

The statement says nothing about the two endpoints $x_0 \pm \rho$. There the series may converge or diverge.
The number $\rho$ is unique, since the two conditions leave no room for a second value.
For example, $\sum x^n$ has $\rho = 1$, and $\sum x^n / n!$ has $\rho = \infty$.
