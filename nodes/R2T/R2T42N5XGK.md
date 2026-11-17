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

Forming a conjecture is the step from data, examples or analogy to a precise statement that can be proved or refuted.
The usual steps are to collect cases systematically, to look for a pattern, to state it with exact hypotheses and quantifiers, and to test it on new cases.
A useful test targets cases unlike the data, such as extreme, degenerate or large cases.
The result is a [[conjecture|WMEMMHZ3BH]]: a statement that is believed for stated reasons and is not yet proved.
The step matters because a precise conjecture tells a later proof what to prove, and a vague belief does not.

## Motivation

Most theorems began as guesses.
A guess becomes useful only when it is sharp enough to be wrong.
"Primes become rarer" is a belief, and "the number of primes up to $x$ is asymptotic to $x/\ln x$" is a conjecture that Gauss and Legendre could test against tables.

The step from data to a statement has its own techniques.
Tables organize the cases, differences and ratios reveal growth, factorization reveals structure, and a search in a database of sequences finds known matches.
[[Plausible reasoning|8DHD3H1CJ9]] then weighs the result, and [[experimental mathematics|BPEPTN0TT9]] supplies data on a large scale.

## Notation

The forward difference of a sequence $(a_n)$ is $\Delta a_n = a_{n+1} - a_n$, and $\Delta^{k+1} a_n = \Delta(\Delta^k a_n)$.
If $a_n$ is a polynomial in $n$ of degree $k$ with leading coefficient $c$, then $\Delta^k a_n = k!\,c$ for every $n$, and $\Delta^{k+1} a_n = 0$.
Conversely, if $\Delta^{k+1} a_n = 0$ for all $n \geq 1$, then [[Newton's forward difference formula|DDHCMKHD2T]] gives
$$a_n = \sum_{j=0}^{k} \binom{n-1}{j} \Delta^j a_1.$$
In practice the differences are known only for finitely many $n$, so the formula gives a conjecture, not a theorem.

## Remarks

### Examples

1. [[A conjecture for the sum of the first n cubes|H19P682F8X]]: the fourth differences of $1, 9, 36, 100, \ldots$ are constant, which gives a polynomial of degree $4$ and then $\left(n(n+1)/2\right)^2$.
2. [[Which primes are sums of two squares|GD5KTM6Y6P]]: a table of primes up to $113$ and a look at residues modulo $4$ lead to Fermat's theorem.
3. [[A table of polyhedra suggests Euler's formula|HTK0AX3RGC]]: a table of $V$, $E$ and $F$ gives $V - E + F = 2$, and a counterexample forces the hypothesis "convex".
4. Gauss compared counts of primes in blocks of $1000$ numbers with $1/\ln x$ and conjectured the [[prime number theorem|0EHBY5Y84N]].

### Non-examples

1. [[A finite list does not determine its continuation|G9FEX51ASB]]: "find the next term of $1, 2, 4, 8, 16$" names no mathematical object. A guess of the next term is not a conjecture, because nothing makes it true or false.
2. A vague belief such as "this sequence grows fast" is not a conjecture until "fast" has a precise meaning.
3. A restatement of a theorem already proved is not a conjecture, since nothing remains to be decided.

### Basic properties

1. A conjecture must be precise: each object is defined, each hypothesis is stated, and the statement is true or false.
2. Every finite set of data fits infinitely many conjectures. The choice among them uses simplicity, a mechanism, and agreement with known theorems.
3. A conjecture that survives tests of a new kind gains more credibility than one tested only on cases like the data.
4. Constant $k$-th differences over the computed range suggest a polynomial of degree $k$. The polynomial is then fixed by $k + 1$ values, and it must be checked on further values and proved.
5. Stronger conjectures are more useful and riskier. A weaker statement, such as an inequality instead of an asymptotic formula, may be the right first target.
6. The refutation of a conjecture often leads to a corrected one, as the polyhedra example shows.

### History

Gauss wrote that he had studied tables of primes in 1792 or 1793 and had noticed that their density near $x$ is about $1/\ln x$.
Fermat stated the theorem on primes that are sums of two squares in a letter to Mersenne in 1640, without a proof.
Pólya described the steps of guessing in "How to Solve It" (1945) and in "Mathematics and Plausible Reasoning" (1954).
Imre Lakatos described in "Proofs and Refutations" how the statement of Euler's polyhedron formula changed through counterexamples.

### Common errors

1. Stating the conjecture without its range. "The formula holds" must say for which $n$ and under which hypotheses.
2. Fitting a polynomial of degree $k$ through exactly $k + 1$ values and calling the fit evidence. Such a polynomial always exists, so the fit tests nothing; only further values test it.
3. Testing only cases like the ones that suggested the pattern. Those tests share the same blind spots.

## Explanations

### L1 human

A conjecture is a guess that is stated exactly, so that it can be checked.
To make one, collect examples, put them in a table, and look for a rule.
Then write the rule down precisely, test it on new examples, and only then try to prove it.
For example, $1 + 3 = 4$, $1 + 3 + 5 = 9$ and $1 + 3 + 5 + 7 = 16$ suggest "the sum of the first $n$ odd numbers is $n^2$".
That sentence is precise, so a proof can confirm it, or a single example can refute it.

### L2 human

We guess a formula for $a_n = 1 \cdot 2 + 2 \cdot 3 + \cdots + n(n+1)$.

1. The data: $a_1, \ldots, a_6 = 2, 8, 20, 40, 70, 112$.
2. First differences: $6, 12, 20, 30, 42$. Second differences: $6, 8, 10, 12$. Third differences: $2, 2, 2$.
3. Constant third differences suggest a cubic with leading coefficient $2/3! = 1/3$.
4. Newton's formula gives $a_n = 2 + 6\binom{n-1}{1} + 6\binom{n-1}{2} + 2\binom{n-1}{3}$, which simplifies to $\dfrac{n(n+1)(n+2)}{3}$.
5. Test on new data: $a_{10} = 10 \cdot 11 \cdot 12 / 3 = 440$, and the direct sum is also $440$.
6. Proof by induction: $\dfrac{n(n+1)(n+2)}{3} + (n+1)(n+2) = \dfrac{(n+1)(n+2)(n+3)}{3}$.

The typical use: differences turn a table into a polynomial conjecture, and induction then proves it.
A trap: if the sequence is not a polynomial in $n$, as $2^n$ is not, the differences never become constant, and the method gives nothing.

### L3 human

Conjecture formation has been studied as a search problem.
The space of candidate statements is large, and the data constrain it only weakly, by the [[strong law of small numbers|8AFXPXCE3N]].
Good conjectures are those of low complexity that fit all known data, follow from a [[heuristic argument|VCQQNJ3SEZ]], and have consequences that can be tested.
Programs that propose conjectures automatically implement parts of this search; see [[machine-assisted mathematical discovery|D1YQW43N3K]].
The [[heuristics of discovery|X1NSTVGDNQ]] describe the complementary search for a proof.
