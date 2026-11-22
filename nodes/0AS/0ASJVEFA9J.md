---
tag: 0ASJVEFA9J
kind: concept
name: Mathematical induction
aliases: [principle-of-mathematical-induction, proof-by-induction]
msc: ["00A35", "03F30"]
topics: [G9JFJGY4TQ, EEH2F76CYQ]
audience: school
specializes: [0B94TKFQJX]
uses: [0MWKJ44V5A, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: History
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Variants
  - book: isbn:9781108439534
    locator: Chapter 6
same_as:
  wikidata: Q178377
  wikipedia: Mathematical induction
---

## Summary

Mathematical induction proves infinitely many statements with one finite argument.
It proves that a property $P(n)$ holds for every [[natural number|0MWKJ44V5A]] $n \ge n_0$, where $n_0$ is a fixed natural number.
The proof has two parts.
The base case proves $P(n_0)$.
The induction step proves, for an arbitrary $n \ge n_0$, that $P(n)$ implies $P(n + 1)$.
In the step, the assumption $P(n)$ is the induction hypothesis.
When both parts are proved, $P(n)$ holds for every $n \ge n_0$.
Most facts about sums, recursive definitions and finite structures are proved in this way.

## Motivation

Many statements speak about all natural numbers at once, such as $1 + 3 + \dots + (2n - 1) = n^2$, or "$3$ divides $n^3 - n$".
We can check such a statement for $n = 1$ to $1000$, but no list of checks covers all $n$.
A [[direct proof|0NTF6DMVAP]] for an arbitrary $n$ is sometimes hard to find.
But often the case $n + 1$ is easy to reach from the case $n$.
The sum of the first $n + 1$ odd numbers is the sum of the first $n$ odd numbers plus one more term.
Induction turns this link between neighboring cases into a proof for all cases.

The reason is a fact about the natural numbers themselves.
They are exactly the numbers that we reach from $0$ by adding $1$ again and again.
Induction states this fact as a rule of proof.

## Notation

The property is written $P(n)$, $S(n)$ or $S_n$, and $n$ is the induction variable.
Books start at $n_0 = 0$ or at $n_0 = 1$, because they differ on whether $0$ is a natural number, so a proof must state its base case.
Some books write the step as "$P(k) \Rightarrow P(k + 1)$" with a new letter $k$.
Others write "$P(n - 1) \Rightarrow P(n)$ for $n \ge n_0 + 1$", which says the same thing.
Lecture notes often shorten "induction hypothesis" to IH.
The names "ordinary", "weak" and "simple" induction all mean the method here, and [[strong induction|0KMVFSHFGZ]] is a different form.

## Remarks

### A first proof by induction

Here is a short theorem that the method proves: for every $n \ge 1$, the [[sum of the first $n$ odd numbers|QSWRESJAZ4]] is $n^2$.
Let $P(n)$ be the statement $1 + 3 + \dots + (2n - 1) = n^2$.
The base case is $n = 1$, where the sum is $1$ and $1^2 = 1$.
For the step, let $n \ge 1$ be arbitrary and assume $P(n)$.
The next odd number after $2n - 1$ is $2n + 1$.
So the sum of the first $n + 1$ odd numbers is $n^2 + (2n + 1)$, by the induction hypothesis.
That equals $(n + 1)^2$, which is the statement $P(n + 1)$.
By induction, $P(n)$ holds for every $n \ge 1$.
Check: $1 + 3 + 5 + 7 = 16 = 4^2$.

Every proof by induction has this shape.
State $P(n)$ and the range $n \ge n_0$, prove $P(n_0)$, then assume $P(n)$ for one arbitrary $n \ge n_0$ and derive $P(n + 1)$.
The step is one argument that works for every $n \ge n_0$, and it must use the hypothesis $P(n)$ somewhere.

### Why the method is valid

For $n_0 = 0$ the method is the induction axiom of the [[Peano axioms|0QFT7Z76N5]].
The axiom says that a set of natural numbers that contains $0$, and contains $n + 1$ whenever it contains $n$, is all of $\mathbb{N}$.
We apply it to the set $A = \{n \in \mathbb{N} : P(n)\}$.
The base case gives $0 \in A$, the step gives $n + 1 \in A$ whenever $n \in A$, so $A = \mathbb{N}$.
For a base $n_0 > 0$, the property $Q(k) = P(n_0 + k)$ reduces the proof to the base $0$, as [[induction from an arbitrary base case|0GF6AJEBZ0]] shows.

The method is equivalent to the [[well-ordering principle|01BX15HSRR]], which says that each nonempty set of natural numbers has a least element.
The equivalence holds over $\mathbb{N}$ and uses the other Peano axioms, among them the fact that each nonzero natural number is a successor.
The [[equivalence of induction and well-ordering|J2P9FWBP3Q]] states the exact base theory.

Induction is deductive reasoning, so its conclusion is certain.
It is not the [[inductive reasoning|5V35SGEN1T]] of the sciences, which guesses a general law from many cases.

### When to choose it

Choose induction when the case $n + 1$ contains the case $n$ as a part.
Sums are the clearest kind, as in the first proof above.
Divisibility is another: [[$3$ divides $n^3 - n$|7RZDHDFSPT]], because $(n + 1)^3 - (n + 1) = (n^3 - n) + 3n^2 + 3n$.
In [[Bernoulli's inequality|0M1MX28VXK]], $(1 + x)^n \ge 1 + nx$ for $x \ge -1$, the step multiplies both sides by $1 + x \ge 0$.
A structure of size $n + 1$ often splits into structures of size $n$.
The [[L-tromino tiling of a $2^n \times 2^n$ board with one square removed|EXRJ0JF2Q3]] cuts the board into four boards of side $2^n$, for any position of the missing square.

The base case need not be $0$ or $1$.
The inequality [[$2^n > n^2$|ST5ZESV7ZR]] holds for $n = 0, 1$ and for $n \ge 5$, and fails for $n = 2, 3, 4$, with equality at $2$ and $4$.
Its step works for every $n \ge 3$, but the base must be $n_0 = 5$, where $32 > 25$.

If the case $n$ needs a case far below $n - 1$, choose [[strong induction|0KMVFSHFGZ]].
If the hypothesis $P(n)$ is too weak to give $P(n + 1)$, prove a stronger property instead, as in [[strengthening the induction hypothesis|F94KJC2RXP]].

### How it fails

A proof by induction fails when one of its parts is missing or wrong.
A [[check of $n^2 + n + 41$ for $n = 0$ to $39$|Q54K0J3PZ4]] finds a prime each time, but it has no step.
The claim fails at $n = 40$, where the value is $1681 = 41^2$.

A step with no base case proves nothing.
The step "$n = n + 1$ implies $n + 1 = n + 2$" is valid, and the claim is false for every $n$.
The [[false claim that $n^2 + n$ is odd|TYDB4F6J2F]] also has a correct step, because $(n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1)$, and no true base case.

A step that works for most $n$ but not for all $n \ge n_0$ also fails.
The argument that [[all horses are the same color|AJ2FDJJGTH]] has a true base case, and its step fails at the step from $1$ to $2$.
Two horses give two groups of one horse, and these groups have no horse in common.
More errors of this kind are in [[errors in induction proofs|V52HDTMPV5]].

### Other forms and Lean names

Induction has many forms, and each one changes the base, the order or the objects.
[[Induction on the integers|0HBS1F00DN]] uses a base at $0$ and two steps, $n \mapsto n + 1$ and $n \mapsto n - 1$, to cover all of $\mathbb{Z}$.
[[Double induction|AABX4YPKRR]] runs on two variables, [[forward-backward induction|QC9FKGZH1V]] goes up to infinitely many cases and then fills the gaps going down, and [[structural induction|12MQ2NJ29A]] runs over lists, trees and formulas.
[[Infinite descent|0EFYCFHYFG]] and the [[minimal counterexample|JGRCNPKNGG]] method use the same principle in the contrapositive form.

In Lean 4 the tactic `induction n with` splits a goal about a natural number `n` into the cases `zero` and `succ`.
The term form is the recursor `Nat.rec`.
Mathlib states induction from a base $m$ as `Nat.le_induction`.

### Watch out

Do not assume $P(n + 1)$ in the step and then derive a true statement from it.
That shows only that $P(n + 1)$ implies something true, which proves nothing about $P(n + 1)$.
The step must start from $P(n)$ and end at $P(n + 1)$.

Do not assume "$P(n)$ for all $n$" as the hypothesis.
That is the claim itself, and the proof becomes circular.
The hypothesis is $P(n)$ for one arbitrary $n$.

Induction proves a formula, but it does not find it.
The formula $n^2$ for the sum of odd numbers comes from a look at small cases, and induction then confirms it.

### History

Francesco Maurolico used the method in 1575 to prove that the sum of the first $n$ odd numbers is $n^2$.
Blaise Pascal gave an explicit form of the method in his *Traité du triangle arithmétique* (1665).
Earlier implicit uses go back to al-Karaji, around the year 1000, and to Gersonides.
The modern formal treatment came in the 19th century, with Boole, De Morgan, Peirce, Dedekind and Peano.

### Try it

First, prove that $2^n \ge n + 1$ for every $n \ge 0$.
The base case is $2^0 = 1 \ge 1$.
If $2^n \ge n + 1$, then $2^{n + 1} = 2 \cdot 2^n \ge 2n + 2 \ge n + 2$.

Second, find the error in this argument: "if $n^2 + n$ is odd, then $(n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1)$ is odd too, so $n^2 + n$ is always odd".
The step is correct, but there is no base case, and the base fails, because $0^2 + 0 = 0$ is even.
In fact $n^2 + n = n(n + 1)$ is always even.

## Explanations

### L1 human

Think of a line of dominoes that never ends.
If the first domino falls, and each falling domino knocks over the next one, then every domino falls.
The base case is the push on the first domino.
The induction step is the rule that each domino knocks over the next one.
For example, $1 = 1^2$, $1 + 3 = 2^2$ and $1 + 3 + 5 = 3^2$.
Each time we add the next odd number, a square of dots grows by one row and one column, so the pattern goes on forever.

### L2 human

We prove that $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$ for every $n \ge 1$.
Let $P(n)$ be this statement.
For the base case $n = 1$, the left side is $1$ and the right side is $\frac{1 \cdot 2}{2} = 1$, so $P(1)$ holds.
For the step, let $n \ge 1$ be arbitrary and assume $P(n)$.
By the induction hypothesis, $1 + 2 + \dots + n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1)$.
The right side is $\frac{n(n + 1) + 2(n + 1)}{2} = \frac{(n + 1)(n + 2)}{2}$, which is the right side of $P(n + 1)$.
So $P(n)$ implies $P(n + 1)$ for every $n \ge 1$, and by induction $P(n)$ holds for every $n \ge 1$.
Check: $1 + 2 + 3 + 4 = 10 = \frac{4 \cdot 5}{2}$.

The same pattern fits a formula for a sum, a bound for a recursive sequence, or a property of a structure with $n$ elements.
Watch out: write $P(n)$ in full before you start, because a vague $P(n)$ hides what the step must prove.

### L3 human

Induction says that $\mathbb{N}$ is the smallest set that contains $0$ and is closed under the successor map.
In the language of categories, $(\mathbb{N}, 0, S)$ is the [[initial algebra|R76EC56V9R]] of the functor $X \mapsto 1 + X$, and induction says that it has no proper subalgebra.
The same idea gives [[structural induction|12MQ2NJ29A]] over any inductive type, and well-founded induction over any [[well-founded relation|0DQPNJNPYK]].
In set theory the method extends to transfinite induction over the ordinals.
In type theory each inductive type comes with its own induction principle, and for $\mathbb{N}$ this principle is the recursor.
In first-order arithmetic, induction is an axiom schema, and the schema restricted to classes of formulas gives the fragments of Peano arithmetic, whose strengths are compared in proof theory.
