---
tag: Z2AJFZQTWT
kind: definition
name: Maximal torus
msc: ["22E15", 22C05]
defines: 3JVGZVVTB0
uses: [9TFC6ADC1C, XNAWD33HN1]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_torus
---

## Definition

Let $G$ be a [[compact Lie group|9TFC6ADC1C]].
A *torus* in $G$ is a compact connected abelian Lie subgroup of $G$.
Each such subgroup is isomorphic to the [[torus group|XNAWD33HN1]] $\mathbb{T}^k$ for some $k \ge 0$.
A *maximal torus* of $G$ is a torus $T \subseteq G$ such that every torus $T'$ with $T \subseteq T' \subseteq G$ satisfies $T' = T$.

## Remarks

Example: in $G = U(n)$, the subgroup $T$ of diagonal matrices $\operatorname{diag}(z_1, \dots, z_n)$ with $\abs{z_j} = 1$ is a maximal torus.
It is a torus, isomorphic to $\mathbb{T}^n$.
Let $T' \supseteq T$ be a torus.
Each element of $T'$ commutes with a diagonal matrix with distinct entries, so it is diagonal; thus $T' = T$.
Non-example: in $U(2)$, the subgroup $\set{\operatorname{diag}(z, 1) : \abs{z} = 1}$ is a torus, but it is not maximal, since it lies in the diagonal torus $\mathbb{T}^2$.
The dimension of a maximal torus is the rank of $G$; for $U(n)$ it is $n$, and for $SU(n)$ it is $n - 1$.
Every torus of $G$ lies in some maximal torus, by a dimension argument.
