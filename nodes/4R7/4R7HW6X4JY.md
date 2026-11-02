---
tag: 4R7HW6X4JY
kind: definition
name: Exponential map of a Lie group
msc: ["22E60", "22E15"]
defines: H3QX1ZFC8K
uses: [7JBRGCVJRB, E7A5DHFT01, YHA64AP1HN, SNA3DVPK0C, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_map_(Lie_theory)
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] with identity $e$ and Lie algebra $\mathfrak{g} = T_eG$, the [[tangent space|E7A5DHFT01]] at $e$.
For $X \in \mathfrak{g}$, let $\gamma_X \colon \R \to G$ be the unique [[one-parameter subgroup|YHA64AP1HN]] with $\gamma_X'(0) = X$.
The *exponential map* of $G$ is
$$\exp \colon \mathfrak{g} \to G, \qquad \exp(X) = \gamma_X(1).$$

## Remarks

Equivalently, $\gamma_X$ is the integral curve through $e$ of the [[left-invariant vector field|SNA3DVPK0C]] with value $X$ at $e$.
By rescaling, $\exp(tX) = \gamma_X(t)$ for all $t \in \R$.

Example: for $G = GL_n(\R)$, $\mathfrak{g} = M_n(\R)$ and $\gamma_A(t) = e^{tA}$ is a one-parameter subgroup with $\gamma_A'(0) = A$.
So $\exp(A) = e^A$ is the [[matrix exponential|020M04FN1H]].

Non-example: in $G = SL_2(\R)$, the matrix $\begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix}$ is not of the form $\exp(X)$ for any $X$ in the Lie algebra $\mathfrak{sl}_2(\R)$.
So $\exp$ need not be surjective, even for a connected group.

The map $\exp$ is smooth and its differential at $0$ is the identity of $\mathfrak{g}$.
By the inverse function theorem, it restricts to a diffeomorphism from a neighbourhood of $0$ in $\mathfrak{g}$ onto a neighbourhood of $e$ in $G$.
For a compact connected Lie group, $\exp$ is surjective.
