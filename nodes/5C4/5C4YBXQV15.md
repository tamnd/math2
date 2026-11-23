---
tag: 5C4YBXQV15
kind: concept
name: Local predicativity and Buchholz's Ω-rule
msc: ["03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: research
uses: [XAMKAB1BZM, 5VNT564Y2W, 45GQ3KQVT3, E7WEFRMQTB, 8S6CT4TMB7, AYRZ98Y0NW, C72RBH0CDR, QH3ENXFRSV, 0A7KV2WB7A, DBD64TH52D, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: Proof-theoretic ordinals
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Ordinal analysis
---

## Summary

The even numbers form the least set $I$ with $0 \in I$ and with $y + 2 \in I$ whenever $y \in I$.
A theory of [[inductive definitions|5VNT564Y2W]] adds such a set $I$ for every positive arithmetical rule, together with an axiom saying that $I$ is the least set closed under the rule.
That minimality axiom quantifies over all closed sets, $I$ among them, and so the theory is impredicative.
Local predicativity and the Ω-rule are two methods to eliminate cuts from infinitary derivations for such theories.

Both methods use the [[ω-rule|XAMKAB1BZM]] for the numbers and a large ordinal $\Omega$ as a height bound for the derivations that build $I$.
Buchholz's *Ω-rule* derives $\Gamma, \neg(t \in I)$ from a family of premises $\Gamma, \Delta$.
There is one premise for each cut-free derivation of $\Delta, t \in I$ without the Ω-rule, where $\Delta$ is a set of formulas in which $I$ occurs only positively.
Pohlers's method of *local predicativity* replaces $I$ by its stages $I^\alpha$ for $\alpha < \Omega$, each defined from the earlier stages, and so predicative for each fixed $\alpha$.
In both methods, a collapsing lemma turns a derivation of uncountable height into one of countable height $\psi_0(\beta)$, with Buchholz's [[collapsing functions|E7WEFRMQTB]] $\psi_\nu$.
This gives the [[proof-theoretic ordinals|C72RBH0CDR]] of the theories $\mathrm{ID}_\nu$.

## Motivation

For Peano arithmetic, the ω-rule makes induction derivable, and predicative [[cut elimination|AYRZ98Y0NW]] bounds the heights below $\varepsilon_0$.
For $\mathrm{ID}_1$ this is not enough.
The minimality axiom says that $I$ is contained in every set closed under the operator, so it quantifies over a class of sets that contains $I$ itself.
A cut on a formula $t \in I$ cannot be reduced by the predicative method, because the derivation of $t \in I$ may be as long as the inductive definition, and that length can be any recursive ordinal.
The two methods give this formula the rank $\Omega$, above all countable ranks, and they handle the impredicative cuts by a separate step.

## Notation

We fix the system of [[Buchholz's psi functions|E7WEFRMQTB]]: $\Omega_0 = 1$, $\Omega_\nu = \aleph_\nu$ for $\nu \ge 1$, and $\Omega = \Omega_1$.
Let $A(X, x)$ be an $X$-positive arithmetical formula, as in the [[definition of ID|45GQ3KQVT3]], and let $I$ be the [[least fixed point|DBD64TH52D]] of the operator $\Gamma(S) = \{ n : A(S, n) \}$.
The stages are $I^\alpha = \Gamma(I^{<\alpha})$, where $I^{<\alpha} = \bigcup_{\beta < \alpha} I^\beta$.
The stage of $n \in I$ is the least $\alpha$ with $n \in I^\alpha$, and it is a countable ordinal.
We use one-sided sequents: a sequent $\Gamma$ is a finite set of formulas, read as a disjunction.
We write $\vdash^\alpha_\rho \Gamma$ when $\Gamma$ has a derivation of height at most $\alpha$ whose cut formulas have rank below $\rho$.

The literature varies.
Buchholz writes the rule for level $\mu + 1$ as the $\Omega_{\mu+1}$-rule, with one such rule for each level of an iterated definition.
Pohlers works with the stage predicates $t \in I^{<\alpha}$ as formulas of the infinitary language.

## Remarks

### Where the methods apply

For the accessible part of a well-order, the stage of an element is the order type of its predecessors, and in [[the stages of an order of type ω+1|TA0AAMRY00]] the last element enters at stage $\omega$.
[[The Ω-rule derives the minimality axiom|QK8QR0TEQM]] by an induction on the given derivation of $t \in I$, which is the step that the ω-rule cannot do.
For $\mathrm{ID}_1$, the Ω-rule and the collapse $\psi_0$ give the bound $\psi_0(\varepsilon_{\Omega+1})$, the [[Bachmann-Howard ordinal|QH3ENXFRSV]].
For $\mathrm{ID}_\nu$, one $\Omega_{\mu+1}$-rule for each $\mu < \nu$ and the collapses $\psi_\mu$ give $\lvert \mathrm{ID}_\nu \rvert = \psi_0(\varepsilon_{\Omega_\nu + 1}) = \psi_0(\Omega_{\nu+1})$.
For [[Π¹₁-comprehension|QMN8CHHE9Y]], the same machinery for all finite levels gives $\lvert \Pi^1_1\text{-}\mathrm{CA}_0 \rvert = \psi_0(\Omega_\omega)$.

### Where the methods do not apply

[[A non-monotone operator|ED681VEX1B]], given by $A(X, x) = \neg X(x)$, has stages that oscillate and never reach a fixed point.
The condition that fails is that $X$ occurs only positively, so there is no stage hierarchy to work with.

The [[ω-rule|XAMKAB1BZM]] alone is not enough either, since its premises are indexed by the numerals and not by derivations.
The Ω-rule refers to all derivations of $t \in I$, and that is what lets it replace the minimality axiom.

### The steps of the upper bound for ID1

1. Boundedness.
   If $t \in I$ has a cut-free derivation without the Ω-rule of height $\alpha$, then the value of $t$ is in $I^\alpha$.
   The proof is an induction on $\alpha$: the last rule derives $t \in I$ from $A(I, t)$, and the atoms $s \in I$ inside $A(I, t)$ have derivations of smaller heights.
2. Soundness of the Ω-rule for the standard model.
   Each $n \in I$ has a cut-free derivation of $n \in I$ without the Ω-rule, by induction on its stage.
   If all premises of an Ω-rule are true, the premise for this derivation, with $\Delta$ empty, is $\Gamma$, so $\Gamma$ is true.
   So the conclusion $\Gamma, \neg(n \in I)$ is true for every $n$.
3. Embedding.
   Each theorem of $\mathrm{ID}_1$ has a derivation with the ω-rule, the Ω-rule and cuts, of height below $\varepsilon_{\Omega + 1}$ and with cut ranks below $\Omega + \omega$.
   The closure axiom uses the rule that derives $t \in I$ from $A(I, t)$, and the minimality axiom uses the Ω-rule.
4. Predicative cut elimination lowers the cut ranks to $\Omega + 1$, and the heights still stay below $\varepsilon_{\Omega + 1}$.
5. Collapsing, which we cite from Buchholz and Pohlers.
   If $\Gamma$ is $I$-positive and $\vdash^\alpha_{\Omega+1} \Gamma$ with $\alpha < \varepsilon_{\Omega+1}$, then $\Gamma$ has a derivation without the Ω-rule and with countable cut ranks, of a height below $\psi_0(\varepsilon_{\Omega+1})$.
6. Predicative cut elimination removes the countable cuts below the same bound, and boundedness gives $\lvert \mathrm{ID}_1 \rvert \le \psi_0(\varepsilon_{\Omega+1})$.

### Watch out

The ordinal $\Omega$ is not a height of the final derivation.
It bounds the derivations that build $I$, and the collapse removes it before the ordinal is read off.

Predicative cut elimination does not apply to a cut on $t \in I$.
Such a cut has rank $\Omega$, and only the collapsing lemma removes it.

The bound $\psi_0(\varepsilon_{\Omega+1})$ is written in Buchholz's system.
The same ordinal is $\psi(\varepsilon_{\Omega+1})$ in Madore's [[collapsing function|8S6CT4TMB7]], and the two $\psi$ are different functions.

### History

Pohlers developed local predicativity, and Buchholz developed the $\Omega_{\mu+1}$-rule for the theories $\mathrm{ID}_\nu$.
Both methods are presented in Lecture Notes in Mathematics 897 (1981), by Buchholz, Feferman, Pohlers and Sieg.
Buchholz's paper "A simplified version of local predicativity" (1992) introduced operator-controlled derivations, which combine the two methods.
Rathjen used methods of this kind for theories that need recursively Mahlo and $\Pi_3$-reflecting ordinals.

### Try it

In the even-numbers example, what is the stage of $6$?
It is $3$, since $I^k = \{ 0, 2, \ldots, 2k \}$.

Which ordinal does the method give for $\mathrm{ID}_2$?
It gives $\psi_0(\varepsilon_{\Omega_2 + 1})$, which equals $\psi_0(\Omega_3)$, using an $\Omega_1$-rule and an $\Omega_2$-rule.

## Explanations

### L1 human

Some sets are built in stages: first the elements that need nothing, then those that need only the first ones, and so on.
A proof about such a set can use the whole set at once, and that makes the proof hard to analyze.
Local predicativity looks at one stage at a time, because each stage only depends on the earlier stages.
The Ω-rule takes another way: to show that every element of the set has a property, it looks at every possible way to build the element.
Both methods then shrink the very long proofs to proofs of countable length.

### L2 human

Let $A(X, x)$ say "$x = 0$ or $x = y + 2$ for some $y \in X$", so $I$ is the set of even numbers.

1. The stages are $I^0 = \{ 0 \}$, $I^1 = \{ 0, 2 \}$, $I^2 = \{ 0, 2, 4 \}$, and in general $I^k = \{ 0, 2, \ldots, 2k \}$.
2. A cut-free derivation of $4 \in I$ applies the closure rule three times: from $0 = 0$ to $0 \in I$, then to $2 \in I$, then to $4 \in I$.
   Its height is at least $3$, and the stage of $4$ is $2$, which agrees with boundedness.
3. Let $F$ be a formula with $F(0)$ and $F(y) \to F(y + 2)$.
   The Ω-rule premise for this derivation asks for a derivation of $F(4)$.
4. Follow the derivation of step 2 from the top: replace $0 \in I$ by $F(0)$, $2 \in I$ by $F(2)$, $4 \in I$ by $F(4)$, and use the closure of $F$ at each step.
5. Doing this for every derivation of $t \in I$ is the induction that the minimality axiom needs.

The typical use is the analysis of $\mathrm{ID}_1$ and of theories with the same ordinal, such as Kripke-Platek set theory.
The trap is to think that the Ω-rule needs a derivation of every true formula $n \notin I$: it only needs a way to transform each derivation of $n \in I$.

### L3 human

The Ω-rule is an infinitary version of an idea from natural deduction: an assumption $t \in I$ is discharged by showing how to use any proof of it.
Its premises are indexed by derivations of lower level, so it is a rule of second order over the predicative ω-derivations.
A positive arithmetical inductive definition closes at a stage at most $\omega_1^{\mathrm{CK}}$, the least non-recursive ordinal, and in this sense $\Omega$ stands in for $\omega_1^{\mathrm{CK}}$.
Local predicativity keeps the stages as formulas and makes the analysis local to each stage, which is closer to the semantics.
Operator-controlled derivations record, by an operator on sets of ordinals, which ordinals may appear in a derivation.
