---
tag: 0XQ2ZVN1PZ
kind: definition
name: Laplacian
msc: [35J05]
defines: 0E0B6RA8K0
uses: [02NSMQVQWK, 0NS2QYVC4Y, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_operator
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Laplace_operator
    locator: Averages
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $f \colon U \to \mathbb{R}$ be twice differentiable on $U$.
The Laplacian of $f$ is the function $\Delta f \colon U \to \mathbb{R}$,
$$\Delta f = \operatorname{div}(\nabla f) = \nabla \cdot \nabla f,$$
the [[divergence|02NSMQVQWK]] of the [[gradient|0NS2QYVC4Y]] of $f$. It is also written $\nabla^2 f$.

## Remarks

In Cartesian coordinates, $\Delta f$ is the [[sum of the unmixed second partial derivatives|05RCT1522R]] of $f$.
The operator $\Delta$ is linear, and it maps functions of [[class C^k|0TCBZMEYGN]] to functions of class $C^{k-2}$ for $k \ge 2$.
Let $f$ be of class $C^2$, and let $\bar{f}_r$ be the average of $f$ on the sphere of radius $r$ about $x$. Then $\Delta f(x)$ is $2n$ times the limit of $(\bar{f}_r - f(x)) / r^2$ as $r \to 0$. So $\Delta f(x) > 0$ means that $f(x)$ is below its nearby averages.
The Laplacian appears in the heat equation $\partial_t u = \Delta u$, the wave equation and Laplace's equation $\Delta u = 0$.

## Explanations

### L1 human

The Laplacian compares the value of a function at a point with its values nearby.
If $f$ at the point is lower than the average around it, the Laplacian is positive. If it is higher, the Laplacian is negative.
