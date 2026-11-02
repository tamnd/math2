---
tag: TM0AXHX3SG
kind: definition
name: Domain decomposition methods
msc: [65N55, 65F10, 65Y05]
defines: AN054RHT1K
uses: [TM8VQJWGHZ, 0GT4WWGWH2, 0KX66CZMBB, 2RPE77ACER, KE98SW3SBD, 6HWFBXYPZP, 98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Domain_decomposition_methods
---

## Definition

Let $A x = b$ be a [[linear system|0GT4WWGWH2]] with an invertible real $n \times n$ matrix $A$, arising from a discretized [[boundary value problem|TM8VQJWGHZ]] on a domain $\Omega$.
Let $\Omega_1, \dots, \Omega_N$ be subdomains with $\Omega = \Omega_1 \cup \cdots \cup \Omega_N$, and let $I_i \subseteq \set{1, \dots, n}$ be the set of unknowns that belong to $\Omega_i$.
Let $R_i$ be the $\abs{I_i} \times n$ matrix that selects the entries in $I_i$, and let $A_i = R_i A R_i^T$ be the local matrix.
A *domain decomposition method* is an [[iterative method|2RPE77ACER]] or [[preconditioner|KE98SW3SBD]] for $A x = b$ in which:

1. each step solves local systems with the matrices $A_i$, or with local matrices built from them;
2. the local solutions are combined through the unknowns shared by, or lying on the interfaces between, the subdomains;
3. optionally, a coarse problem of small size couples all subdomains globally.

The method is *overlapping* if the sets $I_i$ overlap, and *nonoverlapping* if the subdomains meet only along interfaces.

## Remarks

Example: the additive Schwarz preconditioner is $M^{-1} = \sum_{i=1}^{N} R_i^T A_i^{-1} R_i$, for overlapping $I_i$ that cover all unknowns.
Each term solves a local problem, and the terms can be computed in parallel, so clauses 1 and 2 hold.
If $A$ is symmetric [[positive definite|0KX66CZMBB]], each $A_i$ is too, and $M^{-1}$ is symmetric positive definite.
Non-example: the [[finite element method|98GZ9DVHTA]] with a direct solver for the whole of $A$ solves no local systems, so it fails clause 1.
Nonoverlapping methods eliminate the interior unknowns of each subdomain and iterate on the [[Schur complement|6HWFBXYPZP]] for the interface unknowns.
Without a coarse problem, the number of iterations grows with the number of subdomains, because information travels only between neighbours at each step.
