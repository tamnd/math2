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

The law of excluded middle says that there is no third option: a statement is true, or its negation is true.
"The number $2^{67} - 1$ is prime, or it is not prime" is true before anyone checks which part holds.

Let $p$ be a propositional variable.
In classical propositional logic the formula
$$p \lor \neg p$$
is a [[tautology|05006AJ7DZ]]: it is true under every valuation.
Here $\neg$ is [[negation|029JBBF693]] and $\lor$ is [[disjunction|0F72FK8EKB]].
By substitution, $\varphi \lor \neg \varphi$ is a tautology for every formula $\varphi$.

In Lean's Mathlib the law is the theorem `Classical.em`, with the statement `∀ (p : Prop), p ∨ ¬p`.
The [[proof by a truth table|ZNQN1JW1V3]] checks the two rows.

## Remarks

### The truth table in two lines

Let $p$ be "$7$ is even".
Then $p$ is F, so $\neg p$ is T, and the disjunction $p \lor \neg p$ is T because its second part is true.
If instead $p$ is "$10$ is even", then $p$ is T and the first part already makes the disjunction T.
A [[proposition|0ZGC7ZESYN]] has only these two possible values, so the law holds in every case:

| $p$ | $\neg p$ | $p \lor \neg p$ |
|---|---|---|
| T | F | T |
| F | T | T |

### What the law depends on

The law has no hypothesis on $p$, but it depends on the setting, and close variants of it fail.
The truth-table proof uses the [[principle of bivalence|5DYNDW9526]].
In a [[many-valued logic|DWYCKAKXZD]] with a third value U and $\neg \mathrm{U} = \mathrm{U}$, as in the three-valued logics of Kleene and of Łukasiewicz, $p \lor \neg p$ takes the value U when $p$ does, so it is not a tautology there.

Both connectives matter too.
The disjunction $p \lor q$ of two different variables is false in the row $p$ F, $q$ F.
The conjunction $p \land \neg p$ is false in both rows, so it is a contradiction, and the [[law of noncontradiction|MP4R7T546Z]] is about its negation.

### Where intuitionistic logic differs

In [[intuitionistic logic|Q11N8X99FK]], $p \lor \neg p$ is not provable.
There a proof of a disjunction must be a proof of one of its parts, so a proof of $p \lor \neg p$ for every $p$ would decide every statement.
The law also does not say which part is true.
"[[Goldbach's conjecture|063JNBSMJ0]] is true or Goldbach's conjecture is false" is a classical instance of the law, and nobody knows which part holds.
The L3 explanation gives a small model in which the law fails.

### What the law gives you

The law is the first line of every [[proof by cases|0WCP0PVET6]] on one proposition: to prove $q$, prove $p \to q$ and $\neg p \to q$.
In Lean this is `Or.elim` applied to `Classical.em p`.

It also gives double negation elimination.
Assume $\neg\neg p$ and split on $p \lor \neg p$.
In the case $p$ we are done, and in the case $\neg p$ the assumption $\neg\neg p$ gives a contradiction, from which $p$ follows by [[explosion|TTKZGJEEK7]].
This is the basis of [[proof by contradiction|0J0XBKG64S]] and of the [[double negation law|0NFAGWH84K]].
The direction $\neg(p \land q) \to \neg p \lor \neg q$ of [[De Morgan's laws|09PKJKA6J0]] and the backward direction of [[contraposition|04T1CT7212]] follow from the law in the same way, and both fail without it.

The law also allows existence proofs that do not name the object.
There are irrational numbers $a$ and $b$ with $a^b$ rational.
If $\sqrt{2}^{\sqrt{2}}$ is rational, take $a = b = \sqrt{2}$.
Otherwise take $a = \sqrt{2}^{\sqrt{2}}$ and $b = \sqrt{2}$, so that $a^b = \sqrt{2}^{2} = 2$.
The proof never says which case holds; see [[non-constructive existence proof|JZQVJ9XT63]].

### The converse question

The law is a single formula, so it has no converse in the strict sense.
The related question is whether it follows from double negation elimination $\neg\neg p \to p$.
For all formulas together, it does.
The formula $\neg\neg(p \lor \neg p)$ is provable intuitionistically, as in the [[natural deduction proof of the double negation law|D3S30V9ZZ2]], and double negation elimination applied to it gives the law.
So over intuitionistic logic, excluded middle for all formulas and double negation elimination for all formulas are equivalent.
For a single formula the answer is no: $\neg\neg\neg q \to \neg q$ is provable intuitionistically, but $\neg q \lor \neg\neg q$ is not.

### Generalizations

In a [[Boolean algebra|0XADJKM699]] every element satisfies $a \lor \neg a = 1$; for sets this is $A \cup A^c = U$, with $A^c$ the [[complement|0RKF1ZT5JJ]] of $A$ in the universal set $U$.
In a [[Heyting algebra|NG943XNQWH]] the equation can fail, and the Heyting algebras where it always holds are exactly the Boolean algebras.
The [[law of the weak excluded middle|CX032ACTMZ]], $\neg p \lor \neg\neg p$, is weaker, and adding it to intuitionistic logic gives an intermediate logic in which $\neg(p \land q) \to \neg p \lor \neg q$ holds.
For a predicate $P(x)$ on a domain $D$, the law gives $\forall x \, (P(x) \lor \neg P(x))$, and for an infinite domain this is the use that Brouwer rejected.

### Watch out

The law is not the claim that every statement can be proved or refuted.
It says that $p \lor \neg p$ is true, not that we hold a proof of $p$ or a proof of $\neg p$.
By Gödel's first incompleteness theorem, each consistent formal theory of arithmetic of the usual kind has a statement that it can neither prove nor refute, and the law still holds for that statement.

### Try it

Is $p \lor \neg q$ a tautology?
No: in the row $p$ F, $q$ T both parts are F.

Write the instance of the law for "$x > 0$", for a real number $x$, without the symbol $\neg$.
It is "$x > 0$ or $x \le 0$".

## History

Aristotle discussed the law in the Metaphysics, together with the law of noncontradiction.
Its Latin name, tertium non datur, means "a third is not given".
Luitzen Egbertus Jan Brouwer rejected the general use of the law, in particular for infinite collections, and this rejection is the starting point of intuitionism.
Jan Łukasiewicz introduced a three-valued logic in 1920, and in its semantics $p \lor \neg p$ is not a tautology.

## Explanations

### L1 human

The law says that there is no third option: a statement is true, or its opposite is true.
Every whole number is even or not even.
The number $7$ is not even and the number $10$ is even, but no number is neither.
The law does not tell you which option holds.
"There is life on another planet, or there is no life on another planet" is true, although nobody knows which part is true.

### L2 human

Here is the law at work as the first line of a proof: for each integer $n$, the number $n(n + 1)(n + 2)$ is divisible by $3$.
By the law, $3$ divides $n$ or $3$ does not divide $n$.
If $3$ divides $n$, it divides the product.
If not, $n$ leaves remainder $1$ or $2$ on division by $3$.
With remainder $2$ the factor $n + 1$ is divisible by $3$, and with remainder $1$ the factor $n + 2$ is.
In every case one factor is divisible by $3$, so the product is.
Check with $n = 4$: the product is $4 \cdot 5 \cdot 6 = 120 = 3 \cdot 40$.
Proofs by cases and proofs by contradiction start this way, with an instance of the law.

### L3 human

By the [[Brouwer-Heyting-Kolmogorov interpretation|7B53ZGXXEQ]], a proof of $p \lor \neg p$ must be a proof of $p$ or a proof of $\neg p$.
A [[Kripke model|NGHWZ9Y7ZV]] with two worlds $w_0 \le w_1$, where $p$ holds at $w_1$ only, refutes the law at $w_0$.
At $w_0$ the formula $p$ does not hold, and $\neg p$ does not hold either, because $p$ holds at the later world $w_1$.
In the Heyting algebra of open subsets of $\mathbb{R}$, the negation of $U = (0, \infty)$ is the interior of its complement, $(-\infty, 0)$, and $U \cup \neg U = \mathbb{R} \setminus \{0\}$ is not the whole line.

The formula $\neg\neg(p \lor \neg p)$ is provable intuitionistically, so no intuitionistic proof can refute the law.
More generally, the [[double-negation translation|HGJVM49PA4]] embeds classical logic in intuitionistic logic.
In constructive set theory and in topos theory, [[Diaconescu's theorem|6155D300EB]] derives the law from the axiom of choice.
Lean 4 follows this route: `Classical.em` is a theorem proved from the axiom of choice that Lean assumes, not a separate axiom.
