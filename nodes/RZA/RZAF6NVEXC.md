---
tag: RZAF6NVEXC
kind: concept
name: Small index property
aliases: [small-index-property, sip-automorphism-group]
msc: ["03C15", "20B27", "03C50"]
topics: [ZS8X8KS54R]
audience: research
uses: [DSQ17TNW1C, ZDJQRKPWGA, 9C1WSBNQX9, FVGB8ZP67B, 4K9RYSNPG3, 04QEBF8S49, 01TQB88H4C, 92700QAB5Y, A22K1X8GKD]
sources:
  - book: isbn:9780521587136
---

## Summary

Let $M$ be a [[countable|01TQB88H4C]] structure and $G = \operatorname{Aut}(M)$, with the [[topology of pointwise convergence|FVGB8ZP67B]].
$M$ has the *small index property* (SIP) when every subgroup of $G$ of [[index|04QEBF8S49]] less than $2^{\aleph_0}$ is [[open|4K9RYSNPG3]].
Open subgroups always have countable index, so under SIP the open subgroups are exactly the subgroups of small index.
This means that the topology of $G$ can be recovered from its abstract group structure.
$(\Q, <)$, the Rado graph and the countable set with no structure have SIP.

## Motivation

The automorphism group of a countable structure is a [[Polish group|9C1WSBNQX9]], and for an [[$\aleph_0$-categorical|A22K1X8GKD]] structure its topology carries much of the model theory.
One would like to recover $M$ from $G$ as an abstract group, without being told the topology.
SIP is the condition that makes the topology definable from the group.
Then any abstract isomorphism between two such groups is a homeomorphism, and topological reconstruction results apply.

## Notation

The group $G$ is a closed [[permutation group|ZDJQRKPWGA]] on $M$.
For a finite tuple $\bar a$ of $M$, the pointwise stabilizer $G_{\bar a}$ is an open subgroup, and these subgroups form a base of neighborhoods of the identity.
A subgroup is open exactly when it contains some $G_{\bar a}$.

## Remarks

### Examples

- Every finite structure has SIP, since its automorphism group is discrete; see [[this example|ETBNEFNS1E]].
- $(\Z, <)$ has SIP, since its automorphism group is discrete; see [[this example|RSK4ZNRPXN]].
- The full symmetric group $\operatorname{Sym}(\N)$, the automorphism group of a countable set with no structure, has SIP.
- $(\Q, <)$ and the [[Rado graph|RMXR0FEF54]] have SIP.

### Non-examples

- A countable union of labeled pairs has automorphism group $(\Z/2\Z)^{\N}$, which has a non-open subgroup of index $2$; see [[this non-example|232JGD09RV]].

### Basic properties

- If $H$ is open, it contains some $G_{\bar a}$, and the index of $H$ is at most the size of the orbit of $\bar a$, which is countable.
- With SIP, a subgroup of index less than $2^{\aleph_0}$ has countable index.
- If $M$ and $N$ have SIP, every abstract group isomorphism $\operatorname{Aut}(M) \to \operatorname{Aut}(N)$ is a homeomorphism.
- For $\aleph_0$-categorical $M$ and $N$, the groups are isomorphic as [[topological groups|92700QAB5Y]] exactly when $M$ and $N$ are bi-interpretable; with SIP, abstract isomorphism suffices.

### History

Dixon, Neumann and Thomas proved SIP for $\operatorname{Sym}(\N)$ in 1986.
Truss proved it for $(\Q, <)$.
Hodges, Hodkinson, Lascar and Shelah proved it in 1993 for the Rado graph and for $\omega$-stable $\aleph_0$-categorical structures.
The topological reconstruction for $\aleph_0$-categorical structures is due to Ahlbrandt and Ziegler.

### Common errors

- To read "small" as "finite". The bound is $2^{\aleph_0}$, so SIP is a statement about all subgroups of countable index.
- To expect SIP for every countable structure. Products of small groups give non-open subgroups of index $2$, using the axiom of choice.

## Explanations

### L1 human

The automorphism group of a countable structure has a natural topology: two symmetries are close when they agree on many points.
The small index property says that the large subgroups, those of small index, are exactly the ones that fix some finite set of points.
So the group alone already knows its topology.

### L2 human

We see why an open subgroup of $\operatorname{Sym}(\N)$ has countable index.

1. Let $H \supseteq G_{\bar a}$ with $\bar a = (a_1, \dots, a_k)$.
2. Two permutations $g, h$ with $g(\bar a) = h(\bar a)$ satisfy $h^{-1} g \in G_{\bar a} \subseteq H$, so $gH = hH$.
3. So the cosets of $H$ are indexed by some of the countably many $k$-tuples of $\N$.

The typical use of SIP is to show that an abstract group isomorphism is continuous.
A trap is to apply SIP to subgroups of index exactly $2^{\aleph_0}$; those need not be open.

### L3 human

SIP is one of several automatic continuity properties of Polish groups, together with automatic continuity of homomorphisms into separable groups.
Proofs often go through generic automorphisms and the [[extension property for partial automorphisms|TA9KGWV9NM]] of the age.
For $\aleph_0$-categorical structures, SIP turns the reconstruction of a structure from its topological automorphism group into reconstruction from the abstract group.
