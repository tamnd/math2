---
tag: 0QHTX7WQEY
kind: definition
name: Differential form
msc: [58A10]
defines: 0E3G0GRPZ6
uses: [0MTENFBW3Q, 0S166D363M, 004FRCXH6M, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_form
    locator: Multi-index notation
  - url: https://en.wikipedia.org/wiki/Differential_form
    locator: Exterior product
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $0 \le k \le n$.
Take a multi-index $I = (i_1, \dots, i_k)$ with $1 \le i_1 < \dots < i_k \le n$. Let $dx_I$ be the function of $k$ vectors $v_1, \dots, v_k \in \mathbb{R}^n$ given by
$$dx_I(v_1, \dots, v_k) = \det \big[ (v_j)_{i_l} \big]_{l, j = 1}^{k},$$
the determinant of a $k \times k$ matrix. The entry of this matrix in row $l$ and column $j$ is the $i_l$-th component of $v_j$.
A differential $k$-form on $U$ is a sum $\omega = \sum_I f_I \, dx_I$ over these multi-indices, where each $f_I \colon U \to \mathbb{R}$ is a function. At $x \in U$, it gives the function $\omega_x(v_1, \dots, v_k) = \sum_I f_I(x) \, dx_I(v_1, \dots, v_k)$.

## Remarks

The form is of class $C^r$ if all $f_I$ are of [[class C^r|0TCBZMEYGN]]. A $0$-form is a function, and a [[1-form|0MTENFBW3Q]] is $\sum_i f_i \, dx_i$.
Each $\omega_x$ is multilinear and alternating: it changes sign when two of the vectors are swapped. The forms $dx_I$ give a basis of such functions, so there are $\binom{n}{k}$ of them, and no nonzero forms of degree $k > n$.
In the [[wedge product|0S166D363M]] notation, $dx_I = dx_{i_1} \wedge \dots \wedge dx_{i_k}$. On $\mathbb{R}^3$, $dx \wedge dy \wedge dz$ gives the signed volume of the parallelepiped spanned by three vectors.
In $\mathbb{R}^3$, 1-forms and 2-forms correspond to vector fields, and 0-forms and 3-forms to functions. The [[exterior derivative|004FRCXH6M]] then corresponds to the gradient, curl and divergence.

## Explanations

### L1 human

A $k$-form measures small $k$-dimensional pieces: a 1-form measures small arrows, a 2-form small parallelograms, and so on.
Integrating a $k$-form over a $k$-dimensional surface adds up these measurements over the whole surface.
