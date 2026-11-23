---
tag: BJQ77Y2QFX
kind: concept
name: Weak weak König's lemma
aliases: [wwkl]
msc: ["03B30", "03F35", "03D32", "28A12"]
topics: [BY8AAFN7C5]
audience: research
uses: [XQENB067R3, 7W9EG02T79, DC60FYCSPM, W9VYJRBF9N, 2Z2QVWZ262, X5KD3X3VJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Additional systems
  - url: https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma
    locator: Computability aspects
  - url: https://en.wikipedia.org/wiki/Algorithmically_random_sequence
    locator: lead section
---

## Summary

There is a computable binary tree that keeps at least half of all strings at every length and still has no computable path.
*Weak weak König's lemma*, $\mathrm{WWKL}$, is the axiom that every such fat tree has a path, and it is the axiom that measure theory needs where analysis would need compactness.
Exactly, $\mathrm{WWKL}$ is the sentence of [[second-order arithmetic|DC60FYCSPM]] that says: every tree $T \subseteq 2^{<\mathbb{N}}$ of positive measure has an infinite path.
Here $T_n$ is the set of strings in $T$ of length $n$, and $T$ has *positive measure* if some rational $q > 0$ satisfies
$$\frac{\lvert T_n \rvert}{2^n} \ge q \quad \text{for all } n.$$
The system $\mathsf{WWKL}_0$ is [[RCA0|XQENB067R3]] together with $\mathrm{WWKL}$, and the [[definition|KPHM3025GW]] gives it in full.
It lies strictly between $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$, and it measures the basic theorems about [[Lebesgue measure|2Z2QVWZ262]].

## Motivation

[[Weak König's lemma|7W9EG02T79]] says that every infinite binary tree has a path, and it is equivalent over $\mathsf{RCA}_0$ to the Heine-Borel covering property of $[0, 1]$.
Measure theory leans on a different step: a set of positive measure is not empty.
For a closed subset of [[Cantor space|W9VYJRBF9N]], this step is exactly $\mathrm{WWKL}$, since the closed set is the set of paths of a tree and its measure is the limit of $\lvert T_n \rvert / 2^n$.
Yu and Simpson isolated the axiom in 1990, when they asked which axioms the elementary theory of Lebesgue measure needs.
Computability gives a second reading.
The paths of a fat computable tree can all be random, and every random set has a tail in every such class, so $\mathrm{WWKL}$ says, in effect, that random sets exist.
The principle returns in the [[reverse mathematics zoo|E3X5B175ZR]], where it sits between $\mathsf{WKL}_0$ and $\mathrm{DNR}$.

## Notation

We write $T_n = \{\sigma \in T : \lvert \sigma \rvert = n\}$ and $[T]$ for the set of paths of $T$.
The measure on Cantor space is the uniform measure $\mu$, with $\mu([\sigma]) = 2^{-\lvert \sigma \rvert}$, where $[\sigma]$ is the set of sequences that begin with $\sigma$.
Some authors call a tree of positive measure a *fat* tree, and some write $\mathrm{WWKL}$ for the system $\mathsf{WWKL}_0$.

## Remarks

### A tree you can count

Split $\mathbb{N}$ into blocks of $2, 3, 4, \dots$ positions, and keep a string unless it is all ones on some complete block.
At length $9$ the complete blocks have $2$, $3$ and $4$ positions, so
$$\frac{\lvert T_9 \rvert}{2^9} = \frac{3}{4} \cdot \frac{7}{8} \cdot \frac{15}{16} = \frac{315}{512} \approx 0.615.$$
The forbidden fractions add up to less than $\tfrac{1}{4} + \tfrac{1}{8} + \cdots = \tfrac{1}{2}$, so the ratio never drops below $\tfrac{1}{2}$.
The all-zero sequence is a path, and the [[worked example|JF081V3699]] computes every level.

### A tree with no computable path

The first level $U_1$ of a universal Martin-Löf test is an open set of measure at most $\tfrac{1}{2}$ that contains every non-random sequence.
The strings not yet covered by $U_1$ at stage $\lvert \sigma \rvert$ form a computable tree with $\lvert T_n \rvert / 2^n \ge \tfrac{1}{2}$.
Every path of it lies outside $U_1$, so it is random, and no computable sequence is random.
The [[example|7KNY1EMB1G]] checks each step, and it shows that $\mathsf{RCA}_0$ does not prove $\mathrm{WWKL}$.

### Thin trees

The tree $\{0^n : n \in \mathbb{N}\}$ has $\lvert T_n \rvert / 2^n = 2^{-n}$, so no rational $q > 0$ bounds the ratio from below, although the tree has a path.
The separation tree of two disjoint computably enumerable sets with infinite union is a more telling case.
Each enumerated element fixes one bit, so the ratio tends to $0$, and the [[non-example|X9911PGV0N]] computes it.
Weak König's lemma applies to this tree and $\mathrm{WWKL}$ does not, and this is the gap between the two principles.

### Where WWKL sits

$\mathsf{WKL}_0$ proves $\mathrm{WWKL}$, since a tree of positive measure has $\lvert T_n \rvert \ge q 2^n > 0$ for every $n$, so it is infinite.
Yu and Simpson showed that the converse fails.
Since $\mathsf{WWKL}_0$ lies between $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$, Harrington's theorem that $\mathsf{WKL}_0$ is [[Π¹₁-conservative over RCA0|8G2GVRXWG5]] gives the same conservation for $\mathsf{WWKL}_0$.
$\mathrm{WWKL}$ implies $\mathrm{DNR}$, and the converse fails, by Ambos-Spies, Kjos-Hanssen, Lempp and Slaman in 2004.
Ramsey's theorem for pairs does not imply $\mathrm{WWKL}$, by Liu in 2015.
Over $\mathsf{RCA}_0$, Yu and Simpson showed that $\mathrm{WWKL}$ is equivalent to a form of countable additivity: if open intervals $(a_k, b_k)$ cover $[0, 1]$, then $\sum_k (b_k - a_k) \ge 1$.
Brown, Giusto and Simpson showed in 2002 that it is also equivalent to a form of the [[Vitali covering lemma|FCA0J1X07K]].

### Models and randomness

An $\omega$-model $(\mathbb{N}, \mathcal{S})$ satisfies $\mathsf{WWKL}_0$ exactly when $\mathcal{S}$ is a Turing ideal that contains, for each $X \in \mathcal{S}$, a set that is [[Martin-Löf random|X5KD3X3VJ3]] relative to $X$.
For one direction, the tree of the example built relative to $X$ lies in $\mathcal{S}$, and its paths are random relative to $X$.
For the other, let $T \in \mathcal{S}$ have positive measure, and let $Y \in \mathcal{S}$ be random relative to $T$.
By Kučera's lemma, which we cite, some tail $Z$ of $Y$, the sequence $Z(n) = Y(n + k)$ for a fixed $k$, is a path of $T$.
$Z$ is computable from $Y$, so it is in $\mathcal{S}$.
Over $\mathsf{RCA}_0$ the same idea makes $\mathrm{WWKL}$ equivalent to "for every set $X$ there is a set that is Martin-Löf random relative to $X$".

### Watch out

Do not weaken the hypothesis to "each level $T_n$ is non-empty"; that is the hypothesis of weak König's lemma, which is strictly stronger.
Do not define positive measure by $\lim_n \lvert T_n \rvert / 2^n > 0$ inside $\mathsf{RCA}_0$.
The ratios form a non-increasing computable sequence of rationals, and its limit can be a noncomputable real, so $\mathsf{RCA}_0$ need not prove that the limit exists.
The rational bound $q$ says "the limit is positive" without naming the limit.

### History

Xiaokang Yu and Stephen Simpson introduced $\mathrm{WWKL}$ in "Measure theory and weak König's lemma" (Archive for Mathematical Logic, 1990).
They proved that it is strictly weaker than $\mathrm{WKL}$ and equivalent to countable additivity of Lebesgue measure on open sets.
Brown, Giusto and Simpson added the Vitali covering theorem in 2002.

### Try it

Does the tree of strings that do not begin with $11$ have positive measure?
Answer: yes, $\lvert T_n \rvert = 2^n - 2^{n-2} = \tfrac{3}{4} 2^n$ for $n \ge 2$, so $q = \tfrac{3}{4}$ works.

Does the tree of strings with no $1$ at an even position have positive measure?
Answer: no, a string of length $n$ has $\lceil n / 2 \rceil$ even positions, so the ratio is $2^{-\lceil n/2 \rceil}$, which tends to $0$.

## Explanations

### L1 human

Picture all infinite sequences of coin flips.
A binary tree cuts some of them out by forbidding certain starts.
If the tree keeps at least a fixed fraction of all starts at every length, the surviving sequences have positive probability.
Weak weak König's lemma says that such a set is never empty.
For example, forbid every start that begins "heads, heads": three quarters of all starts survive, and "all tails" is a surviving sequence.
Logicians use this axiom to measure how much strength the basic facts about length and area need.

### L2 human

Here is the shape of a typical reversal to $\mathrm{WWKL}$, from countable additivity.
Let $T$ have positive measure with bound $q$, and suppose that $T$ has no path.
Each string $\sigma \notin T$ gives an open interval of reals of length $2^{-\lvert \sigma \rvert}$, and these intervals, slightly enlarged, cover $[0, 1]$, because every sequence leaves $T$ somewhere.
At each length $n$ the intervals of the minimal strings outside $T$ have total length at most $1 - q$, so the sum of all lengths is at most $1 - q$ plus the enlargement.
With a total enlargement below $q$, this contradicts countable additivity, so $T$ has a path.
The typical use is this conversion between trees and covers.
The trap is the binary expansion: dyadic rationals have two expansions, so the intervals must be enlarged a little, and the error budget must stay below $q$.

### L3 human

$\mathrm{WWKL}$ is defined by measure rather than by compactness or comprehension, and it brought measure theory into reverse mathematics as a source of axioms.
In terms of degrees, $\mathrm{WKL}$ asks for sets of PA degree, and $\mathrm{WWKL}$ asks only for random sets.
Every set of PA degree computes a random set, but almost every random set computes no set of PA degree, and this explains the strict inequality.
Randomness itself belongs to [[algorithmic randomness|2B354NY7F7]], and the comparison of $\mathrm{WWKL}$ with $\mathrm{DNR}$ and with Ramsey-type principles belongs to the zoo.
In constructive mathematics, forms of the fan theorem play the part of $\mathrm{WKL}$, a topic of [[constructive reverse mathematics|3XFMHSCVYZ]].
