---
tag: ETJ4WRXC41
kind: definition
name: Brauer character
msc: [20C20]
defines: R2N3GBDBVQ
uses: [G5S1M9, WYGRXCG2RN, 0PF6TM8TWT, 0YV2CKP2AV, 0WE2NHZJ7B, 0BQAA2BK3Q, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_representation_theory
---

## Definition

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime, and let $k$ be an [[algebraically closed field|0PF6TM8TWT]] of characteristic $p$.
An element $g \in G$ is $p$-regular if its [[order|0WE2NHZJ7B]] is not divisible by $p$; let $G_{p'}$ be the set of $p$-regular elements.
Let $\mu_{p'}(k)$ and $\mu_{p'}(\C)$ be the groups of [[roots of unity|0YV2CKP2AV]] of order prime to $p$ in $k$ and in the [[complex numbers|09FTAET5Z4]].
Fix a group isomorphism $\phi \colon \mu_{p'}(k) \to \mu_{p'}(\C)$.
Let $\rho \colon G \to GL(V)$ be a [[representation|WYGRXCG2RN]] of $G$ on a vector space $V$ over $k$ of finite dimension $d$.
For $g \in G_{p'}$, the map $\rho(g)$ has [[eigenvalues|0BQAA2BK3Q]] $\lambda_1, \ldots, \lambda_d \in \mu_{p'}(k)$, listed with multiplicity.
The *Brauer character* of $\rho$ is the function $\beta_\rho \colon G_{p'} \to \C$ given by
$$\beta_\rho(g) = \phi(\lambda_1) + \cdots + \phi(\lambda_d).$$

## Remarks

The eigenvalues lie in $\mu_{p'}(k)$ because $\rho(g)^m = \id$ with $m$ the order of $g$, prime to $p$.
Such an isomorphism $\phi$ exists; it is usually fixed through a $p$-modular system, and other choices change $\beta_\rho$ by a Galois automorphism.
Example: for the trivial representation of degree $d$, all eigenvalues are $1$, so $\beta(g) = d$ for every $g \in G_{p'}$; for $d = p$ this is $p$, while the trace in $k$ is $0$.
Non-example: let $G = \Z/p$ and let $V = k^2$, with the generator acting by $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
The generator is not $p$-regular, so the Brauer character has no value there.
It is defined only at the identity, with value $2$.
Brauer characters are constant on conjugacy classes, additive on short exact sequences, and $\beta_\rho(1) = \dim V$.
The irreducible Brauer characters are linearly independent, and their number is the number of conjugacy classes of $p$-regular elements.
