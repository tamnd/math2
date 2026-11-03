---
tag: JDJTYXMZ0D
kind: statement
role: theorem
name: Hellmann–Feynman theorem
msc: [81Q15, 81Q10]
uses: [0P17NGQQMQ, 0BQAA2BK3Q, VXDEQB46GV, JNK7GJ3AKE]
about: [VXDEQB46GV, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hellmann%E2%80%93Feynman_theorem
same_as:
  wikidata: Q906809
  wikipedia: Hellmann–Feynman theorem
---

## Statement

Let $I \subseteq \R$ be an open interval and let $\lambda \mapsto H(\lambda)$ be a differentiable map from $I$ to the [[Hermitian matrices|0P17NGQQMQ]] of size $n \times n$.
Let $\lambda \mapsto \psi(\lambda)$ be a differentiable map from $I$ to $\C^n$ and $E \colon I \to \R$ a function such that $\norm{\psi(\lambda)} = 1$ and $H(\lambda)\psi(\lambda) = E(\lambda)\psi(\lambda)$ for all $\lambda \in I$.
Then $E$ is differentiable and
$$E'(\lambda) = \left\langle \psi(\lambda), H'(\lambda)\, \psi(\lambda) \right\rangle \quad \text{for all } \lambda \in I.$$

## Remarks

The proof differentiates $E(\lambda) = \langle \psi(\lambda), H(\lambda)\psi(\lambda) \rangle$ by the product rule.
The two terms with $\psi'$ add up to $E(\lambda)\big(\langle \psi', \psi \rangle + \langle \psi, \psi' \rangle\big)$, because $H(\lambda)$ is Hermitian and $\psi(\lambda)$ is an [[eigenvector|0BQAA2BK3Q]].
This sum is $E(\lambda)$ times the derivative of $\norm{\psi(\lambda)}^2 = 1$, so it vanishes, and only the term with $H'$ is left.
Example: for $H(\lambda) = \begin{pmatrix} \lambda & 1 \\ 1 & -\lambda \end{pmatrix}$ the top eigenvalue is $E(\lambda) = \sqrt{1 + \lambda^2}$.
The unit eigenvector is proportional to $(1, E - \lambda)$, and a short computation gives $\langle \psi, H'\psi \rangle = \lambda / \sqrt{1 + \lambda^2}$, which is indeed $E'(\lambda)$.
The normalization is needed: for an eigenvector of non-constant length the right side must be divided by $\norm{\psi(\lambda)}^2$.
The same formula holds for self-adjoint operators on a Hilbert space under suitable domain and differentiability conditions.

## Explanations

### L1 human

A quantum system has a [[Hamiltonian|VXDEQB46GV]] that depends on a knob $\lambda$, such as the strength of an outside field.
The theorem says how fast an energy level moves when the knob turns.
The rate equals the [[expectation value|JNK7GJ3AKE]] of the derivative of the Hamiltonian in the corresponding state.
So one does not need to know how the state itself changes.

### L2 human

For $H(\lambda) = H_0 + \lambda V$ the theorem gives $E'(\lambda) = \langle \psi(\lambda), V \psi(\lambda) \rangle$.
At $\lambda = 0$ this is the first-order energy correction of Rayleigh–Schrödinger perturbation theory.
In quantum chemistry, taking $\lambda$ to be a nuclear coordinate turns the theorem into a formula for the force on a nucleus as an expectation value.
The hypothesis that $\psi$ is differentiable can fail where two eigenvalues cross, since the eigenvectors may jump there.
