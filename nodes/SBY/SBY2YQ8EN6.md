---
tag: SBY2YQ8EN6
kind: statement
role: theorem
name: Danos-Regnier correctness criterion
msc: ["03F52", "05C05"]
topics: [98QF5J4W16]
audience: research
uses: [6G6M2V85RZ, H408H4WHBA]
about: [HN6WN1VE39]
proofs: [N8MC3HNB51]
sources:
  - doi: 10.1007/BF01622878
    locator: pages 181-203
    note: Danos and Regnier, The structure of multiplicatives, Archive for Mathematical Logic 28 (1989)
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.3 Proof nets
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Statement

Let $S$ be a [[proof structure|6G6M2V85RZ]] of MLL without units, possibly with cut links.
Then $S$ is a proof net if and only if every correction graph of $S$ is a tree, that is, acyclic and connected.

The direction "proof net implies trees" is *soundness*, and the converse is *sequentialization*.

## Remarks

### Why each hypothesis is needed

The units are left out.
The rule for $\bot$ adds a conclusion with no link to the rest of the net, so a net with $\bot$ can have a disconnected correction graph.
Without units, each rule of MLL joins its premises into one connected piece, and this is what the criterion tests.

### Consequences

1. In a proof net, the number of axiom links is one more than the number of $\otimes$ links and cut links together.
   The [[proof|N8MC3HNB51]] derives this from the count of edges of a tree.
2. A proof structure can be tested by the criterion without a search for a derivation.
   The test of all $2^k$ switchings takes exponential time in the number $k$ of $\mathbin{\wp}$ links.
3. The SEP entry on linear logic reports that other criteria, based on graph contraction, run in linear time.

### Converse

Both directions hold, so the criterion characterizes proof nets.

## History

The SEP entry on linear logic names the acyclic connected criterion of Danos and Regnier from 1989, the paper cited in this node.
It states that Girard's earlier long-trip criterion appears in his 1987 paper.

## Explanations

### L1 human

A proof net is a picture of a proof.
To test whether a picture comes from a real proof, cut one of the two lines above each "par" in every possible way.
The picture is a proof net exactly when each cut picture is a tree: connected and without loops.

### L2 human

We test the structure with conclusion $p \otimes p^{\perp}$ and with conclusion $p \mathbin{\wp} p^{\perp}$.

1. Both have one axiom link between $p$ and $p^{\perp}$, and a link with premises $p$ and $p^{\perp}$ and conclusion $C$.
2. For $\otimes$, the only correction graph has the edges $p - p^{\perp}$, $C - p$ and $C - p^{\perp}$, which form a cycle.
3. So the $\otimes$ structure is not a proof net, and indeed $\vdash p \otimes p^{\perp}$ is not derivable.
4. For $\mathbin{\wp}$, each correction graph keeps one of the edges $C - p$ and $C - p^{\perp}$, and it is a path.
5. So the $\mathbin{\wp}$ structure is a proof net, and it is the translation of the axiom followed by $\mathbin{\wp}$.

The typical use of the criterion is to check a net built by hand or by a program.
A trap: the criterion asks for every switching, so one good switching is not enough.
