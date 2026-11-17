---
tag: ~aaa3fffe
kind: concept
name: Inventor's paradox
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [~fd7a5df5]
uses: [~fd7a5df5, ~478f3b5e, F94KJC2RXP]
sources:
  - url: https://en.wikipedia.org/wiki/Inventor%27s_paradox
    locator: lead section
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

The inventor's paradox is the observation that a more ambitious problem can be easier to solve than the problem that was asked.
George Pólya stated it in *How to Solve It* (1945): the more ambitious plan may have more chances of success.
The paradox is that a stronger statement says more, and so should be harder to prove, yet its proof is often shorter.
The usual explanation is that the stronger statement gives more to work with: a stronger hypothesis in an induction, a parameter to vary, or a structure that the special case hides.
As a heuristic, the inventor's paradox tells the solver who is stuck to try a more general or a stronger problem, and it is the reason behind [[strengthening the induction hypothesis|F94KJC2RXP]].

## Motivation

A solver who cannot prove a statement usually tries to weaken it, or to add hypotheses.
That move is often right, but sometimes the obstacle is the opposite one: the statement is too weak to support its own proof.
In an induction, the hypothesis is the statement for $n$, and a weak statement gives a weak hypothesis.
In a problem about one number, the number may hide a pattern that a general $n$ shows.
The inventor's paradox names this case, so that the solver remembers to try the stronger problem as well as the weaker one.

## Remarks

### The steps

1. Notice where the proof is stuck: an induction step that does not close, or a special number with no visible structure.
2. Ask what stronger or more general statement would make that step possible.
3. Check that the stronger statement is still plausible, by special cases.
4. Prove the stronger statement.
5. Deduce the given statement as a special case.

### When it applies

The paradox applies most often to proofs by [[induction|0ASJVEFA9J]], where the step needs more than the statement provides, and to problems about one specific number or object.
It also applies when a general theory makes a special case routine, as in the passage from one integral to a family of integrals.

### Examples

1. [[A take-away game solved for every number of counters|~0462ca31]]: the question for $21$ counters is answered by solving the game for every number $n$, which gives the rule "multiples of $4$ lose".
2. [[Products of consecutive integers by the integrality of binomial coefficients|~3b643504]]: the claim that $24$ divides every product of four consecutive integers follows from the general claim that $k!$ divides every product of $k$ consecutive integers.
3. [[The sum of 1/k² is at most 2 − 1/n|DFVCKA01PN]]: the bound $\sum_{k=1}^{n} \frac{1}{k^2} < 2$ has no direct induction step, and the stronger bound $2 - \frac{1}{n}$ has an easy one. The page [[a direct induction on the bound 2|MZXYW75TC3]] shows where the weak form gets stuck.
4. [[The product of (2k − 1)/(2k) is at most 1/√(3n + 1)|MC068WVGWS]]: the bound $\frac{1}{\sqrt{3n}}$ does not support an induction, and the stronger bound $\frac{1}{\sqrt{3n + 1}}$ does.
5. A sum with a fixed end. To find $1 + 3 + 5 + \cdots + 99$, it is easier to find the sum of the first $n$ odd numbers for every $n$, which is $n^2$, and then to take $n = 50$.

### Non-examples

1. [[Fermat's Last Theorem for n = 4 is easier than the general theorem|~9e5c01c9]]: the case $n = 4$ has a short proof by infinite descent, and the general theorem needed more than three hundred years.
2. A strengthening that is false. To prove that $2^n > n$ for $n \ge 1$ one might try the stronger $2^n > n^2$, which fails at $n = 2, 3, 4$; the strengthening must first be tested on special cases.
3. A generalization with no new tool. Replacing the number $7$ in "$7$ is prime" by $n$ gives a question with no single answer; the paradox needs a general problem that has a uniform solution.

### Basic properties

1. If the stronger statement is proved, the given statement follows. So the method is safe as long as the stronger statement is true.
2. A stronger statement is a stronger induction hypothesis and a stronger conclusion at once. The method works when the gain in the hypothesis outweighs the extra demand in the conclusion.
3. The paradox is not a law. In many problems the special case is easier, as in non-example 1.

### Related methods

[[Generalization|~478f3b5e]] is the general heuristic, and the inventor's paradox is the observation that explains why it can succeed.
[[Strengthening the induction hypothesis|F94KJC2RXP]] is the form of the paradox inside proofs by induction.
[[Abstraction and generalization|976RZZCT1H]] discusses the paradox among other effects of generality.
[[Specialization|~701d4f5c]] goes the other way and is the right move when the special case is easier.

### History

Pólya gave the inventor's paradox an entry in the dictionary of heuristic of *How to Solve It* (1945), with the sentence that the more ambitious plan may have more chances of success.
The same idea appears under other names in the theory of induction proofs, for example in automated theorem proving, where a program must sometimes generalize a goal before induction can prove it.

### Common errors

1. To strengthen a statement without testing it, as in non-example 2.
2. To give up a stronger statement because it "must be harder". The point of the paradox is that this is not always so.
3. To prove a stronger statement and then forget to check that it implies the given one.

## Explanations

### L1 human

Sometimes it is easier to answer a bigger question than a small one.
Suppose we want to know who wins a game that starts with $21$ counters.
Working on $21$ alone is hard, but asking "who wins with $1$, $2$, $3$, $\ldots$ counters?" shows a pattern that answers every case at once.
This surprise, that the bigger question is easier, is called the inventor's paradox.

### L2 human

We use the paradox to show that $\sum_{k=1}^{n} \frac{1}{k(k+1)} < 1$ for every $n \ge 1$.

1. A direct induction is stuck: from "the sum up to $n$ is below $1$" we cannot conclude that adding $\frac{1}{(n+1)(n+2)}$ keeps it below $1$.
2. Strengthen to an exact statement: $\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n + 1}$.
3. Test: $n = 1$ gives $\frac{1}{2}$ on both sides, and $n = 2$ gives $\frac{2}{3}$ on both sides.
4. Induction step: $1 - \frac{1}{n+1} + \frac{1}{(n+1)(n+2)} = 1 - \frac{(n + 2) - 1}{(n+1)(n+2)} = 1 - \frac{1}{n + 2}$.
5. Since $\frac{1}{n+1} > 0$, the sum is below $1$.

The typical use: the inequality is the weak statement, and the equation is the strong statement that carries the induction.

A trap: a strengthening must be true; step 3 tests it before the proof starts.

### L3 human

In automated theorem proving, the paradox is a practical problem: a goal often cannot be proved by induction as stated.
Automated provers for induction therefore include generalization steps, which replace a goal by a more general one before induction.
The choice of the stronger statement cannot be automated in general, and it is often the main idea of a proof.
The paradox also explains why mathematicians value general theories: a general framework can make many special results into exercises.
