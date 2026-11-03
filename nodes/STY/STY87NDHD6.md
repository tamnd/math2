---
tag: STY87NDHD6
kind: definition
name: Parastatistics
msc: [81S05, 81V72]
defines: DCZF6J0GC6
uses: [HM2HHE3J51, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Parastatistics
---

## Definition

Let $\mathcal H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $K$ be an index set of single-particle states.
Let $a_k$, $k \in K$, be operators on $\mathcal H$ with adjoints $a_k^\dagger$.
Write $[A, B] = AB - BA$, $\set{A, B} = AB + BA$, and $\delta_{kl}$ for the Kronecker delta.

1. The $a_k$ satisfy *parabose* relations if $[a_k, \set{a_l^\dagger, a_m}] = 2 \delta_{kl} a_m$ and $[a_k, \set{a_l, a_m}] = 0$ for all $k, l, m \in K$.
2. The $a_k$ satisfy *parafermi* relations if $[a_k, [a_l^\dagger, a_m]] = 2 \delta_{kl} a_m$ and $[a_k, [a_l, a_m]] = 0$ for all $k, l, m \in K$.
3. A representation has *order* $p$, a positive integer, if there is a unit vector $\lvert 0 \rangle$ with $a_k \lvert 0 \rangle = 0$ and $a_k a_l^\dagger \lvert 0 \rangle = p \, \delta_{kl} \lvert 0 \rangle$ for all $k, l$.
   Moreover $\mathcal H$ must be spanned by the vectors obtained from $\lvert 0 \rangle$ by applying the $a_l^\dagger$.

*Parastatistics* of order $p$ is the statistics of particles whose creation and annihilation operators form such a representation of the parabose or parafermi relations.

## Remarks

Example: ordinary bosons, with $[a_k, a_l^\dagger] = \delta_{kl}$ and $[a_k, a_l] = 0$, satisfy the parabose relations with $p = 1$.
Check: $\set{a_l^\dagger, a_m} = 2 a_l^\dagger a_m + \delta_{lm}$, and $[a_k, 2 a_l^\dagger a_m] = 2 [a_k, a_l^\dagger] a_m = 2 \delta_{kl} a_m$; also $a_k a_l^\dagger \lvert 0 \rangle = \delta_{kl} \lvert 0 \rangle$.
Likewise ordinary fermions, with $\set{a_k, a_l^\dagger} = \delta_{kl}$ and $\set{a_k, a_l} = 0$, satisfy the parafermi relations with $p = 1$.

Non-example: fermion operators do not satisfy the parabose relations.
For a single mode, $\set{a^\dagger, a} = 1$, so $[a, \set{a^\dagger, a}] = 0 \ne 2a$.

The $n$-particle states carry representations of the [[symmetric group|0515A6D2Y1]] $S_n$.
For parafermions of order $p$ these are the irreducible representations whose Young diagrams have at most $p$ columns.
For parabosons of order $p$ they are those whose Young diagrams have at most $p$ rows.
