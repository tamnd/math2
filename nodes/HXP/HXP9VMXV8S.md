---
tag: HXP9VMXV8S
kind: concept
name: Averaging argument
aliases: [averaging-argument]
msc: ["00A35", "05D40"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: ug1
uses: [0F8YBHF2W3, 0KS0KRDV4Y, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Probabilistic_method
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Maximum_cut
    locator: lead section
---

## Summary

An averaging argument proves that a good object exists by computing the average score of all the objects: some object scores at least the average, and some object scores at most the average.
The average is often easy to compute even when no single good object is easy to find.

Here is a first problem.
Show that every [[graph|00C0BR7D7H]] with $m$ edges has a [[bipartite|0ZVQKTRKVQ]] subgraph with at least $m/2$ edges.
Split the $n$ vertices into two sides in all $2^n$ ways, and score each split by the number of edges that cross it.
A fixed edge $uv$ crosses exactly half of the splits, those that put $u$ and $v$ on different sides, so the average score is $m/2$.
Some split scores at least the average, and its crossing edges form a bipartite subgraph with at least $m/2$ edges; [[the full count|QEP266HZKS]] gives every step.

The principle behind it is exact.
Let $x_1, \ldots, x_n$ be real numbers with $n \ge 1$, and let
$$\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$
be their arithmetic mean.
Then there is an index $i$ with $x_i \ge \bar{x}$, and there is an index $j$ with $x_j \le \bar{x}$.

## Motivation

Many existence questions ask for one object with a large score: a vertex of high degree, a cut with many edges, an integer with many divisors.
Finding the best object can be hard, and a search over all objects can be very long.
The sum of the scores over all objects is often easy, because it can be counted a second way, by [[double counting|0F8YBHF2W3]].
The averaging argument turns that easy sum into an existence result.

The method is the [[pigeonhole principle|0HGVCWQGY3]] for real-valued scores, and it is the first step of the [[probabilistic method|3B55HNS754]].
It appears in graph theory, in number theory, in additive combinatorics and in complexity theory, where averaging over random strings fixes a good one.

## Notation

The arithmetic mean of $x_1, \ldots, x_n$ is written $\bar{x}$ or $\frac{1}{n}\sum_{i=1}^{n} x_i$.
For a function $f$ on a finite nonempty set $S$, the average is $\frac{1}{|S|}\sum_{s \in S} f(s)$.
In the language of probability, this average is the [[expected value|0WQNRCNY3M]] $\mathbb{E}[f]$ under the uniform distribution on $S$, and some books then call the method the first moment method.

## Remarks

### Why it works, and its forms

Suppose every $x_i$ were below the mean.
Adding the $n$ inequalities $x_i < \bar{x}$ gives
$$x_1 + \cdots + x_n < n \bar{x} = x_1 + \cdots + x_n,$$
which is false, so some $x_i \ge \bar{x}$, and the same argument with the inequalities reversed gives some $x_j \le \bar{x}$.
If the values are not all equal, both inequalities can be made strict.

Three forms are used often.
When each $x_i$ is an integer, some $x_i \ge \lceil \bar{x} \rceil$, and this is the [[generalized pigeonhole principle|0BY7GN3449]]: let $x_i$ be the number of objects in box $i$.
With positive weights $w_i$, some $x_i$ is at least the weighted mean $\sum_i w_i x_i / \sum_i w_i$, by the same proof.
The average of a sum $f + g$ is the sum of the averages, which is [[linearity of expectation|0P7PTC8DDE]] for the uniform distribution, so an average can be computed term by term.

### Choosing what to average

The skill is the choice of the family and the score.
The family must be finite and nonempty, and the total score must be computable.
The signal is a score that is a sum of simple 0-or-1 terms, one for each small piece, such as an edge that crosses a split.
Then the total is a count of pairs (object, piece), and you count the pairs by the pieces instead.

Here is the simplest case.
A graph with $n \ge 1$ vertices and $m$ edges has degree sum $2m$ by the [[handshaking lemma|0XAP8WHNES]], so the average [[degree|0KS0KRDV4Y]] is $2m/n$.
For $7$ vertices and $12$ edges, the average is
$$\frac{2 \cdot 12}{7} = \frac{24}{7} \approx 3.43,$$
so some vertex has degree at least $3.43$, and degrees are integers, so it has degree at least $4$.
Check: if all seven degrees were at most $3$, the degree sum would be at most $21 < 24$.

### Divisors and Mantel's theorem

In number theory, let $d(k)$ be the number of divisors of $k$.
The pairs $(j, k)$ with $j \mid k \le n$ can be counted by $j$, and this gives
$$\sum_{k=1}^{n} d(k) = \sum_{j=1}^{n} \left\lfloor \frac{n}{j} \right\rfloor.$$
For $n = 12$ both sides are $35$, so some $k \le 12$ has $d(k) \ge 35/12$, that is, $d(k) \ge 3$.
The [[average number of divisors|320MBBJETV]] works this out for every $n$.

An average can also bound a total from above.
In a triangle-free graph, adjacent vertices $u$ and $v$ have no common neighbor, so $d(u) + d(v) \le n$.
Summing over the $m$ edges counts each vertex $v$ once for each of its $d(v)$ edges, so $\sum_v d(v)^2 \le mn$.
The square of the average is at most the average of the squares, by the [[Cauchy-Schwarz inequality|0RFWW56Y22]], so
$$(2m)^2 = \Big(\sum_v d(v)\Big)^2 \le n \sum_v d(v)^2 \le n \cdot mn,$$
and $m \le n^2/4$, which is [[Mantel's theorem|0MXEHSCYCS]].

### What the average does not say

The average gives one element on each side of it, and nothing about the others.
It does not give an element equal to the average: the [[star|NJB31J8DZT]] $K_{1,3}$ has average degree $3/2$, and every degree is $1$ or $3$, as [[the star example|88TSKF4595]] shows.
It does not bound every element either: a class with marks $0$ and $100$ has average $50$, and the student with $0$ is far below it.
And it needs a finite family: the positive integers have no average, so "some positive integer is at least the average" has no meaning.

### Watch out

The most common slip is to conclude that every element is at least the average.
In $K_{1,3}$ the three leaves have degree $1 < 3/2$.
The second slip is to forget the rounding.
An integer that is at least $20.2$ is at least $21$, and this extra step often gives the sharp bound.
The third slip is a wrong family, where an object is counted twice or the weights are unknown, so the computed number is not the average of anything.

### History

Paul Erdős used averaging over random choices in many existence proofs.
In 1965 he proved that every set of $n$ nonzero integers has a [[sum-free|7SHV2SPYP6]] subset with more than $n/3$ elements, by averaging over multiplications modulo a prime.
The method is now the simplest case of the use of expectation in the probabilistic method.

### Try it

First, ten numbers stand on a circle, and their sum is $100$.
Show that some three consecutive numbers have sum at least $30$.
The ten triples of consecutive numbers use each number three times, so their sums add to $300$, the average triple sum is $30$, and some triple reaches it.

Second, a $5 \times 5$ table of integers has total $101$.
Show that some row has sum at least $21$.
The average row sum is $101/5 = 20.2$, so some row sum is at least $20.2$, and an integer at least $20.2$ is at least $21$.

## Explanations

### L1 human

If the average of some numbers is $10$, then at least one of the numbers is $10$ or more.
If every number were less than $10$, the average would be less than $10$ too.
For example, three friends have $36$ sweets in total, so the average is $12$.
Then at least one friend has $12$ sweets or more, even if you do not know who.
This simple fact proves that good objects exist without a search for them.

### L2 human

Here is a typical problem: the numbers $1, 2, \ldots, 10$ are placed around a circle in some order.
Show that some three neighbors in a row have sum at least $17$.
There are $10$ triples of consecutive places, and each number lies in exactly $3$ of them.
So the sum of all ten triple sums is
$$3(1 + 2 + \cdots + 10) = 3 \cdot 55 = 165,$$
and the average triple sum is $16.5$.
Some triple sum is at least $16.5$, and triple sums are integers, so some triple sum is at least $17$.

The problem shows the usual pattern.
Count a total in a second way (here, by the numbers instead of by the triples), divide by the number of objects, and round.
Watch out for the other side: the same count gives some triple with sum at most $16.5$, so at most $16$, and the two claims need the two halves of the principle.

### L3 human

In probabilistic language, a random variable $X$ on a finite probability space takes a value at least $\mathbb{E}[X]$ with positive probability.
This is the first moment method, and with [[linearity of expectation|0P7PTC8DDE]] it gives most of the simple results of the [[probabilistic method|3B55HNS754]].
A weighted average is an expectation under a nonuniform distribution, and an average over a group, over all translates or all dilates of a set, is a standard tool in additive combinatorics.

The same idea appears in analysis as the mean value theorem for integrals: a continuous function on a closed bounded interval takes its integral mean as a value.
In complexity theory, averaging over random strings shows that a good fixed string exists, and this turns randomized algorithms into nonuniform ones.
Averaging extends the [[pigeonhole principle|0HGVCWQGY3]], uses [[double counting|0F8YBHF2W3]] to find its totals, and is the quantitative form of the [[counting arguments for existence|1KVSS0KRZA]].
