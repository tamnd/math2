---
tag: AYRZ98Y0NW
kind: statement
role: theorem
name: Cut-elimination theorem
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PZX9J3VEMT, W72CA3R9MP, N4EDJNMTEF, ~5bc7d378]
about: [W72CA3R9MP, ~e8e93527]
proofs: [~dac34e15, ~9c2f7b72]
sources:
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: Cut elimination
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Cut-elimination in the sequent calculus
same_as:
  wikidata: Q376166
  wikipedia: Cut-elimination theorem
history:
  first_stated: "1934 to 1935"
  notes: "Gentzen proved the theorem for LK and LJ in his paper Untersuchungen über das logische Schließen, and called it the Hauptsatz."
---

## Statement

Let LK and LJ be the [[sequent calculi|PZX9J3VEMT]] of Gentzen for first-order logic, with the [[cut rule|~5bc7d378]].
The *degree* $|A|$ of a formula $A$ is the number of occurrences of connectives and quantifiers in $A$.
The *cut rank* of a derivation is $0$ if it has no cut, and otherwise the largest value $|C| + 1$ over its cut formulas $C$.

1. **LK.** If a sequent $\Gamma \Rightarrow \Delta$ has a derivation in LK, then it has a derivation in LK without cut.
2. **LJ.** If a sequent $\Gamma \Rightarrow \Delta$ has a derivation in LJ, then it has a derivation in LJ without cut.
3. **A bound, in the one-sided propositional form.** Let $\vdash^h_r \Gamma$ say that the finite set $\Gamma$ of formulas in negation normal form has a derivation of height at most $h$ and cut rank at most $r$ in the one-sided calculus defined below. Then $\vdash^h_r \Gamma$ implies $\vdash^{2_r(h)}_0 \Gamma$.

In part 3, the function $2_r(h)$ is defined by $2_0(h) = h$ and $2_{r+1}(h) = 2^{2_r(h)}$.
So $2_r(h)$ is a tower of $r$ twos with $h$ on top.
The one-sided calculus works with propositional formulas built from literals $p$ and $\neg p$ by $\wedge$ and $\vee$.
For such a formula $A$, the formula $\neg A$ is defined by the de Morgan laws, so $\neg \neg A = A$.
It has the following axioms and rules, where $\Gamma, A$ means $\Gamma \cup \{A\}$.

- Axiom: $\Gamma$, when $p \in \Gamma$ and $\neg p \in \Gamma$ for some propositional variable $p$.
- ${\wedge}$: from $\Gamma, A_0$ and $\Gamma, A_1$ infer $\Gamma$, when $A_0 \wedge A_1 \in \Gamma$.
- ${\vee}$: from $\Gamma, A_i$ for one $i \in \{0, 1\}$ infer $\Gamma$, when $A_0 \vee A_1 \in \Gamma$.
- Cut: from $\Gamma, C$ and $\Gamma, \neg C$ infer $\Gamma$.

Here a literal has degree $0$, and $|A_0 \wedge A_1| = |A_0 \vee A_1| = |A_0| + |A_1| + 1$.

## Remarks

### Why each hypothesis is needed

The theorem is about pure logic.
With extra initial sequents it fails.
Add the initial sequents $\Rightarrow p$ and $p \Rightarrow q$ to LK, for distinct propositional variables $p$ and $q$.
A cut on $p$ gives $\Rightarrow q$.
Without cut, the last step of a derivation of $\Rightarrow q$ can only be a weakening from the empty sequent $\Rightarrow$.
No rule except cut has the empty sequent as its conclusion, and it is not an initial sequent.
So $\Rightarrow q$ has no derivation without cut.
For the same reason, cuts on induction formulas cannot be removed from proofs in arithmetic, and [[Gentzen's consistency proof|QPV0HNP22S]] removes only part of the cuts.

The theorem also needs rules that fit together on the left and the right.
Add a connective $\mathbin{\mathrm{tonk}}$ with a right rule that infers $\Gamma \Rightarrow \Delta, A \mathbin{\mathrm{tonk}} B$ from $\Gamma \Rightarrow \Delta, A$.
Give it a left rule that infers $A \mathbin{\mathrm{tonk}} B, \Gamma \Rightarrow \Delta$ from $B, \Gamma \Rightarrow \Delta$.
From $p \Rightarrow p$ and $q \Rightarrow q$ these rules give $p \Rightarrow p \mathbin{\mathrm{tonk}} q$ and $p \mathbin{\mathrm{tonk}} q \Rightarrow q$, and a cut gives $p \Rightarrow q$.
Without cut, $p \Rightarrow q$ is not an axiom, and the only possible last steps are weakenings from $\Rightarrow q$ or from $p \Rightarrow$.
These two sequents have no cut-free derivations, since their only possible last steps are weakenings from the empty sequent.
So cut is not eliminable in this extension.
This is the connective of [[Prior's tonk|QSVQ1KPNBX]], studied in [[proof-theoretic semantics|~50806e9d]].

### Consequences

- **Consistency.** In LK, every rule except cut has a nonempty conclusion, so the empty sequent $\Rightarrow$ has no cut-free derivation. By part 1 it has no derivation at all, and LK does not derive both $\Rightarrow A$ and $\Rightarrow \neg A$, since ${\neg}$L and a cut would give $\Rightarrow$.
- **Subformula property.** A cut-free derivation contains only subformulas of its end sequent, up to the substitution of terms. See the [[subformula property|~694ac127]].
- **Disjunction property of LJ.** If $\Rightarrow A \vee B$ has a cut-free LJ derivation, then its last step is ${\vee}$R, because the antecedent is empty and the empty sequent has no cut-free derivation. So $\Rightarrow A$ or $\Rightarrow B$ is derivable in LJ.
- **Herbrand's theorem and the midsequent theorem.** The [[midsequent theorem|~f03b8ca3]] refines a cut-free derivation of a prenex sequent, and it gives [[Herbrand's theorem|VZ21F10WRS]].
- **Interpolation.** The [[Craig interpolation theorem|E2CBFNAVZY]] has a proof by induction on a cut-free derivation.

### Converse

The converse, that a cut-free derivation is a derivation, holds by definition.
A stronger converse fails: cut is admissible in cut-free LK, but it is not a derivable rule there.
The example with the initial sequents $\Rightarrow p$ and $p \Rightarrow q$ shows this.
A derivable rule would stay valid after we add initial sequents, and cut does not.

### Generalizations

Cut elimination holds for many other sequent calculi: for linear logic, for the Lambek calculus and for the modal logic S4.
It fails for the usual sequent calculus of the modal logic S5, and [[hypersequent calculi|~908a51bf]] were designed to repair this.
For natural deduction, the corresponding result is the [[normalization theorem|~977456e4]].
The cost of cut elimination is studied in the [[complexity of cut elimination|~29155909]].

### The result is not unique

Cut elimination for LK is not confluent: the cut-free derivation depends on the order of the reduction steps.
Let $D_1$ and $D_2$ be two different cut-free derivations of $\Gamma \Rightarrow \Delta$.
Weaken $D_1$ to $\Gamma \Rightarrow \Delta, A$ and $D_2$ to $A, \Gamma \Rightarrow \Delta$, and cut on $A$.
Both premises end with a weakening on $A$, and a reduction step may keep either side.
So the derivation reduces to $D_1$ and also to $D_2$, followed by structural steps.
So a derivation with cuts has no unique cut-free form, and the question of when two derivations are the same proof is the problem of the [[identity of proofs|~8cb6c275]].

## History

Gerhard Gentzen introduced the calculi LK and LJ and proved the theorem in his paper *Untersuchungen über das logische Schließen*, published in two parts in 1934 and 1935.
He called it the *Hauptsatz*, the main theorem, and proved it with a rule that he called *mix*.
Tait later gave a proof by reduction of the cut rank for one-sided calculi, which also gives the bound of part 3.

## Explanations

### L1 human

The cut rule lets a proof use a lemma: first prove $A$, then use $A$ to prove the goal.
The theorem says that pure logic never needs lemmas.
Every proof can be rewritten so that it only builds up pieces of the final claim, step by step.
For example, a proof of "if $p$ and $q$, then $q$ or $p$" can go through the lemma $q$, and it can also avoid it.
The price is length.
A rewritten proof can be enormously longer than the proof with lemmas.

### L2 human

We remove one cut by hand.
The derivation below proves $p \wedge q \Rightarrow q \vee p$ with a cut on $q$.

1. $q \Rightarrow q$ is an axiom, and ${\wedge}$L gives $p \wedge q \Rightarrow q$.
2. $q \Rightarrow q$ is an axiom, and ${\vee}$R gives $q \Rightarrow q \vee p$.
3. A cut on $q$ gives $p \wedge q \Rightarrow q \vee p$.
4. The cut formula $q$ is atomic, and the left premise ends with ${\wedge}$L. The reduction moves the cut above the ${\wedge}$L step.
5. The cut of $q \Rightarrow q$ with $q \Rightarrow q \vee p$ gives back $q \Rightarrow q \vee p$, so this cut disappears.
6. ${\wedge}$L applied to $q \Rightarrow q \vee p$ gives $p \wedge q \Rightarrow q \vee p$ without cut.

The typical use of the theorem is a proof that something is not derivable: one shows that no cut-free derivation can end with the given sequent.
A trap is to think that the theorem makes proofs shorter.
It does the opposite, and the growth can be a tower of exponentials.

### L3 human

Gentzen's proof is a double induction: on the degree of the cut formula, and on the heights of the derivations above the cut.
The [[first proof|~dac34e15]] follows Gentzen with the mix rule.
The [[second proof|~9c2f7b72]] follows Tait, with a reduction lemma and a bound on the height.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], a cut is a substitution of a program into another, and cut elimination is evaluation.
In categorical semantics a derivation denotes a morphism and a cut denotes a composition, so cut elimination describes composites without composition.
In arithmetic the induction rule blocks full cut elimination, and [[ordinal analysis|C5E5TG8PGP]] measures how far the reduction must go.
