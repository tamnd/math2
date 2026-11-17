---
tag: ZX6ERT3SW7
kind: concept
name: Proof by example
aliases: [proof-by-example-fallacy, hasty-generalization, generalization-from-cases]
msc: ["00A35", "97E50"]
topics: [T6QQ749DM5]
audience: school
uses: [EGTZPA6QH3, 0ED72CTBNP, 5V35SGEN1T, WMEMMHZ3BH]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_example
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Faulty_generalization
    locator: Hasty generalization
  - url: https://en.wikipedia.org/wiki/P%C3%B3lya_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mertens_conjecture
    locator: lead section
---

## Summary

Proof by example is the error of treating one or more cases of a universal statement "$P(x)$ for every $x$" as a proof of the statement.
A finite list of cases can never prove a universal statement over an infinite set, because the statement can fail at a case that was not checked.
The error has the informal name "hasty generalization" in the study of arguments, and it is the step from [[inductive reasoning|5V35SGEN1T]] to a claimed deduction.
Examples are still essential: one example proves an existential statement, one [[counterexample|0ED72CTBNP]] disproves a universal statement, and many examples suggest a [[conjecture|WMEMMHZ3BH]].
The idea matters because many patterns hold for a long time and then fail, and only a proof covers every case.

## Motivation

Checking cases is the first thing that a mathematician does with a new claim.
When $n^2 + n + 41$ is prime for $n = 0, 1, \ldots, 39$, it is natural to believe that it is always prime.
But the check does not say why the pattern holds, and a pattern without a reason can stop.
A proof replaces "it worked so far" by "it must work, because".
The patterns that fail late are the warnings that teach the difference.

## Notation

The words in use:

1. "Proof by example" and "proof by picture" are informal names in teaching and in humorous lists of bad proofs.
2. "Hasty generalization" is the name in informal logic. Its formal analogue is the invalid inference from "$P(a_1), \ldots, P(a_k)$" to "for every $x$, $P(x)$".
3. A [[universal statement|EGTZPA6QH3]] has the form "for every $x$ in $S$, $P(x)$", and an existential statement has the form "there is an $x$ in $S$ with $P(x)$".

## Remarks

### Examples

1. The values of [[$n^2 + n + 41$|H75AB4EJT5]] are prime for $n = 0$ to $39$, and $n = 40$ gives $41^2$.
2. The [[numbers of regions of a circle|E4RAKSC2ZC]] cut by the chords between $n$ points are $1, 2, 4, 8, 16$ for $n = 1$ to $5$, and $31$, not $32$, for $n = 6$.
3. The Pólya conjecture says that, for each $n \ge 2$, at least half of the integers from $1$ to $n$ have an odd number of prime factors, counted with multiplicity. It holds for every $n$ below $906{,}150{,}257$, and Minoru Tanaka found in 1980 that it fails at that $n$.
4. The [[Mertens conjecture|4Y4HWKA2MP]] $|M(n)| < \sqrt{n}$ for $n > 1$ held in all computed cases. Andrew Odlyzko and Herman te Riele disproved it in 1985, and no explicit counterexample is known.
5. The integrals $\int_0^\infty \prod_{k=0}^{m} \frac{\sin(x/(2k+1))}{x/(2k+1)}\,dx$ (Borwein integrals) equal $\frac{\pi}{2}$ for $m = 0, 1, \ldots, 6$, and they are slightly less than $\frac{\pi}{2}$ for $m = 7$, when the factor with $15$ appears.

### Non-examples

1. [[One example proves an existential statement|2XMSKQ7YHG]]: $3^2 + 4^2 = 5^2$ proves that some square is a sum of two positive squares.
2. One counterexample disproves a universal statement: $f(40) = 41^2$ disproves "$n^2 + n + 41$ is prime for every $n$".
3. A check of all cases of a statement about a finite set is a proof by exhaustion, not a proof by example. "Every even integer from $4$ to $20$ is a sum of two primes" is proved by the nine cases $2 + 2$, $3 + 3$, $3 + 5$, $5 + 5$, $5 + 7$, $7 + 7$, $5 + 11$, $7 + 11$, $7 + 13$.
4. A generic example, in which the argument uses no special property of the chosen case, can be rewritten as a proof for an arbitrary case. The rewritten text is a proof, and the example only guided it.

### Basic properties

1. A universal statement over an infinite set $S$ is not implied by any finite number of its cases. For a finite subset $F$ of $S$, the property "$x \in F$" holds at every case in $F$ and fails at every other element of $S$.
2. Examples prove existential statements and disprove universal statements. These are the only kinds of statements that one example can decide.
3. Evidence from cases can be strong or weak. It is stronger when the cases are varied and include extreme cases, and weaker when they share a special feature, such as being small.
4. Late failures are possible because some phenomena appear only at large numbers: the first counterexample can be larger than any feasible computation.

### History

George Pólya stated the conjecture now named after him in 1919, and Haselgrove disproved it in 1958 without an explicit counterexample.
Lehman found an explicit counterexample in 1960, and Tanaka found the smallest one in 1980.
Leonhard Euler studied the polynomial $n^2 + n + 41$, and it has become a standard warning against generalization from cases.

### Common errors

1. A student proves "for every $n$" by checking $n = 1, 2, 3$ and writing "and so on".
2. A student draws one figure, observes a property, and claims it for every figure, although the figure has special features, such as a right angle.
3. A student thinks that examples are useless in proofs, and forgets that one example is a complete proof of an existential statement.

## Explanations

### L1 human

Suppose we check that $2$, $4$ and $6$ are even and conclude that every number is even.
The conclusion is false, because $3$ is odd: we checked only special cases.
Some patterns are much harder to break.
A famous formula gives prime numbers forty times in a row, and then it fails.
So a pattern is a good guess, but only a proof shows that it never fails.

### L2 human

We test the claim "$2^n > n^3$ for every integer $n \ge 1$".

1. For $n = 1$: $2 > 1$. True.
2. For $n = 2$: $4 > 8$ is false. So the claim fails, and $n = 2$ is a counterexample.
3. A student who checked only $n = 1$ and $n = 10$ ($1024 > 1000$) would have seen two true cases and missed the failure.
4. The correct statement: $2^n > n^3$ for every $n \ge 10$. Its proof is by induction: the base case $n = 10$ is in step 3, and for $n \ge 10$ we have $\left(\frac{n+1}{n}\right)^3 \le 1.1^3 = 1.331 < 2$, so $2^{n+1} = 2 \cdot 2^n > 2n^3 > (n+1)^3$.
5. A check of the small cases finds the exact range: the claim fails for $n = 2, 3, \ldots, 9$, since $2^9 = 512 < 729 = 9^3$.

The typical use of cases is to find the right statement, and then to prove it.
A trap is to choose test cases that share one feature, such as only large $n$ or only even $n$.

### L3 human

In logic, a universal statement over an infinite domain is not a consequence of any finite set of its instances, because a model can agree with the instances and contain another element that fails.
So number theory has false statements, such as the Mertens conjecture, with no known explicit counterexample.
Other counterexamples are first found by theory: Littlewood proved that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often.
A bound on the first change of sign is named [[Skewes's number|71JVW6G7M1]].
On the other side, some universal statements are decided by finitely many cases for a reason.
Two polynomials of degree at most $d$ in one variable that agree at $d + 1$ points are equal, so a check at $d + 1$ points is a proof, not an example.
The role of examples in research is discussed in [[examples in mathematical practice|F3NNR77WKP]], and experiments as a source of conjectures in [[plausible reasoning and experimental mathematics|DME0TPC348]].
