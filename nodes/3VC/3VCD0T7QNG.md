---
tag: 3VCD0T7QNG
kind: definition
name: Toeplitz operator
msc: [47B35, 30H10]
defines: GQ0X3R3WM2
uses: [PNNNFJVF6W, 0Q8HZTJC7G, GKY2WSHE26]
sources:
  - url: https://en.wikipedia.org/wiki/Toeplitz_operator
---

## Definition

Let $\mathbb{T}$ be the unit circle with normalised Lebesgue measure, and let $L^2 = L^2(\mathbb{T})$ (Lp space).
Let $H^2 \subseteq L^2$ be the [[Hardy space|PNNNFJVF6W]], the closed subspace of functions whose Fourier coefficients of negative index vanish.
Let $P \colon L^2 \to H^2$ be the [[orthogonal projection|0Q8HZTJC7G]].
For $\varphi \in L^\infty(\mathbb{T})$, the *Toeplitz operator* with symbol $\varphi$ is the operator $T_\varphi \colon H^2 \to H^2$ given by
$$T_\varphi f = P(\varphi f).$$

## Remarks

$T_\varphi$ is a bounded linear operator, and in fact $\norm{T_\varphi} = \norm{\varphi}_\infty$.
With respect to the orthonormal basis $e_n(t) = e^{int}$, $n \ge 0$, its matrix entries are $\ip{T_\varphi e_k}{e_j} = \hat\varphi(j - k)$, so the matrix is a [[Toeplitz matrix|GKY2WSHE26]].
If $\varphi$ is continuous and has no zeros on $\mathbb{T}$, then $T_\varphi$ is a Fredholm operator whose index is minus the winding number of $\varphi$ around $0$.

Example: $\varphi(e^{it}) = e^{it}$.
For $f \in H^2$ the product $\varphi f$ has no negative Fourier coefficients, so $P(\varphi f) = \varphi f$ and $T_\varphi$ is the shift operator $f \mapsto z f$.

Non-example: for $\varphi(e^{it}) = e^{-it}$, plain multiplication by $\varphi$ does not map $H^2$ into itself, since it sends $1$ to $e^{-it} \notin H^2$.
So the projection $P$ in the definition cannot be omitted; the Toeplitz operator $T_\varphi$ is the backward shift.
