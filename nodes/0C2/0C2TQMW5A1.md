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

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *dual map* of $T$, also called its *transpose*, is the map
$$T^* \colon W^* \to V^*, \qquad T^*(\varphi) = \varphi \circ T,$$
between the [[dual spaces|0M856Q1AMZ]].

## Notation

Other notations are $T^{\mathsf{T}}$, $T^t$, ${}^t T$ and $T'$.
Some books call $T^*$ the adjoint of $T$; in this encyclopedia, the adjoint is the [[adjoint for an inner product|0ST8QF9T3T]].
Mathlib writes `Module.Dual.transpose`.

## Remarks

- $T^*(\varphi)$ is linear as a composition of linear maps, and $T^*$ is linear because the operations of $V^*$ are pointwise.
- It reverses the order of composition: $(T \circ S)^* = S^* \circ T^*$, and $(\id_V)^* = \id_{V^*}$; see the [[functoriality lemma|~3163ec56]].
- In dual bases, the matrix of $T^*$ is the transpose of the matrix of $T$; see [[the matrix of the dual map|0ZPB3180AY]].
- The kernel of $T^*$ is the [[annihilator|0R6M158SQ9]] of the image of $T$; see the [[kernel and image of the dual map|~0b4dab92]].

## Explanations

### L1 human

A linear form on $W$ can be pulled back to $V$: first apply $T$, then the form.
The dual map does this pullback.
It goes in the opposite direction, from $W^*$ to $V^*$.
