---
tag: 1X7D5CBXB7
kind: definition
name: Display calculus
msc: ["03F05", "03B45", "03B47"]
topics: [R10RMQCJQX]
audience: research
defines: 2Q62W689SC
uses: [W72CA3R9MP, C3RZY20ETK, NGHWZ9Y7ZV, XBCYFDPS2F]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Structures and connectives
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Definition

A display calculus is a sequent calculus on structures whose invertible structural rules can bring any part of a sequent out to stand alone on one side.
We define Belnap's display calculus $\mathrm{DK_t}$ for the minimal tense logic $\mathrm{K_t}$.
Formulas are built from propositional variables $p, q, \dots$ and the constants $\top, \bot$ with $\neg$, $\wedge$, $\vee$, $\to$, a box $\Box$ and a backward diamond $\blacklozenge$.
In a Kripke model with [[accessibility relation|XBCYFDPS2F]] $R$, $\Box A$ holds at $w$ if $A$ holds at every $v$ with $w R v$, and $\blacklozenge A$ holds at $w$ if $A$ holds at some $v$ with $v R w$.

*Structures* are given by the grammar $X ::= A \mid \mathrm{I} \mid {*}X \mid X \circ Y \mid {\bullet} X$, where $A$ is a formula.
A *sequent* is an expression $X \vdash Y$ with structures $X$ and $Y$.

**Antecedent and succedent parts.**
In $X \vdash Y$, the structure $X$ is an antecedent part and $Y$ is a succedent part.
If $Z_1 \circ Z_2$ or ${\bullet}Z_1$ is an antecedent part, then $Z_1$ and $Z_2$ are antecedent parts, and the same holds for succedent parts.
If ${*}Z$ is an antecedent part, then $Z$ is a succedent part, and conversely.

### The display postulates

The sign $\iff$ means that each sequent can be derived from the other in one step.
The four groups D1 to D4 are the following:
$$\begin{aligned} &(\mathrm{D1}) && X \circ Y \vdash Z \iff X \vdash {*}Y \circ Z \iff Y \vdash {*}X \circ Z, \\ &(\mathrm{D2}) && X \vdash Y \circ Z \iff X \circ {*}Y \vdash Z \iff X \circ {*}Z \vdash Y, \\ &(\mathrm{D3}) && X \vdash Y \iff {*}Y \vdash {*}X \iff {*}{*}X \vdash Y \iff X \vdash {*}{*}Y, \\ &(\mathrm{D4}) && {\bullet}X \vdash Y \iff X \vdash {\bullet}Y. \end{aligned}$$
The calculus $\mathrm{DK_t}$ has D1 to D4, the axioms $p \vdash p$, cut, the structural rules and a left and a right rule for each connective, all listed in the Remarks.
In general, a *display calculus* is a sequent calculus on structures with structural connectives whose display postulates give the display property of the theorem in the Remarks.

## Notation

Belnap's paper writes $\mathrm{I}$ for the structural unit, $*$ for structural negation and $\circ$ for the structural comma.
Many later papers write a comma or a semicolon for $\circ$, and $\sharp$ or $*$ for structural negation.
The structural connective for the modality is written ${\bullet}$, $\circ$ or $\ast$ by different authors, so check each paper.
Some authors use $\Diamond^{-1}$ or $\mathsf{P}$ for the backward diamond $\blacklozenge$ and $\mathsf{G}$ for the forward box.

## Remarks

### Why each part is there

The structural negation ${*}$ is what lets a part change sides, and D3 says that it is an involution that swaps the two sides.
The comma $\circ$ reads as a conjunction on the left and as a disjunction on the right, as the comma does in LK, and D1 and D2 say that these two readings are linked by ${*}$.
The modal structure ${\bullet}$ needs a partner modality, because D4 is an adjunction; that is why the language has both $\Box$ and $\blacklozenge$.
The unit $\mathrm{I}$ plays the role of the empty antecedent or the empty succedent.

A small case: in $p \circ q \vdash r$, the postulate D1 gives $p \vdash {*}q \circ r$, so $p$ is displayed.
A failing case: in Gentzen's LK, which has no ${*}$, the part $p$ of $p, q \Rightarrow r$ cannot be displayed, as the [[non-example|TWXM3REK0K]] shows.
The [[concept of a display calculus|2Q62W689SC]] explains what the display property is for.

### The structural rules

Each rule infers the lower sequent from the upper one, and rules marked $\iff$ work in both directions.

- (IL) $X \vdash Z$ $\iff$ $\mathrm{I} \circ X \vdash Z$, and (IR) $X \vdash Z$ $\iff$ $X \vdash Z \circ \mathrm{I}$.
- (I$*$) $\mathrm{I} \vdash Z$ $\iff$ ${*}\mathrm{I} \vdash Z$, and $X \vdash \mathrm{I}$ $\iff$ $X \vdash {*}\mathrm{I}$.
- (W) from $X \vdash Z$ infer $X \circ Y \vdash Z$; (C) from $X \circ X \vdash Z$ infer $X \vdash Z$; (E) from $X \circ Y \vdash Z$ infer $Y \circ X \vdash Z$.
- (A) $X_1 \circ (X_2 \circ X_3) \vdash Z$ $\iff$ $(X_1 \circ X_2) \circ X_3 \vdash Z$.

The axioms are $p \vdash p$ for each variable $p$, and the cut rule infers $X \vdash Y$ from $X \vdash A$ and $A \vdash Y$.

### The logical rules

The axioms for the constants are $\mathrm{I} \vdash \top$ and $\bot \vdash \mathrm{I}$, and the other rules for the constants and negation are these:
$$\dfrac{\mathrm{I} \vdash X}{\top \vdash X} \qquad \dfrac{X \vdash \mathrm{I}}{X \vdash \bot} \qquad \dfrac{{*}A \vdash X}{\neg A \vdash X} \qquad \dfrac{X \vdash {*}A}{X \vdash \neg A}$$
The rules for conjunction and disjunction are these:
$$\dfrac{A \circ B \vdash X}{A \wedge B \vdash X} \qquad \dfrac{X \vdash A \quad Y \vdash B}{X \circ Y \vdash A \wedge B} \qquad \dfrac{A \vdash X \quad B \vdash Y}{A \vee B \vdash X \circ Y} \qquad \dfrac{X \vdash A \circ B}{X \vdash A \vee B}$$
The rules for implication are these:
$$\dfrac{X \vdash A \quad B \vdash Y}{A \to B \vdash {*}X \circ Y} \qquad \dfrac{X \vdash {*}A \circ B}{X \vdash A \to B}$$
The modal rules ${\Box}$L, ${\Box}$R, ${\blacklozenge}$L and ${\blacklozenge}$R are these:
$$\dfrac{A \vdash X}{\Box A \vdash {\bullet}X} \qquad \dfrac{X \vdash {\bullet}A}{X \vdash \Box A} \qquad \dfrac{{\bullet}A \vdash X}{\blacklozenge A \vdash X} \qquad \dfrac{X \vdash A}{{\bullet}X \vdash \blacklozenge A}$$
In each pair, the first rule is the left rule and the second is the right rule.

### Formula reading and soundness

The structural connectives have two readings, one in the antecedent and one in the succedent.
We define formulas $\tau_1(X)$ and $\tau_2(X)$ by recursion on $X$, with $\tau_1(A) = \tau_2(A) = A$ for a formula $A$:
$$\begin{aligned} \tau_1(\mathrm{I}) &= \top, & \tau_1({*}X) &= \neg \tau_2(X), & \tau_1(X \circ Y) &= \tau_1(X) \wedge \tau_1(Y), & \tau_1({\bullet}X) &= \blacklozenge \tau_1(X), \\ \tau_2(\mathrm{I}) &= \bot, & \tau_2({*}X) &= \neg \tau_1(X), & \tau_2(X \circ Y) &= \tau_2(X) \vee \tau_2(Y), & \tau_2({\bullet}X) &= \Box \tau_2(X). \end{aligned}$$
The sequent $X \vdash Y$ is *valid* if $\tau_1(X) \to \tau_2(Y)$ is true at every world of every Kripke model.

Each display postulate and each rule preserves validity.
For example, D1 holds because $x \wedge y \to z$ and $x \to \neg y \vee z$ are equivalent.
D4 holds because $\blacklozenge x \to y$ is true at every world of a model exactly when $x \to \Box y$ is: $\blacklozenge$ and $\Box$ are adjoint.
For ${\Box}$L, if $a \to x$ is valid, then $\Box a \to \Box x$ is valid, and $\Box x = \tau_2({\bullet}X)$.

### The display theorem

**Theorem.** If $Z$ is an antecedent part of $X \vdash Y$, then the display postulates turn $X \vdash Y$ into a sequent $Z \vdash W$ for some $W$, and back.
If $Z$ is a succedent part, they turn $X \vdash Y$ into a sequent $W \vdash Z$, and back.

*Proof.* We use induction on the depth of $Z$ in the sequent.
If the depth is $0$, then $Z$ is already $X$ or $Y$.
Otherwise it is enough to move the outermost structural connective above $Z$ to the other side.

1. An antecedent $X_1 \circ X_2 \vdash Y$ becomes $X_1 \vdash {*}X_2 \circ Y$ or $X_2 \vdash {*}X_1 \circ Y$ by D1.
2. An antecedent ${*}X_1 \vdash Y$ becomes ${*}Y \vdash X_1$ by D3: first ${*}Y \vdash {*}{*}X_1$, then remove ${*}{*}$.
3. An antecedent ${\bullet}X_1 \vdash Y$ becomes $X_1 \vdash {\bullet}Y$ by D4.
4. A succedent $X \vdash Y_1 \circ Y_2$ becomes $X \circ {*}Y_2 \vdash Y_1$ or $X \circ {*}Y_1 \vdash Y_2$ by D2.
5. A succedent $X \vdash {*}Y_1$ becomes $Y_1 \vdash {*}X$ by D3: first ${*}{*}Y_1 \vdash {*}X$, then remove ${*}{*}$.
6. A succedent $X \vdash {\bullet}Y_1$ becomes ${\bullet}X \vdash Y_1$ by D4.

Each step lowers the depth of $Z$ by one and keeps $Z$ on its side, by the definition of the parts.
Each step is invertible, so the original sequent can be recovered, and this proves the theorem.

### Necessitation and the tense axioms

Necessitation is derivable.
From $\mathrm{I} \vdash A$, W gives $\mathrm{I} \circ {\bullet}\mathrm{I} \vdash A$, IL gives ${\bullet}\mathrm{I} \vdash A$, D4 gives $\mathrm{I} \vdash {\bullet}A$, and ${\Box}$R gives $\mathrm{I} \vdash \Box A$.

The axiom $A \to \Box \blacklozenge A$ comes from $A \vdash A$ by ${\blacklozenge}$R, D4 and ${\Box}$R, through ${\bullet}A \vdash \blacklozenge A$, then $A \vdash {\bullet}\blacklozenge A$, then $A \vdash \Box\blacklozenge A$.
The axiom $\blacklozenge \Box A \to A$ comes from $A \vdash A$ by ${\Box}$L, D4 and ${\blacklozenge}$L, through $\Box A \vdash {\bullet}A$, then ${\bullet}\Box A \vdash A$, then $\blacklozenge\Box A \vdash A$.

Completeness for $\mathrm{K_t}$ follows the usual plan: derive each axiom of a Hilbert system, simulate modus ponens with cut, and use the derived necessitation rule.
Here $A \vdash A$ for a compound $A$ is derived from the axioms $p \vdash p$ by induction on $A$.

### Belnap's conditions

Belnap stated eight conditions on the rules of a display calculus.
A *parameter* of a rule instance is a constituent that is not principal, and parameters in premise and conclusion that correspond are *congruent*.

- C1, preservation of formulas: every formula in a premise is a subformula of a formula in the conclusion, except in cut.
- C2, shape-alikeness: congruent parameters are occurrences of the same structure.
- C3, non-proliferation: each congruence class of parameters contains at most one constituent of the conclusion. Contraction passes, but a rule may not copy a premise constituent into two places of the conclusion.
- C4, position-alikeness: congruent parameters are all antecedent parts or all succedent parts.
- C5, display of principal constituents: a principal formula of a conclusion is the whole antecedent or the whole succedent.
- C6 and C7, closure under substitution: replacing a congruence class of formula parameters in succedent (C6) or antecedent (C7) position by any structure gives an instance of the same rule.
- C8, eliminability of matching principal constituents: a cut on $A$ between two rules with $A$ principal can be replaced by cuts on proper subformulas of $A$.

### Belnap's theorem

**Theorem (Belnap).** Every display calculus whose rules satisfy C2 to C8 has cut elimination.
With C1, a cut-free derivation also has the [[subformula property|Z2NXKDK06G]].

The proof is by induction on the complexity of the cut formula $A$, in two stages.
In the principal stage, $A$ is principal on both sides, it is displayed by C5, and C8 removes the cut.
In the parametric stage, we trace the congruence class of $A$ upward to the points where $A$ is principal.
C2 to C4 make this class a set of occurrences of $A$ in the same position, and C6 and C7 let us replace each occurrence by the other side of the cut.
The lemma that this substitution yields a derivation, with new cuts only at principal occurrences, is the core of Belnap's paper, and we cite it.

For $\mathrm{DK_t}$, C8 for ${\wedge}$ goes as follows.
From $A \circ B \vdash Z$, D1 gives $A \vdash {*}B \circ Z$, and a cut with $X \vdash A$ gives $X \vdash {*}B \circ Z$.
D1 twice gives $B \vdash {*}X \circ Z$, a cut with $Y \vdash B$ gives $Y \vdash {*}X \circ Z$, and D1 gives $X \circ Y \vdash Z$.
C8 for $\Box$ uses D4: from $X \vdash {\bullet}A$ get ${\bullet}X \vdash A$, cut with $A \vdash Y$, and apply D4 to ${\bullet}X \vdash Y$ to get $X \vdash {\bullet}Y$.

## Explanations

### L1 human

In an ordinary sequent, a formula sits inside a list of assumptions or a list of conclusions.
A display calculus adds rules that move parts of a sequent from one side to the other without changing its meaning.
For example, "$x$ and $y$ give $z$" can be rewritten as "$x$ gives not $y$ or $z$".
With such moves, any part of a sequent can be brought out to stand alone on one side.
Then every logical rule only has to deal with a formula that stands alone, which makes the rules simple and uniform.

### L2 human

Let us display the part $r$ of the sequent $p \circ (q \circ {*}r) \vdash s$.
The part $r$ sits under one ${*}$ in the antecedent, so it is a succedent part, and we aim for a sequent $W \vdash r$.
D1 with $X = p$ and then D1 with $X = q$ give the following:
$$q \circ {*}r \vdash {*}p \circ s, \qquad {*}r \vdash {*}q \circ ({*}p \circ s).$$
Step 2 of the display theorem then gives ${*}({*}q \circ ({*}p \circ s)) \vdash r$.
Its formula reading is $\neg(\neg q \vee \neg p \vee s) \to r$, which is equivalent to $p \wedge q \wedge \neg s \to r$, and so to the reading $p \wedge q \wedge \neg r \to s$ of the first sequent.
The [[example of displaying a substructure|83HPD7MWGD]] gives all the details.
The typical use is to bring a formula into position before a logical rule acts on it, as C5 requires.
Watch out: ${*}$ changes the side, so $r$ inside ${*}r$ in the antecedent is a succedent part.

### L3 human

The display property separates two jobs: the logical rules introduce connectives, and the structural rules carry the properties of the logic.
Dropping W, C, E or A gives display calculi for relevant, linear and other substructural logics, with the same logical rules and the same cut-elimination theorem.
The adjoint pair $\blacklozenge \dashv \Box$ is what makes D4 work, and the same pattern appears for residuated connectives in algebraic logic.
For a modal logic such as K, which has no backward modality, one works in its tense extension $\mathrm{K_t}$, which is conservative over K.
