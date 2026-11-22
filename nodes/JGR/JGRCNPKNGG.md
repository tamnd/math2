---
tag: JGRCNPKNGG
kind: concept
name: Minimal counterexample
aliases: [minimal-criminal, smallest-counterexample, least-criminal]
msc: ["00A35", "97E50"]
topics: [EEH2F76CYQ, G9JFJGY4TQ]
audience: ug1
uses: [01BX15HSRR, 0KMVFSHFGZ, 0J0XBKG64S, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_counterexample
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Minimal_counterexample
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: Number theory
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Summary

A minimal counterexample proof says: if the claim fails, look at the smallest case where it fails, and show that this case cannot exist.
The smallest bad case is useful because every smaller case is good, so the proof may use all of them at once.

Here is a first proof of this kind.
Every integer $n \ge 2$ has a prime divisor.
Suppose not, and let $m$ be the least integer $m \ge 2$ with no prime divisor.
Then $m$ is not prime, since a prime divides itself, so $m = ab$ with $1 < a < m$.
The number $a$ is smaller than $m$ and at least $2$, so $a$ has a prime divisor $p$, and $p$ divides $m$.
This contradicts the choice of $m$, so no such $m$ exists.

In general, the method proves that every object $x$ of a set $X$ has a property $P$.
It uses a size function $s \colon X \to \mathbb{N}$ into the [[natural numbers|0MWKJ44V5A]].
For a [[contradiction|0J0XBKG64S]], suppose that the set $C$ of [[counterexamples|0ED72CTBNP]] is not empty.
The [[well-ordering principle|01BX15HSRR]] gives a least value $m$ of $s$ on $C$, and we fix $x_0 \in C$ with $s(x_0) = m$.
Then every $x \in X$ with $s(x) < m$ has the property $P$.
The proof ends with a contradiction: it builds a counterexample $x_1$ with $s(x_1) < m$, or it shows that $x_0$ has the property after all.

## Motivation

Many claims about integers, graphs and groups are proved by breaking an object into smaller objects of the same kind.
A proof by [[strong induction|0KMVFSHFGZ]] must name the induction variable and state the hypothesis for all smaller sizes.
The minimal counterexample says all of this in one sentence: "let $x_0$ be a counterexample of the least size".
After that sentence, the proof studies one object, $x_0$, and it may use every smaller object freely.
Many proofs in number theory, graph theory and finite group theory start with this sentence.

The method is close to [[infinite descent|0EFYCFHYFG]], where each counterexample gives a smaller one.
It is the same as [[induction on size|B2D8PTFNN1]] read backward, and the [[equivalence of induction and well-ordering|J2P9FWBP3Q]] explains why the two always agree.

## Notation

The size is often written $|x|$, $s(x)$ or $n(x)$.
It can be the value of an integer, the number of vertices of a graph, the order of a group or the degree of a polynomial.
Books say "minimal counterexample", "least counterexample" or "smallest counterexample", and the three names mean the same thing.
Graph theorists also say "minimal criminal".
The word "minimal" refers to the size $s$, not to the object: two different counterexamples can both have the least size.

## Remarks

### Why the method is valid

The set $s(C) = \{ s(x) : x \in C \}$ is a nonempty set of natural numbers.
The well-ordering principle gives it a least element $m$, so a counterexample of least size exists.
This is the only place where the method uses a property of $\mathbb{N}$, and it is the step that a careful proof must justify.

The method is strong induction in contrapositive form.
Strong induction proves the step "if every $x$ with $s(x) < n$ has $P$, then every $x$ with $s(x) = n$ has $P$".
A minimal counterexample proof proves the same step by contradiction: it supposes the hypothesis of the step and the failure of the conclusion at one $x_0$.
So the two methods prove exactly the same statements, and the choice between them is a choice of style.

### The steps in order

1. State the claim: every $x \in X$ has the property $P$.
2. Choose a size $s(x) \in \mathbb{N}$.
   The choice decides which smaller objects the proof can use.
3. Suppose that the claim is false, and take a counterexample $x_0$ of least size $m$.
4. Record what this gives: every $x$ with $s(x) < m$ has $P$.
5. Use the structure of $x_0$ to build a smaller counterexample, or to show that $x_0$ has $P$.
6. Conclude that no counterexample exists.

### Three worked uses

The [[prime divisor example|VSHHBWWXVX]] is the proof in the Summary, written out with each step.
For $n = 91 = 7 \cdot 13$, the smaller factor $7$ is prime, and it divides $91$.

The [[coloring example|D2DW12A5M8]] proves that a graph whose vertices have degree at most $D$ has a proper coloring with $D + 1$ colors.
Take a counterexample with the fewest vertices and delete one vertex $v$.
The smaller graph has a coloring, and the at most $D$ neighbors of $v$ leave one of the $D + 1$ colors free for $v$.

The [[irrationality of the square root of 2|0DZGSDHD92]] has a proof of this kind.
Suppose that $\sqrt{2} = a/b$ with positive integers and the least possible $b$.
Then $b < a < 2b$, and a short computation gives
$$\frac{2b - a}{a - b} = \frac{(2 - \sqrt{2}) b}{(\sqrt{2} - 1) b} = \frac{\sqrt{2}(\sqrt{2} - 1)}{\sqrt{2} - 1} = \sqrt{2}.$$
The new denominator $a - b$ is a positive integer smaller than $b$, which contradicts the choice of $b$.

### When the least element does not exist

The method needs a size with values in $\mathbb{N}$.
The [[false argument over the positive rationals|7YZWT2AA6R]] "proves" that every positive rational is at least $1$.
It takes a least rational $q < 1$ and finds $q/2$ below it, but the rationals in $(0, 1)$ have no least element, so the first step names nothing.
The same failure occurs with a size in $\mathbb{Z}$: the set $\{-1, -2, -3, \dots\}$ has no least element.

A proof that picks "a counterexample" without the word "least" is a plain [[proof by contradiction|0J0XBKG64S]].
It may be correct, but it cannot use the smaller cases, because nothing says that they are good.

### Watch out

The first error is to forget that the smaller object must lie in the set $X$.
In the coloring proof the smaller graph must again have all degrees at most $D$.
Deleting a vertex never raises a degree, so the check passes there; adding an edge instead would break it.

The second error is to build a smaller object and not show that it is again a counterexample.
A smaller object that has the property contradicts nothing.
In the prime divisor proof the contradiction comes from the other direction: the minimality of $m$ says that $a$ has a prime divisor, and that divisor passes to $m$.

The third error is the factorization $m = 1 \cdot m$, which gives no smaller number.
The proof must use a divisor strictly between $1$ and $m$.

### History

Euclid's *Elements*, Book VII, Proposition 31, proves that each composite number has a prime divisor with an argument of this kind.
In graph theory the phrase "minimal criminal" is common in work on the [[four color theorem|0M406JC8J1]], where proofs study a smallest map that needs five colors.

### Try it

First, prove that every integer $n \ge 1$ can be written as $2^e k$ with $e \ge 0$ and $k$ odd.
Take the least counterexample $m$.
It is even, because an odd $m$ is $2^0 m$, so $m = 2 m'$ with $1 \le m' < m$.
Then $m' = 2^e k$ with $k$ odd, and $m = 2^{e+1} k$, a contradiction.

Second, say what goes wrong with "every positive real $x$ satisfies $x \ge 1$, by a least counterexample".
The counterexamples form the interval $(0, 1)$, which has no least element, so a least counterexample does not exist and the proof never starts.

## Explanations

### L1 human

Suppose that a claim about whole numbers is false for some numbers.
Then there is a smallest number for which it fails, because whole numbers cannot go down forever.
Call it the smallest bad number.
Every number below it is good, and we may use that.
If we now find an even smaller bad number, we have a contradiction, so no bad number exists.
For example, the smallest number from $2$ on with no prime divisor cannot be $6$, because then $2$, which is smaller, would have no prime divisor either.

### L2 human

We prove that every integer $n \ge 1$ is a sum of distinct powers of $2$, with a least counterexample.
Suppose not, and let $m$ be the least integer $m \ge 1$ that is not such a sum.
The number $1 = 2^0$ is such a sum, so $m \ge 2$.
Let $2^k$ be the largest power of $2$ with $2^k \le m$, so that
$$2^k \le m < 2^{k+1}.$$
If $m = 2^k$, then $m$ is a sum of one power of $2$, which is a contradiction, so $m > 2^k$.
Put $r = m - 2^k$.
Then $1 \le r < m$, so $r$ is a sum of distinct powers of $2$ by the choice of $m$.
Also $r < 2^{k+1} - 2^k = 2^k$, so $2^k$ is not one of the powers in the sum for $r$.
So $m = 2^k + r$ is a sum of distinct powers of $2$, a contradiction.

Check: $m = 13$ gives $2^k = 8$ and $r = 5 = 4 + 1$, so $13 = 8 + 4 + 1$.
The typical use of the method is a statement in which an object splits into smaller objects of the same kind.
Watch out for the inequality $r < 2^k$: without it the sum for $m$ could repeat the power $2^k$.

### L3 human

The method works in every set with a [[well-founded relation|0DQPNJNPYK]], because a relation is well-founded exactly when each nonempty subset has a minimal element.
So the minimal counterexample is well-founded induction read backward, and it extends to the ordinals, to the lexicographic order on pairs used in [[double induction|AABX4YPKRR]], and to the subterm order on formulas.
In finite group theory the size is the order of the group.
The proof of the [[Feit-Thompson theorem|6VK9RSG13Q]] studies a counterexample of least order, whose proper subgroups are then all solvable.
In graph theory a minimal counterexample is treated as a structure: one shows that it cannot contain certain small configurations, and then that every candidate contains one of them.
