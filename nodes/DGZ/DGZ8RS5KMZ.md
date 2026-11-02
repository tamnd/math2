---
tag: DGZ8RS5KMZ
kind: definition
name: Lawvere theory
msc: ["18C10", "08C05"]
defines: NTJ94H2CNS
uses: [A2DE66937D, 28NQ0KRHD3, S5744QZV4N, DAMK8XE1FR]
sources:
  - url: https://en.wikipedia.org/wiki/Lawvere_theory
---

## Definition

Let $\aleph_0$ be the [[category|A2DE66937D]] whose objects are the natural numbers $n \ge 0$.
Each $n$ is viewed as the set $\set{1, \ldots, n}$, and the morphisms are all functions between these sets.
A *Lawvere theory* is a small category $\mathcal{T}$ with finite [[products|S5744QZV4N]], together with a [[functor|28NQ0KRHD3]] $I \colon \aleph_0^{\mathrm{op}} \to \mathcal{T}$ that is bijective on objects and preserves finite products.
A *model* of $\mathcal{T}$ is a functor $\mathcal{T} \to \mathbf{Set}$ that preserves finite products.

## Remarks

In $\aleph_0^{\mathrm{op}}$, the object $n$ is the product of $n$ copies of $1$, with projections given by the inclusions $\set{1} \to \set{1, \ldots, n}$.
So in $\mathcal{T}$ every object is a power $1^n$ of the object $1$.
A model $M$ is determined by the set $M(1)$ and the maps $M(1)^n \to M(1)$ given by the morphisms $n \to 1$.

Example: for a [[variety|AJNZJD8442]] $\mathcal{V}$ with free algebras $F(n)$ on $n$ generators, let $\mathcal{T}_{\mathcal{V}}(n, m)$ be the set of homomorphisms $F(m) \to F(n)$, composed in the opposite order.
This is a Lawvere theory.
Here $\mathcal{T}_{\mathcal{V}}(n, 1) \cong F(n)$ is the set of $n$-ary terms modulo the identities of $\mathcal{V}$.
The object $n$ is the product of $n$ copies of $1$ because $F(n)$ is the coproduct of $n$ copies of $F(1)$ in $\mathcal{V}$.
Its category of models is equivalent to $\mathcal{V}$.

Non-example: the category $\aleph_0$ itself, not its opposite, has finite products, given by cartesian products, so the product of $n$ and $m$ is $n m$.
It is not a Lawvere theory, since in a Lawvere theory every object is a power of one object $x$.
Here $2$ and $3$ are not both powers of the same natural number.
