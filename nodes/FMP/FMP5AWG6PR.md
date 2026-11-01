---
tag: FMP5AWG6PR
kind: statement
role: lemma
name: Prime avoidance lemma
msc: [13A15]
uses: [0GYGHKX834, 0MYSA6MYNA, 06HC6HK0Z8]
about: [06HC6HK0Z8]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_avoidance_lemma
same_as:
  wikidata: Q3229333
  wikipedia: Prime avoidance lemma
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]], let $I$ be an [[ideal|0MYSA6MYNA]] of $R$, and let $P_1, \ldots, P_n$ be finitely many [[prime ideals|06HC6HK0Z8]] of $R$, with $n \ge 1$.
If $I \subseteq P_1 \cup \cdots \cup P_n$, then $I \subseteq P_i$ for some $i$.

## Remarks

The proof is by induction on $n$.
If $I$ is contained in no $P_i$, the induction hypothesis gives, for each $i$, an element $x_i \in I$ that lies in no $P_j$ with $j \ne i$; one may assume $x_i \in P_i$.
Then $y = x_1 + x_2 x_3 \cdots x_n$ lies in $I$ but in none of the $P_i$, using that $P_1$ is prime for the term $x_2 \cdots x_n$.
The same proof works when at most two of the $P_i$ are not prime.
Primality is needed: in $R = \F_2[x, y]/(x, y)^2$, the maximal ideal $(x, y) = \set{0, x, y, x + y}$ is the union of the three ideals $(x)$, $(y)$, $(x + y)$, but it is contained in none of them.
Finiteness is needed: in $k[x, y]$ for a field $k$, every nonzero element of $(x, y)$ has an irreducible factor vanishing at the origin.
So $(x, y)$ is the union of infinitely many principal prime ideals, none of which contains it.

## Explanations

### L1 human

An ideal cannot hide inside a finite union of prime ideals without being inside one of them.
So if an ideal is not contained in any of finitely many primes, one can find a single element of the ideal that avoids all of them at once.
This is the form in which the lemma is used most often.

### L2 human

Prime avoidance is a tool for choosing good elements.
For example, let $M$ be a finitely generated module over a Noetherian ring, and let $I$ be an ideal whose elements are all zero divisors on $M$.
Since [[zero divisors are the union of associated primes|S37DQGW3TZ]], $I$ lies in the union of the finitely many [[associated primes|ERFZ6S8X0X]] of $M$.
So $I$ lies in one associated prime.
In dimension theory the lemma lets one choose elements outside all minimal primes, which is how [[regular sequences|69R5R2FCS5]] and [[systems of parameters|95QTEPMDA4]] are built one element at a time.
If $R$ contains an infinite field, the conclusion holds even when none of the ideals $P_i$ is prime, by a vector space argument.
