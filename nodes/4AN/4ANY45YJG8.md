---
tag: 4ANY45YJG8
kind: definition
name: Separation logic
msc: [68Q60, 03B70, 03B47]
defines: CF5Y39BPB0
uses: [H1M6RSBJ5H, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_logic
---

## Definition

Fix a set $\mathit{Var}$ of variables and a set $\mathit{Loc} \subseteq \Z$ of locations.
A *store* is a [[function|0EPAT51DXQ]] $s \colon \mathit{Var} \to \Z$, and a *heap* is a function $h \colon \mathrm{dom}(h) \to \Z$ with finite domain $\mathrm{dom}(h) \subseteq \mathit{Loc}$.
Two heaps $h_1, h_2$ are *disjoint* if their domains are disjoint, and then $h_1 \cdot h_2$ is the heap on $\mathrm{dom}(h_1) \cup \mathrm{dom}(h_2)$ that agrees with each.
The assertions of *separation logic* extend first-order formulas over the store with the following, and their meaning is a relation $s, h \models P$.

1. $s, h \models \mathsf{emp}$ if $\mathrm{dom}(h)$ is empty.
2. $s, h \models E \mapsto F$ if $\mathrm{dom}(h) = \set{s(E)}$ and $h(s(E)) = s(F)$, where $s(E)$ is the value of the expression $E$ in $s$.
3. $s, h \models P * Q$ if $h = h_1 \cdot h_2$ for some disjoint heaps with $s, h_1 \models P$ and $s, h_2 \models Q$.
4. $s, h \models P \mathrel{-\!\!*} Q$ if for every heap $h'$ disjoint from $h$ with $s, h' \models P$, also $s, h \cdot h' \models Q$.

Separation logic is the [[Hoare logic|H1M6RSBJ5H]] for a language with heap commands, with triples $\set{P}\, C\, \set{Q}$ over these assertions.
Triples are read with fault avoidance.
From any state satisfying $P$, the command $C$ never accesses a location outside the heap, and if it terminates, the final state satisfies $Q$.
Its central rule is the frame rule: from $\set{P}\, C\, \set{Q}$ derive $\set{P * R}\, C\, \set{Q * R}$, provided $C$ assigns no variable that occurs free in $R$.

## Remarks

Example: let $s(x) = 10$, $s(y) = 20$ and let $h$ have domain $\set{10, 20}$ with $h(10) = 3$ and $h(20) = 4$.
Then $s, h \models x \mapsto 3 * y \mapsto 4$: split $h$ into the heap $\set{10 \mapsto 3}$, which satisfies $x \mapsto 3$, and the disjoint heap $\set{20 \mapsto 4}$, which satisfies $y \mapsto 4$.

Non-example: $x \mapsto 3 * x \mapsto 3$ holds in no state.
Both parts would need the location $s(x)$ in their domains, so they are not disjoint, and clause 3 fails.
By contrast, the ordinary conjunction $x \mapsto 3 \land x \mapsto 3$ holds in the one-cell heap $\set{s(x) \mapsto 3}$.

The frame rule is sound because of fault avoidance: a command that runs safely in a heap satisfying $P$ cannot touch the cells of a disjoint part satisfying $R$.
The connective $\mathrel{-\!\!*}$ is the separating implication, or magic wand, and it is the right adjoint of $*$.
