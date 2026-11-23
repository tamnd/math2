---
tag: D1TJYZZDCY
kind: concept
name: Normal modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [G8VGTW9P4F, NGHWZ9Y7ZV, JS8W7PA6JK]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

A normal modal logic is a set of laws in which the box behaves like "true at every alternative": it holds of every theorem, and it passes through implication.
For example, every normal logic proves $\square(p \wedge q) \to \square p$ in three steps.
The formula $(p \wedge q) \to p$ is a tautology, so necessitation gives $\square((p \wedge q) \to p)$.
The axiom $\mathrm{K}$ turns this into $\square(p \wedge q) \to \square p$ by modus ponens.

Exactly, a normal modal logic is a [[modal logic|G8VGTW9P4F]] $\Lambda$ that contains the axiom $\mathrm{K}$ and is closed under the [[necessitation rule|G989VP2NGP]]:
$$\square(p \to q) \to (\square p \to \square q) \in \Lambda, \qquad \varphi \in \Lambda \implies \square\varphi \in \Lambda.$$
So $\Lambda$ contains all tautologies and is closed under modus ponens, uniform substitution and necessitation.
The smallest such set is $\mathsf{K}$, defined in [[normal modal logic K|JS8W7PA6JK]], and $\mathsf{K}\Gamma$ is the smallest normal modal logic that contains a set $\Gamma$.

## Motivation

The formulas valid on a class of [[Kripke frames|NGHWZ9Y7ZV]] always contain $\mathrm{K}$ and are closed under necessitation, by [[soundness of normal modal logics|E87G6ZTMTN]].
So these two conditions are the least that a logic needs if it is to have a relational semantics.
They say that $\square$ acts as a universal quantifier over alternatives: it holds of every theorem, and it commutes with finite conjunctions.

Once we fix these two conditions, the study of normal logics becomes the study of conditions on frames.
Adding $\mathrm{T}$ asks for reflexive frames, adding $\mathrm{4}$ asks for transitive frames, and so on, as [[common modal axiom schemata|FDFQFWPM4X]] shows.
The completeness theorems of the [[canonical model|TVE4F04KME]] and the decision methods of [[filtration|6ZZSHAKG5F]] are theorems about normal logics.

## Notation

We write $\mathsf{K}\Gamma$ or $\mathsf{K} + \Gamma$ for the normal logic axiomatized by $\Gamma$, and $\mathsf{KT4}$, $\mathsf{KD45}$ and so on for named axioms.
Books use two families of names, and both are in use: $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$, $\mathsf{S4} = \mathsf{KT4}$, $\mathsf{B} = \mathsf{KTB}$ and $\mathsf{S5} = \mathsf{KT5}$.
$\operatorname{NExt}(\Lambda)$ is the set of normal logics that contain $\Lambda$, and it is a complete lattice under inclusion.
We write $\Gamma \vdash_\Lambda \varphi$ when $\Lambda \vdash (\gamma_1 \wedge \dots \wedge \gamma_n) \to \varphi$ for some $\gamma_1, \dots, \gamma_n \in \Gamma$.

## Remarks

### Logics you will meet

$\mathsf{K}$ itself is the logic of all frames.
The logics $\mathsf{T}$, $\mathsf{D}$ and $\mathsf{K4}$ of [[modal logics T, D and K4|XVYMEZKH7R]], and the logics [[S4|N60RVXSA5W]] and [[S5|VC3A2VWXND]], are normal.
So is the [[provability logic|WJK0YA4GP2]] $\mathsf{GL}$, which adds [[Löb's axiom|QQ6PZFGGB3]] to $\mathsf{K}$.
At the top sit two consistent extremes, the trivial logic $\mathsf{K} + (\square p \leftrightarrow p)$ and the verum logic $\mathsf{K} + \square\bot$; see [[the two extreme logics|5PZCVXYXDD]].

### A first derivation

In every normal logic the box distributes over conjunction:
$$\square(p \wedge q) \leftrightarrow (\square p \wedge \square q).$$
The direction from left to right is the derivation of the Summary, done once for $p$ and once for $q$.
The direction from right to left needs the tautology $p \to (q \to (p \wedge q))$ and two uses of $\mathrm{K}$.
[[Box distributes over conjunction in K|S860E9DNXA]] writes out both directions.

### What is not normal

The classical logics of [[neighborhood semantics|CN7HK9K1B6]] that omit $\mathrm{K}$, such as the smallest one, $\mathsf{E}$, are modal logics but not normal; see [[the neighborhood example|G2X3PKG55F]].
Lewis's systems $\mathsf{S2}$ and $\mathsf{S3}$ are not normal, because they are not closed under necessitation.
The set of tautologies in the modal language is closed under the three rules of a modal logic, but it is not normal.
It omits $\mathrm{K}$, because $\square(p \to q)$, $\square p$ and $\square q$ act as three unrelated letters.

### The rules you can use

An intersection of normal logics is normal, so $\mathsf{K}\Gamma$ exists and $\operatorname{NExt}(\mathsf{K})$ is a complete lattice.
Every normal logic has the derived rules RM, RE and RK of [[normal modal logic K|JS8W7PA6JK]], which move a theorem under the box.
For every class $\mathsf{C}$ of frames, $\operatorname{Log}(\mathsf{C})$ is a normal logic, by soundness.
A normal logic is consistent exactly when it omits $\bot$, and the only inconsistent one is the set of all formulas.
A normal logic is *Kripke complete* when it equals $\operatorname{Log}(\mathsf{C})$ for some class $\mathsf{C}$.
The logics of the [[completeness theorem|FXTCKYR3AQ]] are Kripke complete, and some normal logics are not; see [[Kripke incompleteness|W67YJQTT50]].

### Watch out

The rule of necessitation is not the formula $\varphi \to \square\varphi$.
Adding $p \to \square p$ as an axiom gives a much stronger logic, and $\mathsf{K}$ does not prove it; see [[the non-theorem p → □p|R2WWD2R5NV]].
The rule also applies only to theorems, never to assumptions of a derivation, or the deduction theorem breaks; see [[the global consequence example|R6MA6TFN5K]].
Finally, $\square$ does not distribute over $\vee$: only $(\square p \vee \square q) \to \square(p \vee q)$ is a theorem, and [[the three-world model|6JXBZ2C9B4]] refutes the converse.

### History

Kripke's paper of 1963 on these logics has "normal modal propositional calculi" in its title.
Kripke treated the non-normal systems $\mathsf{S2}$ and $\mathsf{S3}$ with non-normal worlds in 1965.
Segerberg developed the general theory of normal logics in An Essay in Classical Modal Logic (1971).

### Try it

First, derive $\square p \to \square(p \vee q)$ in $\mathsf{K}$.
The formula $p \to (p \vee q)$ is a tautology, so necessitation gives $\square(p \to (p \vee q))$, and $\mathrm{K}$ with modus ponens gives the claim.

Second, is the verum logic $\mathsf{K} + \square\bot$ consistent?
Yes: on the frame with one world and no arrows, $\square\bot$ is true, so by soundness the logic does not contain $\bot$.

## Explanations

### L1 human

A normal modal logic is a set of laws for "necessarily".
It keeps all laws of ordinary logic.
It adds two rules: a law is itself necessary, and if "$p$ implies $q$" and "$p$" are both necessary, then "$q$" is necessary.
For example, "necessarily, it rains or it does not rain" is a law of every normal logic.

### L2 human

We derive $\square p \wedge \square q \to \square(p \wedge q)$ in a normal logic $\Lambda$, without any semantics.
We start from the tautology $p \to (q \to (p \wedge q))$, which is in $\Lambda$.
Necessitation gives $\square(p \to (q \to (p \wedge q)))$, and then $\mathrm{K}$ with modus ponens gives the following line:
$$\square p \to \square(q \to (p \wedge q)).$$
The instance of $\mathrm{K}$ with $q$ and $p \wedge q$ for its letters is the next line:
$$\square(q \to (p \wedge q)) \to (\square q \to \square(p \wedge q)).$$
Chaining the two lines by the tautology $(a \to b) \to ((b \to c) \to (a \to c))$ gives $\square p \to (\square q \to \square(p \wedge q))$, which is the claim.
The typical use of such derivations is to collect laws of $\square$ that hold in every normal logic.
Watch out: necessitation applies to theorems of $\Lambda$, never to assumptions.

### L3 human

A normal logic $\Lambda$ gives the Lindenbaum algebra of formulas modulo $\Lambda$-provable equivalence, a Boolean algebra with an operator that preserves $\top$ and $\wedge$.
The normal logics correspond one to one to the varieties of such algebras, and $\operatorname{NExt}(\mathsf{K})$ is dually isomorphic to the lattice of subvarieties.
The structure of this lattice is studied in [[the lattice of normal modal logics|EZ011FT3GT]], a topic of [[modal model theory|SPQVNPZDTB]].
