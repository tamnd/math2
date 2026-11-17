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

Let $X$ be a [[set|0BSJ7RQ9BW]] and let $P$ be a property of the elements of $X$.
The phrase "almost all elements of $X$ have property $P$" means that the set of exceptions $\{x \in X : P(x) \text{ is false}\}$ is negligible.
The word negligible has several standard meanings, and a careful text states which one it uses: [[finite|070R982G4B]] (for infinite $X$), [[countable|01TQB88H4C]], of [[measure zero|VQQM4Y550T]] (for $X = \mathbb{R}^n$), of [[natural density|RVG9Z8NYA6]] zero (for $X = \mathbb{N}$), or [[meagre|0XGCZ4GDZ6]] (for a topological space $X$).
A property is generic when it holds for almost all elements in one of these senses; in topology and geometry this usually means that the property holds on a dense open set or on a [[residual set|GRH8MCVN3N]].
The phrase "in general" has two different uses: "true in general" means true in all cases, while "in general false" means not true in all cases.
These words let a theorem ignore a small set of bad cases, but each sense of "small" gives a different theorem, so the sense must be stated.

## Motivation

Many statements are false as stated for all objects, but true outside a small set of exceptions.
The prime $2$ is the only even prime, so "each prime is odd" is false, but it fails for one prime only.
A $2 \times 2$ matrix is invertible unless its determinant is $0$, and the matrices with determinant $0$ form a thin surface in the space $\mathbb{R}^4$ of all such matrices.
A rational number is a rare event on the real line: the rational numbers form a countable set, and a countable set has length zero.
In each case, mathematicians want to say "the statement holds except for a negligible set", and to prove things about typical objects.
The phrase "almost all" does this job, but each field measures "small" in its own way.

## Notation

Each sense has its own words and symbols.

- "For all but finitely many $n$" is the cofinite sense. On $\mathbb{N}$ it is the same as "for all sufficiently large $n$", see [[sufficiently large and eventually|FEQ7WATMHF]].
- "Almost everywhere" (abbreviated `a.e.`) and "for almost every $x$" are the measure sense; see [[almost everywhere|RARTMA0ZEC]]. In probability the same idea is written "almost surely", see [[almost surely|0ST21PGDAP]].
- "A set of density one" or "for almost all $n$ in the sense of density" is the density sense on $\mathbb{N}$.
- "Generic", "typical" and "for a residual set of $x$" are the topological sense.
- In algebraic geometry, "a generic point" or "for generic parameters" means outside a proper Zariski closed set, that is, outside the zero set of a nonzero polynomial.

On this site, a page that uses "almost all" or "generic" says which sense it uses, unless the sense is fixed by the area of the page.

## Remarks

### Examples

1. [[Almost all primes are odd|FTCN4TA67H]], in the cofinite sense. The only even prime is $2$.
2. [[Almost all real numbers are irrational|GF1TE1M8RN]], in the measure sense and in the countable sense. The rational numbers form a countable set, and a countable set has Lebesgue measure zero.
3. Almost all natural numbers are not prime, in the density sense. By the [[prime number theorem|0EHBY5Y84N]], the number $\pi(n)$ of primes up to $n$ satisfies $\pi(n)/n \to 0$. The exceptions, the primes, are infinite, so this is false in the cofinite sense.
4. A generic $2 \times 2$ real matrix is invertible. The non-invertible matrices satisfy $ad - bc = 0$; this set is closed, has empty interior in $\mathbb{R}^4$ and has measure zero. So "invertible" holds on a dense open set of full measure.
5. A generic real polynomial $x^2 + px + q$ has two distinct complex roots. The exceptions satisfy $p^2 - 4q = 0$, a parabola in the $(p, q)$ plane, which is closed with empty interior and has measure zero.

### Non-examples

1. [[The even numbers are not almost all natural numbers|ARHWX7H5BN]]. The odd numbers are infinite, and the even numbers have density $\tfrac12$, not $1$.
2. "Almost all real numbers lie in $[0, 1]$" is false in each sense. The exceptions form the set $\mathbb{R} \setminus [0, 1]$, which is uncountable, has infinite measure and is open and nonempty.
3. "Almost all real numbers are Liouville numbers" is true in the topological sense and false in the measure sense. The set of [[Liouville numbers|0PYEZM6CN9]] is a dense $G_\delta$ set, so it is residual, but it has measure zero.

### Basic properties

1. Finite intersections. In each of the five senses, a union of two negligible sets is negligible. So if $P$ holds for almost all $x$ and $Q$ holds for almost all $x$ in the same sense, then "$P$ and $Q$" holds for almost all $x$. The exceptions of "$P$ and $Q$" are the union of the exceptions of $P$ and of $Q$.
2. Countable intersections. In the countable, measure and topological senses, a countable union of negligible sets is negligible. In the cofinite and density senses this fails: each singleton $\{n\}$ is finite and has density zero, but the union of all of them is $\mathbb{N}$.
3. Cofinite implies density one. A finite set $F \subseteq \mathbb{N}$ has at most $|F|$ elements up to $n$, and $|F|/n \to 0$. The converse fails: the [[square numbers|HCGCPW8ZFE]] are infinite but have density zero, because there are at most $\sqrt{n} + 1$ squares in $\{0, 1, \ldots, n\}$.
4. On $\mathbb{R}$, a countable set has measure zero and is meagre. So "all but countably many" implies both "almost everywhere" and "generic".
5. Measure and category disagree. By non-example 3, $\mathbb{R}$ is the union of the Liouville numbers, a set of measure zero, and their complement, a meagre set. So a property can be true almost everywhere and false generically. Within one sense this cannot happen: a set and its complement are never both null, and by the [[Baire category theorem|0A7KGAYHGV]] they are never both meagre.

### History

Henri Lebesgue built his measure, and with it the measure sense of "almost everywhere", in his thesis of 1902.
René Baire proved the category theorem for the real line in his thesis of 1899, and the topological sense of "generic" comes from his notion of category.
The density sense comes from analytic number theory, where statements about almost all integers are often the first step before a statement about all integers.

### Common errors

1. A student mixes two senses. The Liouville numbers are generic in the topological sense, but a real number chosen at random is a Liouville number with probability zero.
2. A student uses countable intersections in the density sense. Each single number has density zero, but the union of all single numbers is $\mathbb{N}$.
3. A student reads "in general, $(a + b)^2 \neq a^2 + b^2$" as "for all $a, b$, $(a + b)^2 \neq a^2 + b^2$". The sentence means only that the equality is not true for all $a, b$; it holds for $a = 0$, and it holds whenever $ab = 0$.

## Explanations

### L1 human

"Almost all" means "all except a few", where "a few" is so small that we can ignore it.
For example, every prime number is odd except the single prime $2$, so almost all primes are odd.
For numbers on a line, "a few" usually means a set so thin that it has total length zero.
The fractions are such a set, so a number chosen at random on the line is almost never a fraction.
Different parts of mathematics measure "a few" in different ways, so a careful writer says which way is meant.
The phrase "in general" needs care too: "in general this is false" means "this is not always true", not "this is never true".

### L2 human

We decide in which senses almost all natural numbers are not perfect squares.

1. The exceptions are the squares $S = \{0, 1, 4, 9, 16, \ldots\}$.
2. The set $S$ is infinite, so the statement is false in the cofinite sense.
3. The set $S$ is countable, so the statement is true in the countable sense, but this sense says little on the countable set $\mathbb{N}$.
4. For $n \geq 1$, the squares in $\{0, 1, \ldots, n\}$ are $k^2$ with $0 \leq k \leq \sqrt{n}$, so there are at most $\sqrt{n} + 1$ of them. Then the proportion is at most $(\sqrt{n} + 1)/(n + 1)$, which tends to $0$.
5. So the squares have density zero, and almost all natural numbers are not squares in the density sense.

The typical use is a theorem with a negligible set of exceptions, such as "almost all even numbers are a sum of two primes"; the sense, here density among the even numbers, is part of the theorem.
A trap: "almost all" in the density sense on $\mathbb{N}$ allows infinitely many exceptions, so it cannot replace "for all sufficiently large $n$".

### L3 human

Each sense of "negligible" is a family of subsets of $X$ that is closed under subsets and under finite unions, called an ideal of sets; its dual family of "large" sets is a [[filter|15PF73BKY6]].
The cofinite sense is the [[Fréchet filter|QN98V7NMCD]], the measure sense is the ideal of null sets, and the topological sense is the ideal of meagre sets; the last two are $\sigma$-ideals, closed under countable unions.
The phrase "for almost all $x$, $P(x)$" is then the [[filter quantifier|EAJH1P4MK9]] of the chosen filter, and the rules of basic properties 1 and 2 are the closure rules of filters and $\sigma$-filters.
The book of Oxtoby on measure and category studies the parallel and the conflict between the null ideal and the meagre ideal on the real line.
The page on [[generic properties|Q9APSAZGR1]] gives the topological sense in more detail, with [[Sard's theorem|Z7R8J71SJN]] as a model result: almost every value of a smooth map is a regular value.
In probabilistic combinatorics, "almost all graphs have property $P$" means that the probability of $P$ in a random graph on $n$ vertices tends to $1$, which is yet another sense.
The related phrase "for all sufficiently large $n$" is on the page [[sufficiently large and eventually|FEQ7WATMHF]], and the other informal words of mathematics are on the page [[mathematical jargon|4M1FGQ0HNZ]].
