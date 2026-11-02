---
tag: X9XRGMDCQZ
kind: statement
role: theorem
name: Weyl's theorem on compact perturbations
msc: [47A55, 47A10, 47B25]
uses: [HM2HHE3J51, 6HSJBJ8TTQ, M2NEP1K5AE, FRZG0E15SK, PJWY3JJQQ7]
about: [FRZG0E15SK]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_spectrum
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
Let $A$ be a bounded self-adjoint operator on $H$, that is, $A = A^*$ with $A^*$ the [[adjoint|6HSJBJ8TTQ]] of $A$.
Let $K$ be a [[compact operator|M2NEP1K5AE]] on $H$ with $K = K^*$.
Then
$$\sigma_{\mathrm{ess}}(A + K) = \sigma_{\mathrm{ess}}(A),$$
where $\sigma_{\mathrm{ess}}$ denotes the [[essential spectrum|FRZG0E15SK]].

## Remarks

For a self-adjoint operator, $\lambda$ lies in the essential spectrum if and only if there is a Weyl sequence: an orthonormal sequence $(x_n)$ in $H$ with $\norm{(A - \lambda) x_n} \to 0$.
An orthonormal sequence tends to $0$ weakly, and a compact operator maps weakly null sequences to norm null sequences, so $\norm{K x_n} \to 0$.
Hence a Weyl sequence for $A$ at $\lambda$ is also one for $A + K$, and the symmetric argument gives the reverse inclusion.
The theorem also holds for unbounded self-adjoint $A$, with $A + K$ defined on the domain of $A$.
In other words, a compact perturbation of a self-adjoint operator can only change its [[discrete spectrum|PJWY3JJQQ7]], the isolated eigenvalues of finite multiplicity.
With the definition of the essential spectrum through Fredholm operators, the equality holds for every bounded operator $A$ on a Banach space and every compact $K$.
Indeed, $A + K - \lambda I$ is Fredholm exactly when $A - \lambda I$ is.
Example: on $\ell^2$, the zero operator has essential spectrum $\set{0}$, and so does every compact self-adjoint operator, such as the diagonal operator with entries $1/n$.
Without compactness the conclusion fails: a self-adjoint projection $P$ of infinite rank and infinite corank has $\sigma_{\mathrm{ess}}(0 + P) = \set{0, 1}$, while $\sigma_{\mathrm{ess}}(0) = \set{0}$.

## Explanations

### L1 human

The essential spectrum is the robust part of the spectrum of an operator, the part that does not come from finitely many isolated eigenvalues.
Weyl's theorem says that adding a compact operator, a small perturbation in a precise sense, never changes this robust part.
Only the isolated eigenvalues of finite multiplicity can move, appear or disappear.

### L2 human

The theorem is a basic tool of mathematical physics.
For a Schrödinger operator $-\Delta + V$ with a potential $V$ that decays at infinity, one shows that $V$ is a relatively compact perturbation of $-\Delta$.
A version of Weyl's theorem for relatively compact perturbations then gives $\sigma_{\mathrm{ess}}(-\Delta + V) = [0, \infty)$, so the negative spectrum consists of isolated eigenvalues, the bound states.
