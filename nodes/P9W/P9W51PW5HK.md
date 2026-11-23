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

Let $S \subseteq \mathbb{N}$ be an infinite [[computably enumerable|TN9G24VABN]] set that is not computable, such as the halting set.
Let $e : \mathbb{N} \to \mathbb{N}$ be a computable injective function with range $S$, and put
$$a_n = \sum_{k \le n} 2^{-e(k) - 1}.$$
Then $(a_n)$ is a computable nondecreasing sequence of rationals in $[0, 1]$.
By the [[monotone convergence theorem|0FM6N4R0VB]] it converges, and its limit is $x = \sum_{m \in S} 2^{-m - 1}$.

We show that $(a_n)$ has no computable [[rate of convergence|YWZQC5E54B]], that is, no computable $r$ with $x - a_n < 2^{-j - 1}$ for all $j$ and all $n \ge r(j)$.

1. Suppose that $r$ is such a computable function.
   We describe an algorithm that decides $S$.
2. Given $j$, compute $n = r(j)$ and the finite list $e(0), \dots, e(n)$.
   Answer "$j \in S$" if $j$ is on the list, and "$j \notin S$" otherwise.
3. If $j$ is on the list, then $j \in S$, since the list consists of elements of $S$.
4. Suppose that $j \in S$ but $j$ is not on the list.
   Then $j = e(k)$ for some $k > n$, and the term $2^{-j-1}$ is missing from $a_n$, so $x - a_n \ge 2^{-j-1}$.
5. This contradicts $x - a_n < 2^{-j-1}$, which holds because $n = r(j)$.
   So every $j \in S$ is on the list.
6. Steps 3 and 5 show that the algorithm decides $S$, but $S$ is not computable.
   So no computable rate of convergence exists.

## Remarks

The sequence marks the limit of [[proof mining|XR1JXQG1CD]].
The monotone convergence theorem has the form $\forall \varepsilon \, \exists n \, \forall i, j \ge n$, and no proof of it can yield a computable rate of convergence, because here none exists.
What can be extracted is a [[rate of metastability|8WH2SKSAZD]], and the rate $\tilde g^{(\lceil 1/\varepsilon \rceil)}(0)$ holds for this sequence too.
So the theorem has computational content, but only in the metastable form.

Each term $a_n$ is a rational number that we compute exactly, so the noncomputability lives entirely in the speed of convergence.
The limit $x$ is a real number that is not computable, because a computable $x$ would give a computable rate.
Specker introduced such sequences in 1949, as a computable counterexample to the least upper bound principle.
The hypothesis that $S$ is not computable is essential.
If $S$ is computable, let $r(j)$ be the least $n$ such that $e(0), \dots, e(n)$ lists every element of $S$ up to $j + 1$.
The missing terms then add to at most $\sum_{m \ge j+2} 2^{-m-1} = 2^{-j-2} < 2^{-j-1}$, so $r$ is a computable rate.

## Explanations

### L1 human

The sequence adds up small pieces, one for each program that halts, in the order in which the programs are found to halt.
It increases and stays below $1$, so it has a limit.
But knowing how fast it gets close to its limit would tell us which programs halt.
So no algorithm gives the speed of convergence, even though each term is easy to compute.

### L2 human

We check step 4 on a small case.
Say that $3 \in S$ enters late, as $e(10) = 3$, and that a proposed rate gives $r(3) = 5$.
Then $a_5$ lacks the term $2^{-4}$, so
$$x - a_5 \ge 2^{-4} = \tfrac{1}{16}.$$
A correct rate would give $x - a_5 < \tfrac{1}{16}$, so the proposed value $r(3) = 5$ is wrong.

The typical use is to explain why proof mining aims at metastability for convergence theorems.
Watch out: the lesson is not that the monotone convergence theorem has no computational content, since its metastable form has a simple uniform rate.
