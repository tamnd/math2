---
tag: 8YYDZZCFY6
kind: definition
name: Dual object
msc: [18M05, 18M10]
defines: 8A7YXMW727
uses: [M3MSQ3NKAE, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_object
---

## Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]] and let $A$ be an object of $\mathcal{C}$.
A *dual* of $A$ is an object $A^*$ together with morphisms $\mathrm{ev} \colon A^* \otimes A \to I$ and $\mathrm{coev} \colon I \to A \otimes A^*$ such that:

1. $\rho_A \circ (\id_A \otimes \mathrm{ev}) \circ \alpha_{A,A^*,A} \circ (\mathrm{coev} \otimes \id_A) \circ \lambda_A^{-1} = \id_A$;
2. $\lambda_{A^*} \circ (\mathrm{ev} \otimes \id_{A^*}) \circ \alpha^{-1}_{A^*,A,A^*} \circ (\id_{A^*} \otimes \mathrm{coev}) \circ \rho_{A^*}^{-1} = \id_{A^*}$.

These are the zigzag (or triangle) identities.
In this situation $A^*$ is called a right dual of $A$, and $A$ a left dual of $A^*$.
Some authors exchange the words left and right.

## Remarks

Example: in $\mathbf{Vect}_k$, a finite-dimensional space $V$ with basis $e_1, \ldots, e_n$ has the [[dual space|07JBSZE0V4]] $V^*$ with dual basis $e^1, \ldots, e^n$ as dual.
Take $\mathrm{ev}(f \otimes v) = f(v)$ and $\mathrm{coev}(1) = \sum_i e_i \otimes e^i$.
The first identity sends $v$ to $\sum_i e_i \, e^i(v) = v$, and the second sends $f$ to $\sum_i f(e_i)\, e^i = f$.
Non-example: an infinite-dimensional space $V$ has no dual in $\mathbf{Vect}_k$.
The element $\mathrm{coev}(1)$ is a finite sum $\sum_{i=1}^m v_i \otimes w_i$, so the first identity would express every $v \in V$ as a combination of $v_1, \ldots, v_m$, which is impossible.
Duals are unique up to unique isomorphism compatible with $\mathrm{ev}$ and $\mathrm{coev}$.
In a symmetric monoidal category left and right duals coincide, and the trace of $f \colon A \to A$ is $\mathrm{ev} \circ \gamma_{A,A^*} \circ (f \otimes \id_{A^*}) \circ \mathrm{coev} \colon I \to I$.
