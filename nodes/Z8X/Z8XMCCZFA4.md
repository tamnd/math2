---
tag: Z8XMCCZFA4
kind: definition
name: Martin's axiom
msc: ["03E50", "03E57"]
defines: V8KGT8MRFE
uses: [011C29Q1S1, 0QKPNZKNEA, 0WC28W9DNM]
sources:
  - url: https://en.wikipedia.org/wiki/Martin's_axiom
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]], and read $q \le p$ as "$q$ extends $p$".
Two elements $p, q$ are compatible if some $r \in P$ has $r \le p$ and $r \le q$.

1. An antichain of $P$ is a subset whose elements are pairwise incompatible, and $P$ has the countable chain condition, ccc, if each antichain is countable.
2. A set $D \subseteq P$ is dense if for each $p \in P$ there is $q \in D$ with $q \le p$.
3. A filter on $P$ is a nonempty $G \subseteq P$ that is upward closed and in which any two elements have a common extension in $G$.

Let $\kappa$ be a [[cardinal|0QKPNZKNEA]].
The statement $\mathrm{MA}_\kappa$ concerns each ccc partial order $P$ and each family $\mathcal{D}$ of at most $\kappa$ dense subsets of $P$.
It says that some filter on $P$ meets every member of $\mathcal{D}$.
Martin's axiom, MA, is the statement that $\mathrm{MA}_\kappa$ holds for every $\kappa < 2^{\aleph_0}$, the [[cardinality of the continuum|0WC28W9DNM]].

## Remarks

Example: $\mathrm{MA}_{\aleph_0}$ is provable in ZFC.
Check: list the dense sets as $D_0, D_1, \ldots$, choose $p_0 \ge p_1 \ge \cdots$ with $p_n \in D_n$, and take the elements above some $p_n$.
So the continuum hypothesis implies MA.
Non-example: $\mathrm{MA}_{2^{\aleph_0}}$ is false.
Take the ccc order of finite partial functions from $\omega$ to $2$, ordered by reverse inclusion.
Consider the dense sets "$n$ is in the domain" and "the function differs from $x$", for all $n$ and all $x \in 2^\omega$.
A filter that meets them all would give a total function different from every $x$.
Solovay and Tennenbaum showed that MA together with $2^{\aleph_0} > \aleph_1$ is consistent, if ZFC is consistent.
MA with $2^{\aleph_0} > \aleph_1$ implies Suslin's hypothesis, and MA implies $2^\kappa = 2^{\aleph_0}$ for each infinite $\kappa < 2^{\aleph_0}$.
