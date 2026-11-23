---
tag: AYRZ98Y0NW
kind: statement
role: theorem
name: Cut-elimination theorem
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PZX9J3VEMT, W72CA3R9MP, N4EDJNMTEF, DAMGTSY6VV]
about: [W72CA3R9MP, HGVMPZ2DXA]
proofs: [8HV015W88G, Q1799WJA0W]
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

The theorem says that a derivation in pure logic never needs a lemma: every [[cut|DAMGTSY6VV]] can be removed.

Let LK and LJ be Gentzen's [[sequent calculi|PZX9J3VEMT]] for first-order logic, with the cut rule.
The *degree* $|A|$ of a formula $A$ is the number of occurrences of connectives and quantifiers in $A$.
The *cut rank* of a derivation is $0$ if it has no cut, and otherwise the largest value of $|C| + 1$ over its cut formulas $C$.

1. **LK.** If a sequent $\Gamma \Rightarrow \Delta$ has a derivation in LK, then it has a derivation in LK without cut.
2. **LJ.** If a sequent $\Gamma \Rightarrow \Delta$ has a derivation in LJ, then it has a derivation in LJ without cut.
3. **A bound.** Write $\vdash^h_r \Gamma$ when the finite set $\Gamma$ has a derivation of height at most $h$ and cut rank at most $r$ in the one-sided calculus below.
   Then $\vdash^h_r \Gamma$ implies $\vdash^{2_r(h)}_0 \Gamma$.

Here $2_0(h) = h$ and $2_{r+1}(h) = 2^{2_r(h)}$, so $2_r(h)$ is a tower of $r$ twos with $h$ on top.

### The one-sided calculus of part 3

Its formulas are propositional formulas built from literals $p$ and $\neg p$ by $\wedge$ and $\vee$.
For such a formula $A$, the formula $\neg A$ is defined by the de Morgan laws, so $\neg \neg A = A$.
A literal has degree $0$, and $|A_0 \wedge A_1| = |A_0 \vee A_1| = |A_0| + |A_1| + 1$.
Sequents are finite sets of formulas, and $\Gamma, A$ means $\Gamma \cup \{ A \}$.
The axioms and rules are the following.

- Axiom: $\Gamma$, when $p \in \Gamma$ and $\neg p \in \Gamma$ for some propositional variable $p$.
- ${\wedge}$: from $\Gamma, A_0$ and $\Gamma, A_1$ infer $\Gamma$, when $A_0 \wedge A_1 \in \Gamma$.
- ${\vee}$: from $\Gamma, A_i$ for one $i \in \{ 0, 1 \}$ infer $\Gamma$, when $A_0 \vee A_1 \in \Gamma$.
- Cut: from $\Gamma, C$ and $\Gamma, \neg C$ infer $\Gamma$.

## Remarks

### One reduction step, before and after

Here is a derivation of $p \wedge q \Rightarrow q$ with a cut on $q \wedge p$, a formula of degree $1$.
$$\dfrac{\dfrac{\dfrac{q \Rightarrow q}{p \wedge q \Rightarrow q}\,{\wedge}\mathrm{L} \qquad \dfrac{p \Rightarrow p}{p \wedge q \Rightarrow p}\,{\wedge}\mathrm{L}}{p \wedge q \Rightarrow q \wedge p}\,{\wedge}\mathrm{R} \qquad \dfrac{q \Rightarrow q}{q \wedge p \Rightarrow q}\,{\wedge}\mathrm{L}}{p \wedge q \Rightarrow q}\,\mathrm{Cut}$$
The cut formula $q \wedge p$ was just built by ${\wedge}$R on the left and is just taken apart by ${\wedge}$L on the right.
The right side only uses the first conjunct $q$, so we cut the left derivation of $q$ directly against the premise $q \Rightarrow q$.
$$\dfrac{\dfrac{q \Rightarrow q}{p \wedge q \Rightarrow q}\,{\wedge}\mathrm{L} \qquad q \Rightarrow q}{p \wedge q \Rightarrow q}\,\mathrm{Cut}$$
The new cut is on $q$, of degree $0$, so the degree went down.
A cut against an axiom $q \Rightarrow q$ changes nothing, so the second step deletes it and leaves the cut-free derivation, ${\wedge}$L applied to $q \Rightarrow q$.
Notice that the branch for $p$ was thrown away.
Every proof of the theorem repeats these two moves: make the cut formula smaller, or move the cut up past a rule that does not touch it.

### Why the hypotheses are needed: pure logic

The theorem is about pure logic, and it fails once we add initial sequents.
Add $\Rightarrow p$ and $p \Rightarrow q$ to LK, for distinct variables $p$ and $q$, and a cut on $p$ gives $\Rightarrow q$.
Without cut, every formula of a derivation of $\Rightarrow q$ is a subformula of $q$, so the only usable leaves are the axioms $q \Rightarrow q$.
Below such a leaf no rule can empty the antecedent, so $\Rightarrow q$ has no cut-free derivation.
For the same reason the cuts on induction formulas in arithmetic cannot all be removed, and [[Gentzen's consistency proof|QPV0HNP22S]] removes only part of them.

### Why the hypotheses are needed: rules that fit

The rules for each connective must also fit together.
Give a new connective $\mathbin{\mathrm{tonk}}$ a right rule that infers $\Gamma \Rightarrow \Delta, A \mathbin{\mathrm{tonk}} B$ from $\Gamma \Rightarrow \Delta, A$.
Give it a left rule that infers $A \mathbin{\mathrm{tonk}} B, \Gamma \Rightarrow \Delta$ from $B, \Gamma \Rightarrow \Delta$.
From $p \Rightarrow p$ and $q \Rightarrow q$ these rules give $p \Rightarrow p \mathbin{\mathrm{tonk}} q$ and $p \mathbin{\mathrm{tonk}} q \Rightarrow q$, and a cut gives $p \Rightarrow q$.
A cut-free derivation of $p \Rightarrow q$ could contain only $p$ and $q$, so it would use only axioms and structural rules.
Each sequent derived that way from an axiom $A \Rightarrow A$ still has $A$ on both sides, and $p \Rightarrow q$ does not.
So cut is not eliminable here; [[Prior's tonk|QSVQ1KPNBX]] and [[proof-theoretic semantics|K97KZB5R7N]] explain what went wrong.

### What it gives you

Consistency comes first.
Every rule except cut has a nonempty conclusion, so the empty sequent $\Rightarrow$ has no cut-free derivation, and by part 1 no derivation at all.
If LK derived $\Rightarrow A$ and $\Rightarrow \neg A$, then ${\neg}$L would give $\neg A \Rightarrow$, and a cut would give $\Rightarrow$.

A cut-free derivation contains only subformulas of its end sequent, up to substitution of terms, which is the [[subformula property|Z2NXKDK06G]].
In LJ this gives the disjunction property.
In a cut-free derivation of $\Rightarrow A \vee B$ the antecedent is empty and the succedent has one formula.
So the last step is ${\vee}$R or a weakening from the empty sequent, and the empty sequent has no cut-free derivation.
The last step is therefore ${\vee}$R, and LJ derives $\Rightarrow A$ or $\Rightarrow B$.

For prenex sequents, the [[midsequent theorem|1FPWTGE14W]] sharpens cut-free derivations further and yields [[Herbrand's theorem|VZ21F10WRS]].
The [[Craig interpolation theorem|E2CBFNAVZY]] has a proof by induction on a cut-free derivation.

### Admissible, not derivable

The converse, that a cut-free derivation is a derivation, holds by definition.
The interesting point is the kind of rule that cut is.
Cut is *admissible* in cut-free LK: adding it creates no new derivable sequents.
It is not *derivable*: no fixed pattern of other rules imitates it.
The initial sequents $\Rightarrow p$ and $p \Rightarrow q$ above show this, since a derivable rule would stay valid after we add initial sequents, and cut does not.

### Cut-free forms are not unique

Cut elimination for LK is not confluent: the cut-free result depends on the order of the reduction steps.
Let $D_1$ and $D_2$ be two different cut-free derivations of $\Gamma \Rightarrow \Delta$.
Weaken $D_1$ to $\Gamma \Rightarrow \Delta, A$ and $D_2$ to $A, \Gamma \Rightarrow \Delta$, and cut on $A$, then contract.
Both premises of the cut end with a weakening on $A$, and a reduction step may keep either side.
So the derivation reduces to a form of $D_1$ and also to a form of $D_2$.
When two derivations count as the same proof is the problem of the [[identity of proofs|G7B4XWMS7Q]].

### Generalizations

Cut elimination holds for many other sequent calculi, among them those for linear logic, the Lambek calculus and the modal logic S4.
It fails for the usual sequent calculus of the modal logic S5, and [[hypersequent calculi|73J7F0FN4A]] were designed in part to repair this.
For natural deduction the matching result is the [[normalization theorem|W33WAE1XTC]].
The cost of removing cuts is the subject of the [[complexity of cut elimination|B5F5HB4YK7]], and that cost is non-elementary.

## History

Gerhard Gentzen introduced the calculi LK and LJ and proved the theorem in his paper *Untersuchungen über das logische Schließen*, published in two parts in 1934 and 1935.
He called it the *Hauptsatz*, the main theorem, and he proved it with a variant of cut that he called *mix*.
Tait later gave a proof by reduction of the cut rank for one-sided calculi, and that proof also gives the bound of part 3.

## Explanations

### L1 human

The cut rule lets a proof use a lemma: first prove $A$, then use $A$ to prove the goal.
The theorem says that pure logic never needs lemmas.
Every proof can be rewritten so that it only builds up pieces of the final claim, step by step.
For example, a proof of "if $p$ and $q$, then $q$" can go through the lemma "$q$ and $p$", and it can also avoid it.
The price is length, because a rewritten proof can be enormously longer than the proof with lemmas.

### L2 human

We remove one cut by hand, this time a cut on an atom.
The derivation proves $p \wedge q \Rightarrow q \vee p$ in three steps.
First, ${\wedge}$L applied to $q \Rightarrow q$ gives $p \wedge q \Rightarrow q$.
Second, ${\vee}$R applied to $q \Rightarrow q$ gives $q \Rightarrow q \vee p$.
Third, a cut on $q$ gives $p \wedge q \Rightarrow q \vee p$.
The cut formula $q$ is not principal in the left premise, because the last rule there is ${\wedge}$L on $p \wedge q$.
So the reduction moves the cut above that ${\wedge}$L step, where it cuts $q \Rightarrow q$ against $q \Rightarrow q \vee p$.
A cut against an axiom returns the other premise, so the cut disappears, and ${\wedge}$L applied to $q \Rightarrow q \vee p$ ends the cut-free derivation.

The typical use of the theorem is to prove that something is not derivable: one shows that no cut-free derivation can end with the given sequent.
Watch out: the theorem does not make proofs shorter, and the cut-free proof can be longer by a tower of exponentials.

### L3 human

Gentzen's proof is a double induction, on the degree of the cut formula and on the heights of the derivations above the cut.
The [[first proof|8HV015W88G]] follows Gentzen with the mix rule, and the [[second proof|Q1799WJA0W]] follows Tait, with a reduction lemma and a bound on the height.
Under the [[Curry-Howard correspondence|A77FER1Q5H]] a cut is the substitution of one program into another, and cut elimination is evaluation.
In categorical semantics a derivation denotes a morphism and a cut denotes a composition, so cut elimination writes composites without composition.
In arithmetic the induction rule blocks full cut elimination, and [[ordinal analysis|C5E5TG8PGP]] measures how far the reduction must go.
