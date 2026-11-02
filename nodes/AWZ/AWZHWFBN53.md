---
tag: AWZHWFBN53
kind: definition
name: Tensor field
msc: [53A45, 58A10]
defines: WX302T93TW
uses: [F45VQ47GPV, WY6K3P4YCG, 0BF2DE2SYK, WWX7H5W1RP]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_field
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, let $T_pM$ be the tangent space at $p \in M$, and let $T_p^*M$ be its dual space.
Let $k, l \ge 0$ be integers.
A *tensor of type $(k, l)$ at $p$* is an element of the [[tensor product|0BF2DE2SYK]]
$$T^k_l(T_pM) = \underbrace{T_pM \otimes \cdots \otimes T_pM}_{k} \otimes \underbrace{T_p^*M \otimes \cdots \otimes T_p^*M}_{l}.$$
These spaces form a smooth vector bundle $T^k_l M \to M$, built from the [[tangent bundle|WY6K3P4YCG]] as $TM$ is.
A *tensor field of type $(k, l)$* on $M$ is a smooth [[section|WWX7H5W1RP]] of $T^k_l M$.
In a chart with coordinates $x^1, \dots, x^n$, a tensor field $T$ is written as follows, with summation over repeated indices.
$$T = T^{i_1 \cdots i_k}_{j_1 \cdots j_l} \, \partial_{i_1} \otimes \cdots \otimes \partial_{i_k} \otimes dx^{j_1} \otimes \cdots \otimes dx^{j_l}.$$
Smoothness means that the component functions $T^{i_1 \cdots i_k}_{j_1 \cdots j_l}$ are smooth in every chart.

## Remarks

Example: on $\R^2$, $g = dx \otimes dx + dy \otimes dy$ is a tensor field of type $(0, 2)$; its components are the constants $g_{11} = g_{22} = 1$ and $g_{12} = g_{21} = 0$, which are smooth.
A tensor field of type $(1, 0)$ is a vector field, and a tensor field of type $(0, 0)$ is a smooth function.
Non-example: the Christoffel symbols of a connection are not the components of a tensor field.
Under a change of chart they pick up a term with second derivatives of the coordinate change.
A tensor field of type $(0, l)$ is the same as a map $(X_1, \dots, X_l) \mapsto T(X_1, \dots, X_l)$ from $l$ vector fields to smooth functions that is $C^\infty(M)$-linear in each argument.
This criterion is the standard way to check that an expression is tensorial.
