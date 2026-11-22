---
tag: 0C2TQMW5A1
kind: definition
name: Dual map
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
defines: 0AZ5ARP287
uses: [0M856Q1AMZ, 0RJF668P1T]
formal:
  - system: lean4
    library: mathlib
    decl: Module.Dual.transpose
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3F
---

## Definition

The dual map of a linear map pulls each linear form on the target back to a linear form on the source.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *dual map* of $T$, also called its *transpose*, is the map
$$T^* \colon W^* \to V^*, \qquad T^*(\varphi) = \varphi \circ T,$$
between the [[dual spaces|0M856Q1AMZ]].

## Notation

Other notations are $T^{\mathsf{T}}$, $T^t$, ${}^t T$ and $T'$.
Some books call $T^*$ the adjoint of $T$.
In math2 the adjoint is the [[adjoint for an inner product|0ST8QF9T3T]], a different map $W \to V$ that needs inner products.
Mathlib writes `Module.Dual.transpose`.

## Remarks

The definition needs $T$ to be linear and $\varphi$ to be linear, because then $\varphi \circ T$ is a composite of linear maps and so lies in $V^*$.
The map $T^*$ is itself linear, since the sum and the scalar multiple in $W^*$ and $V^*$ are taken value by value.

For example, let $T \colon \R^2 \to \R^2$ be $T(x, y) = (x + 2y, \, 3x + 4y)$ and let $\varphi(a, b) = a$.
Then $T^*(\varphi)(x, y) = \varphi(T(x, y)) = x + 2y$.

Linearity of $T$ is what makes the definition work.
For the map $S(x) = x + 1$ on $\R$, which is not linear, the composite $\varphi \circ S$ with $\varphi(a) = a$ is $x \mapsto x + 1$, and this is not a linear form, since it sends $0$ to $1$.

The [[concept page|0AZ5ARP287]] works out examples and the main properties: the order reversal $(S \circ T)^* = T^* \circ S^*$, the transpose as the matrix in dual bases, and the kernel and image of $T^*$.

## Explanations

### L1 human

A linear form on $W$ is a rule that turns each vector of $W$ into a number.
You can pull such a rule back to $V$: first apply $T$, then the rule.
The dual map does this pullback for every rule at once.
It goes in the opposite direction to $T$, from rules on $W$ to rules on $V$.
