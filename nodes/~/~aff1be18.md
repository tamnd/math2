---
tag: ~aff1be18
kind: definition
name: Labelled sequent calculus
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: research
defines: ~fddc9de5
uses: [W72CA3R9MP, C3RZY20ETK, NGHWZ9Y7ZV, XBCYFDPS2F, MYJ8Y050J0]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
---

## Definition

Formulas of the basic [[modal logic|C3RZY20ETK]] K are built from variables $p, q, \dots$ and $\bot$ with $\wedge$, $\vee$, $\to$, $\Box$, $\Diamond$.
Fix a countable set of *labels* $x, y, z, \dots$, which name worlds of a Kripke model.

- A *labelled formula* is an expression $x : A$, with a label $x$ and a formula $A$.
- A *relational atom* is an expression $x R y$, with labels $x$ and $y$.
- A *labelled sequent* is $\Gamma \Rightarrow \Delta$, with $\Gamma$ a finite [[multiset|MYJ8Y050J0]] of labelled formulas and relational atoms, and $\Delta$ a multiset of labelled formulas.

**Semantics.** Let $\rho$ map labels to worlds of a Kripke model with [[accessibility relation|XBCYFDPS2F]] $R$.
Then $x R y$ is true if $\rho(x) \mathrel{R} \rho(y)$, and $x : A$ is true if $A$ holds at $\rho(x)$.
The sequent $\Gamma \Rightarrow \Delta$ is *valid* in a class of frames if, for every model on such a frame and every $\rho$, some member of $\Gamma$ is false or some member of $\Delta$ is true.

A *labelled sequent calculus* is a set of rules on labelled sequents.
Negri's calculus G3K has these rules, with arbitrary contexts $\Gamma$ and $\Delta$.

- Initial sequents and propositional rules: those of the classical calculus G3c, applied at a single label.
- ${\Box}$L: from $y : A, x : \Box A, x R y, \Gamma \Rightarrow \Delta$ infer $x : \Box A, x R y, \Gamma \Rightarrow \Delta$.
- ${\Box}$R: from $x R y, \Gamma \Rightarrow \Delta, y : A$ infer $\Gamma \Rightarrow \Delta, x : \Box A$, where $y$ does not occur in the conclusion.
- ${\Diamond}$L: from $x R y, y : A, \Gamma \Rightarrow \Delta$ infer $x : \Diamond A, \Gamma \Rightarrow \Delta$, where $y$ does not occur in the conclusion.
- ${\Diamond}$R: from $x R y, \Gamma \Rightarrow \Delta, x : \Diamond A, y : A$ infer $x R y, \Gamma \Rightarrow \Delta, x : \Diamond A$.

For a set $S$ of geometric frame conditions, G3K$S$ adds their *geometric rules*, defined in the remarks below.

## Notation

Negri writes G3K for the basic calculus, and G3KT, G3S4, G3S5 and so on for the extensions.
Some authors write $x \Vdash A$ or $A^x$ instead of $x : A$, and $x \le y$ or $R x y$ instead of $x R y$.
Other labelled systems also allow relational atoms in the succedent, or use labelled natural deduction instead of sequents.

## Remarks

### The propositional rules of G3K

- Initial sequents: $x : p, \Gamma \Rightarrow \Delta, x : p$ for a variable $p$, and $x : \bot, \Gamma \Rightarrow \Delta$.
- ${\wedge}$L: from $x : A, x : B, \Gamma \Rightarrow \Delta$ infer $x : A \wedge B, \Gamma \Rightarrow \Delta$.
- ${\wedge}$R: from $\Gamma \Rightarrow \Delta, x : A$ and $\Gamma \Rightarrow \Delta, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \wedge B$.
- ${\vee}$L: from $x : A, \Gamma \Rightarrow \Delta$ and $x : B, \Gamma \Rightarrow \Delta$ infer $x : A \vee B, \Gamma \Rightarrow \Delta$.
- ${\vee}$R: from $\Gamma \Rightarrow \Delta, x : A, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \vee B$.
- ${\to}$L: from $\Gamma \Rightarrow \Delta, x : A$ and $x : B, \Gamma \Rightarrow \Delta$ infer $x : A \to B, \Gamma \Rightarrow \Delta$.
- ${\to}$R: from $x : A, \Gamma \Rightarrow \Delta, x : B$ infer $\Gamma \Rightarrow \Delta, x : A \to B$.

### Eigenvariables

The label $y$ in ${\Box}$R and ${\Diamond}$L is the *eigenvariable* of the rule.
The rules ${\Box}$L and ${\Diamond}$R repeat their principal formula in the premise, so that it can be used again for other worlds.

### Geometric frame rules

A *geometric implication* is a first-order sentence of the form
$$\forall \bar{x}\, \bigl( P_1 \wedge \cdots \wedge P_m \to \exists \bar{y}_1 M_1 \vee \cdots \vee \exists \bar{y}_n M_n \bigr),$$
where each $P_i$ is a relational atom and each $M_j$ is a conjunction of relational atoms $Q_{j1}, \dots, Q_{jk_j}$.
Its *geometric rule* has the $n$ premises
$$\bar{Q}_j[\bar{z}_j / \bar{y}_j], P_1, \dots, P_m, \Gamma \Rightarrow \Delta \qquad (j = 1, \dots, n)$$
and the conclusion $P_1, \dots, P_m, \Gamma \Rightarrow \Delta$, where the labels $\bar{z}_j$ do not occur in the conclusion.
The rule set satisfies the *closure condition* if, whenever a substitution of labels makes two atoms $P_i$ of a rule equal, the rule with one copy of that atom is also in the set.

For a set $S$ of geometric implications, G3K$S$ contains the rules of $S$ and their contracted instances.

### Common frame rules

The frame rules for the most common conditions are as follows.

- Ref (reflexivity $\forall x\, xRx$): from $x R x, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta$.
- Trans (transitivity): from $x R z, x R y, y R z, \Gamma \Rightarrow \Delta$ infer $x R y, y R z, \Gamma \Rightarrow \Delta$.
- Sym (symmetry): from $y R x, x R y, \Gamma \Rightarrow \Delta$ infer $x R y, \Gamma \Rightarrow \Delta$.
- Eucl (euclideanness): from $y R z, x R y, x R z, \Gamma \Rightarrow \Delta$ infer $x R y, x R z, \Gamma \Rightarrow \Delta$.
- Ser (seriality $\forall x \exists y\, xRy$): from $x R y, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta$, where $y$ does not occur in the conclusion.

For Eucl the closure condition adds the contracted rule: from $y R y, x R y, \Gamma \Rightarrow \Delta$ infer $x R y, \Gamma \Rightarrow \Delta$.

### Soundness

Each rule preserves validity in the frames that satisfy the conditions.
For ${\Box}$R, suppose that the conclusion fails under $\rho$, so $\Box A$ fails at $\rho(x)$.
Then some world $w$ with $\rho(x) \mathrel{R} w$ refutes $A$.
Since $y$ does not occur in the conclusion, we may set $\rho(y) = w$, and the premise fails under the new map.
For Ref, a counter-model of the conclusion on a reflexive frame also makes $x R x$ true, so it refutes the premise.

### Structural properties and cut

**Theorem (Negri).** Let $S$ be a set of geometric implications, and let G3K$S$ satisfy the closure condition.
Then the following hold.

1. Every sequent $x : A, \Gamma \Rightarrow \Delta, x : A$ is derivable, for every formula $A$.
2. Substitution of labels is height-preserving admissible.
3. Weakening is height-preserving admissible, and contraction of labelled formulas and of relational atoms is height-preserving admissible.
4. Every rule is height-preserving invertible.
5. The cut rule, from $\Gamma \Rightarrow \Delta, x : A$ and $x : A, \Gamma' \Rightarrow \Delta'$ infer $\Gamma, \Gamma' \Rightarrow \Delta, \Delta'$, is admissible.

The proof of item 5 is an induction on the weight of the cut formula $A$, with a subinduction on the sum of the heights of the two premises.
Frame rules have no principal labelled formula, so a cut never has a frame rule with the cut formula principal, and the cut moves above the frame rule.
In the case $x : \Box A$ with ${\Box}$R on the left and ${\Box}$L on the right, item 2 renames the eigenvariable $y$ to the world $z$ used by ${\Box}$L.
This produces a cut on $z : A$, of smaller weight, and a cut on $x : \Box A$ of smaller height.
The closure condition is needed for item 3: contraction of two equal atoms in the conclusion of a frame rule needs the contracted rule.
The full case analysis is in Negri's paper "Proof analysis in modal logic"; we cite it.

### Derivable axioms

The Hilbert axiom K, $\Box(A \to B) \to (\Box A \to \Box B)$, is derivable in G3K.
Necessitation is the rule ${\Box}$R applied to a derivation of $\Rightarrow y : A$ weakened by $x R y$.
Modus ponens follows from the admissibility of cut.
So G3K derives all theorems of K, and G3K$S$ derives each axiom whose frame condition is in $S$.
For example Ref gives the axiom T and Trans gives the axiom 4, as the [[example of the axiom T|~c9b5ac2c]] and the [[example of the axiom 4|~bdb8464b]] show.

## Explanations

### L1 human

A modal formula talks about many worlds at once: "$\Box A$" says that $A$ holds in every world that we can reach.
A labelled calculus writes the world next to each formula, as in "$x : A$", which reads "$A$ holds at world $x$".
It also writes facts such as "$x R y$", which reads "world $y$ can be reached from $x$".
The rules then follow the meaning of the symbols world by world.
Properties of reachability, such as "every world reaches itself", become extra rules about these facts.

### L2 human

We derive the axiom K in G3K, written $\Rightarrow x : \Box(p \to q) \to (\Box p \to \Box q)$.

1. Let $\Sigma$ be $x : \Box(p \to q), x : \Box p, x R y$. Then $y : p, \Sigma \Rightarrow y : q, y : p$ and $y : q, y : p, \Sigma \Rightarrow y : q$ are initial sequents.
2. ${\to}$L on these two sequents gives $y : p \to q, y : p, \Sigma \Rightarrow y : q$.
3. ${\Box}$L for $x : \Box p$ removes $y : p$, and ${\Box}$L for $x : \Box(p \to q)$ removes $y : p \to q$.
4. This gives $\Sigma \Rightarrow y : q$.
5. ${\Box}$R with eigenvariable $y$ gives $x : \Box(p \to q), x : \Box p \Rightarrow x : \Box q$.
6. ${\to}$R twice gives $\Rightarrow x : \Box(p \to q) \to (\Box p \to \Box q)$.

The typical use of the calculus is backward proof search, with the rules read from the conclusion upward.
A trap is the eigenvariable condition: in step 5 the label $y$ must not occur in the conclusion.

### L3 human

Labelled calculi internalize the Kripke semantics: the sequent becomes a small piece of a model.
Any logic whose frames are defined by geometric implications gets a cut-free calculus in a uniform way, which covers T, 4, B, 5, D and many others.
The price is extra syntax: a cut-free derivation has the subformula property for labelled formulas, but labels and relational atoms are not formulas of the logic.
The same method applies to intuitionistic logic, to intermediate logics and to provability logic with a changed rule, and it connects proof search with countermodel construction.
Compare with [[hypersequent calculi|~908a51bf]], which encode some of the frame structure without names for worlds.
