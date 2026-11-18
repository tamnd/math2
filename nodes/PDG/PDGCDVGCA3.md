---
tag: PDGCDVGCA3
kind: example
name: The Barcan formula is derivable in quantified S5
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [9PYDNBA5X4]
uses: [9PYDNBA5X4, D2H3S12V7X, G989VP2NGP, 2QPT4KCM0Q, VC3A2VWXND, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: Converse Barcan formula
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

We derive the [[Barcan formula|9PYDNBA5X4]] $\forall x \square \varphi \to \square \forall x \varphi$ in $\mathsf{QKB}$.
This logic has the classical quantifier rules, the axiom K, the [[necessitation rule|G989VP2NGP]], and the axiom B, $A \to \square \lozenge A$, of the [[Brouwerian modal logic|2QPT4KCM0Q]].
We write $\lozenge A$ for $\neg \square \neg A$.
Then we show that $\mathsf{QS5}$ proves B, so the derivation also works in quantified [[S5|VC3A2VWXND]].

First a rule: if $\vdash A \to B$, then $\vdash \lozenge A \to \lozenge B$.

1. Assume $\vdash A \to B$. Propositional logic gives $\vdash \neg B \to \neg A$.
2. Necessitation gives $\vdash \square (\neg B \to \neg A)$, and K with modus ponens gives $\vdash \square \neg B \to \square \neg A$.
3. Contraposition gives $\vdash \neg \square \neg A \to \neg \square \neg B$, that is, $\vdash \lozenge A \to \lozenge B$.

Second a lemma: $\vdash \lozenge \square A \to A$ in $\mathsf{KB}$.

4. The instance of B with $\neg A$ is $\vdash \neg A \to \square \lozenge \neg A$.
5. $\lozenge \neg A$ is $\neg \square \neg \neg A$. From $\vdash \neg \neg A \leftrightarrow A$, necessitation and K give $\vdash \square \neg \neg A \leftrightarrow \square A$, so $\vdash \lozenge \neg A \to \neg \square A$.
6. Necessitation and K applied to step 5 give $\vdash \square \lozenge \neg A \to \square \neg \square A$.
7. Steps 4 and 6 give $\vdash \neg A \to \square \neg \square A$.
8. $\lozenge \square A$ is $\neg \square \neg \square A$, so step 7 is $\vdash \neg A \to \neg \lozenge \square A$ up to a double negation. Contraposition gives $\vdash \lozenge \square A \to A$.

Now the derivation of BF.

9. $\vdash \forall x \square \varphi \to \square \varphi$, by instantiation of $x$ by itself.
10. $\vdash \lozenge \forall x \square \varphi \to \lozenge \square \varphi$, by the rule of steps 1 to 3 applied to step 9.
11. $\vdash \lozenge \square \varphi \to \varphi$, by the lemma of steps 4 to 8.
12. $\vdash \lozenge \forall x \square \varphi \to \varphi$, from steps 10 and 11.
13. $\vdash \forall x \, (\lozenge \forall x \square \varphi \to \varphi)$, by generalization.
14. $\vdash \lozenge \forall x \square \varphi \to \forall x \varphi$, by the axiom $\forall x (A \to B) \to (A \to \forall x B)$, since $x$ is not free in $\lozenge \forall x \square \varphi$.
15. $\vdash \square \lozenge \forall x \square \varphi \to \square \forall x \varphi$, by necessitation and K applied to step 14.
16. $\vdash \forall x \square \varphi \to \square \lozenge \forall x \square \varphi$, the instance of B with $A = \forall x \square \varphi$.
17. $\vdash \forall x \square \varphi \to \square \forall x \varphi$, from steps 16 and 15.

Last, B is a theorem of $\mathsf{S5}$, which has the axioms T, $\square A \to A$, and 5, $\lozenge A \to \square \lozenge A$, from the [[common modal axiom schemata|FDFQFWPM4X]].

18. The instance of T with $\neg A$ is $\square \neg A \to \neg A$. Contraposition gives $A \to \lozenge A$.
19. Axiom 5 gives $\lozenge A \to \square \lozenge A$.
20. Steps 18 and 19 give $A \to \square \lozenge A$, which is B. So steps 1 to 17 are a derivation in $\mathsf{QS5}$.

## Remarks

The derivation uses B twice: once inside the lemma, and once in step 16.
It does not use T or 4, so BF is a theorem of $\mathsf{QKB}$, which is weaker than $\mathsf{QS5}$.
Semantically, B corresponds to a [[symmetric|061J5VGSPT]] accessibility relation, and on a symmetric frame increasing domains are also decreasing.
In $\mathsf{QS4}$ no such derivation exists: $\mathsf{S4}$ lacks B, and an $\mathsf{S4}$ model with growing domains refutes BF.
The converse Barcan formula needs no modal axiom beyond K; see [[the converse Barcan formula and increasing domains|ZYYTXBXNA2]].

## Explanations

### L1 human

A derivation is a list of formulas, where each line follows from earlier lines by a fixed rule.
Here the rules are those of first-order logic and of the modal logic $\mathsf{S5}$.
The main tool is the axiom "if $A$ is true, then necessarily $A$ is possible".
With it we can move a "necessarily" past a "for all", which is what the Barcan formula does.

### L2 human

We check step 14 in detail, since it is the only step where a side condition matters.

1. The axiom is $\forall x (A \to B) \to (A \to \forall x B)$, with the condition that $x$ is not free in $A$.
2. Here $A$ is $\lozenge \forall x \square \varphi$.
3. Every occurrence of $x$ in $A$ lies inside $\forall x$, so $x$ is not free in $A$.
4. So the instance is allowed, and modus ponens with step 13 gives step 14.

The typical use of the derivation is to show that a logic with B forces constant domains in its models.
A trap: generalization in step 13 is allowed because step 12 is a theorem with no hypotheses; from a hypothesis with $x$ free it would not be allowed.
