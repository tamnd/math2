---
tag: KX91FNNS74
kind: definition
name: Coherent state
msc: [81R30, 81V80]
defines: TQGXZYE50R
uses: [HM2HHE3J51, 7N0J4DF8N5]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_state
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] with an orthonormal basis $(e_n)_{n \ge 0}$.
Let $a$ be the [[annihilation operator|7N0J4DF8N5]] given by $a\, e_0 = 0$ and $a\, e_n = \sqrt{n}\, e_{n-1}$ for $n \ge 1$.
For $\alpha \in \C$, the *coherent state* with parameter $\alpha$ is the unit vector
$$\psi_{\alpha} = e^{-\abs{\alpha}^2/2} \sum_{n \ge 0} \frac{\alpha^n}{\sqrt{n!}}\, e_n.$$

## Remarks

Check: $\norm{\psi_{\alpha}}^2 = e^{-\abs{\alpha}^2} \sum_n \abs{\alpha}^{2n}/n! = 1$.
Applying $a$ term by term gives $a \psi_{\alpha} = e^{-\abs{\alpha}^2/2} \sum_{n \ge 1} \frac{\alpha^n}{\sqrt{(n-1)!}}\, e_{n-1} = \alpha \psi_{\alpha}$.
Conversely, every eigenvector of $a$ with eigenvalue $\alpha$ is a multiple of $\psi_{\alpha}$, because the eigen-equation forces $c_n = \alpha c_{n-1}/\sqrt{n}$ for its coefficients.
So the coherent states are exactly the normalized eigenvectors of $a$, up to a phase.
Equivalently $\psi_{\alpha} = \exp(\alpha a^* - \bar\alpha a)\, e_0$, the image of the ground state under a displacement operator.

Further properties: $\abs{\ip{\psi_\beta}{\psi_\alpha}}^2 = e^{-\abs{\alpha - \beta}^2}$, so distinct coherent states are never orthogonal, and $\frac{1}{\pi} \int_{\C} P_\alpha\, d^2\alpha = I$ in the weak sense, where $P_\alpha$ is the orthogonal projection onto the line spanned by $\psi_\alpha$.

Example: $\psi_{0} = e_0$ is the ground state of the oscillator.

Non-example: $e_1$ is not a coherent state, since $a\, e_1 = e_0$ is not a multiple of $e_1$.
Also the creation operator $a^*$ has no eigenvectors at all, so there is no analogous family for $a^*$.

In the Schrödinger realization on $L^2(\R)$ with $\hbar = m = \omega = 1$, one has $a = (Q + iP)/\sqrt{2}$, $e_n$ is the $n$-th Hermite function, and $\psi_{\alpha}$ is a Gaussian centred at position $\sqrt{2}\, \mathrm{Re}\, \alpha$ and momentum $\sqrt{2}\, \mathrm{Im}\, \alpha$.
