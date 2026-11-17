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
    locator: Proof by Cauchy using forward–backward induction
---

## Summary

Forward-backward induction is a method to prove a statement $P(n)$ for every integer $n \ge 1$ in two parts.
The forward part proves $P(n)$ for every $n$ in an infinite set $S$ of positive integers, usually the powers of $2$ by the step from $P(n)$ to $P(2n)$.
The backward part proves, for every integer $n \ge 2$, that $P(n)$ implies $P(n - 1)$.
Together the two parts give $P(n)$ for every $n \ge 1$, because each $n$ lies below some element of $S$.
The method matters when the step from $n$ to $n + 1$ is hard, but doubling and stepping down are easy, as in Cauchy's proof of the inequality of arithmetic and geometric means.

## Motivation

The inequality of arithmetic and geometric means for $2$ numbers follows from $(\sqrt{a} - \sqrt{b})^2 \ge 0$.
For $4$ numbers, we apply the case $2$ to two pairs and then to the two means, and the same idea doubles the number of terms at each stage.
A direct step from $3$ numbers to $4$, or from $n$ to $n + 1$, is much harder to find.
But a step down is easy: from a list of $n - 1$ numbers, we add their mean as an $n$-th number, and the mean does not change.
Forward-backward induction combines the easy step up by doubling with the easy step down by one.

## Notation

1. The forward part is often written $P(2^k)$ for all $k \ge 0$, and the backward part $P(n) \Rightarrow P(n - 1)$ for all $n \ge 2$.
2. Some books call the method "Cauchy induction", after its first famous use, and some call the second part "backward induction".
3. The name "backward induction" also denotes a different method in game theory: [[backward induction|JEMK4V2PCW]] solves a finite game from its last move. The two methods share only the name.

## Remarks

### Examples

1. [[Cauchy's proof of the AM-GM inequality|HM1J3JN5YG]]: the forward part handles $2^k$ numbers by pairing, and the backward part adds the mean as an extra number.
2. [[Jensen's inequality for midpoint convex functions|2XAK5BWA8G]]: a function with $f\left(\frac{x + y}{2}\right) \le \frac{f(x) + f(y)}{2}$ satisfies $f(\text{mean}) \le \text{mean of } f$ for any number of points.
3. The case $f(x) = x^2$ of example 2 gives $(x_1 + \cdots + x_n)^2 \le n (x_1^2 + \cdots + x_n^2)$ for all real numbers $x_i$. For $1, 2, 6$, this says $81 \le 3 \cdot 41 = 123$.
4. The case $f(x) = -\ln x$ on the positive reals gives again the AM-GM inequality for positive numbers, because $-\ln$ is convex.

### Non-examples

1. A [[single-elimination tournament without byes|THE3TBABMK]] exists for $2^k$ players, so the forward part holds. The backward part fails, because $4$ players work and $3$ players do not.
2. A proof of $P(1)$ together with the backward step $P(n) \Rightarrow P(n - 1)$ proves only $P(1)$. The forward part must cover an infinite set, so that every $n$ lies below some proved case.

### Basic properties

1. The method is valid. Let $n \ge 1$, and choose $s \in S$ with $s \ge n$, which exists because an infinite set of positive integers has no largest element.
2. For $j = 0, 1, \ldots, s - n$, let $C(j)$ be the claim $P(s - j)$. Then $C(0)$ is $P(s)$, which the forward part proves.
3. If $C(j)$ holds and $j < s - n$, then $s - j \ge n + 1 \ge 2$, and the backward part gives $P(s - j - 1)$, which is $C(j + 1)$.
4. By induction on $j$, $C(s - n)$ holds, and $C(s - n)$ is $P(n)$.
5. With $S$ the powers of $2$, the choice $s = 2^n$ always works, because $2^n \ge n$. The smallest choice is the least power of $2$ that is at least $n$.
6. The backward part must hold for every $n \ge 2$, not only for $n$ in $S$. The descent from $s$ to $n$ passes through numbers that are not in $S$.

### History

Augustin-Louis Cauchy used the method in his *Cours d'analyse* of 1821 to prove the inequality of arithmetic and geometric means.
He proved the inequality first for $2^k$ numbers and then stepped down from $n$ numbers to $n - 1$.

### Common errors

1. A student proves the forward part for powers of $2$ and stops. The claim is then proved only for $1, 2, 4, 8, \ldots$, and it can be false for the other values, as the [[tournament example|THE3TBABMK]] shows.
2. A student proves the backward step only from a power of $2$ to the number below it. The descent from $8$ to $5$ also needs the steps from $7$ to $6$ and from $6$ to $5$.
3. In the backward step, a student adds an extra element that is not allowed, for example a point outside the domain of the function. The mean of points of an interval lies in the interval, so the extra point of example 2 is allowed.

## Explanations

### L1 human

Suppose that we can climb a ladder only by jumps that double our height: from rung $1$ to rung $2$, to rung $4$, to rung $8$.
Suppose also that from any rung we can step down one rung.
Then we can reach every rung.
To reach rung $5$, we jump up to rung $8$ and then step down three times, to $7$, $6$ and $5$.
Forward-backward induction proves a claim for every number in this way.

### L2 human

We see how the case $n = 3$ of the AM-GM inequality follows from the case $n = 4$.
Take $a = 1$, $b = 2$ and $c = 6$.

1. The mean of $a$, $b$, $c$ is $d = (1 + 2 + 6)/3 = 3$.
2. Add $d$ as a fourth number. The mean of $1, 2, 6, 3$ is $12/4 = 3$, again $d$.
3. The case $n = 4$ says $1 \cdot 2 \cdot 6 \cdot 3 \le 3^4$, that is, $36 \le 81$.
4. Divide by $d = 3 > 0$: $1 \cdot 2 \cdot 6 \le 3^3$, that is, $12 \le 27$.
5. This is the case $n = 3$ for these numbers, and the same steps work for any nonnegative $a$, $b$, $c$ with $d > 0$.

The typical use of the method is an inequality between means, or any claim about $n$ objects where two groups of $n$ objects combine into one group of $2n$.
A trap is the case $d = 0$ in step 4: we cannot divide by $0$, and this case needs its own argument (all three numbers are then $0$).

### L3 human

The method rests on a simple fact about the order of $\mathbb{N}$: a set of positive integers that is closed downward and is unbounded is the set of all positive integers.
The backward part makes the set of $n$ with $P(n)$ closed downward, and the forward part makes it unbounded.
In analysis, the same pattern appears as "prove the claim on a dense set, then extend it".
A midpoint convex function satisfies Jensen's inequality for all dyadic weights by the forward part, and for all rational weights by the backward part.
With continuity, it then satisfies the inequality for all real weights, so a continuous [[midpoint convex function|1TQ1JQXEWP]] is [[convex|07Q7CNM5WF]].
Other variants of induction in this topic are [[double induction|AABX4YPKRR]] and [[strengthening the induction hypothesis|F94KJC2RXP]].
