---
tag: DAMGTSY6VV
kind: definition
name: Cut rule
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
defines: HGVMPZ2DXA
uses: [PZX9J3VEMT, W72CA3R9MP]
sources:
  - url: https://en.wikipedia.org/wiki/Cut_rule
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: The cut rule
---

## Definition

The cut rule joins two sequents that share a formula, one proving it and one assuming it, and drops the shared formula.

We work in a [[sequent calculus|W72CA3R9MP]] whose sequents $\Gamma \Rightarrow \Delta$ have finite lists of formulas as antecedent and succedent.
Let $A$ be a formula, the *cut formula*.
The *context-splitting cut* is the rule
$$\dfrac{\Gamma \Rightarrow \Delta, A \qquad A, \Pi \Rightarrow \Lambda}{\Gamma, \Pi \Rightarrow \Delta, \Lambda}\,\mathrm{Cut}$$
and the *context-sharing cut* is the rule
$$\dfrac{\Gamma \Rightarrow \Delta, A \qquad A, \Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta}\,\mathrm{Cut}$$
where $\Gamma, \Delta, \Pi, \Lambda$ are finite lists of formulas, possibly empty.
In the intuitionistic calculus LJ every succedent has at most one formula, and the context-splitting cut infers $\Gamma, \Pi \Rightarrow C$ from $\Gamma \Rightarrow A$ and $A, \Pi \Rightarrow C$, where $C$ is one formula or nothing.
A derivation is *cut-free* when it contains no instance of a cut rule.
The *degree* of a cut is the number of occurrences of connectives and quantifiers in its cut formula.

## Notation

The calculus LK of the [[definition of the sequent calculus|PZX9J3VEMT]] uses the context-splitting form.
Kleene's calculi G3 use the context-sharing form, with multisets in place of lists.
The two forms are also called multiplicative and additive, after the two kinds of rules in linear logic.
A one-sided calculus writes the cut as: from $\Rightarrow \Gamma, A$ and $\Rightarrow \Delta, \neg A$ infer $\Rightarrow \Gamma, \Delta$.
Gentzen called the rule *Schnitt*, and his rule *mix* deletes every occurrence of the cut formula from both premises at once.

## Remarks

Each part of the definition has a job.
The formula $A$ sits in the succedent of the left premise and in the antecedent of the right premise, because the left premise proves $A$ and the right premise uses it.
If $A$ stands on the same side twice, the rule becomes unsound, as [[the same-side rule|GK0B8HZ8DZ]] shows with a one-row truth table.
The contexts are arbitrary lists, so a cut can carry any side assumptions and any other conclusions along.
The rule puts no condition on $A$, so the cut formula need not be a subformula of anything in the conclusion.

Here is a small instance.
Both $p \Rightarrow p \wedge p$ and $p \wedge p \Rightarrow p$ are derivable in LK, by ${\wedge}$R and by ${\wedge}$L.
With $\Gamma = p$, $A = p \wedge p$, $\Lambda = p$, and $\Delta$ and $\Pi$ empty, the context-splitting cut gives $p \Rightarrow p$.
The cut has degree $1$, and its cut formula does not occur in the conclusion.

In LK with weakening, contraction and exchange, each form of cut is derivable from the other, as [[the comparison of the two forms|2PD8PPKFAQ]] shows.
So LK derives the same sequents with either form.
The concept, its soundness and the reason it can be eliminated are on the [[cut rule|HGVMPZ2DXA]] concept page and in the [[cut-elimination theorem|AYRZ98Y0NW]].

## Explanations

### L1 human

The cut rule is the rule for using a lemma.
One premise proves the lemma $A$, and the other premise uses $A$ as an assumption.
The conclusion keeps the assumptions of both premises and forgets $A$.
For example, "from $p$ we get $q$" and "from $q$ we get $r$" give "from $p$ we get $r$".

### L2 human

We match the cut of $p \Rightarrow p \wedge p$ with $p \wedge p \Rightarrow p$ against the pattern.

1. The left premise has the form $\Gamma \Rightarrow \Delta, A$ with $\Gamma = p$, $\Delta$ empty and $A = p \wedge p$.
2. The right premise has the form $A, \Pi \Rightarrow \Lambda$ with $\Pi$ empty and $\Lambda = p$.
3. The conclusion $\Gamma, \Pi \Rightarrow \Delta, \Lambda$ is $p \Rightarrow p$.

The cut was not needed, since $p \Rightarrow p$ is an axiom.
In pure logic every cut can be removed, and the cut-free derivation can be shorter, as here, or very much longer.
Watch out for the order of the lists in LK: the cut formula must stand at the end of the left succedent and at the front of the right antecedent, so exchanges may be needed first.

### L3 human

Cut is the sequent form of transitivity: if $\Gamma$ entails $A$ and $A$ entails $\Lambda$, then $\Gamma$ entails $\Lambda$.
In categorical semantics a derivation of $A \Rightarrow B$ denotes a morphism, and cut denotes composition.
In linear logic weakening and contraction are missing, so the translation between the two forms breaks down.
The [[cut-elimination theorem|AYRZ98Y0NW]] shows that cut is admissible in LK and LJ, although it is not derivable from the other rules.
