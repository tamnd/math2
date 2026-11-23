---
tag: S4SSDMETJM
kind: statement
role: theorem
name: Sahlqvist's theorem
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: research
uses: [3RYBWYPJVD, YW6YGBMVQY, NGHWZ9Y7ZV, 6W9MEGN982, 086QKPF0A6]
about: [3RYBWYPJVD, C3RZY20ETK]
proofs: [2FN47ZQPYF]
history:
  first_stated: "Sahlqvist, 1975, Completeness and correspondence in the first and second order semantics for modal logic"
  notes: "Sambin and Vaccaro gave a simpler proof of the canonicity half in 1989."
sources:
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Kracht's theorem
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Statement

Take $\square p \to \square \square p$ and ask which frames validate it.
If $\square p$ is true at $x$, then $p$ is true at least on the successors of $x$, so the smallest valuation that makes the antecedent true is $P(u) := R(x, u)$.
The consequent $\square \square p$ translates to $\forall y \, \forall z \, (R(x, y) \wedge R(y, z) \to P(z))$.
Substituting the smallest valuation gives $\forall y \, \forall z \, (R(x, y) \wedge R(y, z) \to R(x, z))$, which is transitivity at $x$.
Sahlqvist's theorem says that this computation is always correct for formulas of a certain shape, and that the logics they axiomatize are complete.

We use the basic modal language and [[Kripke semantics|NGHWZ9Y7ZV]].
A *boxed atom* is a formula $\square^k p$ with $k \geq 0$, where $\square^0 p = p$.
A *positive* formula is built from variables, $\top$ and $\bot$ with $\wedge$, $\vee$, $\square$ and $\lozenge$, and a *negative* formula is $\neg \pi$ with $\pi$ positive.
A *Sahlqvist antecedent* is built from $\top$, $\bot$, boxed atoms and negative formulas with $\wedge$, $\vee$ and $\lozenge$.
A *Sahlqvist implication* is $\varphi \to \psi$ with $\varphi$ a Sahlqvist antecedent and $\psi$ positive.
A *Sahlqvist formula* is built from Sahlqvist implications with $\square$ and $\wedge$, and with $\vee$ applied only to formulas that share no variable.

### The theorem

**Theorem.** Let $\chi$ be a Sahlqvist formula.

1. (Correspondence) There is a [[first-order|086QKPF0A6]] formula $c_\chi(x)$ in the language with $R$ and $=$, computable from $\chi$, with the following property: for every frame $\mathfrak{F} = (W, R)$ and every $w \in W$, $\chi$ is true at $w$ under every valuation if and only if $\mathfrak{F} \models c_\chi[w]$.
   So $\chi$ [[corresponds|3RYBWYPJVD]] to $\forall x \, c_\chi(x)$.
2. (Canonicity) For every normal modal logic $\Lambda$ that contains $\chi$, the canonical frame of $\Lambda$ validates $\chi$.
3. (Completeness) If $\Sigma$ is a set of Sahlqvist formulas, then the normal logic $\mathsf{K} \oplus \Sigma$ is strongly complete for the class of frames that satisfy $\{\forall x \, c_\chi(x) : \chi \in \Sigma\}$.

The [[proof|2FN47ZQPYF]] gives item 1 in full, item 2 as a structure with the cited lemmas named, and item 3 from items 1 and 2.

## Remarks

### Worked examples

The formulas $p \to \lozenge p$, $\square p \to p$, $\lozenge \lozenge p \to \lozenge p$, $p \to \square \lozenge p$, $\lozenge p \to \square \lozenge p$, $\square \square p \to \square p$ and $\lozenge \square p \to \square \lozenge p$ are Sahlqvist.
Their correspondents are reflexivity, reflexivity, transitivity, symmetry, the Euclidean property, density and confluence.
See [[the density example|TBVXHH00GQ]] and [[the confluence example|SD4F3G0EPR]] for two of these checked by hand.

### Why each hypothesis is needed

A box over a diamond in the antecedent is not allowed.
The McKinsey formula $\square \lozenge p \to \lozenge \square p$ breaks this rule, and it has no first-order correspondent; see [[the McKinsey formula|4N4ZNWZRE2]].

A box over an implication in the antecedent is not allowed.
Löb's formula $\square(\square p \to p) \to \square p$ breaks this rule, and it has no first-order correspondent; see [[Löb's formula is not first-order definable|RVTJNF5HMF]].

The variables of a disjunction must be disjoint.
The formulas $\square(\top \to p)$ and $\square(p \to \bot)$ are Sahlqvist, and each is valid at $w$ exactly when $w$ has no successor.
Their disjunction is equivalent to $\square p \vee \square \neg p$, which is valid at $w$ exactly when $w$ has at most one successor.
So the disjunction of the two correspondents is the wrong condition.

### What it gives you

The logics $\mathsf{T}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$, $\mathsf{S5}$ and $\mathsf{S4.2}$, and all their extensions by Sahlqvist axioms, are canonical and complete for first-order classes of frames.
The local correspondent comes from a uniform algorithm, the minimal valuation method of the proof.

### The converse

Read literally, the converse is false.
The formula $\square p \vee \square \neg p$ is not a Sahlqvist formula, since the two disjuncts share $p$.
It is equivalent to the Sahlqvist formula $\lozenge p \to \square p$, so it has a first-order correspondent and is canonical.
Kracht's theorem gives a partial converse: it describes syntactically the first-order formulas that are local correspondents of Sahlqvist formulas.

### Generalizations

The inductive formulas of Goranko and Vakarelov extend the Sahlqvist class and keep both halves of the theorem.
The algorithm SQEMA of Conradie, Goranko and Vakarelov, and the algorithm ALBA of Conradie and Palmigiano, compute correspondents by eliminating second-order quantifiers.
Both succeed on all inductive formulas.
The theorem holds for polymodal languages and for operators of any arity, with the same proof.

## History

Henrik Sahlqvist proved the theorem in 1975, in "Completeness and correspondence in the first and second order semantics for modal logic".
Giovanni Sambin and Virginia Vaccaro gave a simpler proof of the canonicity half in 1989.

## Explanations

### L1 human

Some modal axioms describe a simple shape of the arrows in a picture, such as "every point has an arrow to itself".
Sahlqvist's theorem gives a list of formulas for which this always works, and a recipe that finds the shape.
The formulas on the list also give logics that are complete for their shapes.
For example, "if possibly possibly $p$, then possibly $p$" fits the list, and the recipe returns "arrows compose", that is, transitivity.

### L2 human

We run the recipe on $p \to \square \lozenge p$.
The antecedent is the boxed atom $p$ at the world $x$.
The minimal valuation that makes $p$ true at $x$ is $\{x\}$, that is, $P(u) := (u = x)$.
The consequent $\square \lozenge p$ translates to $\forall y \, (R(x, y) \to \exists z \, (R(y, z) \wedge P(z)))$.
Substituting gives $\forall y \, (R(x, y) \to \exists z \, (R(y, z) \wedge z = x))$, which simplifies to $\forall y \, (R(x, y) \to R(y, x))$.
That is symmetry at $x$.
The typical use is to read off a frame class and a completeness theorem from an axiom at once.
Watch out: the theorem is about syntactic shape, and a formula equivalent to a Sahlqvist formula is covered only after one rewrites it in that shape.

### L3 human

Algebraically, Sahlqvist's theorem says that certain inequalities between terms of modal algebras are preserved by canonical extensions.
On perfect algebras the same inequalities are equivalent to first-order conditions.
The proof works through duality: descriptive frames are the duals of modal algebras, and the minimal valuations are closed sets.
Unified correspondence, the program behind ALBA, transfers this pattern to distributive and non-distributive lattice expansions, and so to intuitionistic, substructural and many-valued logics.
