---
tag: CGY2T895AH
kind: example
name: Proof net of the commutativity of tensor
msc: ["03F52"]
topics: [98QF5J4W16]
audience: research
instance_of: [HN6WN1VE39]
uses: [6G6M2V85RZ, SBY2YQ8EN6, 8KN0QTZ1ED]
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
The [[derivation|8KN0QTZ1ED]] of $\vdash (p^{\perp} \mathbin{\wp} q^{\perp}) \mathbin{\wp} (q \otimes p)$ translates to a [[proof net|6G6M2V85RZ]] with these seven occurrences and five links.

1. Occurrences: $p^{\perp}$, $q^{\perp}$, $q$, $p$, $P = p^{\perp} \mathbin{\wp} q^{\perp}$, $T = q \otimes p$ and $R = P \mathbin{\wp} T$.
2. Axiom links: one between $p^{\perp}$ and $p$, one between $q^{\perp}$ and $q$.
3. A $\otimes$ link with premises $q$, $p$ and conclusion $T$.
4. A $\mathbin{\wp}$ link with premises $p^{\perp}$, $q^{\perp}$ and conclusion $P$, and a $\mathbin{\wp}$ link with premises $P$, $T$ and conclusion $R$.

We check the [[Danos-Regnier criterion|SBY2YQ8EN6]] for all four switchings.

1. Every correction graph has the four edges $p^{\perp} - p$, $q^{\perp} - q$, $T - q$ and $T - p$.
   They connect $p^{\perp}$, $p$, $T$, $q$ and $q^{\perp}$.
2. The inner $\mathbin{\wp}$ link adds $P - p^{\perp}$ or $P - q^{\perp}$.
   Both ends of the other edge are already connected, so $P$ joins the connected part.
3. The outer $\mathbin{\wp}$ link adds $R - P$ or $R - T$, and $R$ joins the connected part.
4. So each correction graph is connected, with $7$ vertices and $6$ edges.
   A connected graph with one edge fewer than vertices is a tree.
5. The count of links holds: $2$ axiom links, $1$ link of type $\otimes$ and $0$ cut links, and $2 = 1 + 0 + 1$.

## Remarks

The two axiom links cross: $p^{\perp}$ is on the left of $q^{\perp}$, but $p$ is on the right of $q$.
In a planar drawing they must cross, and this crossing is the trace of exchange.
In proof nets for the non-commutative Lambek calculus, axiom links may not cross, and the same structure is not allowed.

## Explanations

### L1 human

The picture has two lines that join $p$ with its negation and $q$ with its negation.
The lines cross, because the order of $p$ and $q$ changes.
Every way to cut the lines above the two "par" nodes leaves a connected picture without loops.

### L2 human

We list the four correction graphs by the edge that each $\mathbin{\wp}$ link keeps.

1. $(P - p^{\perp}, R - P)$: the path $q^{\perp} - q - T - p - p^{\perp} - P - R$.
2. $(P - p^{\perp}, R - T)$: the path $q^{\perp} - q - T - p - p^{\perp} - P$, with $R$ attached to $T$.
3. $(P - q^{\perp}, R - P)$: the path $p^{\perp} - p - T - q - q^{\perp} - P - R$.
4. $(P - q^{\perp}, R - T)$: the path $p^{\perp} - p - T - q - q^{\perp} - P$, with $R$ attached to $T$.

Each is a tree with $7$ vertices, so the structure is a proof net.

The typical use of this example is as a first test of the criterion on a net with two $\mathbin{\wp}$ links.
A trap: replace the outer $\mathbin{\wp}$ by $\otimes$, and the switching graph in item 1 gains the edge $R - T$ and a cycle $R - P - p^{\perp} - p - T - R$.
