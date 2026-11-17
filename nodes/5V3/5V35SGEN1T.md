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

Deductive reasoning passes from premises to a conclusion that must be true whenever all the premises are true.
Inductive reasoning, also called enumerative induction, passes from many observed cases to a general claim that the cases make likely, but not certain.
Abductive reasoning passes from an observed fact to a hypothesis that would explain the fact, if the hypothesis were true.
In mathematics only deduction proves a statement: a [[mathematical proof|0B94TKFQJX]] is a deduction from axioms, definitions and earlier results.
Induction and abduction are still part of the work, because they suggest the conjectures and the explanations that deduction then tests.
The method of [[mathematical induction|0ASJVEFA9J]] is a form of deduction, despite its name.

## Motivation

A mathematician who meets a new problem uses all three kinds of reasoning, in a typical order.
First come computations of small cases: $1 = 1$, $1 + 3 = 4$, $1 + 3 + 5 = 9$, $1 + 3 + 5 + 7 = 16$.
The pattern of squares suggests a general claim, and this step is induction.
Next comes a search for a reason: a square of side $n$ splits into $n$ L-shaped layers of sizes $1, 3, 5, \ldots$, and this explanation is abduction.
Last comes a proof that the claim holds for every $n$, and this step is deduction, as [[this example|5W8G4689R2]] shows.
The three names help to say which step gives evidence and which step gives certainty.

## Notation

There is no special notation for the three kinds of reasoning.
In logic, a deduction from premises $\Gamma$ to a conclusion $\varphi$ is written $\Gamma \vdash \varphi$.
The word "induction" has two meanings in mathematics, and this page keeps them apart.
"Inductive reasoning" or "enumerative induction" means generalization from cases.
"Mathematical induction" means the proof method with a base case and an induction step.

## Remarks

### Examples

- Deduction: all primes greater than $2$ are odd, and $7$ is a prime greater than $2$, so $7$ is odd. The conclusion follows from the premises by a rule of inference.
- Induction: the values of $n^2 + n + 41$ are prime for $n = 0$ to $39$, so the claim "always prime" looks likely. The claim is false, as [[this example|H75AB4EJT5]] shows.
- Abduction: the sums $1, 4, 9, 16$ of odd numbers are squares, and the picture of a square cut into L-shaped layers explains why. The [[full example|5W8G4689R2]] shows all three kinds of reasoning on this problem.
- Abduction: a numerical value $1.6449\ldots$ of the sum $\sum_{n \geq 1} 1/n^2$ agrees with $\pi^2/6 = 1.6449\ldots$, and the hypothesis "the sum is $\pi^2/6$" would explain the agreement. Leonhard Euler gave the first proof of this value.
- Deduction by [[mathematical induction|0ASJVEFA9J]]: the proof that $3$ divides $n^3 - n$ for each natural number $n$, as [[this example|7RZDHDFSPT]] shows.

### Non-examples

- "Every multiple of $4$ is even, and $6$ is even, so $6$ is a multiple of $4$" is not a valid deduction. It affirms the consequent, as [[this example|2XXTDXK1ZC]] shows.
- A proof by mathematical induction is not inductive reasoning. Its conclusion is certain, because the base case and the induction step cover each natural number.
- An argument with a false premise can be a valid deduction, but it does not prove its conclusion. From "all primes are odd" we deduce "$2$ is odd", which is false, because the premise is false.

### Basic properties

- A deduction preserves truth: if the premises are true and the steps are valid, the conclusion is true.
- A deduction can be checked step by step, without knowledge of how the argument was found.
- Inductive reasoning does not preserve truth: true observations can support a false general claim. One [[counterexample|0ED72CTBNP]] refutes the claim.
- Abduction can propose several explanations of the same fact. A proof or a counterexample decides between them.
- The conclusion of an inductive or an abductive argument is a candidate for a conjecture. The conclusion of a deductive argument from true premises is a theorem.

### History

Aristotle studied deductive arguments in the form of syllogisms in the fourth century BC.
Charles Sanders Peirce introduced abduction as a third kind of inference, next to deduction and induction, in the nineteenth century.
George Pólya wrote on inductive and plausible reasoning in mathematics in "Mathematics and Plausible Reasoning" (1954).

### Common errors

- To read "proof by induction" as "proof by many examples". Mathematical induction proves the induction step for an arbitrary $n$, and this covers all cases.
- To treat a pattern in the first cases as a fact. The pattern needs a proof, and sometimes it fails, as for $n^2 + n + 41$ at $n = 40$.
- To think that a valid deduction gives a true conclusion from false premises. Validity is about the form of the argument, and truth also needs true premises.

## Explanations

### L1 human

There are three common ways to reach a conclusion.
In deduction, the conclusion must follow: "every square has four sides, this shape is a square, so it has four sides".
In induction, we see many cases and guess a rule: "the sun rose every day so far, so it will rise tomorrow".
In abduction, we look for the best explanation: "the street is wet, so it probably rained".
In mathematics, induction and abduction help us to guess, but only deduction proves.
For example, $1 + 3 = 4$ and $1 + 3 + 5 = 9$ suggest that sums of odd numbers give squares, but we need a deduction to be sure.

### L2 human

We sort the steps of a small investigation into the three kinds.
The question is: which numbers $2^n - 1$ are prime?

1. We compute: $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^5 - 1 = 31$ and $2^7 - 1 = 127$ are prime, while $2^4 - 1 = 15$ and $2^6 - 1 = 63$ are not.
2. Induction: in these cases, $2^n - 1$ is prime only when $n$ is prime. We guess that this holds for each $n \geq 2$.
3. Abduction: if $n = ab$ with $1 < a < n$, the factor $x - 1$ of $x^b - 1$, with $x = 2^a$, would explain why $2^n - 1$ is not prime.
4. Deduction: for $n = ab$, we have $2^n - 1 = (2^a)^b - 1 = (2^a - 1)\left((2^a)^{b-1} + \cdots + 2^a + 1\right)$.
5. With $1 < a < n$, the first factor satisfies $1 < 2^a - 1 < 2^n - 1$, so $2^n - 1$ is not prime. This proves the guess of step 2.
6. Induction again suggests the converse: "if $n$ is prime, then $2^n - 1$ is prime". This guess fails: $2^{11} - 1 = 2047 = 23 \cdot 89$.

The typical use of the three kinds is this cycle: compute cases, guess a rule, look for a reason, and prove or refute.
A trap is step 6: a guess that comes from the same data as a proved result is not proved by that result.

### L3 human

The difference between the three kinds is the relation between premises and conclusion.
A deduction is valid when every interpretation that makes the premises true makes the conclusion true, which is [[logical consequence|1HK0VYWTV7]].
Induction and abduction are ampliative: their conclusions say more than the premises, and so they can fail.
Their study belongs to the philosophy of science, to probability and to statistics, where inductive inference becomes estimation and testing of hypotheses.

In mathematics the inductive and abductive steps are the subject of [[plausible reasoning and experimental mathematics|DME0TPC348]] and of [[heuristics of discovery|X1NSTVGDNQ]].
Pólya described how analogy, specialization and generalization make a conjecture more or less credible, without proving it.
The proof method of [[mathematical induction|0ASJVEFA9J]] is a deduction from the induction axiom of the [[Peano axioms|0QFT7Z76N5]], and its relatives, such as structural and transfinite induction, are deductions too.
