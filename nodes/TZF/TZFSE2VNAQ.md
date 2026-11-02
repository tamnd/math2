---
tag: TZFSE2VNAQ
kind: definition
name: Simplicial object
msc: [18N50, 55U10]
defines: WK0A32TZHB
uses: [A2DE66937D, 28NQ0KRHD3, FRFYHJGAN3, DAMK8XE1FR, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]], and let $\Delta$ be the [[simplex category|FRFYHJGAN3]] with [[opposite category|DAMK8XE1FR]] $\Delta^{\mathrm{op}}$.
A *simplicial object* in $\mathcal{C}$ is a [[functor|28NQ0KRHD3]] $X \colon \Delta^{\mathrm{op}} \to \mathcal{C}$.
One writes $X_n$ for $X([n])$.
A morphism of simplicial objects $X \to Y$ is a [[natural transformation|KYCPCC57FT]] from $X$ to $Y$.

## Remarks

Equivalently, a simplicial object is a family of objects $X_n$, $n \ge 0$, with face maps $d_i \colon X_n \to X_{n-1}$ and degeneracy maps $s_i \colon X_n \to X_{n+1}$ for $0 \le i \le n$, subject to the simplicial identities:
$$d_i d_j = d_{j-1} d_i \ (i < j), \qquad s_i s_j = s_{j+1} s_i \ (i \le j),$$
$$d_i s_j = s_{j-1} d_i \ (i < j), \qquad d_j s_j = d_{j+1} s_j = \id, \qquad d_i s_j = s_j d_{i-1} \ (i > j+1).$$
Here $d_i = X(\delta_i)$ and $s_i = X(\sigma_i)$ for the face and degeneracy maps $\delta_i$, $\sigma_i$ of $\Delta$.
Example: for an object $A$, the constant functor with $X_n = A$ and every $d_i$, $s_i$ equal to $\id_A$ satisfies all identities, so it is a simplicial object.
Non-example: a covariant functor $\Delta \to \mathcal{C}$ is not a simplicial object, because its maps go from $X_{n-1}$ to $X_n$ for faces; such functors are called cosimplicial objects.
Simplicial objects in $\mathbf{Set}$ are [[simplicial sets|WW81ARB8K9]].
