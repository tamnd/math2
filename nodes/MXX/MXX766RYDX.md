---
tag: MXX766RYDX
kind: definition
name: Complex Monge–Ampère operator
msc: [32W20, 32U15]
defines: MXRC891TQS
uses: [FF2P7ER3QT, 00KDZRW4C0, DC81TCR98Y]
sources:
  - url: https://en.wikipedia.org/wiki/Monge%E2%80%93Amp%C3%A8re_equation
---

## Definition

Let $\Omega \subseteq \C^n$ be open and let $u \colon \Omega \to \R$ be of class $C^2$.
Let $d^c = i(\bar\partial - \partial)$, so that $dd^c = 2i \partial\bar\partial$.
The *complex Monge–Ampère operator* applied to $u$ is the $(n, n)$-form
$$(dd^c u)^n = dd^c u \wedge \cdots \wedge dd^c u \quad (n \text{ factors}).$$
In coordinates,
$$(dd^c u)^n = 4^n \, n! \, \det\left( \frac{\partial^2 u}{\partial z_j \partial \bar z_k} \right)_{j,k=1}^n dV,$$
where $dV$ is Lebesgue measure on $\C^n = \R^{2n}$.

## Remarks

The constant $4^n n!$ depends on the normalisation of $d^c$; many authors use $d^c = \frac{i}{4\pi}(\bar\partial - \partial)$ or write simply $\det\left(\partial^2 u / \partial z_j \partial \bar z_k\right)$.
If $u$ is [[plurisubharmonic|FF2P7ER3QT]], the complex Hessian is positive semidefinite, so $(dd^c u)^n$ is a positive measure.
Example: for $u(z) = \abs{z}^2 = \sum_j \abs{z_j}^2$ the complex Hessian is the identity, so $(dd^c u)^n = 4^n n! \, dV$.
For $n = 1$, $dd^c u = 4 \, \frac{\partial^2 u}{\partial z \partial \bar z} \, dV = \Delta u \, dV$, the Laplacian.
Non-example of positivity: for $u = \abs{z_1}^2 - \abs{z_2}^2$ on $\C^2$ the determinant is $-1$, so $(dd^c u)^2$ is a negative measure; this $u$ is not plurisubharmonic.
The operator is nonlinear for $n \ge 2$.
The extension of $(dd^c u)^n$ to locally bounded plurisubharmonic functions, where $u$ need not be differentiable, is the [[Bedford–Taylor theory|EEHQSWFHSB]].
