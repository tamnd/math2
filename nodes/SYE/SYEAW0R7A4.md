---
tag: SYEAW0R7A4
kind: example
name: The natural numbers are not a substructure of the integers with negation
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
not_instance_of:
  - target: 676H7EGTKJ
    note: the natural numbers contain 1 but not its negation, so they are not closed under the unary function symbol for negation
uses: [676H7EGTKJ, 0EREPBVG2G, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Substructure_(mathematics)
    locator: Definition; Examples
---

## Example

Let $L = \set{+, -, 0}$, with a binary function symbol $+$, a unary function symbol $-$ and a constant symbol $0$.
Let $\mathcal{Z} = (\Z, +, -, 0)$ with the usual addition, negation and zero.
We show that $\N = \set{0, 1, 2, \dots}$ is not the domain of a [[substructure|676H7EGTKJ]] of $\mathcal{Z}$.

1. A substructure must contain the constant $0^{\mathcal{Z}} = 0$, and $0 \in \N$; so this condition holds.
2. A substructure must be closed under $+$; for $m, n \in \N$, $m + n \in \N$; so this condition holds.
3. A substructure must be closed under the unary function $-$; but $1 \in \N$ and $-1 \notin \N$; so this condition fails.

So $\N$ is not a substructure of $\mathcal{Z}$, although it is closed under $+$ and contains $0$.

## Remarks

The failure is in one function symbol only.
If we drop $-$ from the signature, $(\N, +, 0)$ is a substructure of $(\Z, +, 0)$.
So the same subset is a substructure for one signature and not for another.

Relations give a second kind of failure.
View a [[graph|00C0BR7D7H]] as a structure with one binary relation $E$.
Let $P$ be the path with vertices $1, 2, 3$ and edges $\set{1, 2}$ and $\set{2, 3}$.
The subgraph $Q$ with vertices $1, 2$ and no edge is a subgraph of $P$, but it is not a substructure.

4. A substructure on $\set{1, 2}$ must have $E^{Q} = E^{P} \cap \set{1, 2}^2$.
5. The pair $(1, 2)$ lies in $E^{P}$, so it must lie in $E^{Q}$; but $Q$ has no edge.

The substructures of a graph are exactly its [[induced subgraphs|0EREPBVG2G]].

## Explanations

### L1 human

The numbers $0, 1, 2, 3, \dots$ are closed under addition: adding two of them gives another.
But if the structure also has the operation "take the opposite", then the opposite of $1$ is $-1$, which is not among them.
So these numbers do not form a part of the integers with addition and opposites.
They do form a part of the integers with addition only.

### L2 human

We test the set $S = \set{-2, -1, 0, 1, 2}$ in $(\Z, +, -, 0)$.

1. $0 \in S$, so the constant condition holds.
2. $-x \in S$ for each $x \in S$, so the condition for $-$ holds.
3. $1 + 2 = 3 \notin S$, so the condition for $+$ fails.

So $S$ is not a substructure.
The typical use of such a check is to find the one operation that leads out of the subset.
A trap is to check the operations only on a few elements: one failure is enough, but a proof of closure needs all elements.
