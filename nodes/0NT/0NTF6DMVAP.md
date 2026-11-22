---
tag: 0NTF6DMVAP
kind: concept
name: Direct proof
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0ZNX6DQ3EJ, FA6YZGR2SS]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_proof
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.1
same_as:
  wikidata: Q3240280
  wikipedia: Direct proof
inventory: [33MF2VWC2Q]
---

## Summary

A direct proof starts from what you are given and walks forward, one justified step at a time, until it reaches what you want.
It is the plainest [[proof method|G9JFJGY4TQ]], and most of the other methods end by handing you a direct proof to write.

Here is a small one: if $a$ and $b$ are odd integers, then $a + b$ is even.
Write $a = 2k + 1$ and $b = 2l + 1$ with integers $k$ and $l$, as the definition of odd allows.
Then
$$a + b = 2k + 2l + 2 = 2(k + l + 1),$$
and $k + l + 1$ is an integer, so $a + b$ is even.

In general, a *direct proof* of an [[implication|0ZNX6DQ3EJ]] "if $P$, then $Q$" assumes the hypothesis $P$ and derives the conclusion $Q$ by a finite chain of steps.
Each step is an axiom, a definition, an earlier theorem, the assumption $P$, or a valid inference from earlier steps.
The proof never assumes $Q$, and it never assumes the negation of $Q$.
A direct proof of a statement $Q$ with no hypothesis is the same kind of chain, started from axioms and known results.

## Motivation

A [[conditional statement|FA6YZGR2SS]] "if $P$, then $Q$" is false in exactly one situation: $P$ is true and $Q$ is false.
So to prove it, you must rule out that one situation.
The most natural way is to take any situation in which $P$ holds and show that $Q$ holds there as well.
That is all a direct proof does.

The method also fits the way definitions work.
A hypothesis such as "$a$ is odd" or "$a$ divides $b$" contains a defined word, and the definition turns it into an equation that you can compute with.
The conclusion contains a defined word too, so the proof ends when the computation produces the form that the definition of the conclusion asks for.
Proofs about parity, divisibility, set inclusion and continuity nearly all begin this way.

## Notation

There is no special symbol for a direct proof.
Books open with "Assume $P$." or "Suppose $P$." and close with "Hence $Q$." or "Therefore $Q$."
Some books call the method *forward reasoning*.
In the proof assistant Lean, the tactic `intro h` starts a direct proof of a goal `P → Q`: it adds the hypothesis `h : P` and leaves the goal `Q`.

## Remarks

### Why the method is valid

The truth table of "if $P$, then $Q$" has four rows, and only the row with $P$ true and $Q$ false makes the implication false.
A direct proof shows that every row with $P$ true also has $Q$ true, so the bad row cannot occur.
The rows with $P$ false need no work, because the implication is true there whatever $Q$ is.

In the language of logic, the step from "under the assumption $P$ we derived $Q$" to "$P$ implies $Q$" is the rule of implication introduction.
It needs neither the [[law of excluded middle|0RYYK8PG4S]] nor the [[double negation law|0NFAGWH84K]], so a direct proof is valid in intuitionistic logic as well as in classical logic, unless one of its steps quotes those laws.

Direct proofs also chain together.
From a direct proof of $P \Rightarrow Q$ and one of $Q \Rightarrow R$, you write the two chains one after the other and get a direct proof of $P \Rightarrow R$.

### Unfold, compute, fold

Most short direct proofs have three moves.
You unfold each defined word of the hypothesis into an equation, you compute, and you fold the result back into the defined word of the conclusion.
Take [[transitivity of divisibility|JZ6667K6YD]]: if $a \mid b$ and $b \mid c$, then $a \mid c$.
Unfold: $b = ak$ and $c = bl$ for integers $k$ and $l$.
Compute:
$$c = bl = (ak)l = a(kl).$$
Fold: $kl$ is an integer, so $a \mid c$ by the definition of divisibility.
Check with numbers: $3 \mid 12$ and $12 \mid 60$ give $k = 4$, $l = 5$ and $60 = 3 \cdot 20$.

The same three moves show that [[the square of an odd integer is odd|E330HD4J2D]], since $(2k + 1)^2 = 2(2k^2 + 2k) + 1$, and that [[the sum of two even integers is even|5M5Q062R1X]].
They work outside number theory too.
In a [[group|28PKCPYA2V]], if $e$ and $e'$ are both identity elements, then $e = ee' = e'$, where the first equality uses that $e'$ is an identity and the second uses that $e$ is one.
That two-step chain is a direct proof of the [[uniqueness of the identity element|GDBV09GFYB]].

### When to choose it

Try a direct proof first whenever the hypothesis gives you something concrete to compute with.
"If $x > 1$, then $x^2 > x$" is a good case: multiply both sides of $x > 1$ by the positive number $x$.
A direct proof is a poor choice when the hypothesis is weak or negative and the conclusion is strong.
"If $n^2$ is even, then $n$ is even" is an example: $n^2 = 2m$ gives no formula for $n$.
The [[contrapositive|0BB5TPGQ1N]] "if $n$ is odd, then $n^2$ is odd" turns it into the easy direct proof above.
When the conclusion is a negative statement, such as "$\sqrt{2}$ is not rational", the usual tool is [[proof by contradiction|0J0XBKG64S]], as in the [[proof by lowest terms|7GNMP4Q32W]].

### What is not a direct proof

A chain that starts from the conclusion is not a direct proof.
In [[an argument that starts from a^2 + b^2 >= 2ab|2VA8Q8BG5Y]], a student begins with the inequality to be proved and reaches $(a - b)^2 \ge 0$.
That shows only that the goal implies a true statement, and every statement, true or false, implies a true statement.
A proof by contrapositive is also not a direct proof of $P \Rightarrow Q$.
It is a direct proof of the different implication $\neg Q \Rightarrow \neg P$, which happens to be equivalent.

### Watch out

The first trap is to prove one case.
"Take $n = 3$; then $n^2 = 9$ is odd" proves the statement for $3$ only.
The proof must work with $n = 2k + 1$ for an arbitrary integer $k$.

The second trap is to reuse a letter.
If $m$ and $n$ are even and you write $m = 2k$ and $n = 2k$, you have assumed $m = n$.
With $m = 2$ and $n = 4$ that assumption is false, so the proof covers only equal pairs.
Two even integers need two letters, $m = 2k$ and $n = 2l$.

The third trap is to stop one step early.
"$ab = 4kl + 2k + 2l + 1$" does not yet say that $ab$ is odd, because the definition asks for the form $2m + 1$ with $m$ an integer.

### Writing it up

State the hypotheses in the first line ("Let $a$ and $b$ be odd integers.").
Introduce every new letter with its quantifier ("so $a = 2k + 1$ for some integer $k$").
Give each step its reason, and end with a sentence that repeats the conclusion in the words of the statement ("Therefore $a + b$ is even.").
A reader should be able to check each line without looking ahead.

### History

Most propositions in [[Euclid's Elements|83WHDAV68J]] are proved by chains of steps from the postulates and from earlier propositions, and many of these chains are direct proofs.
The name "direct proof" contrasts the method with indirect proof, the proof by contradiction, which the Greek geometers also used.

### Try it

First, prove that if $n$ is an integer with $3 \mid n$, then $9 \mid n^2$.
Write $n = 3k$; then $n^2 = 9k^2$, and $k^2$ is an integer, so $9 \mid n^2$.

Second, prove that if $x$ and $y$ are real numbers with $0 < x < y$, then $x^2 < y^2$.
Multiply $x < y$ by $x > 0$ to get $x^2 < xy$, and multiply $x < y$ by $y > 0$ to get $xy < y^2$; together they give $x^2 < y^2$.

## Explanations

### L1 human

A direct proof starts from what is given and walks step by step to what is wanted.
Each step needs a reason, such as a rule of algebra or the meaning of a word.
Take the claim "if a number is odd, then its square is odd".
An odd number is one more than an even number, for example $7 = 6 + 1$.
Then $7 \cdot 7 = 49 = 48 + 1$, and $48$ is even, so $49$ is odd.
A direct proof does the same computation with a letter in place of $7$, so that it covers every odd number at once.

### L2 human

Let us prove that the product of two odd integers is odd, and watch each move.
Assume $a$ and $b$ are odd, so $a = 2k + 1$ and $b = 2l + 1$ for integers $k$ and $l$.
We use two letters, because $a$ and $b$ can be different numbers.
Multiply and collect the terms that carry a factor $2$:
$$ab = (2k + 1)(2l + 1) = 4kl + 2k + 2l + 1 = 2(2kl + k + l) + 1.$$
The number $m = 2kl + k + l$ is an integer, because sums and products of integers are integers, so $ab = 2m + 1$ is odd.
Check: $a = 3$ and $b = 5$ give $k = 1$, $l = 2$, $m = 7$, and $2 \cdot 7 + 1 = 15 = 3 \cdot 5$.
The problem shows the typical use: unfold the definition, compute, and fold the result back into the definition of the conclusion.

### L3 human

In natural deduction, a direct proof of $P \to Q$ is an application of implication introduction: from a derivation of $Q$ under the open assumption $P$, conclude $P \to Q$ and close the assumption.
Under the Curry-Howard correspondence, such a proof is a function that sends a proof of $P$ to a proof of $Q$, which is why Lean writes the step as `intro` or as `fun h => ...`.
Much of the craft lies in choosing the intermediate statements, and the [[forward-backward method|V8ZB838JY5]] is a way to find them.
The other methods change the goal before the direct work starts: the [[contrapositive|0BB5TPGQ1N]] replaces the goal, [[proof by contradiction|0J0XBKG64S]] adds an assumption, and [[mathematical induction|0ASJVEFA9J]], from the topic [[induction and well-ordering|EEH2F76CYQ]], splits a universal goal into a base case and a step.
