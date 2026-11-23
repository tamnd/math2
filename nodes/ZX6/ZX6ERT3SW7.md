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

Here is a "proof" that sounds convincing; find what is wrong with it before you read on.

> Claim: $n^2 + n + 41$ is prime for every integer $n \ge 0$.
> Proof: the values for $n = 0, 1, 2, 3, 4, 5$ are $41, 43, 47, 53, 61, 71$, all prime, and the pattern continues.

The claim is false: at $n = 40$ the value is $1600 + 40 + 41 = 1681 = 41^2$.
The error is called proof by example: a few cases of a [[universal statement|EGTZPA6QH3]] "$P(x)$ for every $x$" are offered as a proof of the statement.
The true statement nearby is that $n^2 + n + 41$ is prime for $n = 0, 1, \ldots, 39$, and checking all forty cases proves it.

A finite list of cases never proves a universal statement over an infinite set, because the statement can fail at a case that was not checked.
Examples still do real work: one example proves an existential statement, one [[counterexample|0ED72CTBNP]] refutes a universal one, and many examples suggest a [[conjecture|WMEMMHZ3BH]].

## Motivation

Checking cases is the first thing a mathematician does with a new claim, and it is a good habit.
The trouble starts when the check is mistaken for the reason.
A check says that the pattern held so far, while a proof says why it must hold.
Patterns without a reason can stop, sometimes after a few cases and sometimes after billions.
Those late failures are the best teachers of the difference.

## Notation

The error has an informal name in logic and several names in teaching.
Informal logic calls it hasty generalization, and its formal shape is the invalid inference from $P(a_1), \ldots, P(a_k)$ to "for every $x$, $P(x)$".
Teachers say "proof by example", "proof by picture" or "and so on".
It is the step where [[inductive reasoning|5V35SGEN1T]], which supports a guess, is passed off as deduction, which proves it.
Do not confuse inductive reasoning with mathematical induction, which is a valid method of proof.

## Remarks

### Patterns that fail late

1. The [[values of $n^2 + n + 41$|H75AB4EJT5]] are prime for $n = 0$ to $39$ and composite at $n = 40$.
2. The [[regions of a circle|E4RAKSC2ZC]] cut by all chords between $n$ points number $1, 2, 4, 8, 16$ for $n = 1$ to $5$, and then $31$, not $32$.
3. The Pólya conjecture says that, for every $n \ge 2$, at least half of the integers from $1$ to $n$ have an odd number of prime factors, counted with multiplicity. The first $n$ where it fails is $906{,}150{,}257$.
4. The [[Mertens conjecture|4Y4HWKA2MP]] $|M(n)| < \sqrt{n}$ for $n > 1$ holds in every computed case, yet it is false, and no explicit counterexample is known.
5. The Borwein integrals $\int_0^\infty \prod_{k=0}^{m} \frac{\sin(x/(2k+1))}{x/(2k+1)}\,dx$ equal $\frac{\pi}{2}$ for $m = 0, 1, \ldots, 6$, and fall just short of $\frac{\pi}{2}$ at $m = 7$, when the factor with $15$ appears.

### When cases are a proof

One checked example proves an existential statement.
For instance, $3^2 + 4^2 = 5^2$ [[proves that some square is a sum of two positive squares|2XMSKQ7YHG]].
One counterexample refutes a universal statement, as $n = 40$ refutes the claim of the Summary.
A check of all cases of a statement about a finite set is a proof by exhaustion.
For example, the nine sums $2 + 2$, $3 + 3$, $3 + 5$, $5 + 5$, $5 + 7$, $7 + 7$, $5 + 11$, $7 + 11$, $7 + 13$ prove that every even number from $4$ to $20$ is a sum of two primes.
A generic example, which uses no special feature of the chosen case, can be rewritten as a proof for an arbitrary case, and then the rewritten text is the proof.

### Why no finite check suffices

Let $S$ be an infinite set and $F$ a finite subset.
The property "$x \in F$" holds at every element of $F$ and fails everywhere else in $S$.
So no finite set of cases can tell a true universal statement from this false one.
Evidence from cases can still be strong or weak.
It is stronger when the cases are varied and include extreme ones, and weaker when they share a special feature, such as all being small.
Some phenomena only begin at large numbers, so the first counterexample can lie beyond any feasible computation.

### Watch out

The most common form in student work is "check $n = 1, 2, 3$ and write and so on".
Another is to draw one figure and claim a property for every figure, though the figure happens to have a right angle or two equal sides.
The opposite error is to think that examples are useless in proofs; one example is a complete proof of "there exists".

### History

George Pólya stated his conjecture in 1919.
Haselgrove disproved it in 1958 without giving an explicit counterexample, Lehman found an explicit one in 1960, and Tanaka found the smallest one, $906{,}150{,}257$, in 1980.
Andrew Odlyzko and Herman te Riele disproved the Mertens conjecture in 1985.
Leonhard Euler studied the polynomial $n^2 + n + 41$, which has since become the standard warning against generalizing from cases.

### Try it

Is "$2^n > n^2$ for every $n \ge 1$" proved by the cases $n = 1$ and $n = 5$?
No: both cases hold ($2 > 1$ and $32 > 25$), but $n = 2, 3, 4$ fail, since $4 = 4$, $8 < 9$ and $16 = 16$.

Is "some prime is one more than a perfect square" proved by $5 = 2^2 + 1$?
Yes: the claim is existential, and one checked example proves it.

## Explanations

### L1 human

Suppose we check that $2$, $4$ and $6$ are even and conclude that every number is even.
The number $3$ says otherwise, because we checked only special cases.
Some patterns are much harder to break.
A famous formula gives prime numbers forty times in a row and then fails.
A pattern is a good guess, but only a proof shows that it never fails.

### L2 human

We test the claim "$2^n > n^3$ for every integer $n \ge 1$".
At $n = 1$ it holds, $2 > 1$, and at $n = 10$ it holds, $1024 > 1000$.
A student who checked only these two cases would miss that $n = 2$ gives $4 > 8$, which is false.
In fact the claim fails for every $n$ from $2$ to $9$; for instance $2^9 = 512 < 729 = 9^3$.

The correct statement is that $2^n > n^3$ for every $n \ge 10$, and induction proves it.
The base case $n = 10$ is checked above.
For $n \ge 10$ we have $\left(\frac{n+1}{n}\right)^3 \le 1.1^3 = 1.331 < 2$, so $2^{n+1} = 2 \cdot 2^n > 2n^3 > (n+1)^3$.

The typical use of cases is to find the right statement, and then to prove it.
Watch out for test cases that share one feature, such as only large $n$ or only even $n$.

### L3 human

A universal statement over an infinite domain is not a logical consequence of any finite set of its instances, since a model can satisfy the instances and contain another element that fails.
So number theory has false statements, such as the Mertens conjecture, with no known explicit counterexample.
Some counterexamples are first found by theory: Littlewood proved that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often, and a bound on the first change of sign is named [[Skewes's number|71JVW6G7M1]].
In the other direction, some universal statements reduce to finitely many cases for a reason.
Two polynomials of degree at most $d$ in one variable that agree at $d + 1$ points are equal, so a check at $d + 1$ points is a proof.
The role of examples in research is discussed in [[examples in mathematical practice|F3NNR77WKP]], and experiments as a source of conjectures in [[plausible reasoning and experimental mathematics|DME0TPC348]].
