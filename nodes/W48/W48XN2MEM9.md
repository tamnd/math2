---
tag: W48XN2MEM9
kind: concept
name: Hypotheses and conclusion of a theorem
aliases: [hypothesis-of-a-theorem, conclusion-of-a-theorem, standing-assumption, sharp-hypothesis]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, KK5F0F03ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem
    locator: Informal account of theorems
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

A theorem is a promise with conditions: when every condition holds, the promised conclusion holds too.
To read a theorem is to find its conditions and its promise, and to use it is to check every condition in the case at hand.
Most [[theorems|KK5F0F03ZW]] have the form "if $H_1, H_2, \dots, H_k$, then $C$".
The statements $H_1, \dots, H_k$ are the *hypotheses*, and $C$ is the *conclusion*.
The theorem asserts that $C$ is true in every case in which all the hypotheses are true, and it asserts nothing about the other cases.
A *standing assumption* is a hypothesis that a text fixes once for a chapter or a book and then leaves out of each statement.
A hypothesis is *needed* when the statement becomes false without it, and it is *sharp* when no weaker condition of the same kind is enough.

## Motivation

[[Rolle's theorem|0194DY35BG]] says: if $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then $f'(c) = 0$ for some $c$ in $(a, b)$.
Try it on $f(x) = |x|$ on $[-1, 1]$.
The function is continuous and $f(-1) = 1 = f(1)$, but its derivative is $-1$ or $1$ wherever it exists, so it is never $0$.
This does not contradict the theorem: $|x|$ has no derivative at $0$, so the second hypothesis fails, and the theorem makes no promise.

So a reader must check every hypothesis before using a theorem, and an author must state every hypothesis that the proof uses.
[[The three failures of Rolle's theorem|YRC4NN8KDJ]] drop each hypothesis in turn.
The same reading skill returns in [[abstraction and generalization|976RZZCT1H]], where weakening a hypothesis is the way a theorem grows.

## Notation

Mathematical English marks hypotheses with "if", "let", "suppose", "assume" and "given", and it marks the conclusion with "then".
In symbols, "if $H$, then $C$" is $H \Rightarrow C$.
Many statements hide this form.
"Every continuous function on $[a, b]$ is bounded" means "if $f$ is continuous on $[a, b]$, then $f$ is bounded".
"Let $G$ be a finite group and $H$ a subgroup; then $|H|$ divides $|G|$" has two hypotheses, "$G$ is a finite group" and "$H$ is a subgroup of $G$".

## Remarks

### Testing a hypothesis by dropping it

To see why a hypothesis is there, keep all the others, drop that one, and look for a case where the conclusion fails.
The [[extreme value theorem|0WS1A8E2P9]] says that a continuous function on a closed and bounded interval has a largest and a smallest value.
Drop "closed": $f(x) = x$ on $(0, 1)$ is continuous on a bounded interval, but it has no largest value, since every $x$ is beaten by $\tfrac{1 + x}{2}$.
Drop "bounded": $f(x) = x$ on $[0, \infty)$ is continuous on a closed interval, and it grows without limit.
Drop "continuous": a function with a jump on $[0, 1]$ can approach $1$ without reaching it.
[[The full test of the extreme value theorem|TK8AKSWV18]] writes out each case.

### What happens when a hypothesis fails

A theorem says nothing about a case in which a hypothesis fails.
In such a case the conclusion can still hold.
For $f(x) = x^2$ on $[-1, 2]$ we have $f(-1) = 1 \ne 4 = f(2)$, so Rolle's theorem does not apply, and yet $f'(0) = 0$.
A failed hypothesis removes the guarantee, not the possibility.

In the other direction, if the conclusion fails, then some hypothesis must fail, which is the contrapositive of the theorem.
That is how the theorem is often used.
For example, $f(x) = x^3 + x$ has $f'(x) = 3x^2 + 1 > 0$ everywhere, so by Rolle's theorem no two points $a < b$ have $f(a) = f(b)$, and $f$ has at most one real root.

### Standing assumptions

Many algebra books state once that "ring" means a commutative ring with an identity element, and every later theorem uses this without saying so.
The theorem "every nonzero ring has a maximal ideal" depends on that assumption.
Take the rational numbers with their usual addition and with the product $xy = 0$ for all $x, y$, a ring without identity.
Its ideals are its additive subgroups, and $\mathbb{Q}$ has no maximal subgroup, so the theorem fails.
So before you cite a result, find the standing assumptions of the book it comes from.

### Sharp hypotheses

For every integer $n \ge 5$ we have $2^n > n^2$.
The hypothesis $n \ge 5$ is sharp, because $2^4 = 16 = 4^2$, so $n \ge 4$ would make the statement false.

Here is the proof by [[mathematical induction|0ASJVEFA9J]].
For $n = 5$, $2^5 = 32 > 25$.
If $2^n > n^2$ for some $n \ge 5$, then $2^{n+1} > 2n^2$.
For $n \ge 3$ we have $n^2 - 2n - 1 = (n - 1)^2 - 2 \ge 2 > 0$, so
$$2n^2 = n^2 + n^2 > n^2 + 2n + 1 = (n + 1)^2.$$
So $2^{n+1} > (n + 1)^2$, and the claim holds for every $n \ge 5$.

### What is not a hypothesis

The "if" in a definition does not introduce a hypothesis.
In "an integer $n$ is even if $n = 2k$ for some integer $k$", the "if" means "if and only if", as [[the definition of even|1YJTRBDGC3]] shows.
The induction hypothesis is not a hypothesis of the theorem either: it is an assumption made inside one step of the proof.
The Riemann hypothesis is not a hypothesis of any theorem.
It is an open conjecture, and "hypothesis" in its name means "a claim not yet proved".

### Watch out

The first error is to apply a theorem without checking every hypothesis, as with $|x|$ and Rolle's theorem.
The second error is to use the converse.
A differentiable $f$ with $f'(c) = 0$ need not have $f(a) = f(b)$: $x^2$ on $[-1, 2]$ shows it.
The third error is to drop two hypotheses at once in a test.
If $x$ on $(0, \infty)$ has no largest value, you have not learned which of "closed" and "bounded" was responsible.

### History

The Greek word "hypothesis" means a thing placed under, a supposition.
Proclus, in his commentary on the first book of Euclid, named six parts of a proposition: the enunciation, the setting out, the specification of what is required, the construction, the proof and the conclusion.
The enunciation states the hypotheses and the conclusion in general terms, and the setting out applies the hypotheses to a named figure.

### Try it

First, the theorem "if $n$ is odd, then $n^2 \equiv 1 \pmod 8$" has one hypothesis; show that it is needed.
Take $n = 2$: then $n^2 = 4$, which is not $1$ modulo $8$.

Second, find the smallest $n_0$ such that $n! > 2^n$ for every $n \ge n_0$.
It is $n_0 = 4$, since $4! = 24 > 16$, while $3! = 6 < 8$; the induction step multiplies the left side by $n + 1 \ge 5$ and the right side by $2$.

## Explanations

### L1 human

A theorem is like a guarantee with conditions: if these things are true, then that thing is true.
The conditions are the hypotheses, and the promise is the conclusion.
For example: if a whole number ends in $0$, then it is divisible by $5$.
The number $30$ meets the condition, so the promise applies.
The number $35$ does not end in $0$, so this theorem says nothing about it, even though $35$ is divisible by $5$.
Before you use a theorem, check that every condition holds.

### L2 human

Here is a full test of [[Fermat's little theorem|0M25PRN3WQ]]: if $p$ is prime and $p$ does not divide the integer $a$, then $a^{p-1} \equiv 1 \pmod p$.
First a case with both hypotheses, $p = 5$ and $a = 2$:
$$2^4 = 16 = 3 \cdot 5 + 1, \qquad \text{so } 2^4 \equiv 1 \pmod 5.$$
Now drop "$p$ is prime" and keep "$p$ does not divide $a$", with $p = 4$ and $a = 3$:
$$3^3 = 27 = 6 \cdot 4 + 3, \qquad \text{so } 3^3 \equiv 3 \pmod 4.$$
The conclusion fails, so primality is needed.
Then drop "$p$ does not divide $a$" and keep "$p$ is prime", with $p = 3$ and $a = 3$: $3^2 = 9 \equiv 0 \pmod 3$, so that hypothesis is needed too.
Each failing case shows what its hypothesis protects against, and that is the point of the test.

### L3 human

A theorem $H_1 \wedge \dots \wedge H_k \Rightarrow C$ splits the cases into those that meet every hypothesis and the rest, and it speaks only about the first group.
Asking which hypotheses are needed leads to two kinds of new result.
Counterexamples show that a hypothesis cannot be dropped, and books such as "Counterexamples in Analysis" and "Counterexamples in Topology" collect them.
Generalizations replace a hypothesis by a weaker one, as the [[law of cosines|060ZVZBV3E]] drops the right angle of the [[Pythagorean theorem|0VP3A1290K]].

Sharpness also has a quantitative side.
A bound is sharp when some case attains it, or comes as close as you like, and finding the weakest working hypotheses is a main source of new definitions.
The search is described further under [[abstraction and generalization|976RZZCT1H]].
