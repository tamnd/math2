---
tag: 3AJTDAP93H
kind: concept
name: Multiple-conclusion logic
aliases: [multiple-conclusion-consequence, set-set-consequence]
msc: ["03B22", "03F03"]
topics: [NJB94B39QK]
audience: grad
uses: [0BSJ7RQ9BW, 1HK0VYWTV7, J78Y1M4GND, W72CA3R9MP, 5DYNDW9526]
sources:
  - wikipedia: en:3748162@r1328744586
    locator: Multiple-conclusion logic
    note: adopted
    mention: wikipedia://en/3748162
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logical-constants/
    locator: Logical Constants (SEP entry), sections 6 and 6.1
  - book: isbn:9780521217651
same_as:
  wikidata: Q6934867
  wikipedia: Multiple-conclusion logic
inventory: [84RVJ504GH]
---

## Summary

A *multiple-conclusion logic* is a logic whose [[consequence|1HK0VYWTV7]] is a relation $\Gamma \vdash \Delta$ between two [[sets|0BSJ7RQ9BW]] of formulas.
The usual reading is: whenever every element of $\Gamma$ is true, some element of $\Delta$ is true.
Dually, whenever every element of $\Delta$ is false, some element of $\Gamma$ is false.
A single-conclusion [[consequence relation|J78Y1M4GND]] is the special case where $\Delta$ has exactly one element.

## Motivation

A single-conclusion relation treats truth and falsity unequally: it says what must be true, given premises, but not what must be false.
A multiple-conclusion relation is symmetric under the exchange of truth with falsity, and of premises with conclusions.
It is the semantic counterpart of the multiple-succedent [[sequent calculus|W72CA3R9MP]] LK of Gentzen.
It also expresses facts that single conclusions cannot express, such as "from $A \lor B$, at least one of $A$ and $B$ follows".
These facts are enough to fix the classical truth tables, a property that single-conclusion classical consequence lacks.

## Notation

For a set $V$ of valuations $v : L \to \set{\mathsf{T}, \mathsf{F}}$ on a language $L$, we write $\Gamma \vDash_V \Delta$ if every $v \in V$ that makes all of $\Gamma$ true makes some element of $\Delta$ true.
We write $\Gamma, A$ for $\Gamma \cup \set{A}$ on either side.
An empty right side means "the premises cannot all be true"; an empty left side means "the conclusions cannot all be false".

## Remarks

### Examples

- [[Disjunction elimination in multiple-conclusion form|SQXC89ZP9F]]: in classical logic $p \lor q \vdash p, q$, while neither $p$ nor $q$ follows alone.
- [[Multiple conclusions fix the classical truth tables|B5TPYADN4W]]: the valuations that respect classical multiple-conclusion consequence are exactly the Boolean valuations.
- [[Multiple-conclusion duality of K3 and LP|H1CSPXEVM1]]: one valuation space gives two dual consequence relations.
- Gentzen reads a sequent $\Gamma \Rightarrow \Delta$ of LK as the formula $\bigwedge \Gamma \to \bigvee \Delta$; for finite sets, this agrees with classical multiple-conclusion consequence.

### Non-examples

- A Hilbert-style system with one formula on the right of $\vdash$ defines only a single-conclusion relation.
- The relation "every element of $\Delta$ follows from $\Gamma$" uses sets on both sides but is not a multiple-conclusion consequence: its conclusions are read conjunctively, not disjunctively.

### Basic properties

- For every set $V$ of valuations, $\vDash_V$ satisfies three conditions: *overlap* ($\Gamma \cap \Delta \neq \emptyset$ implies $\Gamma \vdash \Delta$), *dilution* (adding formulas on either side keeps $\vdash$), and *cut* (from $\Gamma \vdash \Delta, A$ and $\Gamma, A \vdash \Delta$ infer $\Gamma \vdash \Delta$).
- If infinite sets are allowed on both sides, $\vDash_V$ determines $V$.
  For $v \notin V$, put $\Gamma := \set{A : v(A) = \mathsf{T}}$ and $\Delta := \set{A : v(A) = \mathsf{F}}$; then $\Gamma \vDash_V \Delta$ holds and $v$ violates it.
- Single-conclusion classical consequence is respected by valuations that are not Boolean, for example the valuation that makes exactly the tautologies true; the multiple-conclusion relation excludes them.
- The SEP entry on logical constants reports that single-conclusion sequent rules give the intuitionistic connectives, while multiple-conclusion sequent rules give the classical ones.

### History

Gentzen's sequent calculus LK has multiple formulas in the succedent.
Shoesmith and Smiley developed multiple-conclusion logic in the 1970s, in their 1978 book.
The Wikipedia article reports that this form of logic has not been widely adopted.
Some logicians, for example Restall, prefer it because single-conclusion consequence favors truth over falsity, and assertion over denial.

### Common errors

- To read $\Gamma \vdash \Delta$ as "every element of $\Delta$ follows from $\Gamma$". The conclusions are read as a disjunction.
- To think that $p \lor q \vdash p, q$ gives $p \lor q \vdash p$ or $p \lor q \vdash q$. A multiple-conclusion inference does not split into single-conclusion ones.
- To think that an empty set of conclusions means "no information". $\Gamma \vdash \emptyset$ says that $\Gamma$ is unsatisfiable.

## Explanations

### L1 human

Usually an argument goes from several premises to one conclusion.
In multiple-conclusion logic, an argument may also have several conclusions.
It is valid if, whenever all the premises are true, at least one conclusion is true.
For example, from "it is Monday or Tuesday", we get the conclusions "Monday" and "Tuesday", meaning that at least one holds.

### L2 human

A multiple-conclusion relation is like a sequent $\Gamma \Rightarrow \Delta$ of classical sequent calculus.
Premises are read as a conjunction, and conclusions as a disjunction.
It expresses the classical [[principle of bivalence|5DYNDW9526]] as $\emptyset \vdash A, \neg A$ and the law of non-contradiction as $A, \neg A \vdash \emptyset$.
A trap is to confuse the comma on the right with "and"; on the right it means "or".

### L3 human

For finite $\Gamma$ and $\Delta$, a multiple-conclusion relation on a classical language is fixed by the single formulas $\bigwedge \Gamma \to \bigvee \Delta$.
The interest of the notion lies in languages or semantics where this reduction fails, and in the question which semantics a consequence relation determines.
Under bivalence, classical multiple-conclusion consequence determines the classical truth tables uniquely, while the single-conclusion relation does not.
The same frame treats the duality of the three-valued logics K3 and LP in one statement, with empty sides allowed.
