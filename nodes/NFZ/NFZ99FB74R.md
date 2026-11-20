---
tag: NFZ99FB74R
kind: example
name: Proof structures that are not proof nets
msc: ["03F52"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: HN6WN1VE39
    note: each of these proof structures has a switching whose correction graph is not a tree
uses: [6G6M2V85RZ, SBY2YQ8EN6, SYMW99C0EV]
sources:
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.3 Proof nets
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1007/BF01622878
    locator: pages 181-203
    note: Danos and Regnier, The structure of multiplicatives, Archive for Mathematical Logic 28 (1989)
---

## Example

Let $p$ and $q$ be atoms.
The two [[proof structures|6G6M2V85RZ]] below fail the [[Danos-Regnier criterion|SBY2YQ8EN6]], so they are not proof nets.

Structure $S_1$, with conclusion $p \otimes p^{\perp}$:

1. It has an axiom link between $p$ and $p^{\perp}$, and a $\otimes$ link with premises $p$, $p^{\perp}$ and conclusion $T$.
2. It has no $\mathbin{\wp}$ link, so its only correction graph has the edges $p - p^{\perp}$, $T - p$ and $T - p^{\perp}$.
3. These three edges form a cycle, so the graph is not a tree.
4. The sequent $\vdash p \otimes p^{\perp}$ is not derivable.
   A cut-free derivation would end with $\otimes$ and have $\vdash p$ or $\vdash p^{\perp}$ as a premise, and neither is derivable.

Structure $S_2$, with conclusions $P = p \mathbin{\wp} q$ and $Q = p^{\perp} \mathbin{\wp} q^{\perp}$:

1. It has axiom links $p - p^{\perp}$ and $q - q^{\perp}$, a $\mathbin{\wp}$ link on $p$, $q$ with conclusion $P$, and a $\mathbin{\wp}$ link on $p^{\perp}$, $q^{\perp}$ with conclusion $Q$.
2. Take the switching that keeps $P - p$ and $Q - p^{\perp}$.
3. The edges are $p - p^{\perp}$, $q - q^{\perp}$, $P - p$ and $Q - p^{\perp}$.
   No edge joins $\set{q, q^{\perp}}$ to the other four vertices.
4. So the graph is not connected, and it is not a tree.
5. The sequent $\vdash p \mathbin{\wp} q, p^{\perp} \mathbin{\wp} q^{\perp}$ is not derivable.
   A cut-free derivation would reach $\vdash p, q, p^{\perp}, q^{\perp}$ by two $\mathbin{\wp}$ rules, and no rule or axiom gives this sequent of four atoms.

## Remarks

Both structures fail the count of links in the [[proof|N8MC3HNB51]] of the criterion.
$S_1$ has $1$ axiom link and $1$ link of type $\otimes$, and $1 \neq 1 + 0 + 1$.
$S_2$ has $2$ axiom links and no link of type $\otimes$, and $2 \neq 0 + 0 + 1$.
In both cases the conclusions have the right shape for links, so only the criterion or a search for derivations rejects them.
With $\otimes$ in place of the first $\mathbin{\wp}$ of $S_2$, the structure for $\vdash p \otimes q, p^{\perp} \mathbin{\wp} q^{\perp}$ is a proof net.

## Explanations

### L1 human

The first picture has a loop: $p$ and its negation are joined twice.
The second picture falls into two pieces when we cut the right lines.
A real proof never gives a loop or two pieces, so neither picture is a proof.

### L2 human

We check all four switchings of $S_2$, to see which ones fail.

1. $(P - p, Q - p^{\perp})$: the part $\set{q, q^{\perp}}$ is cut off.
2. $(P - q, Q - q^{\perp})$: the part $\set{p, p^{\perp}}$ is cut off.
3. $(P - p, Q - q^{\perp})$: the edges $P - p - p^{\perp}$ and $Q - q^{\perp} - q$ give two paths, so the graph is not connected.
4. $(P - q, Q - p^{\perp})$: two paths $P - q - q^{\perp}$ and $Q - p^{\perp} - p$, again not connected.

Every switching gives $6$ vertices and $4$ edges, so none is a tree.

The typical use of these structures is to test a program that checks the criterion.
A trap: for $S_1$ the criterion fails without any switching, so a check that looks only at $\mathbin{\wp}$ links misses it.
