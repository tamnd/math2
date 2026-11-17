---
tag: 8AFXPXCE3N
kind: concept
name: Strong law of small numbers
aliases: [guys-law, second-strong-law-of-small-numbers]
msc: ["00A35", "00A08"]
topics: [DME0TPC348]
audience: ug1
uses: [8DHD3H1CJ9, WMEMMHZ3BH, 0ED72CTBNP, SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_law_of_small_numbers
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Moser%27s_circle_problem
    locator: lead section
---

## Summary

The strong law of small numbers is Richard Guy's name for the remark "There aren't enough small numbers to meet the many demands made of them."
It means that the first few terms of many different sequences agree by coincidence, because there are many sequences and few small numbers.
So a pattern seen in small cases is weak evidence for a general rule, and it often fails later.
Guy added a second law: "When two numbers look equal, it ain't necessarily so."
The law is a warning, not a theorem, and it guards the step from small cases to a [[conjecture|WMEMMHZ3BH]].

## Motivation

A student who sees $1, 2, 4, 8, 16$ guesses that the next term is $32$.
The guess is natural, and it is often right.
But the numbers $1, 2, 4, 8, 16$ are also the first values of many other rules, and one of them gives $31$ next.
The law of small numbers names this risk and explains its source.
It complements [[plausible reasoning|8DHD3H1CJ9]]: agreement on small cases is a weak consequence, because it would be likely even if the conjecture were false.

## Notation

There is no special notation.
The formal fact behind the law is that a finite list never determines its continuation.
For any values $a_1, \ldots, a_k$ and any $b$, there is a polynomial $p$ of degree at most $k$ with $p(i) = a_i$ for $i \leq k$ and $p(k+1) = b$, by [[polynomial interpolation|SS1YMS2NPC]].

## Remarks

### Examples

1. [[Patterns that eventually fail|A2KSJSQSF6]]: the circle regions $1, 2, 4, 8, 16, 31$, the polynomial $n^2 + n + 41$, the Fermat numbers and the Borwein integrals.
2. [[The primes 31, 331, 3331 and their end|1HBCH5V3AN]]: seven numbers of the form $33\ldots31$ are prime, and the eighth is $17 \cdot 19607843$.
3. [[Fermat's conjecture on Fermat numbers|VDZY463EKP]]: $2^{2^n} + 1$ is prime for $n = 0, 1, 2, 3, 4$, and Euler factored the next one.
4. The second law: $e^{\pi\sqrt{163}}$ looks like an integer to $12$ decimal places, and it is not one; see [[Ramanujan's constant is not an integer|7ZM5VCCB7H]].

### Non-examples

1. [[Sums of the first odd numbers|9WSEMZ8BWN]]: the pattern $1 + 3 + \cdots + (2n-1) = n^2$ seen in small cases is true for all $n$. The small cases did not mislead, so the law does not apply.
2. Two polynomials of degree at most $d$ that agree at $d + 1$ points are equal. Here small cases decide the question by a theorem, and no coincidence is possible.

### Basic properties

1. A finite list of values fits infinitely many rules; interpolation gives one rule for each choice of the next value.
2. Small numbers have many properties at once. For example, $31 = 2^5 - 1 = 1 + 2 + 4 + 8 + 16 = 1 + 5 + 25$, and $31$ is prime.
3. The law applies with more force when the sequence grows slowly, because then the first terms are small and coincidences are common.
4. The law does not apply when a theorem says that the checked cases determine the answer.
5. Agreement in small cases is evidence of low weight in the sense of [[plausible reasoning|8DHD3H1CJ9]], because it would be probable without the conjecture.

### History

Martin Gardner quoted the law from an unpublished paper of Guy in his Scientific American column of December 1980.
Guy published "The strong law of small numbers" in the American Mathematical Monthly in 1988, with many examples of patterns that hold and patterns that fail.
The Mathematical Association of America gave the paper its Lester Ford Award in 1989.
Guy published "The second strong law of small numbers" in Mathematics Magazine in 1990.
Guy used [[Moser's circle problem|M225KZAV4F]] as one of his examples.

### Common errors

1. Predicting the next term from the first few without a reason. The prediction is a conjecture, and it needs a proof or at least a mechanism.
2. Treating the law as a proof that a pattern fails. Many small patterns are true; the law only says that small cases carry little weight.
3. Checking more small cases of the same kind. They share the same coincidences, so they add little.

## Explanations

### L1 human

There are only a few small numbers, and many rules want to use them.
So different rules often give the same first few answers.
For example, $1, 2, 4$ could continue as $8$ (doubling) or as $7$ (adding $1$, then $2$, then $3$).
When a pattern works for the first few cases, it might be a real rule or just a coincidence.
Only a proof can tell.

### L2 human

We find two rules that agree on $1, 2, 4, 8, 16$ and differ at the next term.

1. The rule $a_n = 2^{n-1}$ gives $1, 2, 4, 8, 16, 32$.
2. The rule $b_n = \binom{n-1}{0} + \binom{n-1}{1} + \binom{n-1}{2} + \binom{n-1}{3} + \binom{n-1}{4}$ gives $1, 2, 4, 8, 16$ for $n = 1, \ldots, 5$, because then all subsets of an $(n-1)$-element set have at most $4$ elements.
3. For $n = 6$: $b_6 = 1 + 5 + 10 + 10 + 5 = 31$, because the term $\binom55 = 1$ is missing.
4. The rule $b_n$ counts the regions of a disc cut by the chords between $n$ points on its circle, in general position.

The typical use: before trusting a pattern, look for a second simple rule that fits the same data.
A trap: the more natural rule $2^{n-1}$ is not the true one for the regions.

### L3 human

The law has a counting form.
The number of rules that can be written with at most $\ell$ symbols grows exponentially in $\ell$, while the possible values of the first few terms are few.
So many short rules must share their first terms, and a match on the first terms is a weak test of a short rule.
In the language of [[numerical evidence|JFD3QWCX8Z]], small cases lie far below the scale at which most rules differ.
The second law has the same source: there are many short expressions, and some pairs of them agree to many digits by accident or for a reason that is not equality, as in [[Ramanujan's constant|7ZM5VCCB7H]].
