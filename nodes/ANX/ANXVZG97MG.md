---
tag: ANXVZG97MG
kind: proof
name: Proof of the Pi-0-2 conservativity of PA over HA by the A-translation
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
proves: PY679V9MVR
uses: [6CCK0TT69P, WC4TDGEWZR, PAQ4ZX2TX1, RXHJPVMPJH, NCDZ969V7X]
methods: [12MQ2NJ29A, 0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
---

## Proof

We first show that HA proves the A-translation of each of its theorems, and then apply this to the negative translation of the PA proof, with the goal itself as $A$.
We work in [[Heyting arithmetic|RXHJPVMPJH]] with intuitionistic [[natural deduction|PAQ4ZX2TX1]] NJ.
Fix a formula $A$, and let $B \mapsto B^A$ be the [[A-translation|6CCK0TT69P]], which replaces each atomic subformula $P$, including $\bot$, by $P \vee A$.
Renaming bound variables and eigenvariables does not change what a derivation proves, so we assume that no variable free in $A$ is bound in $B$ or used as an eigenvariable.

### Lemmas F0 and F1: substitution and ex falso

1. The free variables of $B^A$ are those of $B$ and those of $A$.
2. If $x$ is not free in $A$, then $(B[t/x])^A = B^A[t/x]$, by induction on $B$, since each clause commutes with [[substitution|NCDZ969V7X]].
3. Lemma F1 says that $A \vdash_i C^A$ for every formula $C$, and we prove it by induction on $C$.
   For atomic $C$, the rule ${\vee}\mathrm{I}$ turns $A$ into $C \vee A = C^A$.
4. For $D \wedge E$, the induction hypothesis gives $D^A$ and $E^A$, and ${\wedge}\mathrm{I}$ combines them.
   For $D \vee E$, it gives $D^A$, and ${\vee}\mathrm{I}$ gives $D^A \vee E^A$.
5. For $D \to E$, it gives $E^A$, and ${\to}\mathrm{I}$ with no discharged leaf gives $D^A \to E^A$.
6. For $\forall x\, D$, it gives $D^A$ from $A$, and $x$ is not free in $A$, so ${\forall}\mathrm{I}$ applies.
   For $\exists x\, D$, it gives $D^A$, and ${\exists}\mathrm{I}$ with the term $x$ gives $\exists x\, D^A$.

### Lemma F2: the logical rules

If NJ derives $B$ from assumptions $\Gamma$, then NJ derives $B^A$ from $\Gamma^A$.
We use induction on the derivation, with one case for its last rule.

1. For the rules of $\wedge$, $\vee$, $\to$, $\forall$ and $\exists$, the translation commutes with the connective or quantifier, so we apply the same rule.
2. For the quantifier rules, Lemma F0 gives $(D[t/x])^A = D^A[t/x]$, because the bound variable $x$ is not free in $A$.
3. The eigenvariable $y$ is not free in $A$, and by Lemma F0 it is free in a translated formula only if it is free in the original.
   So the eigenvariable conditions still hold.
4. For ${\bot}\mathrm{E}$, we have $\bot^A = \bot \vee A$ and need $C^A$, so we use ${\vee}\mathrm{E}$.
   In the case $\bot$, the rule ${\bot}\mathrm{E}$ gives $C^A$, and in the case $A$, Lemma F1 gives $C^A$.
5. For ${=}\mathrm{I}$, the rule ${\vee}\mathrm{I}$ turns $t = t$ into $t = t \vee A$.
6. For ${=}\mathrm{E}$, we have $s = t \vee A$ and $\varphi^A[s/x]$, with $x$ not free in $A$, and we use ${\vee}\mathrm{E}$.
   In the case $s = t$, the rule ${=}\mathrm{E}$ gives $\varphi^A[t/x]$, and in the case $A$, Lemma F1 gives it.

### Lemma F3: the axioms of HA

1. An equation axiom $s = t$, such as $x + 0 = x$, gives $s = t \vee A$ by ${\vee}\mathrm{I}$.
2. For $S x = S y \to x = y$, assume $S x = S y \vee A$.
   In the first case the axiom gives $x = y$, and in both cases ${\vee}\mathrm{I}$ gives $x = y \vee A$.
3. For $S x = 0 \to \bot$, assume $S x = 0 \vee A$.
   In the first case the axiom gives $\bot$, and in both cases ${\vee}\mathrm{I}$ gives $\bot \vee A$.
4. By Lemma F0, the translation of the induction axiom for $\varphi$ is the induction axiom for $\varphi^A$:
   $$\varphi^A(0) \wedge \forall x\, (\varphi^A(x) \to \varphi^A(S x)) \to \forall x\, \varphi^A(x).$$
5. Hence, if $\mathsf{HA} \vdash B$, then $\mathsf{HA} \vdash B^A$.
   We apply Lemma F2 to a derivation from finitely many axioms, and steps 1 to 4 to those axioms.

### Lemmas F4 and F5: decidable formulas

HA proves $\psi \vee \neg \psi$ for every quantifier-free $\psi$, since it proves this for equations and the connectives preserve it.
Lemma F4 says that HA proves $\varphi^A \leftrightarrow \varphi \vee A$ for quantifier-free $\varphi$, by induction on $\varphi$.

1. For atomic $\varphi$, the formula $\varphi^A$ is $\varphi \vee A$.
2. For $\wedge$ and $\vee$, the equivalences $(\psi \vee A) \wedge (\chi \vee A) \leftrightarrow (\psi \wedge \chi) \vee A$ and $(\psi \vee A) \vee (\chi \vee A) \leftrightarrow (\psi \vee \chi) \vee A$ hold in NJ, by cases.
3. For $\psi \to \chi$, by induction $\varphi^A$ is equivalent to $(\psi \vee A) \to (\chi \vee A)$, and $(\psi \to \chi) \vee A$ implies this, by cases on both disjunctions.
4. Conversely, assume $(\psi \vee A) \to (\chi \vee A)$, and use cases on $\psi \vee \neg \psi$.
   If $\neg \psi$, then $\psi \to \chi$ by ${\bot}\mathrm{E}$.
   If $\psi$, the assumption gives $\chi \vee A$, and either $\chi$ gives $\psi \to \chi$ or we have $A$.
5. Lemma F5 says that HA proves $\varphi^N \leftrightarrow \varphi$ for quantifier-free $\varphi$.
   For atoms, HA proves $\neg \neg \varphi \leftrightarrow \varphi$ by cases on $\varphi \vee \neg \varphi$, and the clauses for $\wedge$ and $\to$ commute.
6. For $\psi \vee \chi$, by induction $(\psi \vee \chi)^N$ is equivalent to $\neg (\neg \psi \wedge \neg \chi)$, hence to $\neg \neg (\psi \vee \chi)$ in NJ.
   HA proves $\neg \neg (\psi \vee \chi) \to \psi \vee \chi$, by cases on the decidable formula $\psi \vee \chi$.

### The main argument

Let $\varphi(x, y)$ be quantifier-free, and assume $\mathsf{PA} \vdash \forall x\, \exists y\, \varphi(x, y)$.

1. The rule ${\forall}\mathrm{E}$ gives $\mathsf{PA} \vdash \exists y\, \varphi(x, y)$.
2. The [[Gödel-Gentzen theorem|WC4TDGEWZR]], part 2, gives $\mathsf{HA} \vdash \neg \forall y\, \neg \varphi^N(x, y)$.
   Lemma F5 turns this into $\mathsf{HA} \vdash \forall y\, (\varphi(x, y) \to \bot) \to \bot$.
3. Let $A = \exists y\, \varphi(x, y)$, in which the bound variable $y$ is not free.
   Lemma F3, step 5, gives the translated theorem:
   $$\mathsf{HA} \vdash \forall y\, (\varphi^A(x, y) \to \bot \vee A) \to \bot \vee A.$$
4. We prove the premise.
   Fix $y$ and assume $\varphi^A(x, y)$, so Lemma F4 gives $\varphi(x, y) \vee A$.
5. In the case $\varphi(x, y)$ the rule ${\exists}\mathrm{I}$ gives $A$, so in both cases ${\vee}\mathrm{I}$ gives $\bot \vee A$.
   The rule ${\to}\mathrm{I}$ discharges $\varphi^A(x, y)$, and no open assumption contains $y$, so ${\forall}\mathrm{I}$ gives the premise.
6. The rule ${\to}\mathrm{E}$ with step 3 gives $\bot \vee A$ in HA, and ${\bot}\mathrm{E}$ in the case $\bot$ gives $A$.
   So $\mathsf{HA} \vdash \exists y\, \varphi(x, y)$.
7. No assumption is open, so ${\forall}\mathrm{I}$ gives $\mathsf{HA} \vdash \forall x\, \exists y\, \varphi(x, y)$.

This proves the [[theorem|PY679V9MVR]].

## Idea

The negative translation gives an HA proof of "no $y$ fails to exist", that is, of $\neg \forall y\, \neg \varphi$.
That proof treats $\bot$ as an arbitrary formula, except in the rule of ex falso.
The A-translation replaces $\bot$ by the goal $\exists y\, \varphi$ and repairs ex falso by adding the goal to every atom.
The double negation then reads "if every $y$ gives the goal, then the goal holds", and its premise is provable because $\varphi$ is decidable.

## Variants

A route through a functional interpretation also works.
The [[Dialectica interpretation|HZ17ES9PDY]] of the negative translation gives a term $t$ of [[system T|A4WR995XZP]] with $\varphi(x, t(x))$.
Then $\mathsf{HA}^\omega$ proves $\forall x\, \exists y\, \varphi(x, y)$, and $\mathsf{HA}^\omega$ is conservative over HA.

In minimal logic the negative translation needs no ex falso, and then it suffices to replace only $\bot$ by $A$.
This refined A-translation is the form used in program extraction.
