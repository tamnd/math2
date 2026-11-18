---
tag: FXTCKYR3AQ
kind: statement
role: theorem
name: Completeness of K, T, D, K4, S4, B and S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, TVE4F04KME, NM4CB7QAYT, E87G6ZTMTN, FDFQFWPM4X, XBCYFDPS2F]
about: [TVE4F04KME, D1TJYZZDCY]
proofs: [BJB500NW0P]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on completeness and canonical models
---

## Statement

Each row of the table pairs a [[normal modal logic|JS8W7PA6JK]] with a class of frames, defined by properties of the [[accessibility relation|XBCYFDPS2F]].

| logic | axioms | frame class |
|---|---|---|
| $\mathsf{K}$ | none | all frames |
| $\mathsf{T}$ | $\mathrm{T}$ | reflexive |
| $\mathsf{D}$ | $\mathrm{D}$ | serial |
| $\mathsf{K4}$ | $\mathrm{4}$ | transitive |
| $\mathsf{S4}$ | $\mathrm{T}, \mathrm{4}$ | reflexive and transitive |
| $\mathsf{B}$ | $\mathrm{T}, \mathrm{B}$ | reflexive and symmetric |
| $\mathsf{S5}$ | $\mathrm{T}, \mathrm{5}$ | equivalence relations |

For each row, with logic $\Lambda$ and class $\mathsf{C}$, and for every set $\Sigma$ of formulas and every formula $\varphi$:

1. Strong completeness. If $\varphi$ is true at every world of every $\mathsf{C}$-model where $\Sigma$ is true, then $\Lambda$ derives $\varphi$ from finitely many members of $\Sigma$.
2. Weak completeness. In particular, $\Lambda \vdash \varphi$ if and only if $\varphi$ is valid on every frame of $\mathsf{C}$.
3. Canonicity. The canonical frame of $\Lambda$ belongs to $\mathsf{C}$.

The proof is in [[the proof of completeness|BJB500NW0P]].

## Remarks

### Why each hypothesis is needed

1. The frame class must be the one that the axioms define. No modal formula defines irreflexivity, and the logic of all irreflexive frames is $\mathsf{K}$ again, so that class gives no new row.
2. Canonicity is the property that makes the proof work, and it is a property of the axioms. Löb's axiom gives a logic $\mathsf{GL}$ that is complete for finite strict orders but not canonical, see [[the GL example|E61769H6KG]]. So the method of this theorem does not apply to it.
3. The axiom sets are fixed. Adding an axiom with no first-order frame condition, such as the McKinsey axiom $\square\lozenge p \to \lozenge\square p$, can break canonicity.

### Consequences

1. The non-theorems of each logic are refuted on its frames: for instance $\mathsf{S4} \nvdash p \to \square\lozenge p$, by the preorder $w \le v$ with $p$ true at $w$ only.
2. With [[soundness|E87G6ZTMTN]], each logic is exactly the set of formulas valid on its frame class.
3. Each logic is compact in the local sense: if every finite subset of $\Sigma$ is satisfiable in $\mathsf{C}$, then so is $\Sigma$.
4. With [[the filtration theorem|T99DK51S0W]], each logic is also complete for the finite frames of its class, see [[the finite model property theorem|XNPJK6B921]].
5. $\mathsf{S5}$ is complete for universal frames, since each class of an equivalence relation is a generated subframe, see [[S5|VC3A2VWXND]].

### Converse

The converse of completeness is [[soundness|E87G6ZTMTN]], which holds for each row by [[common modal axiom schemata|FDFQFWPM4X]].

### Generalizations

1. Every logic $\mathsf{K}\Gamma$ with $\Gamma$ a set of Sahlqvist formulas is canonical and complete for the first-order frame class that $\Gamma$ defines. This is Sahlqvist's theorem, treated in [[modal model theory|SPQVNPZDTB]].
2. The same proof works for $\mathsf{KD45}$, see [[the KD45 example|1CFMP9DEE6]], and for multimodal logics, see [[multimodal logic|ERG3KAQWYF]].
3. Some normal logics are complete for no class of Kripke frames; Thomason and Fine gave the first examples in 1974.

## History

Kripke proved completeness of $\mathsf{T}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ for their frame classes in 1963, with semantic tableaux.
Makinson in 1966 and Lemmon and Scott in notes of 1966, published in 1977, gave the canonical model proofs.
Segerberg's An essay in classical modal logic of 1971 extended the method to many more logics.

## Explanations

### L1 human

Each of these logics is a list of laws for "necessarily".
Each list matches one kind of world network, for example networks where every world can see itself.
Completeness says that the list is enough: every law true in all networks of that kind can be proved from the list.

### L2 human

We use completeness of $\mathsf{T}$ to see that a formula is a theorem without writing its derivation.

1. Take $\varphi = \square p \to \lozenge p$.
2. On a reflexive frame, if $\square p$ is true at $w$, then $p$ is true at $w$, since $w R w$.
3. Then $w$ is a successor of $w$ with $p$, so $\lozenge p$ is true at $w$.
4. So $\varphi$ is valid on all reflexive frames, and completeness gives $\mathsf{T} \vdash \varphi$.

The typical use is to replace a search for a derivation by a semantic argument.
A trap: completeness for a frame class is about validity on frames; a formula true in one reflexive model need not be a theorem.

### L3 human

Completeness of these logics follows from canonicity, a property of the variety of modal algebras: it is closed under canonical extensions.
All the axioms in the table are Sahlqvist formulas, so the theorem is a special case of Sahlqvist's theorem.
The weak and the strong forms differ for other logics: $\mathsf{GL}$ is weakly but not strongly complete for its frames.
The reason is that the set $\set{\lozenge p_0} \cup \set{\square(p_n \to \lozenge p_{n+1}) : n \in \N}$ is finitely satisfiable but not satisfiable on conversely well-founded transitive frames.
