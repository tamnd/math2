---
tag: KWS2STNJAA
kind: definition
name: Clifford module
msc: [15A66, 53C27]
defines: 31Q0RDPZ00
uses: [A38B1QFK20, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Clifford_module
---

## Definition

Let $V$ be a finite-dimensional real vector space with a [[quadratic form|0RBQS1JJCR]] $q$.
Let $\mathrm{Cl}(V, q)$ be the [[Clifford algebra|A38B1QFK20]] of $(V, q)$, with the convention that $v \cdot v = -q(v) \cdot 1$ for $v \in V$.
Let $\mathbb{K}$ be $\R$ or $\C$.
A *Clifford module* over $\mathrm{Cl}(V, q)$ is a $\mathbb{K}$-vector space $W$ together with a homomorphism of real algebras $\rho \colon \mathrm{Cl}(V, q) \to \End_{\mathbb{K}}(W)$ that sends $1$ to $\id_W$.

## Remarks

By the universal property of the Clifford algebra, giving $\rho$ is the same as giving a linear map $c \colon V \to \End_{\mathbb{K}}(W)$ with
$$c(v)^2 = -q(v) \, \id_W \quad \text{for all } v \in V.$$
Authors who use the convention $v \cdot v = q(v) \cdot 1$ get the same theory with $q$ replaced by $-q$.
A Clifford module is irreducible if it has no proper nonzero invariant subspace; when $q$ is nondegenerate, every finite-dimensional Clifford module is a direct sum of irreducible ones.

Example: let $V = \R$ with $q(x) = x^2$, let $W = \C$ as a real vector space and let $c(x)$ be multiplication by $ix$.
Then $c(x)^2 = (ix)^2 = -x^2 = -q(x)$, so $W$ is a Clifford module, and in fact $\mathrm{Cl}(V, q) \cong \C$.

Non-example: with the same $V$ and $q$, let $W = \R$ and $c(x) = x \, \id_W$.
Then $c(1)^2 = 1 \ne -1$, so this is not a Clifford module.
In fact no real vector space of dimension $1$ is a Clifford module here, since no real number squares to $-1$.

## Explanations

### L1 human

A Clifford module is a vector space on which each vector $v$ acts by a linear map whose square is the scalar $-q(v)$.
