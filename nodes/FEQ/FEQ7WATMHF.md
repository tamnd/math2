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

"For $n$ sufficiently large, $2^n > n^3$" says that the inequality may fail at first, but from some point on it is true at every step.
The phrase hides two [[quantifiers|0FYQMKFE77]]: there is a threshold, and every $n$ past it works.

Let $P(n)$ be a statement about a [[natural number|0MWKJ44V5A]] $n$.
$P(n)$ holds *for all sufficiently large* $n$, or *eventually*, when
$$\exists N \;\; \forall n \ge N \;\; P(n).$$
$P(n)$ holds *frequently*, or *for arbitrarily large* $n$, when
$$\forall N \;\; \exists n \ge N \;\; P(n),$$
and for natural numbers this means that $P(n)$ is true for infinitely many $n$.
For a real variable $x$ the definitions are the same with $x \ge M$ in place of $n \ge N$.
"For all sufficiently small $\varepsilon > 0$, $P(\varepsilon)$" means that there is $\delta > 0$ with $P(\varepsilon)$ true for every $\varepsilon$ with $0 < \varepsilon < \delta$.

## Motivation

Compare $2^n$ with $n^3$.
For $n = 2$ we get $4 < 8$ and for $n = 9$ we get $512 < 729$, but for $n = 10$ we get $1024 > 1000$, and from then on $2^n$ stays ahead.
For questions about growth, only the behavior from some point on matters, and the first values are noise.

The same pattern sits inside the definition of a limit.
$a_n \to L$ means that, for every tolerance $\varepsilon > 0$, the terms $a_n$ are within $\varepsilon$ of $L$ from some index on.
The word "eventually" names this pattern, so that a proof can use it without writing the quantifiers each time.
The dual word "frequently" names the negation: a property fails to hold eventually exactly when its negation holds frequently.
The same idea, with a different notion of "small set of exceptions", is in [[almost all, generic and in general|N1XSAXCQY3]].

## Notation

"For all sufficiently large $n$", "for $n$ large enough", "for all $n \ge n_0$", "eventually" and "ultimately" have the same meaning.
"Frequently", "for arbitrarily large $n$", "for infinitely many $n$" and "infinitely often" (abbreviated `i.o.` in probability) have the same meaning for natural numbers.
Some authors write $n \gg 1$ for "$n$ sufficiently large" and $0 < \varepsilon \ll 1$ for "$\varepsilon$ sufficiently small".

In Mathlib, "eventually" is `Filter.Eventually`, written `∀ᶠ n in Filter.atTop, P n`, and "frequently" is `Filter.Frequently`, written `∃ᶠ n in Filter.atTop, P n`.
The filter `Filter.atTop` on $\mathbb{N}$ consists of the sets that contain all $n \ge N$ for some $N$.
The lemmas `Filter.eventually_atTop` and `Filter.frequently_atTop` unfold the two notations into the quantifier forms above.
On this site "for $n$ large" always means "for all sufficiently large $n$", and the page says on which other quantities the threshold depends.

## Remarks

### Finding a threshold

To prove an eventual statement you name a threshold $N$ and show that every $n \ge N$ works.
For $n^2 > 100n$, divide by $n \ge 1$ to get $n > 100$, so $N = 101$ works.
For $n! > 2^n$, start at $n = 4$, where $24 > 16$.
Each step multiplies the left side by $n + 1 \ge 5$ and the right side by $2$, so the inequality stays true; at $n = 3$ it fails, since $6 < 8$.
[[The inequality $2^n > n^3$ for large $n$|HVZ05V7NMJ]] works through the threshold $N = 10$ and shows that no smaller one works.

The threshold may depend on other quantities.
[[For each $\varepsilon > 0$, $1/n < \varepsilon$ for large $n$|C4S1D9R7T0]] uses
$$N = \left\lfloor \frac{1}{\varepsilon} \right\rfloor + 1,$$
which grows as $\varepsilon$ shrinks.
For small $\varepsilon$, the claim $\varepsilon^2 < \varepsilon / 10$ holds exactly when $0 < \varepsilon < \tfrac{1}{10}$, so $\delta = \tfrac{1}{10}$ works.

### Eventually or frequently

The two words say different things, and the difference is the order of the quantifiers.
Read "$(-1)^n = 1$" both ways.
It holds frequently, because every even $n$ works and there are even numbers past every $N$.
It does not hold eventually, because past every $N$ there is an odd $n$ where it fails.

[[Being prime holds frequently but not eventually|BTPEHXK0YH]] is the same pattern with the primes.
There are infinitely many primes, but for every $N$ the number $2N + 4$ is at least $N$, even and larger than $2$, so it is not prime.
To tell which word an author means, translate the sentence into quantifiers and ask whether the threshold comes first.

### The rules you can use

Two eventual statements combine.
If $P(n)$ holds for $n \ge N_1$ and $Q(n)$ holds for $n \ge N_2$, then both hold for $n \ge \max(N_1, N_2)$.
Two frequent statements need not combine: "$n$ is even" and "$n$ is odd" both hold frequently, and their conjunction never holds.
An eventual and a frequent statement do combine into a frequent one.
Given $N$, apply the frequent statement to $\max(N, N_0)$, where $N_0$ is the threshold of the eventual one.

Eventually implies frequently: if $P(n)$ holds for $n \ge N_0$, then for each $N$ the number $\max(N, N_0)$ works.
The [[negation of a universal statement|0P3A06QNDP]] gives the duality
$$\neg \, \exists N \; \forall n \ge N \; P(n) \iff \forall N \; \exists n \ge N \; \neg P(n),$$
so "not eventually $P$" is "frequently not $P$".
Finally, an eventual statement ignores finitely many terms: changing a [[sequence|0G9EKM0E15]] at finitely many indices does not change what holds eventually.

### Infinitely many or arbitrarily large

On $\mathbb{N}$ the two phrases agree.
If $\{n : P(n)\}$ is infinite, it has an element above each $N$, because only finitely many natural numbers lie below $N$.
Conversely, a set with elements above every $N$ has no largest element, so it is infinite.

For a real variable they do not agree.
"$\sin(1/x) = 0$ for infinitely many $x$" is true, with $x = 1/(k\pi)$ for $k = 1, 2, 3, \ldots$, but all these $x$ lie in $(0, 1)$.
So the statement does not hold for arbitrarily large $x$; it is the sentence "frequently as $x \to \infty$" that needs the large values.
When a book about real functions writes "infinitely often", look for the variable that tends to infinity.

### Watch out

The first trap is to swap the quantifiers in the definition of a limit.
"For every $\varepsilon > 0$, eventually $|a_n - L| < \varepsilon$" lets $N$ depend on $\varepsilon$.
"Eventually, for every $\varepsilon > 0$, $|a_n - L| < \varepsilon$" says that $a_n = L$ for all large $n$, which is much stronger.

The second trap is a hidden dependence on a parameter.
"For $x$ large, $x^2 > cx$" is true for each fixed $c$, with threshold $x > |c|$, but no single threshold works for every $c$ at once.

The third trap is a proof by a few values.
$2^n > n^3$ is true at $n = 1$, false from $n = 2$ to $n = 9$, and true again from $n = 10$ on, so no list of small cases settles the question.

### History

Henri Cartan introduced filters in 1937, and the Bourbaki group then used them to state all limits in one language.
In that language, "eventually" and "frequently" are statements about the filter of tails of $\mathbb{N}$.
Mathlib follows this approach, and `∀ᶠ` and `∃ᶠ` are the filter forms of the two phrases.

### Try it

First, find the least threshold for $3n + 5 < n^2$.
At $n = 4$ we get $17 > 16$, and at $n = 5$ we get $20 < 25$; past $5$ the right side grows by $2n + 1 \ge 11$ and the left side by $3$, so $N = 5$.

Second, does "$n$ is a multiple of $7$" hold eventually, frequently, or neither?
It holds frequently, because $7N$ is at least $N$, and not eventually, because $7N + 1$ is at least $N$ and not a multiple of $7$.

## Explanations

### L1 human

"Eventually" means "from some point on, and forever after".
A young tree is shorter than a fence at first, but if it grows past the fence and stays above it, then it is eventually taller than the fence.
In numbers, $2^n$ is smaller than $n^3$ for $n = 2$ to $9$, but from $n = 10$ on, $2^n$ is always larger.
"Frequently" is weaker: it means "again and again, without end", but not "always from some point".
A light that blinks on and off is on frequently, but it is not eventually on.

### L2 human

Here is a typical task: show that $n! > 3^n$ for all sufficiently large $n$, and find the least threshold.
Start with the first values near the change:
$$6! = 720 < 729 = 3^6, \qquad 7! = 5040 > 2187 = 3^7.$$
So the inequality fails at $n = 6$ and holds at $n = 7$.
For the step, suppose $n \ge 7$ and $n! > 3^n$.
Then
$$(n + 1)! = (n + 1) \cdot n! > (n + 1) \cdot 3^n \ge 8 \cdot 3^n > 3 \cdot 3^n = 3^{n+1}.$$
By [[mathematical induction|0ASJVEFA9J]] from $n = 7$, the inequality holds for every $n \ge 7$.
The threshold $N = 7$ is the least one, because the inequality fails at $n = 6$.

The pattern is the usual one: compute until the inequality turns, then prove that it stays turned.
Watch out: the computation alone proves nothing about later $n$, and the induction step is what makes the statement eventual.

### L3 human

The phrases are statements about a [[filter|15PF73BKY6]].
On $\mathbb{N}$, the filter of tails consists of the sets that contain $\{N, N + 1, \ldots\}$ for some $N$, and it equals the [[Fréchet filter|QN98V7NMCD]] of cofinite sets.
A property holds eventually when the set where it holds belongs to the filter, and frequently when that set meets every member of the filter.
So "eventually" on $\mathbb{N}$ is the cofinite sense of "almost all", and both phrases are [[filter quantifiers|EAJH1P4MK9]].

With the neighborhood filter of a point, "eventually" becomes "for all $x$ close enough to $a$".
A [[filter limit|F6QDHKE6J3]] then covers limits of sequences, limits of functions and one-sided limits in one definition.
Mathlib writes the small-$\varepsilon$ phrase as `∀ᶠ ε in 𝓝[>] 0, P ε`, with the filter of right neighborhoods of $0$.
Asymptotic notation such as [[big O|0TGV80E6A4]] is also defined with "eventually": $f = O(g)$ means that $|f(n)| \le C |g(n)|$ holds eventually for some constant $C$.
