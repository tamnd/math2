---
tag: MR5FJXR348
kind: statement
role: theorem
name: Bounded inverse theorem
msc: [46A30, 47A05]
uses: [06GZ956657, 03TM135G0N, 0GG9TVW90M, 0J2WAR83WP]
about: [03TM135G0N, 0J2WAR83WP]
sources:
  - url: https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis)
---

## Statement

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]] over $\R$ or $\C$.
Let $T \colon X \to Y$ be a [[continuous linear map|03TM135G0N]] that is [[bijective|0GG9TVW90M]].
Then the [[inverse|0J2WAR83WP]] $T^{-1} \colon Y \to X$ is continuous, that is, there is a constant $C \ge 0$ with $\norm{T^{-1} y} \le C \norm{y}$ for all $y \in Y$.

## Remarks

The theorem follows from the open mapping theorem: a surjective continuous linear map between Banach spaces sends open sets to open sets.
That theorem is proved with the [[Baire category theorem|0A7KGAYHGV]] applied to the cover $Y = \bigcup_k \overline{T(B(0, k))}$.
For a bijection, openness of $T$ is exactly continuity of $T^{-1}$.

A common application: if a vector space is complete for two norms $\norm{\cdot}_1$ and $\norm{\cdot}_2$ with $\norm{x}_2 \le c \norm{x}_1$, then the two norms are equivalent.
Indeed, the identity map is a continuous bijection from the first norm to the second.
Completeness of $Y$ is necessary.
On $\ell^1$ the identity map from $(\ell^1, \norm{\cdot}_1)$ to $(\ell^1, \norm{\cdot}_\infty)$ is a continuous linear bijection, because $\norm{x}_\infty \le \norm{x}_1$.
Its inverse is not bounded: $x = e_1 + \cdots + e_n$ has $\norm{x}_\infty = 1$ and $\norm{x}_1 = n$.
Here $(\ell^1, \norm{\cdot}_\infty)$ is not complete.

## Explanations

### L1 human

If a continuous linear map between complete normed spaces is one-to-one and onto, then undoing it is also continuous.
So such a map is an isomorphism of Banach spaces, with no extra checks.
Small changes in the output come from small changes in the input.

### L2 human

The theorem is used to prove stability of solutions: if an equation $Tx = y$ has exactly one solution for each $y$, the solution depends continuously on $y$.
It is equivalent, by short arguments, to the open mapping theorem and to the [[closed graph theorem|GXM8BX8YM7]].
Together with the [[uniform boundedness principle|YG0042V8CJ]] these results all rest on the [[Baire category theorem|0A7KGAYHGV]].
