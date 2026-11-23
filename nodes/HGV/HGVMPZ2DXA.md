---
tag: HGVMPZ2DXA
kind: concept
name: Cut rule
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [W72CA3R9MP, PZX9J3VEMT]
sources:
  - url: https://en.wikipedia.org/wiki/Cut_rule
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: The cut rule
---

## Summary

The cut rule is the rule for using a lemma inside a [[sequent calculus|W72CA3R9MP]] derivation.
If you have derived $p \Rightarrow q$ and $q \Rightarrow r$, one cut on $q$ gives $p \Rightarrow r$, and the middle formula $q$ disappears.
In general the rule takes any formula $A$, the *cut formula*, and has the following form.
$$\dfrac{\Gamma \Rightarrow \Delta, A \qquad A, \Pi \Rightarrow \Lambda}{\Gamma, \Pi \Rightarrow \Delta, \Lambda}\,\mathrm{Cut}$$
This is the context-splitting form.
The context-sharing form infers $\Gamma \Rightarrow \Delta$ from $\Gamma \Rightarrow \Delta, A$ and $A, \Gamma \Rightarrow \Delta$, and the [[definition|DAMGTSY6VV]] states both forms.
Cut is the only rule of Gentzen's calculi in which a premise contains a formula that can be missing from the conclusion.

## Motivation

Mathematical proofs are built from lemmas.
We prove $A$ once, and then we use $A$ as an assumption as often as we like.
A calculus of formal proofs needs a step for this, and in the sequent calculus that step is cut.

Gentzen saw that every other rule of his calculi only builds formulas up: each formula of a premise reappears, perhaps inside a larger formula, in the conclusion.
So a derivation without cut can be read off from its last line, one connective at a time.
This raised the question whether cut is needed at all.
The [[cut-elimination theorem|AYRZ98Y0NW]] answers it: in pure logic every derivable sequent has a derivation without cut.
Most results of structural proof theory, from the [[subformula property|Z2NXKDK06G]] to the [[complexity of cut elimination|B5F5HB4YK7]], come from that one fact.

## Notation

The rule is usually written Cut or (cut).
Gentzen's German name is *Schnitt*, and his variant *mix* removes every occurrence of the cut formula at once.
The cut formula stands on the right of the left premise and on the left of the right premise, and that placement is part of the rule.
In a one-sided calculus the rule infers $\Rightarrow \Gamma, \Delta$ from $\Rightarrow \Gamma, A$ and $\Rightarrow \Delta, \neg A$.
In [[natural deduction|6KT3BJZ7D1]] the matching pattern is an introduction rule directly followed by an elimination rule on the same formula, a detour.

## Remarks

### A cut that chains two implications

Here is cut used as a lemma, worked in full in [[the chaining example|JRMABPKF0E]].
From the axioms $p \Rightarrow p$ and $q \Rightarrow q$, the rule ${\to}$L gives the left premise below.
From $q \Rightarrow q$ and $r \Rightarrow r$, the rule ${\to}$L and one exchange give the right premise.
A cut on $q$ joins them.
$$\dfrac{p \to q, p \Rightarrow q \qquad q, q \to r \Rightarrow r}{p \to q, p, q \to r \Rightarrow r}\,\mathrm{Cut}$$
The left premise proves the lemma $q$, and the right premise uses it.
The conclusion keeps the assumptions of both premises and drops the lemma.
Check: with $\Gamma = p \to q, p$, $\Pi = q \to r$, $\Delta$ empty and $\Lambda = r$, the conclusion is $\Gamma, \Pi \Rightarrow \Delta, \Lambda$.

### Two forms of the same rule

The two forms look different, but in LK each one gives the other, as [[the comparison of the two forms|2PD8PPKFAQ]] shows.
The splitting form gives the sharing form: cut two premises with the same context $\Gamma \Rightarrow \Delta$, get $\Gamma, \Gamma \Rightarrow \Delta, \Delta$, and contract the copies.
The sharing form gives the splitting form: first weaken both premises to the common context $\Gamma, \Pi \Rightarrow \Delta, \Lambda$, then cut.
So the choice of form does not change which sequents LK derives.
It does matter in logics without weakening or contraction, such as linear logic, where this translation is not available and the context-splitting form is the standard cut.

### Why the rule is sound

A sequent $\Gamma \Rightarrow \Delta$ is true under an assignment when some formula of $\Gamma$ is false or some formula of $\Delta$ is true.
Suppose both premises of a cut are true, and every formula of $\Gamma$ and $\Pi$ is true.
If $A$ is false, the left premise forces a true formula in $\Delta$.
If $A$ is true, the right premise forces a true formula in $\Lambda$.
In both cases the conclusion is true, so cut never leads from true premises to a false conclusion.

### What a cut is not

The formula must change sides.
The rule that infers $\Gamma, \Pi \Rightarrow \Delta, \Lambda$ from $\Gamma \Rightarrow \Delta, A$ and $\Pi \Rightarrow \Lambda, A$ is not a cut, and it is unsound.
From $p \Rightarrow p$ and $\Rightarrow \neg p, p$ it gives $p \Rightarrow \neg p$, which is false when $p$ is true; [[the same-side rule|GK0B8HZ8DZ]] works this out.

Contraction also makes a formula occurrence disappear, from $A, A, \Gamma \Rightarrow \Delta$ to $A, \Gamma \Rightarrow \Delta$.
It is not a cut, because it has one premise and one copy of $A$ survives.
The rule ${\to}$L has two premises with active formulas $A$ and $B$, but it builds $A \to B$ from them, so nothing is lost.

### Admissible but not derivable

A rule is *derivable* when each instance can be replaced by a fixed pattern of other rules.
A rule is *admissible* when adding it creates no new derivable sequents.
Cut is admissible in LK by the [[cut-elimination theorem|AYRZ98Y0NW]], but it is not derivable.

To see the difference, add the initial sequents $\Rightarrow p$ and $p \Rightarrow q$.
A cut on $p$ gives $\Rightarrow q$.
Without cut, every formula in a derivation of $\Rightarrow q$ is a subformula of $q$, so the only usable leaves are axioms $q \Rightarrow q$.
No rule then empties the antecedent, so $\Rightarrow q$ has no cut-free derivation.
A derivable rule would survive the new initial sequents, so cut is not derivable.

### Watch out

The first slip is to put the cut formula on the same side of both premises, which gives the unsound rule above.
The second slip is to think that the cut formula must occur in the conclusion.
In the cut of $p \Rightarrow p \wedge p$ with $p \wedge p \Rightarrow p$, the conclusion is $p \Rightarrow p$, and $p \wedge p$ appears nowhere in it.
The third slip is to expect cut elimination to shorten a proof.
It removes lemmas, and the lemma-free proof is usually longer, sometimes by a tower of exponentials.

### History

Gerhard Gentzen introduced the rule as *Schnitt* in his calculi LK and LJ, in the paper *Untersuchungen über das logische Schließen* of 1934 and 1935.
In the same paper he proved that the rule can be removed from every derivation, the *Hauptsatz*.
The English name cut translates *Schnitt*.

### Try it

First, cut $\Rightarrow p \vee q$ with $p \vee q \Rightarrow q \vee p$ and name the conclusion.
The cut formula is $p \vee q$, the contexts $\Gamma$, $\Delta$ and $\Pi$ are empty, and $\Lambda = q \vee p$, so the conclusion is $\Rightarrow q \vee p$.

Second, explain why the cut formula can be any formula, even one with many connectives.
The rule places no condition on $A$, and soundness only uses the truth value of $A$, so any formula works.

## Explanations

### L1 human

A lemma is a small result that we prove first and use later.
The cut rule is the step "we proved the lemma, and from the lemma we get the goal, so we get the goal".
For example, "if it rains, the street is wet" and "if the street is wet, it is slippery" give "if it rains, it is slippery".
The middle claim, "the street is wet", is the cut formula.
It does its job and then drops out of the result.

### L2 human

We cut $p \Rightarrow p \vee q$ with $p \vee q \Rightarrow q \vee p$.
The left premise comes from the axiom $p \Rightarrow p$ by ${\vee}$R.
The right premise comes by ${\vee}$L from $p \Rightarrow q \vee p$ and $q \Rightarrow q \vee p$, each by ${\vee}$R from an axiom.
With cut formula $A = p \vee q$, $\Gamma = p$, $\Lambda = q \vee p$ and $\Delta$, $\Pi$ empty, the cut gives the following.
$$\dfrac{p \Rightarrow p \vee q \qquad p \vee q \Rightarrow q \vee p}{p \Rightarrow q \vee p}\,\mathrm{Cut}$$
The derivation reuses a general fact, that disjunction commutes, at one special point.
A cut-free derivation of $p \Rightarrow q \vee p$ also exists: ${\vee}$R in its second form applied to $p \Rightarrow p$.
It never mentions $p \vee q$, which shows how cut elimination throws lemmas away.

### L3 human

Cut is the sequent form of transitivity of entailment.
In categorical semantics a derivation of $A \Rightarrow B$ denotes a morphism from $A$ to $B$, and cut denotes composition.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], a cut substitutes one program into another, and cut elimination runs the composite program.
In substructural logics the choice between the sharing and the splitting form decides how contexts combine, and so which logic you get.
Different ways of eliminating the same cuts can give different cut-free proofs, and this leads to the problem of the [[identity of proofs|G7B4XWMS7Q]].
