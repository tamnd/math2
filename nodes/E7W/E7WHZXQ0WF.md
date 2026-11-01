---
tag: E7WHZXQ0WF
kind: definition
name: Ramification
msc: [11S15, 11R04]
defines: H5RC67SD24
uses: [MWBDFS2KJ5, 7NPY2CN5KB, 00MHHZ9SNE, B7KNZCBFYT, E0VZTNPJXA]
sources:
  - url: https://en.wikipedia.org/wiki/Ramification_(mathematics)
---

## Definition

Let $L/K$ be a finite extension of [[algebraic number fields|MWBDFS2KJ5]], with rings of integers $\mathcal{O}_K \subseteq \mathcal{O}_L$.
Let $\mathfrak{p}$ be a nonzero [[prime ideal|00MHHZ9SNE]] of $\mathcal{O}_K$, and let $\mathfrak{P}$ be a prime ideal of $\mathcal{O}_L$ with $\mathfrak{P} \cap \mathcal{O}_K = \mathfrak{p}$.
The *ramification index* $e(\mathfrak{P} \mid \mathfrak{p})$ is the exponent of $\mathfrak{P}$ in the factorisation of $\mathfrak{p}\mathcal{O}_L$ into prime ideals of the [[Dedekind domain|7NPY2CN5KB]] $\mathcal{O}_L$.
The prime $\mathfrak{P}$ is *ramified* over $\mathfrak{p}$ if $e(\mathfrak{P} \mid \mathfrak{p}) > 1$.
The prime $\mathfrak{p}$ is *ramified in $L$* if some prime of $\mathcal{O}_L$ over $\mathfrak{p}$ is ramified, and *unramified in $L$* otherwise.

## Remarks

For number fields the residue field extensions are finite extensions of finite fields, hence separable, so no separability condition is needed.
A prime number $p$ ramifies in a number field $L$ if and only if $p$ divides the [[discriminant|E0VZTNPJXA]] $d_L$; in particular only finitely many primes ramify.
See [[splitting of prime ideals|B7KNZCBFYT]] for the full description of the factorisation.

Example: in $L = \Q(\sqrt{-5})$, the ideal $2\mathcal{O}_L$ equals $\mathfrak{P}^2$ with $\mathfrak{P} = (2, 1 + \sqrt{-5})$.
So $e(\mathfrak{P} \mid 2) = 2$ and $2$ is ramified, in line with $2 \mid d_L = -20$.

Non-example: $3$ is unramified in $\Q(\sqrt{-5})$.
Indeed $x^2 + 5 \equiv (x - 1)(x + 1) \pmod 3$ has distinct roots, so $3\mathcal{O}_L = (3, \sqrt{-5} - 1)(3, \sqrt{-5} + 1)$ with two distinct primes, each of exponent $1$; and $3 \nmid 20$.
