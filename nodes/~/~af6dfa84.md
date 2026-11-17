---
tag: ~af6dfa84
kind: concept
name: Local predicativity and Buchholz's Ω-rule
msc: ["03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: research
uses: [~e0034cfd, 5VNT564Y2W, ~cd19a8f1, E7WEFRMQTB, ~766739ea, AYRZ98Y0NW, C72RBH0CDR, ~fcf34cb0, 0A7KV2WB7A, DBD64TH52D, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: Proof-theoretic ordinals
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Ordinal analysis
---

## Summary

Local predicativity and the Ω-rule are two methods to eliminate cuts from infinitary derivations for theories of [[inductive definitions|5VNT564Y2W]], where the inductively defined set $I$ makes the theory impredicative.
Both methods use the [[ω-rule|~e0034cfd]] for the numbers and a large ordinal $\Omega$ as a height bound for the derivations that build $I$.
Buchholz's *Ω-rule* derives $\Gamma, \neg(t \in I)$ from a family of premises $\Gamma, \Delta$, one premise for each cut-free derivation of $\Delta, t \in I$ without the Ω-rule, where $\Delta$ is a set of formulas in which $I$ occurs only positively.
Pohlers's method of *local predicativity* replaces $I$ by its stages $I^\alpha$ for $\alpha < \Omega$, each of which is defined from the earlier stages, and so is predicative for each fixed $\alpha$.
In both methods, a collapsing lemma turns a derivation of height $\alpha$ into a derivation of countable height $\psi_0(\beta)$, with Buchholz's [[collapsing functions|E7WEFRMQTB]] $\psi_\nu$, and this gives the [[proof-theoretic ordinals|C72RBH0CDR]] of the theories $\mathrm{ID}_\nu$.

## Motivation

For Peano arithmetic, the ω-rule makes induction derivable, and predicative [[cut elimination|AYRZ98Y0NW]] bounds the heights below $\varepsilon_0$.
For $\mathrm{ID}_1$ this is not enough.
The minimality axiom says that $I$ is contained in every set closed under the operator, so it quantifies over a class of sets that contains $I$ itself.
A cut on a formula $t \in I$ cannot be reduced by the predicative method, because the derivation of $t \in I$ may be as long as the inductive definition, and that length can be any recursive ordinal.
The two methods give this formula a rank of $\Omega$, above all countable ranks, and they handle the impredicative cuts by a separate step.

## Notation

We fix the system of [[Buchholz's psi functions|E7WEFRMQTB]]: $\Omega_0 = 1$, $\Omega_\nu = \aleph_\nu$ for $\nu \ge 1$, and $\Omega = \Omega_1$.
Let $A(X, x)$ be an $X$-positive arithmetical formula, as in the [[definition of ID|~cd19a8f1]], and let $I$ be the [[least fixed point|DBD64TH52D]] of the operator $\Gamma(S) = \set{n : A(S, n)}$.
The stages are $I^\alpha = \Gamma(I^{<\alpha})$, where $I^{<\alpha} = \bigcup_{\beta < \alpha} I^\beta$.
The stage of $n \in I$ is the least $\alpha$ with $n \in I^\alpha$, and it is a countable ordinal.
We use one-sided sequents: a sequent $\Gamma$ is a finite set of formulas, read as a disjunction.
We write $\vdash^\alpha_\rho \Gamma$ when $\Gamma$ has a derivation of height at most $\alpha$ whose cut formulas have rank below $\rho$.

Variants in the literature:

- Buchholz writes the rule for the level $\mu + 1$ as the $\Omega_{\mu+1}$-rule, and uses one such rule for each level of an iterated definition.
- Pohlers works with the stage predicates $t \in I^{<\alpha}$ as formulas of the infinitary language.
- Rathjen uses an ordinal $\Omega$ and a collapsing function $\psi_\Omega$, which name the same ordinals for $\mathrm{ID}_1$ with different terms.

## Remarks

### Examples

- [[The stages of an order of type ω+1|~a1b984d8]]: for the accessible part of a well-order, the stage of an element is the order type of its predecessors. Here the last element enters at stage $\omega$.
- [[The Ω-rule derives the minimality axiom|~cb57c671]]: an induction on the given derivation of $t \in I$ turns each premise into a derivation of $\Gamma_F, \Delta, F(t)$, where $\Gamma_F$ says that $F$ is not closed. This is the step that the ω-rule cannot do.
- $\mathrm{ID}_1$: the Ω-rule and the collapse $\psi_0$ give the bound $\psi_0(\varepsilon_{\Omega+1})$, the [[Bachmann-Howard ordinal|~fcf34cb0]] (Wikipedia, "Ordinal analysis", section "Table of ordinal analyses").
- $\mathrm{ID}_\nu$: one $\Omega_{\mu+1}$-rule for each $\mu < \nu$, and the collapses $\psi_\mu$ for each level, give $\psi_0(\varepsilon_{\Omega_\nu + 1}) = \psi_0(\Omega_{\nu+1})$ (Wikipedia, "Theories of iterated inductive definitions", section "Proof-theoretic ordinals").
- [[Π¹₁-comprehension|~cbd097d9]]: the same machinery for all finite levels gives the bound $\psi_0(\Omega_\omega)$.

### Non-examples

- [[A non-monotone operator|~6fe446f3]]: for $A(X, x) = \neg X(x)$, the stages oscillate and never reach a fixed point. The condition that fails is that $X$ occurs only positively, so there is no stage hierarchy to work with.
- The [[ω-rule|~e0034cfd]] alone: its premises are indexed by the numerals, not by derivations. The condition that fails is the reference to all derivations of $t \in I$, which is what lets the Ω-rule replace the minimality axiom.

### Basic properties

1. Boundedness. If $t \in I$ has a cut-free derivation without the Ω-rule of height $\alpha$, then the value of $t$ is in $I^\alpha$. The proof is an induction on $\alpha$: the last rule derives $t \in I$ from $A(I, t)$, and the derivations of the atoms $s \in I$ inside $A(I, t)$ have smaller heights.
2. The Ω-rule is sound for the standard model. Let $n \in I$, with stage $\alpha$. By induction on $\alpha$, the formula $n \in I$ has a cut-free derivation without the Ω-rule. Assume that all premises of an Ω-rule are true. The premise for this derivation, with $\Delta$ empty, is $\Gamma$, so $\Gamma$ is true. So the conclusion $\Gamma, \neg(n \in I)$ is true for every $n$.
3. Embedding. Each theorem of $\mathrm{ID}_1$ has a derivation with the ω-rule, the Ω-rule and cuts, of height below $\varepsilon_{\Omega + 1}$ and with cut ranks below $\Omega + \omega$. The closure axiom uses the rule that derives $t \in I$ from $A(I, t)$, and the minimality axiom uses the Ω-rule, by the [[example|~cb57c671]].
4. Collapsing (cited, Buchholz and Pohlers). Let $\Gamma$ be a set of formulas in which $I$ occurs only positively. If $\vdash^\alpha_{\Omega+1} \Gamma$, then $\Gamma$ has a cut-free derivation without the Ω-rule of a height below $\psi_0(\beta)$, for an ordinal $\beta$ computed from $\alpha$.
5. Predicative cut elimination lowers the cut ranks of property 3 to $\Omega + 1$, and the heights stay below $\varepsilon_{\Omega + 1}$. Then property 4 and boundedness give the upper bound $\abs{\mathrm{ID}_1} \le \psi_0(\varepsilon_{\Omega+1})$.

### History

Pohlers developed local predicativity and Buchholz developed the $\Omega_{\mu+1}$-rule for the theories $\mathrm{ID}_\nu$.
Both methods are presented in Lecture Notes in Mathematics 897 (1981), by Buchholz, Feferman, Pohlers and Sieg.
Buchholz's paper "A simplified version of local predicativity" (1992) introduced operator-controlled derivations, which combine the two methods.
Rathjen used methods of this kind for theories that need Mahlo and weakly compact cardinals.

### Common errors

- Treating $\Omega$ as an actual height of the final derivation. It is a bound for the derivations that build $I$, and the collapse removes it before the ordinal is read off.
- Applying predicative cut elimination to a cut on $t \in I$. Such a cut has rank $\Omega$, and only the collapsing lemma removes it.
- Mixing the collapsing systems: the bound $\psi_0(\varepsilon_{\Omega+1})$ is in Buchholz's system, and the same ordinal is $\psi(\varepsilon_{\Omega+1})$ in the system of the [[collapsing function page|~766739ea]].

## Explanations

### L1 human

Some sets are built in stages: first the elements that need nothing, then those that need only the first ones, and so on.
A proof about such a set can use the whole set at once, and that makes the proof hard to analyse.
Local predicativity looks at one stage at a time, because each stage only depends on the earlier stages.
The Ω-rule takes another way: to show that every element of the set has a property, it looks at every possible way to build the element.
Both methods then shrink the very long proofs to proofs of countable length.

### L2 human

Let $A(X, x)$ say "$x = 0$ or $x = y + 2$ for some $y \in X$", so $I$ is the set of even numbers.

1. The stages are $I^0 = \set{0}$, $I^1 = \set{0, 2}$, $I^2 = \set{0, 2, 4}$, and in general $I^k = \set{0, 2, \dots, 2k}$.
2. A cut-free derivation of $4 \in I$ applies the closure rule three times: from $0 = 0$ to $0 \in I$, then to $2 \in I$, then to $4 \in I$. Its height is at least $3$, and the stage of $4$ is $2$, which agrees with boundedness.
3. Let $F$ be a formula with $F(0)$ and $F(y) \to F(y + 2)$. The Ω-rule premise for this derivation asks for a derivation of $F(4)$.
4. Follow the derivation of step 2 from the top: replace $0 \in I$ by $F(0)$, $2 \in I$ by $F(2)$, $4 \in I$ by $F(4)$, and use the closure of $F$ at each step.
5. Doing this for every derivation of $t \in I$ is the induction that the minimality axiom needs.

The typical use is the analysis of $\mathrm{ID}_1$ and of theories with the same ordinal, such as Kripke-Platek set theory.
The trap is to think that the Ω-rule needs a derivation of every true formula $n \notin I$: it only needs a way to transform each derivation of $n \in I$.

### L3 human

The Ω-rule is an infinitary version of an idea from natural deduction: an assumption $t \in I$ is discharged by showing how to use any proof of it.
Its premises are indexed by derivations of lower level, so it is a rule of the second order over the predicative ω-derivations.
The collapse corresponds to the fact that $\Omega$ stands for $\omega_1^{\mathrm{CK}}$, the least non-recursive ordinal: a recursive derivation of a positive statement can only use recursive stages.
Local predicativity keeps the stages as formulas and makes the analysis local to each stage, which is closer to the semantics.
Operator-controlled derivations record the ordinals that may appear by an operator on sets of ordinals.
Methods of this kind were used for the extension to recursively Mahlo and $\Pi_3$-reflecting ordinals.
