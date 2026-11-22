---
tag: N1XSAXCQY3
kind: concept
name: Almost all, generic and in general
aliases: [frivolous-theorem-of-arithmetic]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug2
uses: [0BSJ7RQ9BW, 0BJR9QR08E, 070R982G4B, 01TQB88H4C, VQQM4Y550T, RVG9Z8NYA6, 0XGCZ4GDZ6, GRH8MCVN3N]
sources:
  - wikipedia: en:1309@r1328127267
    locator: Almost all
    note: adopted
    mention: wikipedia://en/1309
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Almost_all
    locator: Meanings in different areas of mathematics
  - url: https://en.wikipedia.org/wiki/Generic_property
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
same_as:
  wikidata: Q1397701
  wikipedia: Almost all
inventory: [AEKZWNRA55]
---

## Summary

"Almost every real number is irrational" and "almost all primes are odd" both say that a property holds except on a small set of exceptions.
But the two sentences measure "small" in different ways: the rational numbers are a set of length zero, and the even primes are a finite set with one element.
So the phrase "almost all" is precise only when the text says which kind of small it means.

Let $X$ be a [[set|0BSJ7RQ9BW]] and let $P$ be a property of the elements of $X$.
"Almost all elements of $X$ have $P$" means that the set of exceptions $\{x \in X : P(x) \text{ is false}\}$ is negligible.
The standard meanings of *negligible* are: [[finite|070R982G4B]] (for infinite $X$), [[countable|01TQB88H4C]] (for uncountable $X$), of [[measure zero|VQQM4Y550T]] (for $X = \mathbb{R}^n$), of [[natural density|RVG9Z8NYA6]] zero (for $X = \mathbb{N}$), and [[meager|0XGCZ4GDZ6]] (for a topological space $X$).
A property is *generic* when it holds outside a negligible set, usually on a dense open set or on a [[residual set|GRH8MCVN3N]] in topology, and on a nonempty Zariski open set in algebraic geometry.

## Motivation

Many statements are false for all objects but true outside a few bad cases.
The prime $2$ is the only even prime, so "every prime is odd" fails for one prime only.
A $2 \times 2$ real matrix is invertible unless $ad - bc = 0$, and those matrices form a thin surface in the space $\mathbb{R}^4$ of all such matrices.
The rational numbers form a countable set, and a countable set has length zero on the real line.
In each case we want to say "true except on a negligible set" and prove things about typical objects.

Each field measures "small" in its own way, because each field has its own idea of size.
Number theory counts, analysis measures length or volume, topology uses density and category, and algebraic geometry uses zero sets of polynomials.
The same phrase therefore carries different theorems, and readers who mix the senses reach false conclusions.
The phrase returns in [[sufficiently large and eventually|FEQ7WATMHF]], which is the cofinite sense on $\mathbb{N}$.

## Notation

Each sense has its own usual words.

- "For all but finitely many $n$" is the cofinite sense.
- "Almost everywhere", abbreviated `a.e.`, and "for almost every $x$" are the measure sense, as in [[almost everywhere|RARTMA0ZEC]]; probability writes [[almost surely|0ST21PGDAP]].
- "For almost all $n$ in the sense of density" and "a set of density one" are the density sense on $\mathbb{N}$.
- "Generic", "typical" and "for a residual set of $x$" are the topological sense, and "for generic parameters" is the algebraic one.

In algebraic geometry, "generic" means "on a nonempty Zariski open set", that is, outside the zero set of a nonzero polynomial.
On an irreducible space such a set is dense, which is why it counts as almost all.
Watch out: in scheme theory "the generic point" is one single point, and that is a different use of the word.
On this site a page that uses "almost all" or "generic" names its sense, unless the area of the page fixes it.

## Remarks

### One sentence, several readings

Take the sentence "almost all natural numbers are not prime" and read it in each sense.
The exceptions are the primes.
In the cofinite sense the sentence is false, because there are infinitely many primes.
In the density sense it is true, because the share of primes below $n$ tends to $0$; this follows from the [[prime number theorem|0EHBY5Y84N]], $\pi(n) \sim n / \ln n$.
In the countable sense it is true and empty, because every subset of $\mathbb{N}$ is countable.

So the same words give a false statement, a true theorem and a statement with no content.
To tell which sense an author uses, look at the set: on $\mathbb{N}$ the sense is cofinite or density, on $\mathbb{R}$ it is measure or category.
Then look for the words that pin it down, such as "Lebesgue", "density", "residual" or "all but finitely many".

### Almost all real numbers are irrational

Here the exceptions are the rationals $\mathbb{Q}$, a dense set.
List them as $q_1, q_2, q_3, \ldots$ and cover $q_k$ by an interval of length $\varepsilon / 2^k$.
The total length is
$$\sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon,$$
and $\varepsilon > 0$ is arbitrary, so $\mathbb{Q}$ has measure zero.
[[Almost all real numbers are irrational|GF1TE1M8RN]] also checks the countable and the topological sense, and the three senses agree there.
[[Almost all primes are odd|FTCN4TA67H]] is the model of the cofinite sense, with one exception.

### Generic objects

"A generic $2 \times 2$ real matrix is invertible."
The exceptions satisfy $ad - bc = 0$.
That set is closed and has empty interior in $\mathbb{R}^4$, so the invertible matrices form a dense open set.
It is also the zero set of the nonzero polynomial $ad - bc$, so the statement holds in the algebraic sense too, and the exceptions have measure zero.

In the same way, a generic quadratic $x^2 + px + q$ has two distinct roots.
The exceptions lie on the parabola $p^2 - 4q = 0$ in the $(p, q)$ plane, the zero set of a nonzero polynomial.
For such polynomial conditions the topological, the algebraic and the measure senses all agree.

### When the senses disagree

The [[Liouville numbers|0PYEZM6CN9]] form a dense $G_\delta$ set of measure zero.
So "almost every real number is a Liouville number" is true in the topological sense and false in the measure sense.
The real line splits as the Liouville numbers, a null set, and their complement, a meager set.
So a property can hold almost everywhere and fail generically.

Inside one sense this cannot happen.
A set and its complement in $\mathbb{R}$ are never both null, and by the [[Baire category theorem|0A7KGAYHGV]] they are never both meager.
On $\mathbb{N}$, a finite set has density zero, so the cofinite sense implies the density sense.
The converse fails: the [[squares|HCGCPW8ZFE]] are infinite, but at most $\sqrt{n} + 1$ of them lie in $\{0, \ldots, n\}$, so they have density zero.

### The rules you can use

In every sense, the union of two negligible sets is negligible.
So if $P$ and $Q$ each hold for almost all $x$ in one sense, then "$P$ and $Q$" holds for almost all $x$ in that sense, because its exceptions are the union of the two sets of exceptions.

The countable, measure and topological senses allow countable unions too.
The cofinite and density senses do not.
Every singleton $\{n\}$ is finite and has density zero, but the union of all of them is $\mathbb{N}$.
On $\mathbb{R}$, a countable set has measure zero and is meager, so "all but countably many" implies both "almost everywhere" and "generic".

### What is not almost all

[[The even numbers are not almost all natural numbers|ARHWX7H5BN]]: the exceptions, the odd numbers, are infinite and have density $\tfrac{1}{2}$, so the claim fails in both senses for $\mathbb{N}$.
"Almost all real numbers lie in $[0, 1]$" fails in every sense.
The exceptions, $\mathbb{R} \setminus [0, 1]$, form an uncountable open set of infinite measure.

### Watch out

The first trap is to mix two senses.
The Liouville numbers are generic, but a real number chosen at random is a Liouville number with probability zero.

The second trap is to take a countable union in the density sense.
Each single number has density zero, and yet all of them together make up $\mathbb{N}$.

The third trap is the phrase "in general", which has two uses.
"In general, $(a + b)^2 \neq a^2 + b^2$" means that the equality is not true for all $a$ and $b$.
It does not mean that the equality fails for all $a$ and $b$: it holds whenever $ab = 0$, for example at $a = 0$.
In the other use, "true in general" means true in all cases.
Read the sentence with "always" and with "not always", and keep the reading that the author can prove.

### History

Henri Lebesgue built his measure, and with it the sense of "almost everywhere", in his thesis of 1902.
René Baire proved the category theorem for the real line in his thesis of 1899, and the topological sense of "generic" comes from his notion of category.

### Try it

First, in which senses are almost all natural numbers not multiples of $100$?
The multiples of $100$ are infinite and have density $\tfrac{1}{100}$, so the claim fails in the cofinite sense and in the density sense.

Second, is a generic real $2 \times 2$ matrix diagonalizable over $\mathbb{C}$?
Yes, in the algebraic sense: a matrix with distinct eigenvalues is diagonalizable, and the exceptions satisfy $(a - d)^2 + 4bc = 0$, the zero set of a nonzero polynomial.

## Explanations

### L1 human

"Almost all" means "all except a few", where "a few" is small enough to ignore.
Every prime number is odd except the single prime $2$, so almost all primes are odd.
For numbers on a line, "a few" usually means a set so thin that its total length is zero.
The fractions are such a set, so a number picked at random on the line is almost never a fraction.
Different parts of mathematics measure "a few" in different ways, so a careful writer says which way is meant.

### L2 human

In which senses are almost all natural numbers not perfect squares?
The exceptions are the squares $S = \{0, 1, 4, 9, 16, \ldots\}$.
The set $S$ is infinite, so the statement is false in the cofinite sense.
For the density sense, count the squares in $\{0, 1, \ldots, n\}$.
They are $k^2$ with $0 \le k \le \sqrt{n}$, so there are at most $\sqrt{n} + 1$ of them, and their share is
$$\frac{|S \cap \{0, \ldots, n\}|}{n + 1} \le \frac{\sqrt{n} + 1}{n + 1} \to 0.$$
So the squares have density zero, and almost all natural numbers are not squares in the density sense.
Check at $n = 100$: there are $11$ squares, $0$ to $100$, among $101$ numbers, a share below $\tfrac{1}{9}$.

The typical use is a theorem with a negligible set of exceptions, such as "almost all even numbers are sums of two primes".
There the sense, density among the even numbers, is part of the theorem.
Watch out: density allows infinitely many exceptions, so it cannot replace "for all sufficiently large $n$".

### L3 human

Each sense of "negligible" is an ideal of sets: a family of subsets of $X$ closed under subsets and finite unions.
Its dual family of large sets is a [[filter|15PF73BKY6]].
The cofinite sense is the [[Fréchet filter|QN98V7NMCD]], and the measure and the topological senses come from the $\sigma$-ideals of null sets and of meager sets, which are closed under countable unions.
"For almost all $x$, $P(x)$" is then the [[filter quantifier|EAJH1P4MK9]] of the chosen filter, and the rules above are the closure rules of filters.
Mathlib follows this design: `∀ᵐ x ∂μ, P x` is the measure sense and `∀ᶠ n in Filter.cofinite, P n` is the cofinite sense.

The [[generic property|Q9APSAZGR1]] page gives the topological sense in more detail.
[[Sard's theorem|Z7R8J71SJN]] is a model result in the measure sense: almost every value of a smooth map is a regular value.
In probabilistic combinatorics, "almost all graphs have $P$" means that the probability of $P$ in a random graph on $n$ vertices tends to $1$, which is yet another sense.
The other informal words of mathematics are in [[mathematical jargon|4M1FGQ0HNZ]].
