---
tag: 6FMKG1AB6W
kind: definition
name: Weight space
msc: ["17B10", "17B20"]
defines: KZ7RZC8XC4
uses: [TZAZ163QGK, WKSSTQ69AK, 07JBSZE0V4, 0G0RFPG8HR]
sources:
  - url: https://en.wikipedia.org/wiki/Weight_(representation_theory)
---

## Definition

Let $\mathfrak{g}$ be a Lie algebra over a field $F$, and let $\rho \colon \mathfrak{g} \to \mathfrak{gl}(V)$ be a [[representation|TZAZ163QGK]] of $\mathfrak{g}$ on a vector space $V$.
Let $\mathfrak{h}$ be a [[Lie subalgebra|WKSSTQ69AK]] of $\mathfrak{g}$, and let $\lambda \in \mathfrak{h}^*$ be a linear form on $\mathfrak{h}$, an element of the [[dual space|07JBSZE0V4]].
The *weight space* of $V$ for $\lambda$ is the subspace
$$V_\lambda = \set{v \in V : \rho(h) v = \lambda(h) v \text{ for all } h \in \mathfrak{h}}.$$
If $V_\lambda \ne 0$, then $\lambda$ is a *weight* of $V$, and the nonzero elements of $V_\lambda$ are *weight vectors* of weight $\lambda$.

## Remarks

Example: let $\mathfrak{g} = \mathfrak{sl}_2(\C)$ act on $V = \C^2$, and let $\mathfrak{h}$ be spanned by $h = \operatorname{diag}(1, -1)$.
For $\lambda(h) = 1$, the weight space $V_\lambda$ is the line $\C e_1$, since $h e_1 = e_1$ and the only eigenvectors of $h$ for $1$ are the multiples of $e_1$.
Non-example: for $\lambda(h) = 2$, the space $V_\lambda$ is $0$, since $2$ is not an eigenvalue of $h$, so this $\lambda$ is not a weight.
If $\mathfrak{h}$ is spanned by one element $h$, then $V_\lambda$ is the [[eigenspace|0G0RFPG8HR]] of $\rho(h)$ for the eigenvalue $\lambda(h)$.
The *generalized weight space* is the larger space of the $v$ such that for each $h \in \mathfrak{h}$ some power of $\rho(h) - \lambda(h)$ kills $v$.
For nilpotent $\mathfrak{h}$ the space $V$ is the direct sum of these spaces when $F$ is algebraically closed of characteristic $0$ and $V$ is finite-dimensional.

## Explanations

### L1 human

A weight space collects the vectors on which every element of $\mathfrak{h}$ acts as multiplication by a number.
The numbers depend linearly on the element, and this linear dependence is the weight.
