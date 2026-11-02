---
tag: M53B55WESR
kind: definition
name: Inverse limit of algebras
msc: [08B25, 18A30]
defines: DE2KEQ85ZT
uses: [KBXSZC6BV1, WJ73XYBNE4]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_limit
---

## Definition

Let $(I, \le)$ be a directed partially ordered set and fix a signature.
An *inverse system* of algebras over $I$ consists of:

1. an algebra $A_i$ for each $i \in I$;
2. a [[homomorphism|KBXSZC6BV1]] $\varphi_{ij} \colon A_j \to A_i$ for each pair $i \le j$;
3. the conditions $\varphi_{ii} = \id_{A_i}$ and $\varphi_{ij} \circ \varphi_{jk} = \varphi_{ik}$ for all $i \le j \le k$.

The *inverse limit* $\varprojlim A_i$ of the system is the set of all $(a_i)_{i \in I}$ in the [[direct product|WJ73XYBNE4]] $\prod_{i \in I} A_i$ such that $\varphi_{ij}(a_j) = a_i$ for all $i \le j$.

## Remarks

The inverse limit is closed under the operations of the product, so it is a [[subalgebra|7CHG6SD365]] of $\prod_i A_i$; it can be empty when the signature has no constant symbols.
The projections $\pi_i \colon \varprojlim A_j \to A_i$ satisfy $\varphi_{ij} \circ \pi_j = \pi_i$.
For every algebra $B$ with homomorphisms $\psi_i \colon B \to A_i$ satisfying $\varphi_{ij} \circ \psi_j = \psi_i$, there is a unique homomorphism $\psi \colon B \to \varprojlim A_i$ with $\pi_i \circ \psi = \psi_i$, namely $\psi(b) = (\psi_i(b))_i$.

Example: let $p$ be a prime, let $I = \N$, let $A_n = \Z/p^n\Z$ as rings, and let $\varphi_{mn}$ be reduction modulo $p^m$ for $m \le n$.
Reduction modulo $p^n$ followed by reduction modulo $p^m$ is reduction modulo $p^m$, so clause 3 holds.
The inverse limit is the ring $\Z_p$ of $p$-adic integers.

Non-example: on $I = \set{1, 2, 3}$ with the usual order, take $A_i = \Z/2\Z$ as groups, $\varphi_{ii} = \varphi_{12} = \varphi_{23} = \id$ and $\varphi_{13} = 0$.
Then $\varphi_{12} \circ \varphi_{23} = \id \ne \varphi_{13}$, so clause 3 fails and the data is not an inverse system.

Some authors allow any partially ordered set, or any small category, as the index; the construction is the same.
