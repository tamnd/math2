---
tag: "7RSJJNNZZJ"
kind: statement
name: General solution of a second-order homogeneous linear equation
role: theorem
msc:
  - 34A30
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-higher-order-ode.tex#L173
    locator: ch-higher-order-ode.tex:173
uses:
  - 0EQZSAB9EC
  - 0CRMGPAH83
about:
  - 0KP0QNXPRT
---

## Statement

Let $I$ be an open interval and let $p, q : I \to \mathbb{R}$ be continuous.
Consider the [[homogeneous linear equation|0EQZSAB9EC]] $y'' + p(x)\, y' + q(x)\, y = 0$ on $I$.
Let $y_1$ and $y_2$ be two solutions on $I$ that are [[linearly independent|0CRMGPAH83]].
Then each solution $y$ on $I$ can be written as $y = C_1 y_1 + C_2 y_2$ for some constants $C_1, C_2$.

## Remarks

So the expression $C_1 y_1 + C_2 y_2$ with arbitrary constants is the general solution of the equation.
Every such combination is also a solution, by linearity of the equation.
Example: $\cos x$ and $\sin x$ are independent solutions of $y'' + y = 0$, so each solution is $C_1 \cos x + C_2 \sin x$.
