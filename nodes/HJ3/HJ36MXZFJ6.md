---
tag: HJ36MXZFJ6
kind: definition
name: Spin
msc: [81R05, 81R25, 81V72]
defines: YBS1CHXFTW
uses: [VKWHPCHH6K, E5P8AG6CK7, FX3NEFYFFN, 5S7FCJMCD7, XAQCW3D4QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_(physics)
---

## Definition

Let $s \in \set{0, \frac12, 1, \frac32, \ldots}$ and $\hbar > 0$.
Let $S = (S_1, S_2, S_3)$ be a triple of Hermitian operators on $\C^{2s+1}$ that acts irreducibly.
Assume it is an [[angular momentum operator|VKWHPCHH6K]]: $[S_1, S_2] = i\hbar S_3$, and the same for cyclic permutations.
Then it comes from the [[irreducible representation|FX3NEFYFFN]] of [[SU(2)|E5P8AG6CK7]] of dimension $2s + 1$.
It satisfies $S_1^2 + S_2^2 + S_3^2 = \hbar^2 s(s+1) I$.
A particle of *spin* $s$ has the state space $L^2(\R^3) \otimes \C^{2s+1}$.
This is the [[tensor product|5S7FCJMCD7]] of the space of wave functions with the space of internal states.
The triple $S$, acting on the second factor, is its *spin operator*.
Its total angular momentum is $J = L \otimes I + I \otimes S$, where $L$ is the orbital angular momentum.

## Remarks

The eigenvalues of $S_3$ are $\hbar m$ for $m = -s, \ldots, s$.
A rotation by angle $\theta$ about a unit axis $n$ acts on internal states by $e^{-i\theta\, n \cdot S/\hbar}$.
For $\theta = 2\pi$ this is $(-1)^{2s} I$, so for half-integer $s$ the internal states form a representation of SU(2) that is only a projective representation of SO(3).

Example: for $s = \frac12$, $S = \frac{\hbar}{2}\sigma$ with the [[Pauli matrices|XAQCW3D4QQ]] $\sigma = (\sigma_1, \sigma_2, \sigma_3)$.
Since $\sigma_k^2 = I$, one gets $S^2 = \frac{3\hbar^2}{4} I = \hbar^2 \cdot \frac12 \cdot \frac32 \, I$, as required, and $S_3$ has eigenvalues $\pm\frac{\hbar}{2}$.

Non-example: the orbital angular momentum $L$ on $L^2(\R^3)$ is an angular momentum operator, but it is not a spin.
The space $L^2(\R^3)$ is infinite-dimensional, $L_1^2 + L_2^2 + L_3^2$ is not a multiple of the identity, and only integer values $\ell$ occur.
