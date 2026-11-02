---
tag: 7KHRRDRVA6
kind: definition
name: Regularity structures
msc: [60L30, 60H17, 35R60]
defines: BQ6CYHQW02
uses: [06GZ956657, 0NRYHJPQG2, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Regularity_structure
---

## Definition

A *regularity structure* is a triple $\mathscr{T} = (A, T, G)$ such that:

1. $A \subset \R$ is an index set that is bounded below, locally finite, and contains $0$.
2. $T = \bigoplus_{\alpha \in A} T_\alpha$ is a graded vector space, each $T_\alpha$ is a [[Banach space|06GZ956657]], and $T_0 \cong \R$ is spanned by an element written $\mathbf{1}$.
3. $G$ is a [[group|G5S1M9]] of continuous [[linear maps|0NRYHJPQG2]] $T \to T$ such that for all $\Gamma \in G$, $\alpha \in A$ and $\tau \in T_\alpha$,
$$\Gamma \tau - \tau \in \bigoplus_{\beta \in A, \ \beta < \alpha} T_\beta,$$
and $\Gamma \mathbf{1} = \mathbf{1}$.

The set $A$ is the set of homogeneities, $T$ is the model space, and $G$ is the structure group.

## Remarks

Example: the polynomial regularity structure on $\R^d$.
Take $A = \N$, let $T_k$ be the space of homogeneous polynomials of degree $k$ in abstract variables $X = (X_1, \ldots, X_d)$, and let $G = \set{\Gamma_h : h \in \R^d}$ with $(\Gamma_h P)(X) = P(X + h)$.
The check: $A$ contains $0$ and is locally finite, $T_0$ is spanned by the constant $\mathbf{1}$, $\Gamma_h \Gamma_{h'} = \Gamma_{h + h'}$, and $P(X + h) - P(X)$ has only terms of degree less than $\deg P$.
Non-example: adding the scaling $P(X) \mapsto P(2X)$ to $G$ breaks clause 3, since it sends $X_1$ to $2X_1$ and $2X_1 - X_1 = X_1$ has degree $1$, not less than $1$.
To use a structure one adds a model, which realises each symbol as a concrete distribution near each point.
The reconstruction theorem then turns local expansions into a global distribution.
