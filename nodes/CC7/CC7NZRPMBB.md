---
tag: CC7NZRPMBB
kind: statement
role: theorem
name: Uniqueness theorem for Poisson's equation
msc: [35J05, 78A30]
uses: [FC64B1A65B, QDXXWA1QGF, 8D56GQ4AG8, 61VG0XSDM6, 0DEB0JMN0W]
about: [FC64B1A65B]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_theorem_for_Poisson%27s_equation
same_as:
  wikidata: Q7886967
  wikipedia: Uniqueness theorem for Poisson's equation
---

## Statement

Let $\Omega \subset \R^3$ be a bounded, connected open set with $C^1$ boundary $\partial \Omega$ and outward unit normal $n$.
Let $f \colon \Omega \to \R$ be continuous.
Let $\varphi_1, \varphi_2 \in C^2(\Omega) \cap C^1(\overline{\Omega})$ both solve [[Poisson's equation|FC64B1A65B]] $\Delta \varphi = f$ in $\Omega$.

1. If $\varphi_1 = \varphi_2$ on $\partial \Omega$, then $\varphi_1 = \varphi_2$ on $\Omega$.
2. If $\partial_n \varphi_1 = \partial_n \varphi_2$ on $\partial \Omega$, then $\varphi_1 - \varphi_2$ is constant on $\Omega$.

## Remarks

The difference $w = \varphi_1 - \varphi_2$ is [[harmonic|0DEB0JMN0W]] in $\Omega$.
By the first of [[Green's identities|QDXXWA1QGF]], $\int_\Omega \abs{\nabla w}^2 \, dx = \int_{\partial \Omega} w \, \partial_n w \, dA$, and the right side is $0$ under either boundary condition.
So $\nabla w = 0$, and $w$ is constant because $\Omega$ is connected; in case 1 the constant is $0$ since $w = 0$ on $\partial \Omega$.
The same argument gives uniqueness for mixed data, with $\varphi$ given on one part of the boundary and $\partial_n \varphi$ on the rest.
In case 2 the constant cannot be removed: $\varphi$ and $\varphi + 1$ have the same normal derivative.
On an unbounded region, uniqueness needs a condition at infinity, such as $\varphi(x) \to 0$ as $\abs{x} \to \infty$.

## Explanations

### L1 human

If you know the charge inside a region and the potential on its boundary, then the potential inside is completely fixed.
There is only one answer.
So any trick that produces a potential with the right charges and the right boundary values gives the true potential.

### L2 human

The theorem gives uniqueness for the [[Dirichlet problem|8D56GQ4AG8]] and, up to constants, for the [[Neumann problem|61VG0XSDM6]] of Poisson's equation.
In electrostatics it justifies guessing: the method of image charges and separation of variables work because any solution found is the solution.
It also shows that the field inside a closed hollow conductor without charge is zero.
Existence is a separate question, answered by potential theory or by variational methods.
