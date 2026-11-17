---
tag: 0RYYK8PG4S
kind: statement
role: theorem
name: Law of excluded middle
aliases: [excluded-middle, tertium-non-datur]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
about: [0F72FK8EKB, 029JBBF693, 05006AJ7DZ]
uses: [0ZGC7ZESYN, 029JBBF693, 0F72FK8EKB, 05006AJ7DZ, 05RSK4Q657]
formal:
  - system: lean4
    library: mathlib
    decl: Classical.em
    match: exact
history:
  first_stated: "Aristotle discussed the law in the Metaphysics"
  notes: "L. E. J. Brouwer rejected the general use of the law in his intuitionism. Jan Łukasiewicz's three-valued logic of 1920 gives a semantics in which the law is not a tautology."
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_excluded_middle
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 1.2
  - book: isbn:9781108439534
    locator: Section 1.2
same_as:
  wikidata: Q468422
  wikipedia: Law of excluded middle
---

## Statement

Let $p$ be a propositional variable.
In classical propositional logic, the formula
$$p \lor \neg p$$
is a [[tautology|05006AJ7DZ]]: it is true under every valuation.
Here $\neg$ is [[negation|029JBBF693]] and $\lor$ is [[disjunction|0F72FK8EKB]].
By substitution, $\varphi \lor \neg \varphi$ is a tautology for every formula $\varphi$.
In words: for each [[proposition|0ZGC7ZESYN]], the proposition or its negation is true.
The proof is on the page [[proof of the law of excluded middle by a truth table|ZNQN1JW1V3]].

In Lean and Mathlib the law is the theorem `Classical.em`, with the statement `∀ (p : Prop), p ∨ ¬p`.

## Remarks

### Why each hypothesis is needed

The law has no hypotheses on $p$.
It depends on the setting, classical two-valued logic, and close variants of it fail.

1. Two truth values are needed. The truth-table proof uses the [[principle of bivalence|5DYNDW9526]]. In a [[many-valued logic|DWYCKAKXZD]] with a third value U and $\neg \mathrm{U} = \mathrm{U}$, as in Kleene's and Łukasiewicz's three-valued logics, the formula $p \lor \neg p$ takes the value U when $p$ does. So it is not a tautology there.
2. Classical reasoning is needed. In [[intuitionistic logic|Q11N8X99FK]] the formula $p \lor \neg p$ is not provable. The L3 explanation gives a model where it fails.
3. The negation is needed. The disjunction $p \lor q$ of two different variables is not a tautology: it is false in the row $p = \mathrm{F}$, $q = \mathrm{F}$.
4. The disjunction is needed. The formula $p \land \neg p$ is false in both rows, so it is a contradiction, not a tautology.
5. The law does not say which disjunct is true. "[[Goldbach's conjecture|063JNBSMJ0]] is true or Goldbach's conjecture is false" is an instance of the law, but nobody knows which part holds.

### Consequences

1. [[Proof by cases|0WCP0PVET6]] on a proposition. To prove $q$, it is enough to prove $p \to q$ and $\neg p \to q$, because one of $p$ and $\neg p$ is true. In Lean, this is `Or.elim` applied to `Classical.em p`.
2. Double negation elimination. From $\neg\neg p$ we get $p$: in the case $p$ we are done, and in the case $\neg p$ the assumption $\neg\neg p$ gives a contradiction, from which $p$ follows by [[explosion|TTKZGJEEK7]]. This is the basis of [[proof by contradiction|0J0XBKG64S]] and of the [[double negation law|0NFAGWH84K]].
3. Non-constructive existence proofs. There are irrational numbers $a$ and $b$ with $a^b$ rational. If $\sqrt{2}^{\sqrt{2}}$ is rational, take $a = b = \sqrt{2}$. Otherwise take $a = \sqrt{2}^{\sqrt{2}}$ and $b = \sqrt{2}$, so $a^b = \sqrt{2}^2 = 2$. See [[non-constructive existence proof|JZQVJ9XT63]].
4. The second De Morgan law $\neg(p \land q) \to \neg p \lor \neg q$ and the backward direction of [[contraposition|04T1CT7212]] follow from the law, and both fail without it. See [[De Morgan's laws (logic)|09PKJKA6J0]].
5. The negation $\neg(p \lor \neg p)$ is a contradiction. By De Morgan's law it is equivalent to $\neg p \land \neg\neg p$, an instance of $q \land \neg q$, which the [[law of noncontradiction|MP4R7T546Z]] excludes.

### Converse

The law is a single formula, not an implication, so it has no converse in the strict sense.
The related question is whether the law follows from double negation elimination $\neg\neg p \to p$.
For all formulas together, the answer is yes.
The formula $\neg\neg(p \lor \neg p)$ is provable intuitionistically, as in part 3 of the [[natural deduction proof of the double negation law|D3S30V9ZZ2]].
Double negation elimination applied to $p \lor \neg p$ then gives the law.
So over intuitionistic logic, the law of excluded middle for all formulas and double negation elimination for all formulas are equivalent.
For a single formula the answer is no: $\neg\neg\neg q \to \neg q$ is provable intuitionistically, but $\neg q \lor \neg\neg q$ is not.

### Generalizations

1. In a [[Boolean algebra|0XADJKM699]], each element $a$ satisfies $a \lor \neg a = 1$. For sets this is $A \cup A^c = U$, where $A^c$ is the [[complement|0RKF1ZT5JJ]] of $A$ in the universal set $U$.
2. In a [[Heyting algebra|NG943XNQWH]], $a \lor \neg a = 1$ can fail, and the Heyting algebras where it always holds are exactly the Boolean algebras.
3. The [[law of the weak excluded middle|CX032ACTMZ]] $\neg p \lor \neg\neg p$ is a weaker principle. Adding it to intuitionistic logic gives an intermediate logic in which the second De Morgan law holds.
4. For a predicate $P(x)$ on a domain $D$, the law gives $\forall x \, (P(x) \lor \neg P(x))$. For an infinite domain this is the use that Brouwer rejected.

## History

Aristotle discussed the law in the Metaphysics, together with the [[law of noncontradiction|MP4R7T546Z]].
Its Latin name, tertium non datur, means "a third is not given".
Luitzen Egbertus Jan Brouwer rejected the general use of the law, in particular for infinite collections, and this rejection is the starting point of intuitionism.
Jan Łukasiewicz introduced a three-valued logic in 1920, and in its semantics $p \lor \neg p$ is not a tautology.

## Explanations

### L1 human

The law says that there is no third option: a statement is true, or its negation is true.
For example, each whole number is even or it is not even.
The number $7$ is not even, and the number $10$ is even, but no number is neither.
The law does not tell us which of the two options holds.
"There is life on another planet, or there is no life on another planet" is true, although nobody knows which part is true.

### L2 human

We prove that for each integer $n$, the number $n(n + 1)(n + 2)$ is divisible by $3$, with the law as the start of a case split.

1. By the law of excluded middle, $3$ divides $n$, or $3$ does not divide $n$.
2. If $3$ divides $n$, then $3$ divides the product $n(n + 1)(n + 2)$.
3. If $3$ does not divide $n$, then $n$ has remainder $1$ or $2$ on division by $3$.
4. With remainder $2$, the number $n + 1$ is divisible by $3$. With remainder $1$, the number $n + 2$ is divisible by $3$.
5. In each case one factor is divisible by $3$, so the product is divisible by $3$.

The typical use is the first line of a proof by cases or of a proof by contradiction.
A trap is to confuse the law with the claim that each statement can be proved or refuted.
The law says that $p \lor \neg p$ is true, not that we have a proof of $p$ or a proof of $\neg p$.

### L3 human

In intuitionistic logic, by the [[Brouwer–Heyting–Kolmogorov interpretation|7B53ZGXXEQ]], a proof of $p \lor \neg p$ must be a proof of $p$ or a proof of $\neg p$, so the law would decide every statement.
A [[Kripke model|NGHWZ9Y7ZV]] with two worlds $w_0 \le w_1$, where $p$ holds at $w_1$ only, refutes the law at $w_0$.
At $w_0$, the formula $p$ does not hold, and $\neg p$ does not hold either, because $p$ holds at the later world $w_1$.
In the Heyting algebra of open subsets of $\mathbb{R}$, the negation of $U = (0, \infty)$ is the interior of its complement, $(-\infty, 0)$, and $U \cup \neg U = \mathbb{R} \setminus \{0\}$ is not the whole line.

The formula $\neg\neg(p \lor \neg p)$ is provable intuitionistically, so no intuitionistic proof can refute the law.
More generally, the [[double-negation translation|HGJVM49PA4]] embeds classical logic in intuitionistic logic.
In constructive set theory and in topos theory, [[Diaconescu's theorem|6155D300EB]] derives the law from the axiom of choice.
Lean 4 follows this route: `Classical.em` is a theorem, proved from the axiom of choice that Lean assumes, and not a separate axiom.
