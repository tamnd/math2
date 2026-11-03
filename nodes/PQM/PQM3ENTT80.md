---
tag: PQM3ENTT80
kind: definition
name: Beta normal form
msc: [03B40, 68N18]
defines: FPD6AN79QX
uses: [BD756KR8FM, Y9B9CVY6SJ]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_normal_form
---

## Definition

Let $M$ be a term of the [[lambda calculus|BD756KR8FM]].
The term $M$ is in *$\beta$-normal form* if no subterm of $M$ is a $\beta$-redex, that is, a term of the form $(\lambda x.\, P)\, Q$.
Equivalently, there is no term $N$ with $M \to_\beta N$, where $\to_\beta$ is one-step [[beta reduction|Y9B9CVY6SJ]].
A term $M$ *has a $\beta$-normal form* $N$ if $N$ is in $\beta$-normal form and $M \twoheadrightarrow_\beta N$.

## Remarks

The terms in $\beta$-normal form are exactly the terms of the shape
$$\lambda x_1.\, \cdots \lambda x_n.\, y\, N_1 \cdots N_k,$$
with $n, k \ge 0$, a variable $y$, and terms $N_1, \ldots, N_k$ in $\beta$-normal form.

Example: $\lambda f.\, \lambda x.\, f\, (f\, x)$ is in $\beta$-normal form.
Each application in it has the variable $f$ in function position, so no subterm is a redex.

Non-example: $\lambda x.\, (\lambda y.\, y)\, x$ is not in $\beta$-normal form, since it contains the redex $(\lambda y.\, y)\, x$.
It has the $\beta$-normal form $\lambda x.\, x$.

The term $\Omega = (\lambda x.\, x\, x)(\lambda x.\, x\, x)$ reduces in one step to itself and to nothing else, so it has no $\beta$-normal form.
