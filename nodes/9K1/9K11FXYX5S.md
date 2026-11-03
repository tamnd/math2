---
tag: 9K11FXYX5S
kind: definition
name: Hilbert C*-module
msc: [46L08]
defines: KBPJH3J56K
uses: [NA8DF5X3M4, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_C*-module
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
Let $E$ be a complex vector space that is a right $A$-module, with $\lambda (x a) = (\lambda x) a = x (\lambda a)$ for $\lambda \in \C$, $x \in E$ and $a \in A$.
An *$A$-valued inner product* on $E$ is a map $\ip{\cdot}{\cdot} \colon E \times E \to A$ such that for all $x, y, z \in E$, $a \in A$ and $\lambda \in \C$:

1. $\ip{x}{y + \lambda z} = \ip{x}{y} + \lambda \ip{x}{z}$.
2. $\ip{x}{y a} = \ip{x}{y} a$.
3. $\ip{y}{x} = \ip{x}{y}^*$.
4. $\ip{x}{x}$ is a [[positive element|NA8DF5X3M4]] of $A$, and $\ip{x}{x} = 0$ only for $x = 0$.

Then $\norm{x} = \norm{\ip{x}{x}}^{1/2}$ is a norm on $E$.
A *Hilbert C*-module* over $A$ is such a module $E$ that is complete for this norm.

## Remarks

The inner product is linear in the second argument and conjugate-linear in the first, as is usual in this theory.
A Hilbert $\C$-module is the same as a complex [[Hilbert space|HM2HHE3J51]] with this convention.

Example: $E = A$ with $\ip{a}{b} = a^* b$.
Clauses 1 to 3 follow from the algebra rules and $(a^* b)^* = b^* a$; the element $a^* a$ is positive, and $a^* a = 0$ forces $a = 0$.
The norm is $\norm{a^* a}^{1/2} = \norm{a}$ by the C* identity, so $E$ is complete.

Another example is $A^n$ with $\ip{x}{y} = \sum_{i=1}^n x_i^* y_i$.

Non-example: $E = \C$ over $A = \C$ with $\ip{x}{y} = -\overline{x} y$.
Clauses 1 to 3 hold, but $\ip{1}{1} = -1$ is not positive, so clause 4 fails.
