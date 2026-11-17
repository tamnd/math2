---
tag: P9W51PW5HK
kind: example
name: A Specker sequence has no computable rate of convergence
msc: ["03F60", "03D80"]
topics: [8XY7JYZKFW]
audience: research
not_instance_of:
  - target: XR1JXQG1CD
    note: "A Specker sequence is monotone and bounded but has no computable rate of convergence, so proof mining can extract only a rate of metastability, not a rate of convergence."
uses: [XR1JXQG1CD, TN9G24VABN, 0FM6N4R0VB, YWZQC5E54B, 8WH2SKSAZD]
sources:
  - url: https://en.wikipedia.org/wiki/Specker_sequence
    locator: Construction 1
  - url: https://en.wikipedia.org/wiki/Proof_mining
    locator: lead section
---

## Example

Let $S \subseteq \N$ be a [[computably enumerable|TN9G24VABN]] set that is not computable, such as the halting set.
Let $e : \N \to \N$ be a computable injective function with range $S$.
Let $a_n = \sum_{k \le n} 2^{-e(k) - 1}$.
Then $(a_n)$ is a computable nondecreasing sequence of rationals in $[0, 1]$, and by the [[monotone convergence theorem|0FM6N4R0VB]] it converges to $x = \sum_{m \in S} 2^{-m - 1}$.
We show that $(a_n)$ has no computable [[rate of convergence|YWZQC5E54B]]: no computable $r$ with $x - a_n < 2^{-j - 1}$ for all $n \ge r(j)$.

1. Suppose $r$ is such a computable function.
2. To decide whether $j \in S$, compute $n = r(j)$ and check whether $j$ is one of $e(0), \ldots, e(n)$.
3. If $j$ is among them, then $j \in S$.
4. If $j = e(k)$ with $k > n$, then $x - a_n \ge 2^{-e(k) - 1} = 2^{-j - 1}$, since the term for $k$ is missing from $a_n$.
5. This contradicts $x - a_n < 2^{-j - 1}$. So $j \in S$ only if $j$ is among $e(0), \ldots, e(n)$.
6. So steps 2 and 3 decide $S$, which is not computable. Hence no computable rate exists.

## Remarks

This example shows the limit of [[proof mining|XR1JXQG1CD]]: the monotone convergence theorem has a $\forall \varepsilon\, \exists n\, \forall i, j \ge n$ form, and its proof yields no computable rate of convergence.
What proof mining extracts is the [[rate of metastability|8WH2SKSAZD]] $\tilde g^{(\lceil 1/\varepsilon \rceil)}(0)$, which also holds for this sequence.
Specker introduced such sequences in 1949, as a computable counterexample to the least upper bound principle.
The limit $x$ is a real number that is not computable.

## Explanations

### L1 human

The sequence adds up small pieces, one for each program that halts, in the order in which they are found to halt.
It increases and stays below $1$, so it has a limit.
But knowing how fast it gets close to its limit would tell which programs halt.
So no algorithm gives the speed of convergence, even though each term is easy to compute.

### L2 human

We check step 4 on a small case.

1. Say $j = 3$ enters $S$ late, as $e(10) = 3$, and $r(3) = 5$.
2. Then $a_5$ lacks the term $2^{-4}$, so $x - a_5 \ge 2^{-4}$.
3. A correct rate would give $x - a_5 < 2^{-4}$, a contradiction. So a correct $r$ never says $5$ here.

The typical use is to explain why proof mining aims at metastability for convergence theorems.
A trap is to conclude that the monotone convergence theorem has no computational content; it has content in the form of metastability.
