---
tag: QWQC5SV0SD
kind: statement
role: theorem
name: Nonemptiness of the spectrum
msc: [46H05, 47A10]
uses: [EH0CZ19RKP, 09FTAET5Z4]
about: [EH0CZ19RKP]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
---

## Statement

Let $A$ be a Banach algebra over the [[complex numbers|09FTAET5Z4]] with unit $1 \ne 0$.
For $a \in A$, let $\sigma(a) = \set{\lambda \in \C : a - \lambda 1 \text{ is not invertible in } A}$ be the [[spectrum|EH0CZ19RKP]] of $a$.
Then $\sigma(a)$ is nonempty for every $a \in A$.

## Remarks

Proof idea: suppose $\sigma(a)$ is empty.
Then the resolvent $R(\lambda) = (a - \lambda 1)^{-1}$ is defined on all of $\C$.
For each continuous linear functional $\varphi$ on $A$, the function $\lambda \mapsto \varphi(R(\lambda))$ is entire and tends to $0$ as $\abs{\lambda} \to \infty$.
By [[Liouville's theorem|0EHKVRF4J6]] it is zero, and by the [[Hahn–Banach theorem|QB5AE3VYZZ]] this forces $R(0) = a^{-1} = 0$, which is impossible since $1 \ne 0$.
Together with the [[compactness of the spectrum|FA5V5KRWDF]], the spectrum of every element is a nonempty compact subset of $\C$.

Example: in the algebra $C([0,1])$ of continuous complex functions with the sup norm, the spectrum of $f$ is its range $f([0,1])$, which is nonempty.

The complex scalars are needed.
In the real Banach algebra of real $2 \times 2$ matrices, the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ minus $\lambda 1$ has determinant $\lambda^2 + 1 > 0$ for every real $\lambda$, so its real spectrum is empty.
The condition $1 \ne 0$ is also needed: in the zero algebra every element is invertible.

## Explanations

### L1 human

For a square complex matrix, the spectrum is the set of eigenvalues, and every such matrix has an eigenvalue.
The theorem says the same thing for every element of a complex Banach algebra: there is always at least one number $\lambda$ for which $a - \lambda 1$ cannot be inverted.
The proof uses complex analysis instead of polynomials.

### L2 human

This result is the first step of spectral theory in Banach algebras.
It gives the [[Gelfand–Mazur theorem|3D6XH41A3B]]: a complex Banach division algebra is $\C$.
It also makes the spectral radius $\max \set{\abs{\lambda} : \lambda \in \sigma(a)}$ well defined, which is the subject of [[Gelfand's spectral radius formula|T4RFYT8HDN]].
