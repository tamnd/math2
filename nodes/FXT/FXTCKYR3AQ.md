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

Each row of the table pairs a [[normal modal logic|JS8W7PA6JK]] with a class of frames, given by a property of the [[accessibility relation|XBCYFDPS2F]].

| logic | also written | axioms added to $\mathsf{K}$ | frame class |
|---|---|---|---|
| $\mathsf{K}$ | $\mathsf{K}$ | none | all frames |
| $\mathsf{T}$ | $\mathsf{KT}$ | $\mathrm{T}$ | reflexive |
| $\mathsf{D}$ | $\mathsf{KD}$ | $\mathrm{D}$ | serial |
| $\mathsf{K4}$ | $\mathsf{K4}$ | $\mathrm{4}$ | transitive |
| $\mathsf{S4}$ | $\mathsf{KT4}$ | $\mathrm{T}, \mathrm{4}$ | reflexive and transitive |
| $\mathsf{B}$ | $\mathsf{KTB}$ | $\mathrm{T}, \mathrm{B}$ | reflexive and symmetric |
| $\mathsf{S5}$ | $\mathsf{KT5}$ | $\mathrm{T}, \mathrm{5}$ | equivalence relations |

Fix a row, with logic $\Lambda$ and frame class $\mathsf{C}$, and let $\Sigma$ be a set of formulas and $\varphi$ a formula.

1. Strong completeness. If $\varphi$ is true at every world of a $\mathsf{C}$-model where all of $\Sigma$ is true, then $\Lambda$ derives $\varphi$ from finitely many members of $\Sigma$.
2. Weak completeness. In particular, $\Lambda \vdash \varphi$ holds if and only if $\varphi$ is valid on every frame of $\mathsf{C}$.
3. Canonicity. The canonical frame of $\Lambda$ belongs to $\mathsf{C}$.

The proof is in [[the proof of completeness|BJB500NW0P]].

## Remarks

### Why each hypothesis is needed

The frame class must be one that the axioms describe.
No modal formula defines irreflexivity, and the logic of all irreflexive frames is $\mathsf{K}$ again, so that class gives no new row.

Canonicity is the property that makes the proof work, and it depends on the axioms.
Löb's axiom gives the logic $\mathsf{GL}$, which is complete for finite strict orders but not canonical, as [[the GL example|E61769H6KG]] shows, so the method of this theorem does not reach it.

The class in part 3 must be the full class.
$\mathsf{S5}$ is also complete for the universal frames, but its canonical frame is not universal: the sets containing $p$ and the sets containing $\square\neg p$ lie in different classes.
So part 3 holds for equivalence relations and fails for universal frames.

### What it gives you

Non-theorems are refuted on small frames of the class.
For instance, $\mathsf{S4} \nvdash p \to \square\lozenge p$, as the preorder $w \le v$ with $p$ true at $w$ only shows.
With [[soundness|E87G6ZTMTN]], each logic is exactly the set of formulas valid on its frame class.
Each logic is compact in the local sense: if every finite subset of $\Sigma$ is satisfiable on $\mathsf{C}$, then so is $\Sigma$.
With [[the filtration theorem|T99DK51S0W]], each logic is also complete for the finite frames of its class, as in [[the finite model property theorem|XNPJK6B921]].
$\mathsf{S5}$ is complete for universal frames as well, since each class of an equivalence relation is a generated subframe, as on [[the S5 page|VC3A2VWXND]].

### The converse

The converse of completeness is [[soundness|E87G6ZTMTN]].
It holds for each row, because each axiom is valid on the frames of its class, as in [[common modal axiom schemata|FDFQFWPM4X]].

### Generalizations

[[Sahlqvist's theorem|S4SSDMETJM]] says that $\mathsf{K}$ plus any set of Sahlqvist formulas is canonical and complete for the first-order frame class those formulas define.
Every axiom in the table is a Sahlqvist formula, so the theorem is a special case.
The same proof works for $\mathsf{KD45}$, as in [[the KD45 example|1CFMP9DEE6]], and for logics with several boxes, as in [[multimodal logic|ERG3KAQWYF]].
Some normal logics are complete for no class of Kripke frames, and Thomason and Fine gave the first examples in 1974, as on [[Kripke incompleteness|W67YJQTT50]].

## History

Kanger and Hintikka had related semantic ideas in the 1950s.
Kripke proved completeness of $\mathsf{S5}$ for its relational semantics in 1959, and in 1963 he proved completeness of $\mathsf{T}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ for their frame classes with semantic tableaux.
Makinson gave proofs with maximal consistent sets in 1966.
Lemmon and Scott developed canonical models in the 1960s, and their notes were published in 1977, edited by Segerberg.
Segerberg's An Essay in Classical Modal Logic of 1971 extended the method to many more logics.

## Explanations

### L1 human

Each of these logics is a list of laws for "necessarily".
Each list matches one kind of network of worlds, for example networks in which every world can see itself.
Completeness says that the list is enough: every law that holds in all networks of that kind can be proved from the list.

### L2 human

We use completeness of $\mathsf{T}$ to see that $\square p \to \lozenge p$ is a theorem without writing a derivation.
On a reflexive frame, if $\square p$ is true at $w$, then $p$ is true at $w$, since $w R w$.
Then $w$ is a successor of itself where $p$ holds, so $\lozenge p$ is true at $w$.
So the formula is valid on all reflexive frames, and completeness gives $\mathsf{T} \vdash \square p \to \lozenge p$.
The typical use is to replace a search for a derivation by a semantic argument.
Watch out: completeness for a frame class is about validity on frames, and a formula true in one reflexive model need not be a theorem.

### L3 human

Algebraically, canonicity says that the variety of modal algebras of $\Lambda$ is closed under canonical extensions.
The weak and strong forms of completeness differ for other logics: $\mathsf{GL}$ is weakly but not strongly complete for its frames.
The reason is that the set $\{ \lozenge p_0 \} \cup \{ \square(p_n \to \lozenge p_{n+1}) : n \in \mathbb{N} \}$ is finitely satisfiable but not satisfiable on any transitive conversely well-founded frame.
