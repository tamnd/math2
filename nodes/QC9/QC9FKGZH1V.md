---
tag: QC9FKGZH1V
kind: concept
name: Forward-backward induction
aliases: [cauchy-induction, backward-forward-induction]
msc: ["00A35", "97E50", "26D15"]
topics: [EEH2F76CYQ, G9JFJGY4TQ]
audience: ug2
specializes: [0ASJVEFA9J]
uses: [0ASJVEFA9J, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Forward-backward induction
  - url: https://en.wikipedia.org/wiki/AM%E2%80%93GM_inequality
    locator: Proof by Cauchy using forward-backward induction
---

## Summary

Forward-backward induction proves a claim for every positive integer $n$ in two moves: first jump up to infinitely many values, usually the powers of $2$, and then step down by one to fill the gaps.
It is the method to try when doubling a case is easy but adding one to it is hard.

The standard example is the [[inequality of arithmetic and geometric means|0DRF0F3XC9]]: for nonnegative reals $x_1, \dots, x_n$ with mean $A$, the product $x_1 \cdots x_n$ is at most $A^n$.
For two numbers this is $(x_1 - x_2)^2 \ge 0$.
To go from $n$ numbers to $2n$, split them into two halves with means $B$ and $C$, use the case $n$ on each half and the case $2$ on $B$ and $C$:
$$x_1 \cdots x_{2n} \le B^n C^n = (BC)^n \le \left(\frac{B + C}{2}\right)^{2n}.$$
To go from $n$ numbers down to $n - 1$, add the mean $m$ of $x_1, \dots, x_{n - 1}$ as an extra number, which does not change the mean, and divide the case $n$ by $m$.
[[Cauchy's forward-backward proof of the AM-GM inequality|HM1J3JN5YG]] writes out every step.

In general, let $P(n)$ be a statement for each integer $n \ge 1$, and let $S$ be an infinite set of positive integers.
The *forward part* proves $P(s)$ for every $s \in S$, often by proving $P(1)$ and $P(n) \Rightarrow P(2n)$, which gives every power of $2$.
The *backward part* proves, for every integer $n \ge 2$, that $P(n)$ implies $P(n - 1)$.
Together the two parts give $P(n)$ for every $n \ge 1$.

## Motivation

Some claims about $n$ objects combine well: two groups of $n$ objects merge into one group of $2n$, and the claim for the halves gives the claim for the whole.
Means are the main source of such claims, because the mean of $2n$ numbers is the mean of the two half-means.
A direct step from $n$ to $n + 1$ is often much harder to find, as anyone who tries to get AM-GM for $3$ numbers from the case $2$ discovers.
But a step down is often easy, because one extra object can be chosen so that it changes nothing.
Forward-backward induction combines the easy jump up by doubling with the easy step down by one.

The method sits beside [[mathematical induction|0ASJVEFA9J]] as one of its variants, with [[double induction|AABX4YPKRR]] and [[strengthening the induction hypothesis|F94KJC2RXP]].
Its main uses are in inequalities between means and in the theory of [[convex functions|07Q7CNM5WF]].

## Notation

The forward part is often written as $P(2^k)$ for all $k \ge 0$, and the backward part as $P(n) \Rightarrow P(n - 1)$ for all $n \ge 2$.
Some books call the method "Cauchy induction", after its first famous use, and some call the second part "backward induction".
Watch out for the name: [[backward induction|JEMK4V2PCW]] in game theory is a different method, which solves a finite game from its last move.

## Remarks

### Why the method is valid

Fix $n \ge 1$, and choose $s \in S$ with $s \ge n$, which exists because an infinite set of positive integers has no largest element.
The forward part gives $P(s)$.
If $s > n$, the backward part gives $P(s - 1)$, because $s \ge 2$, and then $P(s - 2)$, and so on.
Each step down starts from a number at least $n + 1 \ge 2$, so the backward part applies, and after $s - n$ steps we reach $P(n)$.
Formally, this is an ordinary induction on $j$ for the claim $P(s - j)$, with $0 \le j \le s - n$.

With $S$ the powers of $2$, the choice $s = 2^n$ always works, because $2^n \ge n$.
The smallest choice is the least power of $2$ that is at least $n$; for $n = 5$ it is $8$, and the descent is
$$P(8) \Rightarrow P(7) \Rightarrow P(6) \Rightarrow P(5).$$

### When to choose it

Choose the method when the claim for $2n$ objects follows from the claim for two groups of $n$, and when one extra object can be added without effect.
The extra object is usually the mean of the others, as in AM-GM.
If no such harmless extra object exists, the backward part fails, and the method gives nothing for the numbers outside $S$.

### A second use: Jensen's inequality

A [[midpoint convex function|1TQ1JQXEWP]] $f$ on an interval satisfies $f\left(\frac{x + y}{2}\right) \le \frac{f(x) + f(y)}{2}$.
The same two moves prove [[Jensen's inequality for midpoint convex functions|2XAK5BWA8G]]: $f$ of the mean of $n$ points is at most the mean of the $n$ values.
For $f(x) = x^2$ and the points $1, 2, 6$ this says
$$\left(\frac{1 + 2 + 6}{3}\right)^2 = 9 \le \frac{1 + 4 + 36}{3} = \frac{41}{3}.$$
Multiplied by $n^2$, the case $f(x) = x^2$ reads $(x_1 + \cdots + x_n)^2 \le n (x_1^2 + \cdots + x_n^2)$, and for $1, 2, 6$ this is $81 \le 123$.
The case $f(x) = -\ln x$ on the positive reals gives AM-GM again, since $-\ln$ is convex.

### What it is not

A [[knockout tournament without byes|THE3TBABMK]] exists for every power of $2$ players, so the forward part holds.
The backward part fails: $4$ players work and $3$ do not, because $3$ players cannot all be in pairs.
So the forward part alone proves nothing about $3$, $5$, $6$ or $7$.

A proof of $P(1)$ together with the backward part also proves nothing new.
The backward part only moves down, so the forward part must reach an infinite set, and every $n$ must lie below some proved case.

### Watch out

The first error is to prove the forward part and stop, which proves the claim only for $1, 2, 4, 8, \dots$.
The tournament shows that the claim can be false at every other value.

The second error is to prove the backward step only from a power of $2$ to the number just below it.
The descent from $8$ to $5$ also needs the steps from $7$ to $6$ and from $6$ to $5$, so the backward part must hold for every $n \ge 2$.

The third error is to add an extra object that is not allowed.
In Jensen's inequality the extra point must lie in the domain of $f$, which is why the domain is an interval: the mean of points of an interval lies in the interval.

### History

Augustin-Louis Cauchy used the method in his *Cours d'analyse* of 1821 to prove the inequality of arithmetic and geometric means.
He proved the inequality first for $2^k$ numbers and then stepped down from $n$ numbers to $n - 1$.

### Try it

First, which backward steps give $P(6)$ from the forward part with $S$ the powers of $2$?
The least power of $2$ at least $6$ is $8$, so the steps are $P(8) \Rightarrow P(7)$ and $P(7) \Rightarrow P(6)$.

Second, check AM-GM for $2, 4, 6$ by the backward step from $4$ numbers.
The mean is $4$, so add $4$: the case $4$ says $2 \cdot 4 \cdot 6 \cdot 4 = 192 \le 4^4 = 256$, and division by $4$ gives $48 \le 64 = 4^3$.

## Explanations

### L1 human

Suppose that you can climb a ladder only by jumps that double your height: from rung $1$ to rung $2$, then to rung $4$, then to rung $8$.
Suppose also that from any rung you can step down one rung.
Then you can reach every rung.
To reach rung $5$, jump up to rung $8$ and then step down three times, to $7$, $6$ and $5$.
Forward-backward induction proves a claim for every number in this way.

### L2 human

See how the case $n = 3$ of AM-GM follows from the case $n = 4$, for $a = 1$, $b = 2$ and $c = 6$.
The mean is $d = (1 + 2 + 6)/3 = 3$.
Add $d$ as a fourth number, and the mean of $1, 2, 6, 3$ is $12/4 = 3$, still $d$.
The case $n = 4$ gives
$$1 \cdot 2 \cdot 6 \cdot 3 = 36 \le 3^4 = 81,$$
and division by $d = 3$ gives $1 \cdot 2 \cdot 6 = 12 \le 3^3 = 27$, which is the case $n = 3$ for these numbers.
The same steps work for any nonnegative $a$, $b$, $c$ with $d > 0$.
Watch out for $d = 0$: we cannot divide, and this case needs its own argument, which is short because all three numbers are then $0$.

### L3 human

The method rests on a fact about the order of $\mathbb{N}$: a set of positive integers that is closed downward and unbounded contains every positive integer.
The backward part makes the set of $n$ with $P(n)$ closed downward, and the forward part makes it unbounded.

In the theory of convex functions, the two parts have a clear meaning.
For a midpoint convex function, the forward part alone gives Jensen's inequality with dyadic weights such as $\tfrac{3}{8}$ and $\tfrac{5}{8}$.
The backward part gives equal weights for every $n$, and repeating points then gives all rational weights.
With continuity, a limit gives all real weights, so a continuous midpoint convex function is [[convex|07Q7CNM5WF]].
This two-stage pattern, prove on a dense set and extend by continuity, is the analyst's version of filling the gaps.
