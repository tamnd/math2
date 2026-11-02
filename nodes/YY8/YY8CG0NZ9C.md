---
tag: YY8CG0NZ9C
kind: definition
name: Gelfand–Kirillov dimension
msc: [16P90]
defines: MDVSY2NMD2
uses: [3CTW1P4HBP, 04C5ZBG1WT, 000AYPA9AJ, EHY4PYSMGZ, 0T3RZQXDYD, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand–Kirillov_dimension
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $k$ with identity.
For a finite-dimensional [[subspace|000AYPA9AJ]] $V \subseteq A$ and $n \ge 1$, let $V^n$ be the span of all products of $n$ elements of $V$.
The *Gelfand–Kirillov dimension* of $A$ is
$$\operatorname{GKdim} A = \sup_{V} \, \limsup_{n \to \infty} \frac{\log \dim_k \big( k + V + V^2 + \cdots + V^n \big)}{\log n},$$
where the supremum runs over all finite-dimensional subspaces $V$ of $A$ and $\limsup$ is the [[limit superior|0T3RZQXDYD]].
It is a number in $[0, \infty]$.

## Remarks

If $A$ is finitely generated and $V$ is a finite-dimensional generating subspace with $1 \in V$, then the supremum is attained at $V$: $\operatorname{GKdim} A = \limsup_n \log d_V(n) / \log n$, where $d_V$ is the [[growth function|EHY4PYSMGZ]] of $A$.
So $\operatorname{GKdim} A$ depends only on the growth of $A$.

Example: let $A = k[x_1, \ldots, x_m]$ be a [[polynomial ring|0SDC934R52]] and $V = k + k x_1 + \cdots + k x_m$.
The space $V^n$ is spanned by the monomials of degree at most $n$, so $\dim V^n = \binom{n + m}{m}$, which is a polynomial of degree $m$ in $n$.
Hence $\operatorname{GKdim} A = m$.

Example: if $A$ is finite-dimensional, then $\dim V^n \le \dim A$ for all $n$, so $\operatorname{GKdim} A = 0$.

Non-example of finiteness: for the free algebra $A = k\langle x, y \rangle$ and $V = k + kx + ky$, one has $\dim V^n = 2^{n+1} - 1$.
Then $\log \dim V^n / \log n \to \infty$, so $\operatorname{GKdim} A = \infty$.

The base of the logarithm does not matter, because only the ratio of two logarithms appears.
