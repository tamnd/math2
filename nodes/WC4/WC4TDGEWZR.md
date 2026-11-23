---
tag: WC4TDGEWZR
kind: statement
role: theorem
name: Gödel-Gentzen translation theorem
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
uses: [QEZR7PZ2DD, PAQ4ZX2TX1, Q11N8X99FK, 0QFT7Z76N5, RXHJPVMPJH, VM8TQ70CVJ, ZV2MWBRN04]
about: [HGJVM49PA4, CK8ZQRN183]
proofs: [3WH3N4GY7W]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Results
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Arithmetic
  - book: isbn:9781447145578
history:
  first_stated: "Kurt Gödel and Gerhard Gentzen, 1933"
  notes: "Gödel and Gentzen found the translation independently in 1933 and used it to reduce the consistency of classical arithmetic to that of intuitionistic arithmetic."
---

## Statement

The theorem says that every classical proof becomes an intuitionistic proof once the assumptions and the conclusion are put through the negative translation, and that classical and intuitionistic arithmetic are therefore equally consistent.

Fix a first-order language with equality.
Read $\neg B$ as $B \to \bot$, and let $A \mapsto A^N$ be the Gödel-Gentzen [[negative translation|QEZR7PZ2DD]].
For a set of formulas $\Gamma$, write $\Gamma^N = \{ B^N : B \in \Gamma \}$.
Write $\Gamma \vdash_c A$ when classical [[natural deduction|PAQ4ZX2TX1]] NK derives $A$ with all open assumptions in $\Gamma$.
Write $\Gamma \vdash_i A$ for the same with intuitionistic natural deduction NJ, which is NK without the rule RAA.
Let PA be [[Peano arithmetic|0QFT7Z76N5]] and HA be [[Heyting arithmetic|RXHJPVMPJH]], with the same language and axioms, where PA uses classical logic and HA uses [[intuitionistic logic|Q11N8X99FK]].

**Theorem.**

1. For every set of formulas $\Gamma$ and every formula $A$, $\Gamma \vdash_c A$ if and only if $\Gamma^N \vdash_i A^N$.
2. For every formula $A$ of arithmetic, $\mathsf{PA} \vdash A$ if and only if $\mathsf{HA} \vdash A^N$.
3. PA is [[consistent|VM8TQ70CVJ]] if and only if HA is consistent.

## Remarks

### A first use

PA proves $\forall x\, \forall y\, (x = y \vee \neg x = y)$ by the excluded middle.
Part 2 gives a proof in HA of its translation,
$$\forall x\, \forall y\, \neg (\neg \neg \neg\, x = y \wedge \neg \neg \neg \neg\, x = y).$$
Here HA proves the original sentence as well, by induction on $x$ and $y$.
Now replace the equation by the halting formula $\exists y\, T(x, x, y)$ with Kleene's predicate $T$.
Part 2 still gives HA a proof of the translation, but HA does not prove the original, because that proof would decide the halting problem.

### Why each hypothesis is needed

The assumptions must be translated too.
Let $\Gamma = \{ \forall x\, (P(x) \vee \neg P(x)) \to Q \}$ with a unary predicate $P$ and a sentence $Q$.
Then $\Gamma \vdash_c Q$, but $\Gamma \vdash_i Q^N$ fails.
The [[Kripke model of the prefixed double negation|ZV2MWBRN04]], with $Q$ false at every node, forces $\Gamma$ vacuously and does not force $Q^N = \neg \neg Q$.

The translation must act on every subformula.
Putting $\neg \neg$ only in front of the whole formula fails in predicate logic, by the same Kripke model.

In part 2, HA must prove the translation of every axiom of PA.
It does, because the translation of an induction axiom is again an induction axiom, and the other axioms have no $\vee$ and no $\exists$.
For a classical theory whose axioms have translations that the intuitionistic version cannot prove, part 2 can fail.

### What it gives you

Part 3 follows from $\bot^N = \bot$: a classical derivation of $\bot$ becomes an intuitionistic derivation of $\bot$.
If $A$ has no $\vee$ and no $\exists$, then $\mathsf{HA} \vdash A^N \leftrightarrow A$, so [[PA proves such a formula only if HA does|DC1X1S0DJE]].
For a propositional formula, $\vdash_i A^N \leftrightarrow \neg \neg A$, and this gives Glivenko's theorem.
The theorem is also the first step of [[Friedman's A-translation|6CCK0TT69P]] and of the [[Dialectica interpretation|HZ17ES9PDY]] of PA.

### The converse

Part 1 is already an equivalence.
The direction from right to left holds because $A^N$ and $A$ are classically equivalent, and NJ is a part of NK.
A different converse is false: $\Gamma^N \vdash_i A^N$ does not give $\Gamma \vdash_i A$, since NJ proves $(P \vee \neg P)^N$ but not $P \vee \neg P$.

### Generalizations

The Kolmogorov and Kuroda translations satisfy the same theorem, because they are intuitionistically equivalent to $A^N$.
The theorem holds for arithmetic in all finite types: $\mathsf{PA}^\omega$ proves $A$ if and only if $\mathsf{HA}^\omega$ proves $A^N$.
It holds for any classical theory and its intuitionistic version whenever the intuitionistic version proves the translation of each axiom.
For example, universal axioms qualify when the theory proves $P \vee \neg P$ for every atomic $P$.

## History

Kolmogorov gave a translation of this kind in 1925, and Glivenko proved the propositional case in 1929.
Gödel and Gentzen proved the theorem for arithmetic independently in 1933.
It showed that classical arithmetic is consistent if intuitionistic arithmetic is, which answered the worry that classical reasoning in arithmetic is less safe.
Kuroda gave his variant of the translation in 1951.

## Explanations

### L1 human

The theorem says that a classical proof can always be rewritten as an intuitionistic proof.
The price is a weaker conclusion: "there is a number with property $P$" becomes "it is impossible that no number has property $P$".
For example, classical logic proves "every number is even or not even" in one step.
Intuitionistic logic proves the rewritten claim "it is impossible that some number is neither even nor not even".
So any contradiction that classical reasoning finds would also appear in intuitionistic reasoning.

### L2 human

We use part 3 to compare the two theories.
Suppose a classical derivation of $0 = 1$ from the axioms of PA were found.
Part 2 turns it into an HA proof of $(0 = 1)^N = \neg \neg (0 = 1)$.
HA decides equations, so it proves $\neg \neg (0 = 1) \to 0 = 1$, and hence it proves $0 = 1$.
So HA is inconsistent as soon as PA is.

The typical use is this transfer of consistency from an intuitionistic theory to a classical one.
Watch out: the transfer is of provability of translations, so $\mathsf{HA} \vdash A^N$ is never by itself a constructive proof of $A$.

### L3 human

Classical first-order logic is the $\neg \neg$-part of intuitionistic logic.
Algebraically, the regular elements $a = \neg \neg a$ of a Heyting algebra form a Boolean algebra, and the translation sends formulas to such elements.
In categorical logic this is the inclusion of the double-negation sheaves into a topos.
In proof theory the theorem is the first step of Gödel's [[Dialectica interpretation|HZ17ES9PDY]] of PA and of Spector's interpretation of analysis by [[bar recursion|8CCG6F2FAT]].
The [[no-counterexample interpretation|4BCD1EM542]] of PA also comes out of the Dialectica interpretation of the translation of a prenex formula.
