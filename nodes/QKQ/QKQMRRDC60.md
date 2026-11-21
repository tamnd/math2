---
tag: QKQMRRDC60
kind: example
name: The natural number order is rigid
msc: ["03C50", "06A05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [EPNZKJQHWJ]
uses: [EPNZKJQHWJ, DSQ17TNW1C, 0ASJVEFA9J, DKAGC639W9, 4NJS7W57VK]
sources:
  - url: https://en.wikipedia.org/wiki/Rigidity_(mathematics)
    locator: Examples
---

## Example

Let $\mathcal{N} = (\N, <)$ and let $\sigma$ be an [[automorphism|DSQ17TNW1C]] of $\mathcal{N}$.

1. The element $0$ is the least element. An automorphism maps the least element to the least element, so $\sigma(0) = 0$.
2. The element $n + 1$ is the least element above $n$. An automorphism preserves this relation, so $\sigma(n + 1)$ is the least element above $\sigma(n)$.
3. By [[induction|0ASJVEFA9J]] on $n$, if $\sigma(n) = n$, then $\sigma(n + 1) = n + 1$.
4. So $\sigma$ is the identity, and $\mathcal{N}$ is [[rigid|EPNZKJQHWJ]].

## Remarks

Steps 1 and 2 use only first-order properties, so every $n$ is definable without parameters: $\operatorname{dcl}(\emptyset) = \N$; see [[algebraic and definable closure|DKAGC639W9]].
So $\mathcal{N}$ is homogeneous for a degenerate reason: the only partial elementary maps are restrictions of the identity.
A nonstandard model $\N + \Z \times D$ of $\operatorname{Th}(\N, <)$, with a nonempty order $D$, is not rigid: the map that fixes $\N$ and sends $(d, z)$ to $(d, z + 1)$ is an automorphism.

## Explanations

### L1 human

Every natural number can be described from the order alone: $0$ is the first, $1$ the second, and so on.
A symmetry must respect these descriptions, so it moves nothing.

### L2 human

The argument has two parts.

1. Find a description of each element that a symmetry must respect.
2. Conclude that each element is fixed.

The typical use is to prove rigidity by showing that every element is definable.
The trap is to expect the same for the elementary extensions, which have non-definable elements and shifts.
