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

The strong law of small numbers is Richard Guy's warning that the first few cases of a pattern prove very little.
In his words, there are not enough small numbers to meet the many demands made of them, so different rules often agree on their first values by coincidence.

Here is the case to check with a pencil.
Put $n$ points on a circle, join every pair by a chord, and count the regions inside the circle, with no three chords through one point.
For $n = 1, 2, 3, 4, 5$ you get
$$1, \ 2, \ 4, \ 8, \ 16,$$
and the doubling rule predicts $32$ for $n = 6$.
The count for $n = 6$ is $31$.
The true formula is
$$\binom{n}{4} + \binom{n}{2} + 1,$$
which gives $15 + 15 + 1 = 31$ at $n = 6$ and agrees with $2^{n-1}$ only for $n \le 5$.

So a pattern seen in small cases is weak evidence for a general rule.
Guy added a second law: when two numbers look equal, they need not be equal.
Both laws are warnings, not theorems, and they guard the step from small cases to a [[conjecture|WMEMMHZ3BH]].

## Motivation

A student who sees $1, 2, 4, 8, 16$ guesses that $32$ comes next.
The guess is natural, and it is often right.
But $1, 2, 4, 8, 16$ also starts many other rules, and the circle gives one of them.
The law names this risk and explains its source: there are many simple rules and few small numbers.

In the language of [[plausible reasoning|8DHD3H1CJ9]], agreement on small cases is a consequence that would be likely even if the conjecture were false, so it adds little credibility.
The law returns in [[patterns that eventually fail|A2KSJSQSF6]], in [[numerical evidence for conjectures|JFD3QWCX8Z]] at a much larger scale, and in [[forming conjectures|R2T42N5XGK]], where it tells you to test cases of a new kind.

## Notation

There is no special notation.
The exact fact behind the law is that a finite list never determines its continuation.
For any values $a_1, \ldots, a_k$ and any number $b$, [[polynomial interpolation|SS1YMS2NPC]] gives a polynomial $p$ of degree at most $k$ with
$$p(1) = a_1, \ \ldots, \ p(k) = a_k, \quad p(k+1) = b.$$
[[A finite list does not determine its continuation|G9FEX51ASB]] works this out for $1, 2, 4, 8, 16$.

## Remarks

### Small cases that mislead

The circle regions, the polynomial $n^2 + n + 41$, the Fermat numbers and the Borwein integrals are collected in [[patterns that eventually fail|A2KSJSQSF6]].
[[The primes 31, 331, 3331 and their end|1HBCH5V3AN]] adds a case from decimal digits.
The numbers $31, 331, \ldots, 33333331$ are seven primes in a row, and the eighth is
$$333333331 = 17 \cdot 19607843.$$
In [[Fermat's conjecture on Fermat numbers|VDZY463EKP]], $2^{2^n} + 1$ is prime for $n = 0$ to $4$, and Euler factored the next one in 1732:
$$2^{32} + 1 = 4294967297 = 641 \cdot 6700417.$$

### The second law

The second law is about numbers that agree to many digits.
The number $e^{\pi \sqrt{163}}$ is $262537412640768743.99999999999925\ldots$, within $10^{-12}$ of an integer and not equal to it; see [[Ramanujan's constant is not an integer|7ZM5VCCB7H]].
The Borwein integrals fall below $\pi/2$ only in the eleventh decimal place.
Close agreement has a cause in both cases, but the cause is not equality.

### When small cases do decide

[[Sums of the first odd numbers|9WSEMZ8BWN]] is a case where the law has nothing to warn about.
The sums $1, 4, 9, 16, 25$ suggest $1 + 3 + \cdots + (2n - 1) = n^2$, and induction proves it for every $n$.
Small cases can also decide a question by a theorem.
Two polynomials of degree at most $d$ that agree at $d + 1$ points are equal, so checking $d + 1$ values is a proof, not evidence.

### The rules you can use

A finite list fits infinitely many rules, one for each choice of the next value.
Small numbers have many properties at once; for example
$$31 = 2^5 - 1 = 1 + 2 + 4 + 8 + 16 = 1 + 5 + 25,$$
and $31$ is prime.
The law has more force when a sequence grows slowly, because then the first terms are small and coincidences are common.
It does not apply when a theorem says that the checked cases determine the answer.

### Watch out

A pattern that holds in many cases is not a proof, and a pattern that holds in five cases is barely evidence.
Predict the next term only with a reason, a mechanism or a proof.

The opposite error is to read the law as a proof that a pattern fails.
Many small patterns are true, as the odd numbers show; the law only says that small cases carry little weight.

A third error is to check more small cases of the same kind.
They share the same coincidences, so they add little.

### History

Martin Gardner quoted the law from a paper of Guy in his *Scientific American* column of December 1980.
Guy published "The strong law of small numbers" in the *American Mathematical Monthly* in 1988, with many patterns that hold and many that fail.
The paper received the Lester R. Ford Award of the Mathematical Association of America.
Guy published "The second strong law of small numbers" in *Mathematics Magazine* in 1990.
[[Moser's circle problem|M225KZAV4F]] is one of his examples.

### Try it

Find a rule that gives $1, 2, 4$ and then $7$.
Add $1$, then $2$, then $3$: the rule $a_n = 1 + n(n-1)/2$ gives $1, 2, 4, 7, 11$.

How many regions do $7$ points give?
The formula gives $\binom{7}{4} + \binom{7}{2} + 1 = 35 + 21 + 1 = 57$, against $64$ for doubling.

## Explanations

### L1 human

There are only a few small numbers, and many rules want to use them.
So different rules often give the same first few answers.
For example, $1, 2, 4$ could go on as $8$ (doubling) or as $7$ (add $1$, then $2$, then $3$).
When a pattern works for the first few cases, it might be a real rule or a coincidence.
Only a proof can tell.

### L2 human

We find two rules that agree on $1, 2, 4, 8, 16$ and differ at the next term.
The first rule is $a_n = 2^{n-1}$, which gives $1, 2, 4, 8, 16, 32$.
The second rule is
$$b_n = \binom{n-1}{0} + \binom{n-1}{1} + \binom{n-1}{2} + \binom{n-1}{3} + \binom{n-1}{4}.$$
For $n \le 5$ this sum counts all subsets of a set with $n - 1 \le 4$ elements, so $b_n = 2^{n-1}$.
For $n = 6$ the term $\binom{5}{5} = 1$ is missing, so
$$b_6 = 1 + 5 + 10 + 10 + 5 = 31.$$
The rule $b_n$ equals $\binom{n}{4} + \binom{n}{2} + 1$, so it counts the circle regions.

The typical use: before trusting a pattern, look for a second simple rule that fits the same data.
Watch out: here the less obvious rule is the true one.

### L3 human

The law has a counting form.
The number of rules that can be written with at most $\ell$ symbols grows exponentially in $\ell$, while the possible values of the first few terms are few.
So many short rules must share their first terms, and a match on the first terms is a weak test of a short rule.
In the language of [[numerical evidence|JFD3QWCX8Z]], small cases lie far below the scale at which most rules differ.
The second law has the same source: there are many short expressions, and some pairs agree to many digits by accident or for a reason that is not equality, as with [[Ramanujan's constant|7ZM5VCCB7H]].
