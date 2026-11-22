---
tag: 5V35SGEN1T
kind: concept
name: Deductive, inductive and abductive reasoning
aliases: [deductive-reasoning, inductive-reasoning, abductive-reasoning]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: school
uses: [0B94TKFQJX, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Deductive_reasoning
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inductive_reasoning
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Abductive_reasoning
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Mathematicians reason in three ways, and only one of them proves anything.
Deduction gives certainty, while induction and abduction give guesses and explanations that deduction must then confirm or refute.
*Deductive reasoning* passes from premises to a conclusion that must be true whenever all the premises are true.
*Inductive reasoning*, also called enumerative induction, passes from many observed cases to a general claim that the cases make likely but not certain.
*Abductive reasoning* passes from an observed fact to a hypothesis that would explain the fact if the hypothesis were true.
A [[mathematical proof|0B94TKFQJX]] is a deduction from axioms, definitions and earlier results.
The proof method of [[mathematical induction|0ASJVEFA9J]] is also a deduction, despite its name.

## Motivation

Watch a small investigation, and all three kinds appear in order.
First compute some cases:
$$1 = 1, \quad 1 + 3 = 4, \quad 1 + 3 + 5 = 9, \quad 1 + 3 + 5 + 7 = 16.$$
The answers are squares, so we guess that the sum of the first $n$ odd numbers is $n^2$; that step is induction.
Then we look for a reason: a square of $n \times n$ dots peels into $n$ L-shaped layers of $1, 3, 5, \dots$ dots; that step is abduction.
Last we prove that the layer between the $(k-1) \times (k-1)$ and the $k \times k$ squares has $k^2 - (k-1)^2 = 2k - 1$ dots, and that step is deduction.
[[The full investigation|5W8G4689R2]] writes out every step.

The three names let you say which step gave evidence and which gave certainty.
That distinction returns throughout the area, in [[plausible reasoning and experimental mathematics|DME0TPC348]], which studies the guessing steps, and in the [[proof methods|G9JFJGY4TQ]], which study the deductive ones.

## Notation

No special symbols mark the three kinds of reasoning.
In logic, a deduction of a conclusion $\varphi$ from premises $\Gamma$ is written $\Gamma \vdash \varphi$.
The word "induction" has two meanings, and they must be kept apart.
"Inductive reasoning" or "enumerative induction" is generalization from cases.
"Mathematical induction" is the proof method with a base case and an induction step.

## Remarks

### Three arguments about primes

Here is one argument of each kind.
Deduction: every prime greater than $2$ is odd, and $7$ is a prime greater than $2$, so $7$ is odd.
The conclusion cannot be false while the premises are true.
Induction: the values of $n^2 + n + 41$ are prime for $n = 0$ to $39$, so "always prime" looks likely.
The claim is false, since $40^2 + 40 + 41 = 41^2$, as [[the forty-case example|H75AB4EJT5]] shows.
Abduction: the numbers $2^n - 1$ that are prime seem to have $n$ prime, and the factorization $x^b - 1 = (x - 1)(x^{b-1} + \dots + 1)$ would explain it.
The L2 explanation below turns that explanation into a deduction.

### Why only deduction proves

A valid deduction preserves truth: if the premises are true and each step follows a valid rule, the conclusion is true.
So a reader can check a deduction step by step, with no idea of how the author found it.
Inductive reasoning does not preserve truth.
True observations can support a false claim, and one [[counterexample|0ED72CTBNP]] refutes the claim at once.

Abduction can offer several explanations for the same fact, and none of them is proved by the fact.
The conclusions of induction and abduction are therefore candidates for conjectures.
A deduction from true premises gives a theorem.

### Abduction at work

Sum the series $1 + \tfrac14 + \tfrac19 + \tfrac1{16} + \cdots$ numerically and you find a value near $1.6449$.
The number $\pi^2/6$ is also about $1.6449$.
The hypothesis "the sum is exactly $\pi^2/6$" would explain the agreement, and it is the kind of guess that abduction makes.
Leonhard Euler found this value in the 1730s, and the result is now a theorem with many proofs.
The numerical agreement alone, to any number of digits, would not have been a proof.

### Two meanings of induction

Mathematical induction proves a statement $P(n)$ for every natural number $n$ from two facts: $P(0)$ holds, and $P(n)$ implies $P(n + 1)$ for an arbitrary $n$.
Each of those facts is proved, and the principle of induction then gives every case.
So the conclusion is certain, and the method is deductive.
[[The proof that 3 divides n^3 - n|7RZDHDFSPT]] shows such a proof and checks that no step generalizes from cases.

Enumerative induction would look at $n^3 - n$ for $n = 0, \dots, 5$, which gives $0, 0, 6, 24, 60, 120$, see multiples of $3$, and guess.
That is how the statement is found, and it is not how it is proved.

### What is not a deduction

The argument "every multiple of $4$ is even, and $6$ is even, so $6$ is a multiple of $4$" looks like a deduction and is not.
Its form, "if $P$ then $Q$; $Q$; so $P$", [[affirms the consequent|2XXTDXK1ZC]], and here it leads from true premises to a false conclusion.
In the other direction, a valid deduction from a false premise proves nothing.
From "all primes are odd" we deduce "$2$ is odd", and the conclusion is false because the premise is.

### Watch out

Three errors come from mixing up the kinds.
The first is to read "proof by induction" as "proof by many examples".
The induction step must be proved for an arbitrary $n$, not checked for some values.
The second is to treat a pattern in the first cases as a fact, which fails for $n^2 + n + 41$ at $n = 40$.
The third is to trust a valid form with an unchecked premise, as in the deduction that $2$ is odd.

### History

Aristotle studied deductive arguments in the form of syllogisms in the fourth century BC.
Charles Sanders Peirce described abduction as a third kind of inference, next to deduction and induction.
George Pólya wrote on inductive and plausible reasoning in mathematics in "Mathematics and Plausible Reasoning" (1954).

### Try it

First, name the kind of reasoning: "the Fibonacci number $F_p$ is prime for $p = 3, 5, 7, 11, 13, 17$, so it is prime for every odd prime $p$."
It is induction, and the next case fails: $F_{19} = 4181 = 37 \cdot 113$.

Second, is "if $n$ is odd then $n^2$ is odd; $n^2 = 25$; so $n$ is odd" a valid deduction?
No: it affirms the consequent, although here the conclusion happens to be true.

## Explanations

### L1 human

There are three common ways to reach a conclusion.
In deduction the conclusion must follow: every square has four sides, this shape is a square, so it has four sides.
In induction we see many cases and guess a rule: the sun rose every day so far, so it will rise tomorrow.
In abduction we look for the best explanation: the street is wet, so it probably rained.
In mathematics, induction and abduction help us to guess, but only deduction proves.
For example, $1 + 3 = 4$ and $1 + 3 + 5 = 9$ suggest that sums of odd numbers are squares, and we need a deduction to be sure.

### L2 human

Here is a small investigation with all three kinds: which numbers $2^n - 1$ are prime?
Compute: $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^5 - 1 = 31$ and $2^7 - 1 = 127$ are prime, while $2^4 - 1 = 15$ and $2^6 - 1 = 63$ are not.
Induction suggests that $2^n - 1$ is prime only when $n$ is prime.
Abduction suggests why: if $n = ab$, then $2^n - 1 = (2^a)^b - 1$, and $x^b - 1$ has the factor $x - 1$.
Now deduce: for $n = ab$ with $1 < a < n$,
$$2^n - 1 = (2^a - 1)\left(2^{a(b-1)} + 2^{a(b-2)} + \dots + 2^a + 1\right),$$
and $1 < 2^a - 1 < 2^n - 1$, so $2^n - 1$ is not prime.
Check: $n = 6$, $a = 2$ gives $63 = 3 \cdot 21$.
Induction then suggests the converse, "if $n$ is prime then $2^n - 1$ is prime", and that guess fails: $2^{11} - 1 = 2047 = 23 \cdot 89$.
A guess drawn from the same data as a proved result is not proved by that result.

### L3 human

The three kinds differ in the relation between premises and conclusion.
A deduction is valid when every interpretation that makes the premises true makes the conclusion true, which is [[logical consequence|1HK0VYWTV7]].
Induction and abduction are ampliative: their conclusions say more than the premises, so they can fail.
Their study belongs to the philosophy of science and to statistics, where inductive inference becomes estimation and the testing of hypotheses.

Inside mathematics the guessing steps are the subject of [[heuristics of discovery|X1NSTVGDNQ]], where Pólya described how analogy, specialization and generalization make a conjecture more or less credible.
The proof method of mathematical induction is a deduction from the induction axiom of the [[Peano axioms|0QFT7Z76N5]].
Its relatives, structural and transfinite induction, are deductions too.
