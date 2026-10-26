---
tag: ~bde2fa70
kind: definition
name: Dual map
msc: [15A04]
defines: ~fc62086c
uses: [~adaeb46b, ~1b1da4fe]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Definition
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|~2402e937]].
The *dual map* of $T$, also called its *transpose*, is the map
$$T^* \colon W^* \to V^*, \qquad T^*(f) = f \circ T,$$
between the [[dual spaces|~d8a7f260]].

## Remarks

The dual map is linear.
It reverses the order of composition: $(T \circ S)^* = S^* \circ T^*$, and $(\id_V)^* = \id_{V^*}$.
In dual bases, the matrix of $T^*$ is the transpose of the matrix of $T$, see [[the matrix of the dual map|~b94758ad]].
The kernel of $T^*$ is the [[annihilator|~b4a0e802]] of the image of $T$.

## Explanations

### L1 human

A linear form on $W$ can be pulled back to $V$: first apply $T$, then the form.
The dual map does this pullback.
It goes in the opposite direction, from $W^*$ to $V^*$.
