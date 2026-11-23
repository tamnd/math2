---
tag: HGJVM49PA4
kind: concept
name: Double-negation translation
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
uses: [Q11N8X99FK, 0XR7A7RSXB, 6KT3BJZ7D1, 0QFT7Z76N5, CK8ZQRN183, QEZR7PZ2DD]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Propositional logic
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: First-order logic
  - url: https://en.wikipedia.org/wiki/Glivenko%27s_theorem
    locator: lead section
  - book: isbn:9781447145578
same_as:
  wikidata: Q5299605
  wikipedia: Double-negation translation
---

## Summary

A double-negation translation rewrites every classical statement as a statement of the form "a failure is impossible", and this weaker form always has an [[intuitionistic|Q11N8X99FK]] proof.
So classical logic sits inside intuitionistic logic, and a classical proof can never reach a contradiction that an intuitionistic proof cannot reach.

The standard case is the excluded middle $p \vee \neg p$, which intuitionistic logic does not prove.
Its Gödel-Gentzen translation is the formula
$$(p \vee \neg p)^N = \neg (\neg \neg \neg p \wedge \neg \neg \neg \neg p),$$
and intuitionistic logic proves it in four steps.

In general, a double-negation translation is a map $A \mapsto A^*$ on the formulas of a first-order language that inserts double [[negations|0XR7A7RSXB]] $\neg \neg$, where $\neg B$ means $B \to \bot$.
It must satisfy two conditions: $A^*$ is classically equivalent to $A$, and for every set of formulas $\Gamma$,
$$\Gamma \vdash_c A \quad \text{if and only if} \quad \Gamma^* \vdash_i A^*.$$
The translations of Kolmogorov, of Gödel and Gentzen, and of Kuroda are the standard ones, and the [[definition|QEZR7PZ2DD]] gives their clauses.

## Motivation

Intuitionistic logic drops the excluded middle, so at first it looks like a weaker and safer logic than classical logic.
Is classical reasoning then a risk that intuitionistic reasoning avoids?
The double-negation translation answers no.
Intuitionistic logic proves $\neg \neg (B \vee \neg B)$ for every $B$, and in the same way it proves a negative form of every classical theorem.

The main use is in arithmetic.
Classical [[Peano arithmetic|0QFT7Z76N5]] proves $A$ exactly when intuitionistic [[Heyting arithmetic|CK8ZQRN183]] proves $A^N$, and $\bot^N = \bot$.
So a contradiction in PA would give a contradiction in HA, and the two theories are equiconsistent.

The translation is also the first step of every method that extracts programs from classical proofs.
[[Friedman's A-translation|6CCK0TT69P]] and the [[Dialectica interpretation|HZ17ES9PDY]] of PA both start from it, and in computer science it is the continuation-passing transform.

## Notation

We write $A^N$ for the Gödel-Gentzen translation, $A^K$ for Kolmogorov's and $A^{Ku}$ for Kuroda's.
Many books call $A^N$ the *negative translation*, and some write $A^g$ or $A^\circ$.
For a set of formulas, $\Gamma^N = \{ B^N : B \in \Gamma \}$.
We write $\vdash_c$ for classical [[natural deduction|6KT3BJZ7D1]] NK and $\vdash_i$ for intuitionistic natural deduction NJ, which is NK without the rule of reductio ad absurdum.
Watch the reading of $\neg$: it is always $B \to \bot$, so $\neg \neg \neg p$ is $((p \to \bot) \to \bot) \to \bot$.

## Remarks

### A first translation

The Gödel-Gentzen clauses put $\neg \neg$ on each atom, keep $\wedge$, $\to$ and $\forall$, and replace $\vee$ and $\exists$ by negative forms.
For $p \vee \neg p$, first translate the two parts:
$$p^N = \neg \neg p, \qquad (\neg p)^N = (p \to \bot)^N = \neg \neg p \to \bot = \neg \neg \neg p.$$
The clause $(B \vee C)^N = \neg (\neg B^N \wedge \neg C^N)$ then gives the formula of the Summary.

To prove it, assume the conjunction $\neg \neg \neg p \wedge \neg \neg \neg \neg p$.
Its second part is $\neg \neg \neg p \to \bot$, and its first part is $\neg \neg \neg p$, so modus ponens gives $\bot$.
Discharging the assumption proves the negation of the conjunction.
Check: only the rules for $\wedge$ and $\to$ were used, and no assumption is left open.
The [[worked derivation|F8789WMFC6]] writes out each step.

### Three translations, one meaning

Kolmogorov puts $\neg \neg$ in front of every subformula, Gödel and Gentzen put it on atoms and rewrite $\vee$ and $\exists$, and Kuroda puts it after each $\forall$ and once in front.
For $\forall x\, (P(x) \vee \neg P(x))$ the three results look quite different, yet NJ proves all three, as [[three translations of one formula|28D8ACKEY0]] checks.
In general $\vdash_i A^K \leftrightarrow A^N$ and $\vdash_i A^N \leftrightarrow A^{Ku}$ for every $A$, so the choice is a matter of convenience.

### What a translated theorem says

Take a $\Pi^0_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$ with $\varphi$ quantifier-free.
In HA the equations are decidable, so its translation is equivalent to
$$\forall x\, \neg \forall y\, \neg \varphi(x, y).$$
This says that no $x$ has all $y$ as counterexamples, but it names no witness $y$.
Friedman's A-translation recovers the witness, and that is the content of the [[Pi-0-2 conservativity of PA over HA|PY679V9MVR]].

For a formula with no $\vee$ and no $\exists$, HA proves $A \leftrightarrow A^N$.
So [[PA proves no new negative formulas|DC1X1S0DJE]] over HA.

### The rules you can use

The [[Gödel-Gentzen translation theorem|WC4TDGEWZR]] gives $\Gamma \vdash_c A$ if and only if $\Gamma^N \vdash_i A^N$, and $\mathsf{PA} \vdash A$ if and only if $\mathsf{HA} \vdash A^N$.
Its main lemma is stability, $\vdash_i \neg \neg A^N \to A^N$, which holds because $A^N$ has no $\vee$ and no $\exists$ and has a negation on each atom.
Stability is what turns the classical rule of reductio into an intuitionistic step, as the [[proof|3WH3N4GY7W]] shows.
For propositional formulas the plain prefix works: [[Glivenko's theorem|B9M3P61ZVA]] says $\vdash_c A$ if and only if $\vdash_i \neg \neg A$.

### What it is not

The identity map is not a double-negation translation, since $p \vee \neg p$ is classically provable but not intuitionistically provable.
The plain prefix $A \mapsto \neg \neg A$ fails in predicate logic: [[a Kripke model|ZV2MWBRN04]] shows that NJ does not prove $\neg \neg \forall x\, (P(x) \vee \neg P(x))$.
Negating only the atoms and keeping $\vee$ also fails, since it sends $p \vee \neg p$ to $\neg \neg p \vee \neg \neg \neg p$.
That formula is equivalent to $\neg \neg p \vee \neg p$, which NJ does not prove.

### Watch out

The most common slip is to read $\mathsf{HA} \vdash A^N$ as a constructive proof of $A$.
Let $T$ be [[Kleene's T predicate|S9DK13K5PS]] and let $A$ be $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$.
HA proves $A^N$, because $A$ is an instance of the excluded middle.
HA does not prove $A$, because a proof would give an algorithm that decides the halting problem.

A second slip is to drop the $\neg \neg$ on atoms in pure logic.
In HA we may drop it, since HA proves $s = t \vee \neg s = t$, but in pure logic $\neg \neg p \to p$ is not provable.

### History

Kolmogorov gave his translation in 1925, and Glivenko proved the propositional result in 1929.
Gödel and Gentzen found the negative translation independently in 1933, and both used it to reduce the consistency of classical arithmetic to that of intuitionistic arithmetic.
Kuroda gave his translation in 1951.

### Try it

First, compute $(\exists x\, P(x))^N$ for an atomic $P$.
The clause for $\exists$ gives $\neg \forall x\, \neg \neg \neg P(x)$, which is equivalent in NJ to $\neg \forall x\, \neg P(x)$.

Second, is $(p \to q)^N$ intuitionistically equivalent to $\neg \neg (p \to q)$?
Yes: $(p \to q)^N = \neg \neg p \to \neg \neg q$, and NJ proves $(\neg \neg p \to \neg \neg q) \leftrightarrow \neg \neg (p \to q)$.

## Explanations

### L1 human

Intuitionistic logic accepts a claim only when it has a direct reason for it.
It does not accept "this program halts or it does not" without knowing which one holds.
It does accept "it is impossible that the program neither halts nor fails to halt".
A double-negation translation rewrites each classical claim in this careful form.
For example, "some number $n$ has property $P$" becomes "it is impossible that no number has property $P$".
Every classical proof then turns into an intuitionistic proof of the careful form, so classical reasoning is no more dangerous than intuitionistic reasoning.

### L2 human

We translate the sentence $A = \forall x\, \exists y\, (x < y)$ of arithmetic and see what HA gets.
The clause for $\exists$ gives
$$(\exists y\, (x < y))^N = \neg \forall y\, \neg (x < y)^N.$$
In HA the atom $x < y$ is decidable, so $(x < y)^N = \neg \neg (x < y)$ is equivalent to $x < y$.
The clause for $\forall$ then gives, up to equivalence in HA,
$$A^N \leftrightarrow \forall x\, \neg \forall y\, \neg (x < y).$$
PA proves $A$, so the translation theorem gives $\mathsf{HA} \vdash A^N$.
Here HA proves $A$ itself as well, with the witness $y = x + 1$, but the translation alone does not find this witness.
This is the typical use and the typical limit: the translation moves a classical result into intuitionistic logic, but the result keeps only its negative content.

### L3 human

In a Heyting algebra the map $a \mapsto \neg \neg a$ is a nucleus, and its fixed points, the regular elements, form a Boolean algebra.
Glivenko's theorem is the logical form of this fact, and the negative translation extends it to quantifiers.
In topos theory the same map is the double-negation topology, whose sheaves form a Boolean topos.
In programming languages the translation is the continuation-passing transform, with $\bot$ as the type of answers.
Replacing $\bot$ by an arbitrary formula gives [[Friedman's A-translation|6CCK0TT69P]], and composing the translation with the [[Dialectica interpretation|HZ17ES9PDY]] gives Gödel's interpretation of PA in [[system T|A4WR995XZP]].
