---
tag: F3D3X49ZBW
kind: definition
name: First class constraint
msc: [70H45]
defines: SV6K39RSA6
uses: [2S0MXDT4YH, 0NS2QYVC4Y]
sources:
  - url: https://en.wikipedia.org/wiki/First-class_constraint
---

## Definition

Let $V \subseteq \R^{2n}$ be open, with coordinates $(q, p)$ and the [[Poisson bracket|2S0MXDT4YH]] $\{f, g\} = \sum_{i=1}^n \big(\frac{\partial f}{\partial q_i} \frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i}\big)$.
Let $\phi_1, \ldots, \phi_m \colon V \to \R$ be smooth constraint functions, and let $\Sigma = \set{x \in V : \phi_1(x) = \cdots = \phi_m(x) = 0}$ be the constraint surface.
Assume that the [[gradients|0NS2QYVC4Y]] $\nabla \phi_1, \ldots, \nabla \phi_m$ are linearly independent at each point of $\Sigma$.

1. A smooth function $f$ on $V$ is *first class* when $\{f, \phi_a\} = 0$ on $\Sigma$ for every $a = 1, \ldots, m$.
2. A constraint $\phi_a$ is *first class* when it is a first class function, and *second class* otherwise.

## Remarks

A function that vanishes on $\Sigma$ is called weakly zero, written $f \approx 0$; so $f$ is first class when $\{f, \phi_a\} \approx 0$ for all $a$.
In Dirac's procedure, the $\phi_a$ are all the constraints, primary and secondary, of a system obtained from a degenerate Lagrangian.
Often one first replaces the $\phi_a$ by suitable combinations so that as many as possible are first class.

Example: $n = 2$ and the single constraint $\phi_1 = p_2$.
Then $\{\phi_1, \phi_1\} = 0$, so $\phi_1$ is first class.
The flow it generates, $q_2 \mapsto q_2 + s$, moves along $\Sigma$ and is a gauge freedom.

Non-example: $n = 2$ and the constraints $\phi_1 = q_2$, $\phi_2 = p_2$.
Then $\{\phi_1, \phi_2\} = 1 \ne 0$ on $\Sigma$, so neither constraint is first class; both are second class.
