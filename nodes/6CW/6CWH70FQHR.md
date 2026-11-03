---
tag: 6CWH70FQHR
kind: definition
name: Weight of a representation
msc: [17B10]
defines: KFVNC2W720
uses: [5JJYBJ6A8K, TZAZ163QGK, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Weight_(representation_theory)
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $F$, let $\mathfrak{h}$ be an abelian subalgebra of $\mathfrak{g}$, and let $V$ be a $\mathfrak{g}$-[[module|TZAZ163QGK]].
Let $\mathfrak{h}^*$ be the [[dual space|07JBSZE0V4]] of $\mathfrak{h}$.
For $\lambda \in \mathfrak{h}^*$ put $V_\lambda = \set{v \in V : h \cdot v = \lambda(h) v \text{ for all } h \in \mathfrak{h}}$.
A *weight* of $V$ with respect to $\mathfrak{h}$ is a $\lambda \in \mathfrak{h}^*$ with $V_\lambda \ne 0$.
Then $V_\lambda$ is the *weight space* of $\lambda$, its nonzero elements are *weight vectors*, and $\dim V_\lambda$ is the *multiplicity* of $\lambda$.

## Remarks

The main case is a complex semisimple Lie algebra $\mathfrak{g}$ with a [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$.
Example: $\mathfrak{g} = \mathfrak{sl}_2(\C)$, $\mathfrak{h} = \C h$ with $h = \operatorname{diag}(1, -1)$, and $V = \C^2$.
Here $h e_1 = e_1$ and $h e_2 = -e_2$, so the weights are the forms with $\lambda(h) = 1$ and $\lambda(h) = -1$, each of multiplicity one.
Non-example: the form with $\lambda(h) = 0$ is not a weight of $\C^2$, since $h$ has no nonzero vector in its kernel.
For the adjoint representation, the nonzero weights are the roots and $V_0 = \mathfrak{h}$.
If $x \in \mathfrak{g}_\alpha$ is a root vector, then $x \cdot V_\lambda \subseteq V_{\lambda + \alpha}$.
For a nilpotent $\mathfrak{h}$ one often uses generalised weight spaces, the vectors killed by a power of $h - \lambda(h)$ for every $h$, as in [[weight space|KZ7RZC8XC4]].
