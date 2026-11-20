---
tag: HN6WN1VE39
kind: concept
name: Proof net
msc: ["03F52", "03F07"]
topics: [98QF5J4W16]
audience: research
uses: [2P2184B6HE, H408H4WHBA]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_net
    locator: Correctness criteria
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.3 Proof nets
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1007/BF01622878
    locator: pages 181-203
    note: Danos and Regnier, The structure of multiplicatives, Archive for Mathematical Logic 28 (1989)
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
---

## Summary

A *proof net* is a graph that represents a derivation of multiplicative [[linear logic|2P2184B6HE]] without the order of its rules; see [[the definition|6G6M2V85RZ]].
Its nodes are formula occurrences, and its links are axiom, cut, $\otimes$ and $\mathbin{\wp}$ links.
A graph of this shape that need not come from a derivation is a *proof structure*.
A correctness criterion tells which proof structures are proof nets, and the [[Danos-Regnier criterion|SBY2YQ8EN6]] is one of them.

## Motivation

Two sequent derivations can differ only in the order of independent rules.
For example, $\vdash A \mathbin{\wp} B, C \mathbin{\wp} D$ has two derivations from $\vdash A, B, C, D$, which apply the two $\mathbin{\wp}$ rules in the two orders.
These derivations give the same proof net, so the net keeps only the structure that matters.
Cut elimination on nets uses local graph rewrites and has no commutative cases.

## Notation

We draw a link as a node with its premises above and its conclusion below.
An axiom link has two conclusions $A$ and $A^{\perp}$ and no premise, and a cut link has two premises $A$ and $A^{\perp}$ and no conclusion.
A $\otimes$ link and a $\mathbin{\wp}$ link have two premises $A$, $B$ and one conclusion $A \otimes B$ or $A \mathbin{\wp} B$.

## Remarks

### Examples

1. The [[net of the commutativity of tensor|CGY2T895AH]] has two axiom links, one $\otimes$ link and two $\mathbin{\wp}$ links.
2. Every axiom link alone is a proof net with conclusions $A$ and $A^{\perp}$.
3. A [[cut on two small nets|SY0QVH7S09]] reduces in three steps to a net without cut.

### Non-examples

The proof structures for $\vdash p \otimes p^{\perp}$ and for $\vdash p \mathbin{\wp} q, p^{\perp} \mathbin{\wp} q^{\perp}$ are [[not proof nets|NFZ99FB74R]].
Each one has a correction graph that is not a tree.

### Basic properties

1. Each sequent derivation of MLL without units translates into a proof net, by induction on the derivation.
2. A proof structure is a proof net if and only if each of its correction graphs is a tree, by the [[Danos-Regnier theorem|SBY2YQ8EN6]].
3. In a proof net, the number of axiom links is one more than the number of $\otimes$ links and cut links together.

### History

The Wikipedia article on proof nets states that Girard introduced them, and that his long-trip criterion was the first correctness criterion.
The SEP entry on linear logic states that the long-trip criterion appears in Girard's 1987 paper, and it names the acyclic connected criterion of Danos and Regnier from 1989.
The same SEP entry reports a 2016 result of Heijltjes and Houston: MLL with units has no satisfactory notion of proof net.

### Common errors

A proof structure with the correct conclusions need not be a proof net.
The structure for $\vdash p \otimes p^{\perp}$ has an axiom link and a $\otimes$ link, but the sequent is not derivable.

## Explanations

### L1 human

A sequent proof is a list of steps in a fixed order.
Often the order of two steps does not matter.
A proof net draws the proof as a picture with lines from each formula to its parts, so the order disappears.

### L2 human

We draw the net of $\vdash p \mathbin{\wp} q, p^{\perp} \otimes q^{\perp}$.

1. Draw two axiom links: one between $p$ and $p^{\perp}$, one between $q$ and $q^{\perp}$.
2. Join $p$ and $q$ by a $\mathbin{\wp}$ link with conclusion $p \mathbin{\wp} q$.
3. Join $p^{\perp}$ and $q^{\perp}$ by a $\otimes$ link with conclusion $p^{\perp} \otimes q^{\perp}$.
4. Count: two axiom links and one $\otimes$ link, so the count of property 3 holds.
5. A switching keeps one premise edge of the $\mathbin{\wp}$ link.
   Each of the two graphs has $6$ vertices and $5$ edges and is connected, so it is a tree.

The typical use of proof nets is to compare derivations and to run cut elimination in parallel.
A trap: with a $\mathbin{\wp}$ link in step 3 as well, the structure for $\vdash p \mathbin{\wp} q, p^{\perp} \mathbin{\wp} q^{\perp}$ has the same shape, but it is not a proof net.

### L3 human

Proof nets are the MLL case of a general aim: to find canonical representatives of proofs modulo the permutation of rules.
For MLL without units this aim succeeds, and correctness can be checked in linear time, as the SEP entry reports.
For the additives, the exponentials and the units, the SEP entry reports that the known notions are less satisfactory.
