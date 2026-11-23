---
tag: R2T42N5XGK
kind: concept
name: Forming conjectures
aliases: [conjecture-formation, guessing-a-formula, polynomial-fitting]
msc: ["00A35", "97E50"]
topics: [DME0TPC348]
audience: ug1
uses: [WMEMMHZ3BH, 8DHD3H1CJ9, BPEPTN0TT9, DDHCMKHD2T]
sources:
  - url: https://en.wikipedia.org/wiki/Conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finite_difference
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Forming a conjecture is the step from examples to an exact statement that a proof or a counterexample can settle.
A good conjecture is precise, fits all the data, and has been tested on cases unlike the ones that suggested it.

Fermat's numbers show both the strength and the risk of the step.
The numbers $F_n = 2^{2^n} + 1$ for $n = 0$ to $4$ are
$$3, \ 5, \ 17, \ 257, \ 65537,$$
and all five are prime.
Fermat stated the conjecture "every $F_n$ is prime", which is exact enough to be tested.
The next case is $F_5 = 2^{32} + 1 = 4294967297$, and Euler found in 1732 that
$$4294967297 = 641 \cdot 6700417.$$
The statement was a good conjecture, because it was sharp enough to be refuted, and it was false.
A test of the sixth case before any attempt at a proof would have settled it.

In general the work has four steps.
Collect cases in a systematic way, look for a pattern, state it with exact hypotheses and quantifiers, and test it on new cases, especially extreme, degenerate or large ones.
The result is a [[conjecture|WMEMMHZ3BH]]: a statement that is believed for stated reasons and is not yet proved.

## Motivation

Most theorems began as guesses, and a guess becomes useful only when it is sharp enough to be wrong.
"Primes become rarer" is a belief.
"The number of primes up to $x$ is asymptotic to $x / \ln x$" is a conjecture that Gauss and Legendre could test against tables, and it became the [[prime number theorem|0EHBY5Y84N]].

The step from data to a statement has its own techniques.
Tables organize the cases, differences and ratios show growth, factorization shows structure, and a database of sequences finds known matches.
[[Plausible reasoning|8DHD3H1CJ9]] then weighs the result, and [[experimental mathematics|BPEPTN0TT9]] supplies data on a large scale.
A precise conjecture also tells a later proof what to prove, which a vague belief cannot do.

## Notation

The forward difference of a sequence $(a_n)$ is $\Delta a_n = a_{n+1} - a_n$, and $\Delta^{k+1} a_n = \Delta(\Delta^k a_n)$.
If $a_n$ is a polynomial in $n$ of degree $k$ with leading coefficient $c$, then $\Delta^k a_n = k! \, c$ for every $n$, and $\Delta^{k+1} a_n = 0$.
Conversely, if $\Delta^{k+1} a_n = 0$ for all $n \ge 1$, then [[Newton's forward difference formula|DDHCMKHD2T]] gives
$$a_n = \sum_{j=0}^{k} \binom{n-1}{j} \Delta^j a_1.$$
In practice the differences are known only for finitely many $n$, so the formula gives a conjecture, not a theorem.

## Remarks

### From a table to a formula

[[A conjecture for the sum of the first n cubes|H19P682F8X]] starts from the sums $1, 9, 36, 100, 225, \ldots$.
Their fourth differences are constant, which suggests a polynomial of degree $4$.
Fitting gives
$$1^3 + 2^3 + \cdots + n^3 = \left( \frac{n(n+1)}{2} \right)^2,$$
which is tested on new values and then proved by induction.

[[Which primes are sums of two squares|GD5KTM6Y6P]] needs a different idea.
A table of the primes up to $113$ shows no formula, but sorting them by their remainder modulo $4$ does: the odd primes that are sums of two squares are exactly those with remainder $1$.
That is Fermat's two-square theorem.

### A counterexample that improves the statement

[[A table of polyhedra suggests Euler's formula|HTK0AX3RGC]] collects $V$, $E$ and $F$ for many solids and finds $V - E + F = 2$ each time.
A picture frame with a square hole gives $V - E + F = 0$.
The repaired statement adds the hypothesis "convex", and in that form it is a theorem.
So a refutation often produces a better conjecture rather than nothing.

### What it is not

[[A finite list does not determine its continuation|G9FEX51ASB]] shows that "find the next term of $1, 2, 4, 8, 16$" names no mathematical object.
A guess of the next term is not a conjecture, because nothing makes it true or false.
A vague belief such as "this sequence grows fast" is not a conjecture until "fast" has a precise meaning.
A restatement of a theorem already proved is not a conjecture either, since nothing remains to be decided.

### The rules you can use

A conjecture must be precise: each object is defined, each hypothesis is stated, and the statement is true or false.
Every finite set of data fits infinitely many conjectures, so the choice among them uses simplicity, a mechanism and agreement with known theorems.
A conjecture that survives tests of a new kind gains more credibility than one tested only on cases like the data.
Stronger conjectures are more useful and more risky, and a weaker statement, such as an inequality in place of an asymptotic formula, may be the right first target.

### Watch out

A pattern that holds in many cases is not a proof, so a conjecture stays a conjecture after any number of checks.

Do not fit a polynomial of degree $k$ through exactly $k + 1$ values and call the fit evidence.
Such a polynomial always exists, so the fit tests nothing, and only further values test it.

Do not test only cases like the ones that suggested the pattern.
Five Fermat numbers are all small, and the first large one broke the rule.

### History

Gauss wrote that he studied tables of primes around 1792 and noticed that their density near $x$ is about $1/\ln x$.
Fermat stated the theorem on primes that are sums of two squares in a letter to Mersenne in 1640, without a proof.
Pólya described the steps of guessing in *How to Solve It* (1945) and in *Mathematics and Plausible Reasoning* (1954).
Imre Lakatos described in *Proofs and Refutations* how the statement of Euler's polyhedron formula changed through counterexamples.

### Try it

The sums $1, 1 + 2, 1 + 2 + 3, \ldots$ are $1, 3, 6, 10, 15$; state a conjecture and test it once.
The second differences are constant, and fitting gives $n(n+1)/2$; at $n = 10$ it gives $55$, which matches $1 + 2 + \cdots + 10$.

State the polyhedron conjecture in a form that the picture frame does not refute.
"Every convex polyhedron has $V - E + F = 2$" is one such form, and it is Euler's theorem.

## Explanations

### L1 human

A conjecture is a guess stated exactly, so that it can be checked.
To make one, collect examples, put them in a table, and look for a rule.
Then write the rule down precisely, test it on new examples, and only then try to prove it.
For example, $1 + 3 = 4$, $1 + 3 + 5 = 9$ and $1 + 3 + 5 + 7 = 16$ suggest "the sum of the first $n$ odd numbers is $n^2$".
That sentence is precise, so a proof can confirm it, or one example can refute it.

### L2 human

We guess a formula for $a_n = 1 \cdot 2 + 2 \cdot 3 + \cdots + n(n+1)$.
The data for $n = 1$ to $6$ are $2, 8, 20, 40, 70, 112$.
The first differences are $6, 12, 20, 30, 42$, the second are $6, 8, 10, 12$, and the third are $2, 2, 2$.
Constant third differences suggest a cubic with leading coefficient $2/3! = 1/3$.
Newton's formula gives
$$a_n = 2 + 6 \binom{n-1}{1} + 6 \binom{n-1}{2} + 2 \binom{n-1}{3} = \frac{n(n+1)(n+2)}{3}.$$
We test it on a new value: the formula gives $a_{10} = 10 \cdot 11 \cdot 12 / 3 = 440$, and the direct sum is also $440$.
Induction then proves it, because
$$\frac{n(n+1)(n+2)}{3} + (n+1)(n+2) = \frac{(n+1)(n+2)(n+3)}{3}.$$
The typical use: differences turn a table into a polynomial conjecture, and induction proves it.
Watch out: if the sequence is not a polynomial in $n$, as $2^n$ is not, the differences never become constant and the method gives nothing.

### L3 human

Forming conjectures can be studied as a search problem.
The space of candidate statements is large, and by the [[strong law of small numbers|8AFXPXCE3N]] the data constrain it only weakly.
Good conjectures have low complexity, fit all known data, follow from a [[heuristic argument|VCQQNJ3SEZ]], and have consequences that can be tested.
Programs that propose conjectures automatically carry out parts of this search; see [[machine-assisted mathematical discovery|D1YQW43N3K]].
The [[heuristics of discovery|X1NSTVGDNQ]] describe the matching search for a proof.
