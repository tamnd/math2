---
tag: C37R11WREF
kind: definition
name: Trace class operator
msc: [47B10]
defines: Z2CP530WDE
uses: [HM2HHE3J51, 6HSJBJ8TTQ, 77020CY5ZW, 3JY5HNFRMF, 0S9GGTR0EX, QSJKPKPM7H, 153N5DW55Z, 0XC1RDBY7A]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_class
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $T$ be a bounded operator on $H$ with [[adjoint|6HSJBJ8TTQ]] $T^*$.
Let $\abs{T} = (T^* T)^{1/2}$ be the [[square root|3JY5HNFRMF]] of the [[positive operator|77020CY5ZW]] $T^* T$.
The operator $T$ is *trace class* if for some [[orthonormal basis|0S9GGTR0EX]] $(e_i)_{i \in I}$ of $H$,
$$\norm{T}_1 = \sum_{i \in I} \ip{\abs{T} e_i}{e_i} < \infty.$$
The number $\norm{T}_1$ does not depend on the orthonormal basis; it is the *trace norm* of $T$.

## Remarks

If $T$ is trace class, then for every orthonormal basis $(e_i)$ the sum $\operatorname{tr} T = \sum_i \ip{T e_i}{e_i}$ converges absolutely, and its value does not depend on the basis.
On $\C^n$, this is the usual [[trace|0XC1RDBY7A]] of a matrix.
Equivalently, $T$ is trace class if and only if $T$ is compact and its [[singular values|QSJKPKPM7H]] satisfy $\sum_n s_n(T) < \infty$, so the trace class is the [[Schatten class|153N5DW55Z]] $S_1$.
Example: on $\ell^2$, let $T e_n = e_n / n^2$; then $\abs{T} = T$ and $\norm{T}_1 = \sum 1/n^2 < \infty$, so $T$ is trace class with $\operatorname{tr} T = \pi^2 / 6$.
Non-example: $D e_n = e_n / n$ gives $\sum_n \ip{\abs{D} e_n}{e_n} = \sum 1/n = \infty$, so $D$ is compact but not trace class.
The trace class operators form a two-sided ideal of the bounded operators, and $\operatorname{tr}(AT) = \operatorname{tr}(TA)$ for $T$ trace class and $A$ bounded.
