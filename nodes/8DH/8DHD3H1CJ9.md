---
tag: 8DHD3H1CJ9
kind: concept
name: Plausible reasoning
aliases: [patterns-of-plausible-inference, heuristic-reasoning-polya]
msc: ["00A35"]
topics: [DME0TPC348]
audience: ug2
uses: [5V35SGEN1T, WMEMMHZ3BH, 0B94TKFQJX, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Plausible_reasoning
    locator: George Polya and plausible reasoning
  - url: https://en.wikipedia.org/wiki/Mathematics_and_Plausible_Reasoning
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Plausible reasoning is the reasoning that makes a statement more or less believable without proving it or refuting it.
It is how mathematicians decide which guesses deserve a proof, and it never replaces the proof.

Here is a case you can check.
Take the claim $A$: "$n^2 + n + 41$ is prime for every integer $n \ge 0$".
If $A$ is true, then $41$, $43$, $47$ and $53$ are prime, and they are.
In fact all forty values for $n = 0$ to $39$ are prime, so $A$ looks very believable.
Then $n = 40$ gives
$$40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41 = 1681,$$
and $A$ is false.
Forty true consequences made $A$ more credible, and one false consequence refuted it with certainty.

George Pólya described this kind of reasoning by patterns of inference.
The basic pattern has the premises "$A$ implies $B$" and "$B$ is true", and the conclusion "$A$ is more credible".
Other patterns use analogy ("$A$ is like $B$, and $B$ is true") and the weight of the evidence (a surprising consequence counts more than an expected one).
The conclusion of a plausible inference is never "$A$ is true", only a change in confidence.

## Motivation

A [[proof|0B94TKFQJX]] is the end of a piece of mathematical work, but it is seldom the start.
Before the proof, a mathematician guesses a result and collects reasons to believe it: special cases, a similar known result, a consequence that turns out true, a number that agrees.
None of these is a proof, and some are much stronger than others.
Pólya asked whether the weighing of such reasons follows rules, and his patterns are his answer.

The patterns also explain an asymmetry between proof and refutation.
If $A$ implies $B$ and $B$ is false, then $A$ is false: this is a deduction, called modus tollens.
If $A$ implies $B$ and $B$ is true, nothing follows by deduction.
Yet every working mathematician feels that a true consequence supports $A$, and plausible reasoning is the name for that support.
The rest of the sub-area studies its sources: [[experimental mathematics|BPEPTN0TT9]], [[numerical evidence|JFD3QWCX8Z]] and [[heuristic arguments|VCQQNJ3SEZ]].

## Notation

Pólya wrote each pattern as two premises above a line and a conclusion below it, like a rule of inference.
His fundamental inductive pattern reads:
$$\frac{A \text{ implies } B \qquad B \text{ true}}{A \text{ more credible}}$$
Weaker forms replace "true" by "more credible", and the conclusion by "somewhat more credible".
Later authors model the patterns with probability.
If $B$ follows from $A$, then the event "$A$ and $B$" is the event $A$, so
$$P(A \mid B) = \frac{P(A)}{P(B)} \ge P(A).$$
A true consequence raises the probability of $A$ by the factor $1/P(B)$, which is large when $B$ was unlikely.
This model is a reading of Pólya's patterns, not part of them.

## Remarks

### Verified consequences and their weight

[[Euler's evaluation of the Basel sum|A1NXVMGPG0]] is Pólya's favorite case.
Euler guessed $\sum 1/n^2 = \pi^2/6$ by treating $\sin x / x$ as a polynomial with infinitely many roots.
He then checked consequences of the same analogy: the numerical value $1.6449\ldots$, the value $\pi^4/90$ of $\sum 1/n^4$, and the Wallis product for $\pi$.
The Wallis product was already a theorem and of a different kind, so it added the most credibility.

The probability model explains why.
A consequence that was likely anyway, so that $P(B)$ is near $1$, adds little.
A consequence that would be a surprise without $A$ adds much.
For example, if the sum $\sum_{n \ge 1} 1/(n^2 \binom{2n}{n})$ agrees with $\pi^2/18$ to $70$ digits, a chance agreement is about as likely as $10^{-70}$, so the guess $\pi^2/18$ gains very much; see [[identifying the sum of 1/(n^2 C(2n,n))|SQHXXFTXEY]].

### Cases of a new kind

[[A table of polyhedra suggests Euler's formula|HTK0AX3RGC]] shows a second rule.
The tetrahedron, the cube and the octahedron all give $V - E + F = 2$.
A prism or a pyramid adds more support than another regular solid, because it is a new kind of shape.
Then a picture frame with a hole gives $V - E + F = 16 - 32 + 16 = 0$, and the statement needs the hypothesis "convex".
Many checks of one kind share the same blind spot, and here the blind spot was the hole.

Analogy works in the same way.
The integers and the polynomials over a field both have division with remainder and unique factorization.
So a theorem about integers makes the analogous statement about polynomials more credible, and the reverse.

### What it is not

[[Refuting a conjecture by a false consequence|GHWRJ1BQTN]] is not plausible reasoning.
The claim "$2^p - 1$ is prime for every prime $p$" fails at $p = 11$, since $2^{11} - 1 = 2047 = 23 \cdot 89$.
That conclusion is certain, so the condition "only a change in confidence" fails.
A [[mathematical proof|0B94TKFQJX]], for example by [[mathematical induction|0ASJVEFA9J]], is not plausible reasoning for the same reason.
A bare guess such as "the answer is probably $7$" is not plausible reasoning either, because it has no premise.

### The rules you can use

Plausible reasoning cannot make a false statement true, and a false conjecture can have many true consequences, as the [[patterns that eventually fail|A2KSJSQSF6]] show.
The patterns do not chain well: if $C$ supports $B$ and $B$ supports $A$, the support of $C$ for $A$ can be very weak.
One false consequence outweighs any number of true ones, because it refutes $A$ by deduction; this is the job of a [[counterexample|0ED72CTBNP]].
Plausible reasoning is the step from data to a conjecture in [[inductive reasoning|5V35SGEN1T]] and in [[forming conjectures|R2T42N5XGK]].

### Watch out

The first error is to read "more credible" as "true".
The Pólya conjecture on the Liouville function held for every $n$ from $2$ to $906150256$ and failed at $906150257$; [[numerical evidence for conjectures|JFD3QWCX8Z]] tells the story.

The second error is to count cases without weighing them.
In the $n^2 + n + 41$ case, forty prime values are strong evidence that the polynomial gives many primes, and weak evidence that it gives only primes.

The third error is to confuse a pattern with its converse.
"$B$ implies $A$" and "$B$ true" prove $A$.
"$A$ implies $B$" and "$B$ true" only support $A$, and to treat this as a proof is the fallacy of affirming the consequent.

### History

Pólya published *Mathematics and Plausible Reasoning* in two volumes in 1954, with the subtitles *Induction and Analogy in Mathematics* and *Patterns of Plausible Inference*.
His earlier book *How to Solve It* (1945) already has entries on induction, analogy and heuristic reasoning.
He took many of his examples from Leonhard Euler, who described in his papers how he found results by observation and checks.

### Try it

The claim "every odd number greater than $1$ is prime or a square" holds for $3$, $5$, $7$, $9$, $11$ and $13$; test it on the next odd number.
The next is $15 = 3 \cdot 5$, which is neither prime nor a square, so the claim is false.

Which adds more support to "$V - E + F = 2$ for convex polyhedra": a tenth prism or a first pyramid?
The pyramid, since it is a new kind of shape and could fail in a way that prisms cannot.

## Explanations

### L1 human

Suppose a friend claims that a coin is fair.
If it is fair, about half of many tosses should be heads.
You toss it $100$ times and get $52$ heads.
This does not prove that the coin is fair, but it makes the claim more believable.
Mathematicians reason in the same way before they have a proof.
When a test of a guess works out, the guess becomes more believable, and when one test fails, the guess is dead for certain.

### L2 human

We weigh the evidence for $A$: "$f(n) = n^2 + n + 41$ is prime for every $n \ge 0$".
The value $f(0) = 41$ is prime, and so are $f(1) = 43$, $f(2) = 47$ and so on up to $f(39) = 1601$.
Each value is a true consequence of $A$, so $A$ becomes more credible by the fundamental pattern.
How much?
A number near $1000$ is prime with a chance of about $1/\ln 1000 \approx 0.14$, so forty primes in a row would be very unlikely by chance.

But all forty consequences are of one kind.
They support "$f$ gives many primes" just as much as "$f$ gives only primes".
A consequence of a new kind is a value where $f$ has an obvious factor, and $n = 40$ is such a value:
$$f(40) = 40 \cdot (40 + 1) + 41 = 41 \cdot 41.$$
So $A$ is false by deduction.
The typical use is this division of labor: plausible reasoning picks the conjecture, and deduction tests it.
[[Forty prime values of n^2 + n + 41 do not prove a statement|H75AB4EJT5]] tells the same story from the side of proof.

### L3 human

Pólya's patterns are close to Bayesian confirmation theory.
If credibility is a probability, then "$A$ implies $B$" gives $P(A \mid B) = P(A)/P(B)$, which yields the fundamental pattern and the rule that a surprising consequence counts more.
The patterns of analogy have no such simple model.
Philosophers of mathematics still discuss how to give probabilities to mathematical statements, which are true or false by necessity.

Plausible reasoning is the logic of the whole sub-area.
[[Experimental mathematics|BPEPTN0TT9]] supplies verified consequences at high precision, [[numerical evidence|JFD3QWCX8Z]] studies when many verified cases mislead, and [[heuristic arguments|VCQQNJ3SEZ]] supply models from which a conjecture follows.
The [[heuristics of discovery|X1NSTVGDNQ]] describe the search for a conjecture and a proof, and plausible reasoning describes how the results of the search are judged.
