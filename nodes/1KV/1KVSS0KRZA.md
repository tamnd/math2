---
tag: 1KVSS0KRZA
kind: concept
name: Counting arguments for existence
aliases: [counting-arguments-for-existence]
msc: ["00A35", "05D40"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: ug1
uses: [0HGVCWQGY3, 01TQB88H4C, 0GBZM0MT0F, 0EGSEE9J9R]
sources:
  - url: https://en.wikipedia.org/wiki/Probabilistic_method
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Transcendental_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Circuit_complexity
    locator: lead section
---

## Summary

A counting argument for existence proves that an object with a property exists by showing that there are fewer bad objects than objects.
Let $S$ be a finite set, and let $B \subseteq S$ be the set of bad objects.
If $|B| < |S|$, then some element of $S$ is not in $B$, so a good object exists.
The infinite form compares sizes of sets: if $S$ is [[uncountable|0W7FBYS1F1]] and $B$ is [[countable|01TQB88H4C]], then $S \setminus B$ is nonempty.
The method is important because it proves existence when no single good object is known.

## Motivation

Some objects are hard to describe one by one, but easy to count as a class.
A specific real number is hard to prove [[transcendental|0VTQXTCR2G]], but the [[algebraic numbers|0MNF0BYFQC]] are easy to list.
A specific [[Boolean function|0X05GS525E]] is hard to prove complex, but small circuits are easy to count.
In both cases, the bad objects are few, and the good objects must fill the rest.
The argument turns a count into an existence proof, often with the extra result that most objects are good.

## Remarks

### The steps

1. Choose a set $S$ of candidates and compute or bound $|S|$ from below.
2. Write the bad objects as a union $B = B_1 \cup \cdots \cup B_m$ of simple classes.
3. Bound each $|B_i|$ from above, and use $|B| \le |B_1| + \cdots + |B_m|$.
4. Show that the bound on $|B|$ is strictly less than $|S|$.
5. Conclude that some candidate is in no class $B_i$, so it is good.

### Examples

- Real [[transcendental numbers|0VTQXTCR2G]] exist. The algebraic numbers form a countable set, and the real numbers are [[uncountable|0518MM6BE1]], so some real number is not algebraic, as [[this example|8H2PE4ZS53]] shows.
- Some [[Boolean function|0X05GS525E]] of $10$ variables has no [[circuit|SQXNFGVADX]] with at most $71$ gates. There are $2^{1024}$ such functions and fewer than $2^{1020}$ circuits of this size, as [[this example|WFAC541D0V]] shows. The general form is [[Shannon's counting argument|2R30KR3Z5G]].
- The [[Ramsey number|0K9QVPJYJF]] $R(k, k)$ is greater than $n$ when $\binom{n}{k} 2^{1 - \binom{k}{2}} < 1$. There are $2^{\binom{n}{2}}$ colourings of the edges of $K_n$, and each set of $k$ vertices is one colour in $2^{1 + \binom{n}{2} - \binom{k}{2}}$ of them. The bad colourings are fewer than all colourings, so some colouring has no monochromatic $K_k$. This is the [[probabilistic lower bound|SAZNT80CG5]] in counting form. For $k = 10$ and $n = 32$, the left side is about $3.7 \cdot 10^{-6}$, so $R(10, 10) > 32$.
- Some binary string of length $n$ is not the output of any shorter description. There are $2^n$ strings of length $n$, and only $2^0 + 2^1 + \cdots + 2^{n-1} = 2^n - 1$ shorter strings.
- Some real number is not computable. A computer program is a finite string, so there are only countably many programs and countably many computable real numbers.

### Non-examples

- If the count of bad objects is at least the count of all objects, the argument gives nothing. For triangles in $K_6$, the bound on the bad colourings is $5$ times the number of colourings, as [[this example|H8GK0ABYVC]] shows.
- Liouville's proof that the [[Liouville number|0PYEZM6CN9]] $\sum_{k \ge 1} 10^{-k!}$ is transcendental is not a counting argument. It proves one specific number transcendental, by [[Liouville's theorem on Diophantine approximation|0N3WFZEFPM]].
- A comparison of two infinite sets of the same size gives nothing. The rational numbers and the integers are both countable, and a count of this kind cannot prove that a non-integer rational exists.

### Basic properties

- Union bound: $|B_1 \cup \cdots \cup B_m| \le |B_1| + \cdots + |B_m|$. This is [[Boole's inequality|0EGSEE9J9R]] for counting measure. An overcount of the bad objects is safe, and an undercount is not.
- Most objects are good: if $|B| \le \varepsilon |S|$, then at least $(1 - \varepsilon)|S|$ objects are good. The proof of one good object often gives this stronger result.
- Probabilistic form: choose an element of $S$ uniformly at random. Then $|B| < |S|$ is the statement that the probability of a bad element is less than $1$.
- Infinite form: if $S$ is uncountable and $B$ is countable, then $S \setminus B$ is uncountable, and not only nonempty.
- The argument is non-constructive. It proves that a good object exists, and it gives no method to name one.

### When it fails

The plain count fails when the bad classes overlap heavily, so that the sum $\sum_i |B_i|$ is much larger than $|B|$.
Two refinements help in this case.
The alteration method removes a few bad parts from a random object.
The [[Lovász local lemma|35YQ94FNV1]] uses limited dependence between the bad events.

### Related methods

The [[pigeonhole principle|0HGVCWQGY3]] is the counting argument for a map: if $|A| > |C|$, then no map from $A$ to $C$ is injective.
The [[averaging argument|HXP9VMXV8S]] is the quantitative form: it gives an object with a score at least the average.
The [[probabilistic method|3B55HNS754]] states the same counts in the language of probability.
Counting arguments are a main source of [[non-constructive existence proofs|958EF46EYJ]].

### History

Georg Cantor proved in 1874 that the algebraic numbers are countable and the real numbers are not.
His result gave a new proof that transcendental numbers exist, and it showed that they are most of the real numbers.
Paul Erdős proved the lower bound on Ramsey numbers by a count of colourings in 1947.
Claude Shannon proved in 1949 that most Boolean functions of $n$ variables need large circuits.

### Common errors

- To use a non-strict inequality. The conclusion needs $|B| < |S|$, and $|B| \le |S|$ is not enough.
- To undercount the bad objects. Each bad object must lie in at least one class $B_i$.
- To expect the argument to give an example. It proves existence only, and an explicit example can remain unknown.
- To compare infinite sets by "both are infinite". The infinite form needs a difference in cardinality.

## Explanations

### L1 human

Suppose a bag holds $100$ balls, and at most $99$ of them are red.
Then at least one ball is not red, even if we cannot see which one.
A counting argument for existence works in this way.
We count all the objects, we count the bad ones, and we show that the bad ones are fewer.
For example, there are more real numbers than roots of whole-number equations, so some real number is not such a root.

### L2 human

We show that some binary string of length $4$ is not the output of a given rule applied to a shorter string.

1. The set $S$ is the set of binary strings of length $4$. So $|S| = 2^4 = 16$.
2. The inputs are the binary strings of length $0$, $1$, $2$ or $3$. There are $1 + 2 + 4 + 8 = 15$ of them.
3. Any rule maps each input to at most one output. So at most $15$ strings of length $4$ are outputs.
4. Since $15 < 16$, some string of length $4$ is not an output of the rule.

The typical use is in this form: count the possible short descriptions, and compare with the number of objects.
A trap is to try to name the string that is missed.
The missed string depends on the rule, and the argument does not identify it.

### L3 human

A counting argument for existence is the case of the [[probabilistic method|3B55HNS754]] where the probability space is uniform and the bad event has probability less than $1$.
Its strength is that it often proves that almost all objects are good, which is a statement about a typical object.
Its weakness is the gap between existence and construction.
Most Boolean functions need circuits of size about $2^n/n$, by [[Shannon's counting argument|2R30KR3Z5G]], but the best known lower bounds for explicit functions are only linear in $n$.
Most real numbers are transcendental and [[normal|C98T2T5FJS]], but the proof that a specific number such as $\pi$ is normal is an open problem.

The same idea gives incompressible strings in Kolmogorov complexity, codes with large distance by a greedy count, and graphs with many properties at once.
In set theory, the infinite form is a comparison of cardinal numbers.
A sharper tool than the count is often the [[averaging argument|HXP9VMXV8S]], which gives an object better than average and not only an object outside a small set.
