---
tag: PR9A84ZPT1
kind: definition
name: Biharmonic equation
msc: [31B30, 35J30]
defines: AS8A9F5SKE
uses: [GC5BDZ6QBC, 0E0B6RA8K0, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Biharmonic_equation
---

## Definition

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be an open set.
Let $u \colon \Omega \to \R$ be four times continuously differentiable.
The *biharmonic equation* on $\Omega$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\Delta^2 u = 0,$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $\Delta^2 u = \Delta(\Delta u)$.
A solution is called a *biharmonic function*.

## Remarks

In coordinates, $\Delta^2 u = \sum_{i,j=1}^n \partial_i^2 \partial_j^2 u$; in the plane, $\Delta^2 u = u_{xxxx} + 2 u_{xxyy} + u_{yyyy}$.
Example: on $\R^n$, $u(x) = \abs{x}^2$ is biharmonic, since $\Delta \abs{x}^2 = 2n$ is constant and so $\Delta^2 u = 0$.
Non-example: $u(x) = \abs{x}^4$ is not biharmonic, since $\Delta \abs{x}^4 = 4(n + 2) \abs{x}^2$ and then $\Delta^2 u = 8n(n + 2) \ne 0$.
Every [[harmonic function|0DEB0JMN0W]] is biharmonic.
The inhomogeneous equation $\Delta^2 u = f$ is the plate equation; boundary conditions usually prescribe two quantities, such as $u$ and its normal derivative.
