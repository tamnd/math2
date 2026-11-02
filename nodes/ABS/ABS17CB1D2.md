---
tag: ABS17CB1D2
kind: statement
role: theorem
name: Atkinson's theorem
msc: [47A53]
uses: [06GZ956657, 03TM135G0N, 8HWGKWD6ZM, M2NEP1K5AE, Z8FABSYQTS, 6FE7JZ2VF1]
about: [8HWGKWD6ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Atkinson%27s_theorem
same_as:
  wikidata: Q4815899
  wikipedia: Atkinson's theorem
---

## Statement

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]], and let $T \colon X \to Y$ be a [[bounded linear map|03TM135G0N]].
Then $T$ is a [[Fredholm operator|8HWGKWD6ZM]] if and only if there is a bounded linear map $S \colon Y \to X$ such that $ST - I_X$ and $TS - I_Y$ are [[compact operators|M2NEP1K5AE]].

## Remarks

If $T$ is Fredholm, choose closed complements $X = \ker T \oplus X_0$ and $Y = T(X) \oplus Y_0$, with $Y_0$ finite-dimensional.
Then $T$ maps $X_0$ bijectively onto $T(X)$, and $S$ can be taken as its inverse on $T(X)$ and $0$ on $Y_0$.
With this choice, $I_X - ST$ and $I_Y - TS$ are projections onto $\ker T$ and $Y_0$, so they are even [[finite-rank operators|Z8FABSYQTS]].
Conversely, if $ST = I_X + K$ with $K$ compact, then $\ker T \subseteq \ker(I_X + K)$ is finite-dimensional, and $TS = I_Y + K'$ shows that $T(X) \supseteq (I_Y + K')(Y)$ has finite codimension.
For a Hilbert space $H$, the theorem says that $T \in B(H)$ is Fredholm if and only if its image is invertible in the [[Calkin algebra|6FE7JZ2VF1]] $B(H)/K(H)$.
Example: the right shift $S$ on $\ell^2$ and the left shift $S^*$ satisfy $S^* S = I$ and $S S^* = I - P$, where $P$ is the rank-one projection onto the first coordinate, so $S$ is Fredholm.

## Explanations

### L1 human

A Fredholm operator is one that can be inverted up to a compact error.
The theorem says that this is exactly the condition of finite-dimensional kernel and cokernel.
So Fredholm operators are the operators that are invertible once one ignores compact operators.

### L2 human

The theorem turns Fredholm theory into algebra: Fredholm operators are the preimages of the invertible elements of a quotient algebra.
From this view, it follows at once that compact perturbations of Fredholm operators are Fredholm, and that products of Fredholm operators are Fredholm.
It also leads to the essential spectrum of an operator $T$ on a Hilbert space, the spectrum of its image in the Calkin algebra.
