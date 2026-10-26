---
tag: 0C2TQMW5A1
kind: definition
name: Dual map
msc: [15A04]
defines: 0AZ5ARP287
uses: [0M856Q1AMZ, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Definition
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *dual map* of $T$, also called its *transpose*, is the map
$$T^* \colon W^* \to V^*, \qquad T^*(f) = f \circ T,$$
between the [[dual spaces|07JBSZE0V4]].

## Remarks

The dual map is linear.
It reverses the order of composition: $(T \circ S)^* = S^* \circ T^*$, and $(\id_V)^* = \id_{V^*}$.
In dual bases, the matrix of $T^*$ is the transpose of the matrix of $T$, see [[the matrix of the dual map|0ZPB3180AY]].
The kernel of $T^*$ is the [[annihilator|0ASHNYF7AG]] of the image of $T$.

## Explanations

### L1 human

A linear form on $W$ can be pulled back to $V$: first apply $T$, then the form.
The dual map does this pullback.
It goes in the opposite direction, from $W^*$ to $V^*$.
