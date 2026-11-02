---
tag: B33WNK1SVN
kind: definition
name: Harish-Chandra module
msc: ["22E47", "22E46"]
defines: 2MKHH636C3
uses: [42ZCE14AD2, T2EB8R9HEV, SCZ8PRVY00, P6ZP0TE07M, FX3NEFYFFN]
sources:
  - url: https://en.wikipedia.org/wiki/(g,K)-module
---

## Definition

Let $G$ be a [[real reductive Lie group|42ZCE14AD2]] with Lie algebra $\mathfrak g_0$, and let $\mathfrak g = \mathfrak g_0 \otimes_\R \C$ be its complexified Lie algebra.
Let $K$ be a [[maximal compact subgroup|T2EB8R9HEV]] of $G$, with Lie algebra $\mathfrak k_0 \subseteq \mathfrak g_0$, acting on $\mathfrak g$ by the [[adjoint representation|P6ZP0TE07M]] $\mathrm{Ad}$.
A $(\mathfrak g, K)$-module is a complex vector space $V$ with a representation of $\mathfrak g$, written $X \cdot v$, and a representation $\pi$ of $K$, such that:

1. each $v \in V$ lies in a finite-dimensional $\pi(K)$-invariant subspace on which $K$ acts continuously;
2. $\frac{d}{dt}\big|_{t=0} \pi(\exp tX) v = X \cdot v$ for all $X \in \mathfrak k_0$ and $v \in V$;
3. $\pi(k)(X \cdot v) = (\mathrm{Ad}(k) X) \cdot (\pi(k) v)$ for all $k \in K$, $X \in \mathfrak g$ and $v \in V$.

A *Harish-Chandra module* is a $(\mathfrak g, K)$-module $V$ such that:

4. $V$ is finitely generated as a module over the [[universal enveloping algebra|SCZ8PRVY00]] $U(\mathfrak g)$;
5. each [[irreducible representation|FX3NEFYFFN]] of $K$ occurs in $V$ with finite multiplicity.

## Remarks

The derivative in clause 2 makes sense by clause 1, since it is taken inside a finite-dimensional space.

Example: let $\pi$ be a finite-dimensional continuous representation of $G$ on $V$, with differential $d\pi$ extended complex-linearly to $\mathfrak g$.
Then $V$ with $X \cdot v = d\pi(X) v$ and $\pi|_K$ is a Harish-Chandra module.
Clause 1 holds because $V$ itself is finite-dimensional, clauses 2 and 3 hold by the definition of $d\pi$ and by $\pi(k) \pi(\exp tX) \pi(k)^{-1} = \pi(\exp t \mathrm{Ad}(k) X)$, and clauses 4 and 5 hold because $\dim V < \infty$.

Non-example: an infinite direct sum of copies of the trivial one-dimensional module, with $\mathfrak g$ acting by $0$ and each $k \in K$ acting as the identity, is a $(\mathfrak g, K)$-module.
It is not a Harish-Chandra module, because the trivial representation of $K$ occurs infinitely often and clause 5 fails.

If $\pi$ is an [[admissible representation|SZV8Y806Y7]] of $G$ on a Hilbert space $H$, its $K$-finite vectors are smooth and form a Harish-Chandra module when $\pi$ has finite length.
Two such representations are called infinitesimally equivalent when their Harish-Chandra modules are isomorphic.
