---
tag: BH7C1Y1F0E
kind: definition
name: Symmetric spectrum
msc: [55P42, 55P43, 55U35]
defines: 1RY6DQJ1RV
uses: [1GHF4EKBXS, 0RJMNEN3BJ, T9DG8DDE75, 26GTNMAF7B]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_spectrum
---

## Definition

Let $S^1 = \Delta[1] / \partial \Delta[1]$ be the simplicial circle and $S^p = S^1 \wedge \cdots \wedge S^1$ ($p$ factors), with the [[symmetric group|0RJMNEN3BJ]] $\Sigma_p$ acting by permuting the factors.
A *symmetric spectrum* $X$ consists of:

1. for each $n \ge 0$, a pointed [[simplicial set|WW81ARB8K9]] $X_n$ with a base-point-preserving left action of $\Sigma_n$;
2. for each $n \ge 0$, a pointed map $\sigma_n \colon S^1 \wedge X_n \to X_{n+1}$;
3. such that for all $n, p \ge 0$ the iterated structure map $S^p \wedge X_n \to X_{n+p}$ is $\Sigma_p \times \Sigma_n$-equivariant, where $\Sigma_p \times \Sigma_n$ acts on $X_{n+p}$ through the inclusion $\Sigma_p \times \Sigma_n \subseteq \Sigma_{p+n}$.

A map $f \colon X \to Y$ of symmetric spectra is a sequence of $\Sigma_n$-equivariant pointed maps $f_n \colon X_n \to Y_n$ that commute with the structure maps.

## Remarks

Forgetting the actions gives a sequential [[spectrum|1GHF4EKBXS]], after geometric realization.
The same definition with [[pointed|T9DG8DDE75]] topological spaces in place of simplicial sets gives symmetric spectra of spaces.

Example: the *symmetric sphere spectrum* $\mathbb{S}$ has $\mathbb{S}_n = S^n$ with the permutation action of $\Sigma_n$.
Its structure maps are the identifications $S^1 \wedge S^n = S^{n+1}$.
The equivariance in clause 3 holds because both actions permute the same circle factors.

Non-example: on the sequence $X_n = S^n$ with the same structure maps, let every $\Sigma_n$ act as the identity.
Clauses 1 and 2 hold, but clause 3 fails for $p = 2$ and $n = 0$.
The map $S^2 \wedge S^0 \to X_2$ is the identity of $S^2$.
It does not carry the swap of the two circle factors, which is not the identity of $S^2$, to the identity action on $X_2$.

Symmetric spectra form a closed symmetric monoidal category under a smash product with unit $\mathbb{S}$.
They carry a stable model structure whose homotopy category is equivalent to the [[stable homotopy category|26GTNMAF7B]]; this is the theorem of Hovey, Shipley and Smith.
Monoids and commutative monoids in symmetric spectra model $A_\infty$ and $E_\infty$ ring spectra.
