---
tag: 0BB5TPGQ1N
kind: concept
name: Proof by contrapositive
aliases: [proof-by-contraposition]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [04T1CT7212, 0NTF6DMVAP, K930V33BSC]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
same_as:
  wikidata: Q1077442
  wikipedia: Contraposition
---

## Summary

Sometimes an implication is hard to prove forward but easy to prove backward from the failure of its conclusion.
A proof by contrapositive takes that route: to show "if $P$, then $Q$", it shows "if not $Q$, then not $P$", which says exactly the same thing.

Here is the standard case: for every integer $n$, if $n^2$ is even, then $n$ is even.
The hypothesis $n^2 = 2m$ gives no formula for $n$, so we prove the contrapositive, "if $n$ is odd, then $n^2$ is odd".
Let $n$ be odd, so $n = 2k + 1$ for an integer $k$.
Then
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
so $n^2$ is odd.
Every integer is either even or odd, so this proves that an even square has an even root.

In general, a *proof by contrapositive* of an [[implication|0ZNX6DQ3EJ]] $P \Rightarrow Q$ is a [[direct proof|0NTF6DMVAP]] of $\neg Q \Rightarrow \neg P$.
That implication is the [[contrapositive|04T1CT7212]] of the first, and the two are logically equivalent: each is false exactly when $P$ is true and $Q$ is false.

## Motivation

Some hypotheses give little to work with, while the negation of the conclusion gives a formula.
"$n^2$ is even" is such a hypothesis, and "$n$ is odd" is such a negated conclusion.
The method trades the first for the second.
The trade pays off most often when $Q$ is a negative statement, such as "$x$ is irrational", "$x \ne 0$" or "$f$ is not constant", because then $\neg Q$ is a positive statement with an equation in it.

The method is used far beyond parity.
In analysis, "if $a_n$ does not tend to $0$, then $\sum a_n$ diverges" is the contrapositive of "if $\sum a_n$ converges, then $a_n \to 0$", and it is the form in which the divergence test is applied.
The lemma that an even square has an even root returns in the proof that [[$\sqrt{2}$ is irrational|0DZGSDHD92]].

## Notation

For $P \Rightarrow Q$ the contrapositive is $\neg Q \Rightarrow \neg P$.
It is not the [[converse|09A3N7ZN5G]] $Q \Rightarrow P$, and it is not the inverse $\neg P \Rightarrow \neg Q$; neither of those is equivalent to $P \Rightarrow Q$.
For "for all $x$, if $P(x)$ then $Q(x)$", the contrapositive is "for all $x$, if not $Q(x)$ then not $P(x)$", with the quantifier left in front.
A written proof opens with "We prove the contrapositive." and then "Assume not $Q$."
In Lean, the Mathlib tactic `contrapose` turns a goal `P → Q` into `¬Q → ¬P`, `contrapose!` also pushes the negations inward, and the lemma `not_imp_not` states the equivalence.

## Remarks

### Why the two forms are equivalent

Look at the four rows of the truth table.
$P \Rightarrow Q$ is false only in the row with $P$ true and $Q$ false.
$\neg Q \Rightarrow \neg P$ is false only when $\neg Q$ is true and $\neg P$ is false, which is the same row.
So the two implications are true in the same three rows, and a proof of one proves the other; the [[proof by a truth table|SWH5EJP8PS]] writes this out.

One direction is even simpler.
If $P \Rightarrow Q$ holds and $Q$ fails, then $P$ cannot hold, or $Q$ would follow.
That reasoning is valid in intuitionistic logic.
The other direction, from $\neg Q \Rightarrow \neg P$ back to $P \Rightarrow Q$, needs the [[double negation law|0NFAGWH84K]], so it is valid in classical logic only.

### The converse and the inverse

Take "if $n$ is a multiple of $4$, then $n$ is even", which is true.
Its contrapositive "if $n$ is odd, then $n$ is not a multiple of $4$" is also true.
Its converse "if $n$ is even, then $n$ is a multiple of $4$" is false, since $n = 2$ fails.
Its inverse "if $n$ is not a multiple of $4$, then $n$ is even" is false too, since $n = 3$ fails.
The inverse is the contrapositive of the converse, so the inverse and the converse are always equivalent to each other and in general not to the original.
[[Proving the inverse instead of the contrapositive|D0531MQ745]] shows this error in a real proof.

### More examples

When the conclusion is an "or", its negation is an "and", which gives two facts to use at once.
The claim [[if a + b >= 100, then a >= 50 or b >= 50|3ENDPQZA6V]] becomes "if $a < 50$ and $b < 50$, then $a + b < 100$", and adding the two inequalities finishes it.
In the same way, "if $ab$ is even, then $a$ or $b$ is even" becomes "a product of two odd integers is odd".

A known theorem is often applied in contrapositive form.
"Differentiable at $a$ implies continuous at $a$" is used as "not continuous at $a$, so not [[differentiable|0K57YG3BB8]] at $a$", which is how we see at once that a function with a jump has no derivative there.

### Watch out

The first trap is a wrong negation of the conclusion.
The negation of "$a \ge 50$ or $b \ge 50$" is "$a < 50$ and $b < 50$", by [[De Morgan's laws|09PKJKA6J0]], not "$a < 50$ or $b < 50$".
With only one inequality known, the sum cannot be bounded, and the proof stops.
The rules for [[negating mathematical statements|K930V33BSC]] give the correct form each time.

The second trap is to prove the inverse $\neg P \Rightarrow \neg Q$ and call it the contrapositive.
Write out $\neg Q \Rightarrow \neg P$ before you start, and compare it with the claim.

The third is to add a needless contradiction.
If the argument assumes $\neg Q$ and ends with $\neg P$, it is finished; writing "this contradicts $P$" turns a clean contrapositive into a [[proof by contradiction|0J0XBKG64S]] with an extra step.

### Writing it up

Say which method you use in the first line, and state the contrapositive in full.
"We prove the contrapositive: if $n$ is odd, then $n^2$ is odd." tells the reader exactly what the rest of the proof must reach.
Then write a direct proof of that statement, and end with its conclusion, $\neg P$.

### History

The equivalence of an implication with its contrapositive is a law of classical propositional logic, the logic that Frege and Russell made formal.
Arend Heyting's formal system of intuitionistic logic of 1930 keeps only the direction from $P \Rightarrow Q$ to $\neg Q \Rightarrow \neg P$.

### Try it

First, prove that for real $x$, if $x^3 + x \ne 0$, then $x \ne 0$.
The contrapositive is "if $x = 0$, then $x^3 + x = 0$", and substituting $x = 0$ gives $0 + 0 = 0$.

Second, write the contrapositive of "if $f$ is increasing, then $f$ is injective" for a real function $f$.
It is "if $f$ is not injective, then $f$ is not increasing", where "increasing" means $x < y \Rightarrow f(x) < f(y)$; two points $x \ne y$ with $f(x) = f(y)$ break that rule.

## Explanations

### L1 human

"If it rains, then the street is wet" says the same thing as "if the street is dry, then it did not rain".
Both sentences rule out the same situation: rain on a dry street.
So to prove the first sentence, you can prove the second one instead.
In mathematics this helps when the second sentence is easier.
"If $n \times n$ is even, then $n$ is even" is hard to start.
"If $n$ is odd, then $n \times n$ is odd" is easy: $3 \times 3 = 9$, $5 \times 5 = 25$, and the algebra shows it for every odd $n$.

### L2 human

Let us prove that for every integer $n$, if $n^2 - 6n + 5$ is even, then $n$ is odd.
The conclusion "$n$ is odd" is hard to reach from the hypothesis, so we prove the contrapositive: if $n$ is even, then $n^2 - 6n + 5$ is odd.
Assume $n$ is even, so $n = 2k$ for an integer $k$, and compute:
$$n^2 - 6n + 5 = 4k^2 - 12k + 5 = 2(2k^2 - 6k + 2) + 1.$$
The number $2k^2 - 6k + 2$ is an integer, so $n^2 - 6n + 5$ is odd, which proves the contrapositive and so the claim.
Check: $n = 4$ gives $16 - 24 + 5 = -3$, which is odd, and $n = 3$ gives $9 - 18 + 5 = -4$, which is even.
The problem shows the typical use: when the conclusion is "odd", "irrational" or "$\ne 0$", its negation gives a formula to start from.
Watch out: "not odd means even" is a theorem about integers, not a rule of logic, and for real numbers there is no such split.

### L3 human

In intuitionistic logic $\neg Q$ is defined as $Q \to \bot$, and composing a proof of $P \to Q$ with a proof of $Q \to \bot$ gives $(P \to Q) \to (\neg Q \to \neg P)$ with no extra axiom.
The reverse implication is not provable there, which is one reason why constructive mathematics prefers direct proofs of positive statements.
In a cartesian closed category the same step says that $X \mapsto (X \Rightarrow \bot)$ reverses arrows.
The more general method of [[proof by contradiction|0J0XBKG64S]] assumes $P$ and $\neg Q$ together and may reach any contradiction, and the topic [[fallacies and errors in proofs|T6QQ749DM5]] treats the confusion of an implication with its converse and inverse.
