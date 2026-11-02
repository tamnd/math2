---
tag: 2RXEM9BQFY
kind: definition
name: Pluriharmonic function
msc: [32U05, 31C10]
defines: 4A7VAXPG4F
uses: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Pluriharmonic_function
---

## Definition

Let $\Omega \subseteq \C^n$ be an open set.
A function $u \colon \Omega \to \R$ of class $C^2$ is *pluriharmonic* if
$$\frac{\partial^2 u}{\partial z_j \partial \bar z_k} = 0 \quad \text{on } \Omega \text{ for all } j, k \in \set{1, \dots, n},$$
where $\partial / \partial z_j = \frac{1}{2}(\partial / \partial x_j - i \, \partial / \partial y_j)$ and $\partial / \partial \bar z_k = \frac{1}{2}(\partial / \partial x_k + i \, \partial / \partial y_k)$ for $z_j = x_j + i y_j$.

## Remarks

Equivalently, for all $a \in \Omega$ and $b \in \C^n$, the function $\lambda \mapsto u(a + \lambda b)$ is [[harmonic|0DEB0JMN0W]] where it is defined.
Example: $u = \operatorname{Re} f$ for a holomorphic $f$ is pluriharmonic, because $\partial f / \partial \bar z_k = 0$ and $\partial \bar f / \partial z_j = 0$ give $\partial^2 (f + \bar f) / \partial z_j \partial \bar z_k = 0$.
Non-example: $u = \abs{z_1}^2$ has $\partial^2 u / \partial z_1 \partial \bar z_1 = 1 \ne 0$.
Conversely, on a ball, or more generally on a simply connected domain, every pluriharmonic function is the real part of a holomorphic function; on other domains this holds locally.
A pluriharmonic function is real analytic.
The condition can be written $\partial \bar\partial u = 0$.
