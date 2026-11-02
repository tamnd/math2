---
tag: NPBWWBGV37
kind: definition
name: Hilbert–Schmidt operator
msc: [47B10, 45P05, 47G10]
defines: W3BX66Y47G
uses: [HM2HHE3J51, 0S9GGTR0EX, 03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_operator
---

## Definition

Let $H$ and $K$ be [[Hilbert spaces|HM2HHE3J51]] and let $A \colon H \to K$ be a [[bounded linear operator|03TM135G0N]].
The operator $A$ is a *Hilbert–Schmidt operator* if there is an [[orthonormal basis|0S9GGTR0EX]] $(e_i)_{i \in I}$ of $H$ such that
$$\sum_{i \in I} \norm{A e_i}^2 < \infty.$$
The *Hilbert–Schmidt norm* of $A$ is $\norm{A}_{\mathrm{HS}} = \big( \sum_{i \in I} \norm{A e_i}^2 \big)^{1/2}$.

## Remarks

The condition and the value of the sum do not depend on the orthonormal basis.
Indeed, for an orthonormal basis $(f_j)_{j \in J}$ of $K$, Parseval's identity gives $\sum_i \norm{A e_i}^2 = \sum_i \sum_j \abs{\ip{A e_i}{f_j}}^2 = \sum_j \norm{A^* f_j}^2$, and the right side does not involve $(e_i)$.

Every Hilbert–Schmidt operator is [[compact|M2NEP1K5AE]] and satisfies $\norm{A} \le \norm{A}_{\mathrm{HS}}$.
A compact operator is Hilbert–Schmidt if and only if its [[singular values|QSJKPKPM7H]] $\sigma_n$ satisfy $\sum_n \sigma_n^2 < \infty$, and then $\norm{A}_{\mathrm{HS}}^2 = \sum_n \sigma_n^2$.
The Hilbert–Schmidt operators form the Schatten class $S_2$; every [[trace class operator|C37R11WREF]] is Hilbert–Schmidt.
On $L^2$ spaces of $\sigma$-finite measure spaces, they are the [[integral operators with square-integrable kernels|CB5G212Q03]], and $\norm{A}_{\mathrm{HS}}$ is the $L^2$ norm of the kernel.

Example: on $\ell^2$, the operator $A(x_1, x_2, \dots) = (x_1, x_2/2, x_3/3, \dots)$ is Hilbert–Schmidt.
For the standard basis, $\norm{A e_n} = 1/n$ and $\sum_n 1/n^2 = \pi^2/6$.

Non-example: on $\ell^2$, the operator $B(x_1, x_2, \dots) = (x_1, x_2/\sqrt{2}, x_3/\sqrt{3}, \dots)$ is compact but not Hilbert–Schmidt, since $\sum_n \norm{B e_n}^2 = \sum_n 1/n$ diverges.
The identity of an infinite-dimensional Hilbert space is not Hilbert–Schmidt either.

## Explanations

### L1 human

An operator is Hilbert–Schmidt when the total squared size of the images of the basis vectors is finite.
