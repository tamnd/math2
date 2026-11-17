---
tag: FEQ7WATMHF
kind: concept
name: Sufficiently large, eventually and frequently
aliases: [large-enough, sufficiently-large]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [0MWKJ44V5A, 0G9EKM0E15, 0GHS47PDAQ, 0MSRQHCNN9, 0FYQMKFE77]
sources:
  - wikipedia: en:10077292@r1343441049
    locator: Eventually (mathematics)
    note: adopted
    mention: wikipedia://en/10077292
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Eventually_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - book: isbn:9781108439534
same_as:
  wikidata: Q5416789
  wikipedia: Eventually (mathematics)
inventory: [HQ68GV00KF]
---

## Summary

Let $P(n)$ be a statement about a [[natural number|0MWKJ44V5A]] $n$.
The statement $P(n)$ holds for all sufficiently large $n$, or eventually, when there is a number $N$ such that $P(n)$ is true for every $n \geq N$: in symbols, $\exists N \; \forall n \geq N \; P(n)$.
The statement $P(n)$ holds frequently, or for arbitrarily large $n$, when for every $N$ there is an $n \geq N$ with $P(n)$ true: in symbols, $\forall N \; \exists n \geq N \; P(n)$; for natural numbers this means that $P(n)$ is true for infinitely many $n$.
For a real variable the definitions are the same with $x \geq M$ in place of $n \geq N$.
The phrase "for all sufficiently small $\varepsilon > 0$, $P(\varepsilon)$" means that there is a $\delta > 0$ such that $P(\varepsilon)$ is true for every $\varepsilon$ with $0 < \varepsilon < \delta$.
These phrases hide a pair of [[quantifiers|0FYQMKFE77]], and every definition of a limit and every comparison of growth rates is written with them.

## Motivation

Compare the numbers $2^n$ and $n^3$.
For $n = 2$ we get $4 < 8$, for $n = 9$ we get $512 < 729$, but for $n = 10$ we get $1024 > 1000$, and from then on $2^n$ stays larger.
The statement "$2^n > n^3$" is false for some small $n$ and true from some point on.
For growth questions only the behaviour from some point on matters, and the first values are noise.
The same pattern is in the definition of a limit: $a_n \to L$ means that, for each tolerance $\varepsilon > 0$, the terms $a_n$ are within $\varepsilon$ of $L$ from some index on.
The words "eventually" and "for $n$ large enough" name this pattern, so that a proof can use it without writing the quantifiers each time.
The dual word "frequently" names the negation: a property fails eventually exactly when its negation holds frequently.

## Notation

The phrases "for all sufficiently large $n$", "for $n$ large enough", "for all $n \geq n_0$", "eventually" and "ultimately" have the same meaning.
The phrases "frequently", "for arbitrarily large $n$", "for infinitely many $n$" and "infinitely often" have the same meaning for natural numbers; the abbreviation `i.o.` is common in probability.
Some authors write $n \gg 1$ for "$n$ sufficiently large" and $0 < \varepsilon \ll 1$ for "$\varepsilon$ sufficiently small".
In Lean's Mathlib, "eventually" is `Filter.Eventually`, with the notation `∀ᶠ n in Filter.atTop, P n`, and "frequently" is `Filter.Frequently`, with the notation `∃ᶠ n in Filter.atTop, P n`.
The filter `Filter.atTop` on $\mathbb{N}$ consists of the sets that contain all $n \geq N$ for some $N$.
On this site, "for $n$ large" always means "for all sufficiently large $n$", and the dependence of $N$ on other parameters is stated.

## Remarks

### Examples

1. [[The inequality $2^n > n^3$ holds for all sufficiently large $n$|~47330189]], namely for all $n \geq 10$. It fails for $n = 2, \ldots, 9$.
2. [[For each $\varepsilon > 0$, the inequality $1/n < \varepsilon$ holds for all sufficiently large $n$|~6b9beb6c]]. The threshold $N = \lfloor 1/\varepsilon \rfloor + 1$ depends on $\varepsilon$.
3. The inequality $n^2 > 100n$ holds eventually, for all $n \geq 101$. For $n \geq 1$ it is equivalent to $n > 100$.
4. The inequality $n! > 2^n$ holds eventually, for all $n \geq 4$. At $n = 4$ we have $24 > 16$, and the step from $n$ to $n + 1$ multiplies the left side by $n + 1 \geq 5$ and the right side by $2$; at $n = 3$ we have $6 < 8$.
5. The statement $(-1)^n = 1$ holds frequently, for each even $n$. It does not hold eventually, because it fails for each odd $n$.
6. For all sufficiently small $\varepsilon > 0$, $\varepsilon^2 < \varepsilon / 10$. This holds exactly for $0 < \varepsilon < \tfrac{1}{10}$, so $\delta = \tfrac{1}{10}$ works.

### Non-examples

1. [[Being prime holds frequently but not eventually|~a573dcc9]]. There are infinitely many primes, but for each $N$ the number $2N + 4$ is at least $N$, even and larger than $2$, so it is not prime.
2. The statement "$n$ is even" does not hold eventually, and its negation "$n$ is odd" does not hold eventually either. Both hold frequently.
3. For a fixed $\varepsilon > 0$, the statement $1/n > \varepsilon$ does not hold for sufficiently large $n$. It holds only for $n < 1/\varepsilon$, so its negation $1/n \leq \varepsilon$ holds eventually.

### Basic properties

1. Two eventual statements combine. If $P(n)$ holds for $n \geq N_1$ and $Q(n)$ holds for $n \geq N_2$, then both hold for $n \geq \max(N_1, N_2)$.
2. Eventually implies frequently. Let $P(n)$ hold for $n \geq N_0$, and let $N$ be given. Then $n = \max(N, N_0)$ satisfies $n \geq N$ and $P(n)$.
3. Negation. "$P(n)$ does not hold eventually" is equivalent to "$\neg P(n)$ holds frequently". The [[negation of a universal statement|0P3A06QNDP]] turns $\neg \exists N \, \forall n \geq N \, P(n)$ into $\forall N \, \exists n \geq N \, \neg P(n)$.
4. Frequently means infinitely often. If $\{n : P(n)\}$ is infinite, then it has an element above each $N$, since a set of natural numbers below $N$ is finite. Conversely, if $P(n)$ holds frequently, then the set $\{n : P(n)\}$ has no largest element, so it is infinite.
5. If $P(n)$ holds eventually and $Q(n)$ holds frequently, then "$P(n)$ and $Q(n)$" holds frequently. Given $N$, apply the frequent property to $\max(N, N_0)$, where $P$ holds from $N_0$ on.
6. Two frequent statements need not combine. "$n$ is even" and "$n$ is odd" both hold frequently, but "$n$ is even and odd" never holds.
7. Eventual statements ignore finitely many terms. If two sequences differ only at finitely many indices, then a statement about $a_n$ holds eventually exactly when the same statement about $b_n$ holds eventually.
8. Limits. A [[sequence|0G9EKM0E15]] $a_n$ converges to $L$ exactly when, for each $\varepsilon > 0$, the statement $|a_n - L| < \varepsilon$ holds eventually. Here $N$ may depend on $\varepsilon$, as in the [[definition of a limit|05M5SWSZZD]].

### History

Henri Cartan introduced filters in 1937, and the Bourbaki group then used them to state all limits in one language.
In that language, "eventually" and "frequently" become statements about the filter of tails of $\mathbb{N}$.
The library Mathlib follows this approach, and its notation `∀ᶠ` and `∃ᶠ` is the filter form of the two phrases.

### Common errors

1. A student swaps the quantifiers in the definition of a limit. "For each $\varepsilon > 0$, eventually $|a_n - L| < \varepsilon$" allows $N$ to depend on $\varepsilon$. "Eventually, for each $\varepsilon > 0$, $|a_n - L| < \varepsilon$" means that $a_n = L$ for all large $n$, which is much stronger.
2. A student confuses "infinitely often" with "eventually". The sequence $(-1)^n$ equals $1$ infinitely often, but it does not equal $1$ eventually.
3. A student hides a dependence on a parameter. "For $x$ large, $x^2 > cx$" is true for each fixed $c$, with threshold $x > |c|$, but no single threshold works for all $c$ at once.

## Explanations

### L1 human

"Eventually" means "from some point on, and forever after".
A small plant is shorter than a fence at first, but if it keeps growing past the fence and stays above it, then it is eventually taller than the fence.
In numbers: $2^n$ is smaller than $n^3$ for $n = 2$ to $9$, but from $n = 10$ on, $2^n$ is always larger.
"Frequently" is weaker: it means "again and again, without end", but not necessarily "always from some point".
A light that blinks on and off is on frequently, but it is not eventually on.

### L2 human

We show that $n! > 3^n$ holds for all sufficiently large $n$, and we find the least threshold.

1. We compute the first values. For $n = 6$: $6! = 720$ and $3^6 = 729$, so the inequality fails. For $n = 7$: $7! = 5040$ and $3^7 = 2187$, so it holds.
2. Induction step. Suppose $n \geq 7$ and $n! > 3^n$. Then $(n + 1)! = (n + 1) \cdot n! > (n + 1) \cdot 3^n \geq 8 \cdot 3^n > 3^{n+1}$.
3. By [[mathematical induction|0ASJVEFA9J]] from $n = 7$, the inequality holds for every $n \geq 7$.
4. So $n! > 3^n$ holds eventually, with $N = 7$, and $N = 7$ is the least threshold, since step 1 shows that it fails at $n = 6$.

The typical use of "eventually" is in limits and growth comparisons, where the first finitely many terms do not matter.
A trap: a check of a few values is not a proof of an eventual statement.
For example, $2^n > n^3$ is true at $n = 1$, false from $n = 2$ to $n = 9$, and true again from $n = 10$ on.

### L3 human

The phrases are statements about a [[filter|15PF73BKY6]].
On $\mathbb{N}$, the filter of tails consists of the sets that contain $\{N, N + 1, \ldots\}$ for some $N$; it equals the [[Fréchet filter|QN98V7NMCD]] of cofinite sets.
A property holds eventually when the set where it holds is in the filter, and frequently when that set meets every set of the filter.
So "eventually" on $\mathbb{N}$ is the cofinite sense of [[almost all|N1XSAXCQY3]], and both phrases are [[filter quantifiers|EAJH1P4MK9]].
With the neighbourhood filter of a point, "eventually" becomes "for all $x$ close enough to $a$", and a [[filter limit|F6QDHKE6J3]] covers limits of sequences, limits of functions and one-sided limits in one definition.
Mathlib writes the small-$\varepsilon$ phrase as `∀ᶠ ε in 𝓝[>] 0, P ε`, with the filter of right neighbourhoods of $0$.
Asymptotic notation such as [[big O|0TGV80E6A4]] is also defined with "eventually": $f = O(g)$ means that $|f(n)| \leq C |g(n)|$ holds eventually for some constant $C$.
