---
tag: VW8XP95XCB
kind: definition
name: Labelled sequent calculus
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: research
defines: F46GV42XCE
uses: [W72CA3R9MP, C3RZY20ETK, NGHWZ9Y7ZV, XBCYFDPS2F, MYJ8Y050J0]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
---

## Definition

A labelled sequent names the worlds of a Kripke model, as in $x : \Box p, x R y \Rightarrow y : p$.
Formulas of the basic [[modal logic|C3RZY20ETK]] K are built from variables $p, q, \dots$ and $\bot$ with $\wedge$, $\vee$, $\to$, $\Box$ and $\Diamond$.
Fix a countable set of *labels* $x, y, z, \dots$, which name worlds.
A *labelled formula* is an expression $x : A$, with a label $x$ and a formula $A$.
A *relational atom* is an expression $x R y$, with labels $x$ and $y$.
A *labelled sequent* is $\Gamma \Rightarrow \Delta$, where $\Gamma$ is a finite [[multiset|MYJ8Y050J0]] of labelled formulas and relational atoms, and $\Delta$ is a finite multiset of labelled formulas.

Let $\rho$ map labels to worlds of a Kripke model with [[accessibility relation|XBCYFDPS2F]] $R$.
Then $x R y$ is true if $\rho(x) \mathrel{R} \rho(y)$, and $x : A$ is true if $A$ holds at $\rho(x)$.
The sequent $\Gamma \Rightarrow \Delta$ is *valid* in a class of frames if, for every model on such a frame and every $\rho$, some member of $\Gamma$ is false or some member of $\Delta$ is true.
A *labelled sequent calculus* is a set of rules on labelled sequents.

### Negri's calculus G3K

The initial sequents and propositional rules of G3K are those of the classical calculus G3c, applied at a single label.
The modal rules are as follows, with arbitrary contexts $\Gamma$ and $\Delta$:
$$\dfrac{y : A, x : \Box A, x R y, \Gamma \Rightarrow \Delta}{x : \Box A, x R y, \Gamma \Rightarrow \Delta} \ ({\Box}\mathrm{L}) \qquad \dfrac{x R y, \Gamma \Rightarrow \Delta, y : A}{\Gamma \Rightarrow \Delta, x : \Box A} \ ({\Box}\mathrm{R})$$
$$\dfrac{x R y, y : A, \Gamma \Rightarrow \Delta}{x : \Diamond A, \Gamma \Rightarrow \Delta} \ ({\Diamond}\mathrm{L}) \qquad \dfrac{x R y, \Gamma \Rightarrow \Delta, x : \Diamond A, y : A}{x R y, \Gamma \Rightarrow \Delta, x : \Diamond A} \ ({\Diamond}\mathrm{R})$$
In ${\Box}$R and ${\Diamond}$L the label $y$ must not occur in the conclusion.
For a set $S$ of geometric frame conditions, the calculus G3K$S$ adds their *geometric rules*, defined in the remarks below.

## Notation

Negri writes G3K for the basic calculus, and G3KT, G3S4, G3S5 and so on for the extensions.
Some authors write $x \Vdash A$ or $A^x$ instead of $x : A$, and $x \le y$ or $R x y$ instead of $x R y$.
Other labelled systems also allow relational atoms in the succedent, or use labelled natural deduction instead of sequents.

## Remarks

### The propositional rules of G3K

The initial sequents are $x : p, \Gamma \Rightarrow \Delta, x : p$ for a variable $p$, and $x : \bot, \Gamma \Rightarrow \Delta$.
Each propositional rule acts on formulas with one label $x$, as in G3c.

- ${\wedge}$L: from $x : A, x : B, \Gamma \Rightarrow \Delta$ infer $x : A \wedge B, \Gamma \Rightarrow \Delta$.
- ${\wedge}$R: from $\Gamma \Rightarrow \Delta, x : A$ and $\Gamma \Rightarrow \Delta, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \wedge B$.
- ${\vee}$L: from $x : A, \Gamma \Rightarrow \Delta$ and $x : B, \Gamma \Rightarrow \Delta$ infer $x : A \vee B, \Gamma \Rightarrow \Delta$.
- ${\vee}$R: from $\Gamma \Rightarrow \Delta, x : A, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \vee B$.
- ${\to}$L: from $\Gamma \Rightarrow \Delta, x : A$ and $x : B, \Gamma \Rightarrow \Delta$ infer $x : A \to B, \Gamma \Rightarrow \Delta$.
- ${\to}$R: from $x : A, \Gamma \Rightarrow \Delta, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \to B$.

### Why each part is there

The labels let a single sequent talk about several worlds, which an ordinary modal sequent cannot do.
The relational atoms record which worlds reach which, so the rules for $\Box$ and $\Diamond$ can follow the truth clauses.
The label $y$ in ${\Box}$R and ${\Diamond}$L is the *eigenvariable* of the rule.
It must be fresh because ${\Box}$R claims $A$ at an arbitrary reachable world, and a world already named might carry extra assumptions.
The rules ${\Box}$L and ${\Diamond}$R repeat their principal formula in the premise, so that it can be used again for other worlds.
That copy is what makes contraction admissible.
Relational atoms stay in the antecedent, so only frame rules act on them, and frame rules never touch a labelled formula.

### A small case and a failing case

The sequent $x : \Box p, x R y \Rightarrow y : p$ is derivable in G3K.
Backward ${\Box}$L adds $y : p$ to the antecedent, and $y : p, x : \Box p, x R y \Rightarrow y : p$ is initial.

The sequent $x : p \Rightarrow x : \Box p$ is not derivable, and it is not valid.
Backward ${\Box}$R must use a fresh label $y$, which gives the goal $x R y, x : p \Rightarrow y : p$.
No rule closes it, and the model with worlds $x, y$, $x R y$, and $p$ true at $x$ only refutes it.
If ${\Box}$R allowed $y = x$, the premise $x R x, x : p \Rightarrow x : p$ would be initial and the invalid sequent would follow.

### Geometric frame rules

A *geometric implication* is a first-order sentence of the following form:
$$\forall \bar{x}\, \bigl( P_1 \wedge \cdots \wedge P_m \to \exists \bar{y}_1 M_1 \vee \cdots \vee \exists \bar{y}_n M_n \bigr).$$
Each $P_i$ is a relational atom, and each $M_j$ is a conjunction of relational atoms $Q_{j1}, \dots, Q_{jk_j}$.
Its *geometric rule* has the conclusion $P_1, \dots, P_m, \Gamma \Rightarrow \Delta$ and the $n$ premises below:
$$\bar{Q}_j[\bar{z}_j / \bar{y}_j], P_1, \dots, P_m, \Gamma \Rightarrow \Delta \qquad (j = 1, \dots, n).$$
The labels $\bar{z}_j$ must not occur in the conclusion.
A rule set satisfies the *closure condition* if, whenever a substitution of labels makes two atoms $P_i$ of a rule equal, the rule with one copy of that atom is also in the set.
For a set $S$ of geometric implications, G3K$S$ contains the rules of $S$ and their contracted instances.

### Common frame rules

The frame rules for the most common conditions are as follows.

- Ref, for reflexivity $\forall x\, x R x$: from $x R x, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta$.
- Trans, for transitivity: from $x R z, x R y, y R z, \Gamma \Rightarrow \Delta$ infer $x R y, y R z, \Gamma \Rightarrow \Delta$.
- Sym, for symmetry: from $y R x, x R y, \Gamma \Rightarrow \Delta$ infer $x R y, \Gamma \Rightarrow \Delta$.
- Eucl, for euclideanness: from $y R z, x R y, x R z, \Gamma \Rightarrow \Delta$ infer $x R y, x R z, \Gamma \Rightarrow \Delta$.
- Ser, for seriality $\forall x \exists y\, x R y$: from $x R y, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta$, with $y$ not in the conclusion.

For Eucl the substitution $z := y$ makes the two atoms of the conclusion equal.
The closure condition then adds the contracted rule, which infers $x R y, \Gamma \Rightarrow \Delta$ from $y R y, x R y, \Gamma \Rightarrow \Delta$.

### Soundness

Each rule preserves validity in the frames that satisfy the conditions.
For ${\Box}$R, suppose that the conclusion fails under $\rho$, so $\Box A$ fails at $\rho(x)$.
Then some world $w$ with $\rho(x) \mathrel{R} w$ refutes $A$.
Since $y$ does not occur in the conclusion, we may set $\rho(y) = w$, and the premise fails under the new map.
For Ref, a countermodel of the conclusion on a reflexive frame also makes $x R x$ true, so it refutes the premise.
For Ser, a countermodel on a serial frame gives $\rho(x)$ a successor $w$, and setting $\rho(y) = w$ refutes the premise.

### Structural properties and cut

**Theorem (Negri).** Let $S$ be a set of geometric implications, and let G3K$S$ satisfy the closure condition.
Then the following hold.

1. Every sequent $x : A, \Gamma \Rightarrow \Delta, x : A$ is derivable, for every formula $A$.
2. Substitution of labels is height-preserving admissible.
3. Weakening is height-preserving admissible, and contraction of labelled formulas and of relational atoms is height-preserving admissible.
4. Every rule is height-preserving invertible.
5. The cut rule, from $\Gamma \Rightarrow \Delta, x : A$ and $x : A, \Gamma' \Rightarrow \Delta'$ infer $\Gamma, \Gamma' \Rightarrow \Delta, \Delta'$, is admissible.

### Structural properties and cut, continued

The proof of item 5 is an induction on the weight of the cut formula $A$, with a subinduction on the sum of the heights of the two premises.
Frame rules have no principal labelled formula, so the cut formula is never principal in a frame rule, and the cut moves above it.
Take the case $x : \Box A$, with ${\Box}$R on the left and ${\Box}$L with the atom $x R z$ on the right.
Item 2 renames the eigenvariable $y$ of the left premise to $z$.
A cut on $x : \Box A$ of smaller height removes the copy of $x : \Box A$ in the right premise.
A cut on $z : A$, of smaller weight, then joins the two, and item 3 removes the duplicated context.
The closure condition is needed for item 3, because contracting two equal atoms in the conclusion of a frame rule needs the contracted rule.
The full case analysis is in Negri's paper "Proof analysis in modal logic", and we cite it.

### Derivable axioms

The Hilbert axiom K, $\Box(A \to B) \to (\Box A \to \Box B)$, is derivable in G3K.
Necessitation is admissible: if $\Rightarrow x : A$ is derivable, item 2 gives $\Rightarrow y : A$, weakening gives $x R y \Rightarrow y : A$, and ${\Box}$R gives $\Rightarrow x : \Box A$.
Modus ponens is admissible too: invert ${\to}$R on $\Rightarrow x : A \to B$ and cut with $\Rightarrow x : A$.
So G3K derives all theorems of K, and G3K$S$ derives each axiom whose frame condition is in $S$.
For example, Ref gives the axiom T and Trans gives the axiom 4, as the [[example of the axiom T|HDWFDRR42X]] and the [[example of the axiom 4|2N9E5E8HRX]] show.

## Explanations

### L1 human

A modal formula talks about many worlds at once: "$\Box A$" says that $A$ holds in every world that we can reach.
A labelled calculus writes the world next to each formula, as in "$x : A$", which reads "$A$ holds at world $x$".
It also writes facts such as "$x R y$", which reads "world $y$ can be reached from $x$".
The rules then follow the meaning of the symbols world by world.
Properties of reachability, such as "every world reaches itself", become extra rules about these facts.

### L2 human

We derive the axiom K in G3K, written $\Rightarrow x : \Box(p \to q) \to (\Box p \to \Box q)$.
Let $\Sigma$ be the multiset $x : \Box(p \to q), x : \Box p, x R y$.
The sequents $y : p, \Sigma \Rightarrow y : q, y : p$ and $y : q, y : p, \Sigma \Rightarrow y : q$ are initial.
The rule ${\to}$L on these two sequents gives $y : p \to q, y : p, \Sigma \Rightarrow y : q$.
${\Box}$L for $x : \Box p$ removes $y : p$, and ${\Box}$L for $x : \Box(p \to q)$ removes $y : p \to q$, which leaves $\Sigma \Rightarrow y : q$.
${\Box}$R with eigenvariable $y$ gives $x : \Box(p \to q), x : \Box p \Rightarrow x : \Box q$, and ${\to}$R twice gives the goal.
The typical use of the calculus is backward proof search, with the rules read from the conclusion upward.
Watch out for the eigenvariable condition: in the ${\Box}$R step the label $y$ must not occur in the conclusion, and it does not.

### L3 human

Labelled calculi internalize the Kripke semantics: the sequent becomes a small piece of a model.
Any logic whose frames are defined by geometric implications gets a cut-free calculus in a uniform way, which covers T, 4, B, 5, D and many others.
The price is extra syntax: a cut-free derivation has the subformula property for labelled formulas, but labels and relational atoms are not formulas of the logic.
The same method applies to intuitionistic logic and intermediate logics, and to provability logic with a changed rule.
It also connects proof search with countermodel construction.
Compare with [[hypersequent calculi|73J7F0FN4A]], which encode some of the frame structure without names for worlds.
