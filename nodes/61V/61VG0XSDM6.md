---
tag: 61VG0XSDM6
kind: problem
name: Neumann problem
msc: [31B20, 35J25, 31A25]
uses: [0DEB0JMN0W, GS3KT2H645, 02BH3MCBQB, 05D5EGMFYV, 0X3WGX95FE]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Neumann_boundary_condition
history:
  posed_by: "Carl Neumann"
---

## Problem

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded connected [[open set|02BH3MCBQB]] whose [[boundary|05D5EGMFYV]] $\partial\Omega$ is a $C^1$ hypersurface, with outward unit normal $\nu$.
Let $g \colon \partial\Omega \to \R$ be a [[continuous function|0X3WGX95FE]].
Find a function $u$ that is twice continuously differentiable on $\Omega$, continuously differentiable on $\overline{\Omega}$, [[harmonic|0DEB0JMN0W]] on $\Omega$, and satisfies the [[Neumann boundary condition|GS3KT2H645]]
$$\frac{\partial u}{\partial \nu} = g \quad \text{on } \partial\Omega.$$

## Remarks

A necessary condition is $\int_{\partial\Omega} g \, dS = 0$: by the [[divergence theorem|0JX86PSSA9]], $\int_{\partial\Omega} \partial u / \partial \nu \, dS = \int_\Omega \Delta u \, dx = 0$.
A solution is unique up to an additive constant: the difference $w$ of two solutions satisfies $\int_\Omega \abs{\nabla w}^2 \, dx = \int_{\partial\Omega} w \, \partial w / \partial \nu \, dS = 0$, so $w$ is constant on the connected set $\Omega$.
For bounded domains with sufficiently smooth boundary, for example $C^2$, a solution exists whenever the condition $\int_{\partial\Omega} g \, dS = 0$ holds; one proof uses layer potentials and Fredholm theory.
Example: on the unit disc with $g(\theta) = \cos\theta$, the condition holds and $u(x, y) = x$ is a solution, since $\partial u / \partial \nu = x = \cos\theta$ on the unit circle.
The problem is the companion of the [[Dirichlet problem|8D56GQ4AG8]], which prescribes $u$ instead of its normal derivative.

## Explanations

### L1 human

Imagine a metal body in thermal equilibrium, where you control how much heat flows in or out through each piece of its surface.
The Neumann problem asks for the temperature inside.
In equilibrium the total inflow must be zero, and the temperature is then determined up to adding a constant.
