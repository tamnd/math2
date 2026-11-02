---
tag: Q71WX8HFYT
kind: statement
role: theorem
name: Spectral mapping theorem for polynomials
msc: [46H05, 47A10]
uses: [EH0CZ19RKP, QWQC5SV0SD, 0SDC934R52]
about: [EH0CZ19RKP]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theory
---

## Statement

Let $A$ be a complex Banach algebra with unit $1 \ne 0$, let $a \in A$, and let $p \in \C[z]$ be a [[polynomial|0SDC934R52]].
Let $\sigma(b)$ denote the [[spectrum|EH0CZ19RKP]] of $b \in A$.
Then
$$\sigma(p(a)) = p(\sigma(a)) = \set{p(\lambda) : \lambda \in \sigma(a)}.$$

## Remarks

Proof idea: if $p$ is constant equal to $c$, both sides are $\set{c}$, using the [[nonemptiness of the spectrum|QWQC5SV0SD]].
Otherwise fix $\mu \in \C$ and factor $p(z) - \mu = c (z - \lambda_1) \cdots (z - \lambda_k)$ with $c \ne 0$.
Then $p(a) - \mu 1 = c (a - \lambda_1 1) \cdots (a - \lambda_k 1)$, a product of commuting factors.
A product of commuting elements is invertible if and only if each factor is invertible.
So $\mu \in \sigma(p(a))$ if and only if some root $\lambda_i$ of $p - \mu$ lies in $\sigma(a)$, that is, if and only if $\mu = p(\lambda)$ for some $\lambda \in \sigma(a)$.

Example: if $a$ is a $2 \times 2$ complex matrix with eigenvalues $1$ and $-1$, then $a^2$ has the single eigenvalue $1$, matching $p(\sigma(a)) = \set{1}$ for $p(z) = z^2$.

## Explanations

### L1 human

If you know the spectrum of $a$, you know the spectrum of every polynomial in $a$: just apply the polynomial to each point.
For matrices this is the familiar fact that $p(A)$ has eigenvalues $p(\lambda)$ for the eigenvalues $\lambda$ of $A$.

### L2 human

The theorem gives $\sigma(a^n) = \set{\lambda^n : \lambda \in \sigma(a)}$, which is the easy half of [[Gelfand's spectral radius formula|T4RFYT8HDN]].
It extends to holomorphic functions in the holomorphic functional calculus, and to continuous functions of normal elements in the [[continuous functional calculus|JB7S6WPZ77]] of C*-algebras.
