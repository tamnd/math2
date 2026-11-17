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

An averaging argument proves that some element of a finite family has a large value, or a small value, by a comparison with the average.
Let $x_1, \ldots, x_n$ be real numbers with $n \ge 1$, and let $\bar{x} = (x_1 + \cdots + x_n)/n$ be their arithmetic mean.
Then there is an index $i$ with $x_i \ge \bar{x}$, and there is an index $j$ with $x_j \le \bar{x}$.
The method has three steps: choose a finite set and a score on it, compute the average score, and pick an element on the correct side.
The average is often computed by [[double counting|0F8YBHF2W3]].
The method is important because the average is often easy to compute when no single element is easy to find.

## Motivation

Many existence questions ask for one object with a large score: a vertex of high degree, a cut with many edges, a number with many divisors.
To find the best object can be hard, and a search over all objects can be very long.
The sum of the scores over all objects is often easy, because it can be counted in a second way.
The averaging argument turns the easy sum into an existence result.
It is the [[pigeonhole principle|0HGVCWQGY3]] for real-valued scores: if each object scored below the average, the sum of the scores would be below the sum that we computed.

## Notation

The arithmetic mean of $x_1, \ldots, x_n$ is written $\bar{x}$ or $\frac{1}{n}\sum_{i=1}^{n} x_i$.
For a function $f$ on a finite nonempty set $S$, the average is $\frac{1}{|S|}\sum_{s \in S} f(s)$.
In the language of probability, this average is the [[expected value|0WQNRCNY3M]] $\mathbb{E}[f]$ of $f$ under the uniform distribution on $S$.
Some books call the method the "first moment method" in this probabilistic form.

## Remarks

### Examples

- A [[graph|00C0BR7D7H]] with $n \ge 1$ vertices and $m$ edges has a vertex of [[degree|0KS0KRDV4Y]] at least $2m/n$. The [[handshaking lemma|0XAP8WHNES]] gives the sum $2m$ of the degrees, and the average degree is $2m/n$.
- Every graph with $m$ edges has a [[bipartite|0ZVQKTRKVQ]] subgraph with at least $m/2$ edges. The average size of a cut over all $2^n$ vertex subsets is $m/2$, as [[this example|QEP266HZKS]] shows.
- Some integer $k$ with $1 \le k \le n$ has at least $H_n - 1$ divisors, where $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$. The total number of divisors of $1, \ldots, n$ is $\sum_{d=1}^{n} \lfloor n/d \rfloor$, as [[this example|320MBBJETV]] shows.
- Five integers with sum $101$ include one that is at least $21$. The average is $101/5 = 20.2$, so some integer is at least $20.2$, and an integer at least $20.2$ is at least $21$.
- A triangle-free graph with $n$ vertices has at most $n^2/4$ edges, which is [[Mantel's theorem|0MXEHSCYCS]]. Adjacent vertices $u, v$ have $d(u) + d(v) \le n$, and summing over the $m$ edges gives $\sum_v d(v)^2 \le mn$. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] compares the square of the average degree with the average of the squares: $(2m)^2 \le n \sum_v d(v)^2 \le n \cdot mn$, so $m \le n^2/4$.

### Non-examples

- The average does not give an element equal to the average. The [[star|NJB31J8DZT]] $K_{1,3}$ has average degree $3/2$ and no vertex of degree $3/2$, as [[this example|88TSKF4595]] shows.
- The average does not bound every element. A class with marks $0$ and $100$ has average $50$, and the student with $0$ is far below it.
- The average of an infinite family can fail to exist. The positive integers have no average, so the statement "some positive integer is at least the average" has no meaning.

### Basic properties

- Existence on both sides: if $x_i < \bar{x}$ for every $i$, then $\sum_i x_i < n\bar{x} = \sum_i x_i$, which is false. So some $x_i \ge \bar{x}$, and the same argument gives some $x_j \le \bar{x}$.
- Integer rounding: if each $x_i$ is an integer, then some $x_i \ge \lceil \bar{x} \rceil$. This form contains the [[generalized pigeonhole principle|0BY7GN3449]]: put $N$ objects in $k$ boxes, and let $x_i$ be the number of objects in box $i$.
- Weighted form: if $w_1, \ldots, w_n > 0$, then some $x_i$ is at least the weighted mean $\sum_i w_i x_i / \sum_i w_i$. The proof is the same.
- Strictness: if the $x_i$ are not all equal, then some $x_i > \bar{x}$ and some $x_j < \bar{x}$.
- Linearity: the average of $f + g$ is the sum of the averages. This is [[linearity of expectation|0P7PTC8DDE]] for the uniform distribution, and it lets us compute an average term by term.

### When it applies

The method applies when a problem asks for one object with a score above or below a threshold.
The total score over a natural family must be computable.
The signal is a sum that can be counted in two ways, or a score that is a sum of simple indicator terms.
The method fails when the threshold is above the maximum: the average never exceeds the maximum, so a bound that needs more than the average needs another idea.

### History

Paul Erdős used averaging over random choices in many existence proofs.
In 1965 he proved that every set of $n$ nonzero integers has a [[sum-free|7SHV2SPYP6]] subset with more than $n/3$ elements.
His proof averages over multiplications modulo a prime.
The method is now a part of the [[probabilistic method|3B55HNS754]], where it is the simplest case of the use of expectation.

### Common errors

- To conclude that every element is at least the average. Only some element is, and some other element is at most the average.
- To average over the wrong family. The family must be finite and nonempty, and each object must have its score counted once, or with known weights.
- To forget the rounding. An integer score at least $20.2$ is at least $21$, and this extra step often gives the sharp bound.

## Explanations

### L1 human

If the average of some numbers is $10$, then at least one of the numbers is $10$ or more.
If every number were less than $10$, the average would be less than $10$ too.
For example, three friends have $36$ sweets in total, so the average is $12$.
Then at least one friend has $12$ sweets or more.
This simple fact proves that good objects exist, without a search for them.

### L2 human

We show that every graph with $7$ vertices and $12$ edges has a vertex of degree at least $4$.

1. Let the vertices be $v_1, \ldots, v_7$ with degrees $d_1, \ldots, d_7$.
2. By the handshaking lemma, $d_1 + \cdots + d_7 = 2 \cdot 12 = 24$, because each edge has two ends.
3. The average degree is $24/7 \approx 3.43$.
4. By the averaging argument, some $d_i \ge 24/7$.
5. The degree $d_i$ is an integer, and the least integer at least $24/7$ is $4$. So $d_i \ge 4$.

The typical use is in this order: count a total in a second way, divide by the number of objects, and round.
A trap is to treat the lower side as automatic, for example the claim "some vertex has degree at most $3$".
This claim is also true here, but it needs the second half of the principle, $d_j \le 24/7$, and then rounding down gives $d_j \le 3$.

### L3 human

In probabilistic language, a random variable $X$ on a finite probability space takes some value at least $\mathbb{E}[X]$ with positive probability.
This is the first moment method, and with [[linearity of expectation|0P7PTC8DDE]] it gives most of the simple results of the [[probabilistic method|3B55HNS754]].
The averaging may be weighted, which corresponds to a nonuniform distribution, and it may be over a group: an average over all translates or all dilates of a set is a standard tool in additive combinatorics.

The same idea appears in analysis as the mean value theorem for integrals: a continuous function on a compact interval takes a value equal to its integral mean, which is the integral form of averaging.
In complexity theory, averaging over random strings gives the existence of good fixed advice strings, and it turns randomized algorithms into nonuniform ones.
Within this sub-area, averaging generalizes the [[pigeonhole principle|0HGVCWQGY3]], it uses [[double counting|0F8YBHF2W3]] to compute averages, and it is the quantitative form of the [[counting arguments for existence|1KVSS0KRZA]].
