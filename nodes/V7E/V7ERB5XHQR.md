---
tag: V7ERB5XHQR
kind: definition
name: Krull topology
msc: [12F10, "20E18"]
defines: F3GTF5NT4M
uses: [0DS2F7GK05, 0XVR72M51M, 02NBKVQFRQ, 0CNQXVBHCX, 0QPHW703PV, 0MXB4CKHFW, KA0YDB6QXE]
sources:
  - url: https://en.wikipedia.org/wiki/Profinite_group
---

## Definition

Let $L/K$ be a [[Galois extension|0DS2F7GK05]], possibly of infinite degree, with [[Galois group|0XVR72M51M]] $G = \Gal(L/K)$.
Let $\mathcal{E}$ be the set of [[intermediate fields|02NBKVQFRQ]] $E$ of $L/K$ with $[E : K]$ finite.
The *Krull topology* on $G$ is the following [[topology|0CNQXVBHCX]].
A subset $U \subseteq G$ is open if and only if for each $\sigma \in U$ there is $E \in \mathcal{E}$ with $\sigma \Gal(L/E) \subseteq U$.
Equivalently, the cosets $\sigma \Gal(L/E)$, for $\sigma \in G$ and $E \in \mathcal{E}$, form a basis of the topology.

## Remarks

With this topology $G$ is a topological group that is [[compact|0QPHW703PV]], [[Hausdorff|0MXB4CKHFW]] and totally disconnected, that is, a [[profinite group|KA0YDB6QXE]].
In fact $G$ is isomorphic, as a topological group, to the inverse limit of the finite groups $\Gal(E/K)$ over the finite Galois subextensions $E/K$.
Example: if $L/K$ is finite, then $L \in \mathcal{E}$ and $\Gal(L/L) = \set{\id}$, so every subset of $G$ is open and the topology is discrete.
Non-example of an open set: for $L$ an algebraic closure of $\F_p$, the one-point set $\set{\id}$ is not open.
Indeed it would contain some $\Gal(L/\F_{p^n})$, which is infinite since $L/\F_{p^n}$ has infinite degree.
