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

A counting argument for existence proves that a good object exists by showing that the bad objects are fewer than all the objects.
It names no good object, and it often proves more: most objects are good.

Here is a first problem.
Is there a real number that is not a root of any nonzero polynomial with integer coefficients, that is, a [[transcendental number|0VTQXTCR2G]]?
The integer polynomials can be put in one list, each has finitely many roots, so the [[algebraic numbers|0MNF0BYFQC]] can be listed too, and they form a [[countable set|01TQB88H4C]].
The real numbers [[cannot be listed|0518MM6BE1]].
So some real number is missing from the list of algebraic numbers, and it is transcendental; [[the transcendental example|8H2PE4ZS53]] gives every step.

The exact form is short.
Let $S$ be a finite set of candidates and $B \subseteq S$ the set of bad candidates.
If $|B| < |S|$, then $S \setminus B$ is nonempty, so a good candidate exists.
The infinite form compares sizes of sets: if $S$ is [[uncountable|0W7FBYS1F1]] and $B$ is countable, then $S \setminus B$ is nonempty, and in fact uncountable.

## Motivation

Some objects are hard to describe one by one but easy to count as a class.
A specific real number is hard to prove transcendental: the proofs for $e$ and $\pi$ need serious analysis.
A specific [[Boolean function|0X05GS525E]] is hard to prove complex: no explicit function is known to need more than a small multiple of $n$ gates.
But the algebraic numbers are easy to list, and the small circuits are easy to count.
In both cases the bad objects are few, and the good objects must fill the rest.

The method is the root of the [[probabilistic method|3B55HNS754]] in combinatorics, of lower bounds in complexity theory and of incompressible strings in information theory.
It is a main source of [[non-constructive existence proofs|JZQVJ9XT63]].

## Notation

The method has no notation of its own.
Its basic tool is the union bound $|B_1 \cup \cdots \cup B_m| \le |B_1| + \cdots + |B_m|$, which is [[Boole's inequality|0EGSEE9J9R]] for counting measure.
In probabilistic language, $|B| < |S|$ says that a uniformly random candidate is bad with probability less than $1$.

## Remarks

### How to set up the count

A counting proof has four steps.

1. Choose a set $S$ of candidates, and compute $|S|$ or bound it from below.
2. Write the bad candidates as a union $B = B_1 \cup \cdots \cup B_m$ of simple classes, one for each way to fail.
3. Bound each $|B_i|$ from above, and add: $|B| \le |B_1| + \cdots + |B_m|$.
4. Show that this bound is strictly less than $|S|$, and conclude that some candidate lies in no class $B_i$.

An overcount of the bad candidates is safe, because it only makes step 4 harder.
An undercount is fatal: each bad candidate must lie in at least one class $B_i$.
The skill is in step 2, where a good choice of classes makes each $|B_i|$ easy and the overlaps small.

### Boolean functions without small circuits

A Boolean function of $n$ variables is a map $\{0, 1\}^n \to \{0, 1\}$.
Its domain has $2^n$ points, and each point has $2$ possible values, so there are $2^{2^n}$ functions.
A [[circuit|SQXNFGVADX]] with $s$ gates over AND, OR and NOT can be described by a type and two input nodes for each gate, and an output node.
The $n$ inputs and $s$ gates give $n + s$ nodes, so at most
$$(n + s) \cdot \big(3 (n + s)^2\big)^s$$
functions have a circuit with at most $s$ gates, after padding smaller circuits with unused gates.
For $n = 10$ and $s = 71$ this is about $2^{1019.1} < 2^{1024}$, so some function of $10$ variables needs more than $71$ gates, as [[the circuit count|WFAC541D0V]] checks.
For large $n$ the same count gives [[Shannon's counting argument|2R30KR3Z5G]]: most functions need circuits of size of order $2^n/n$.

### Ramsey numbers by counting

Color each edge of the [[complete graph|03WKB2H474]] $K_n$ red or blue, in all $2^{\binom{n}{2}}$ ways.
A fixed set of $k$ vertices has all its $\binom{k}{2}$ edges of one color in $2 \cdot 2^{\binom{n}{2} - \binom{k}{2}}$ colorings.
There are $\binom{n}{k}$ such sets, so if
$$\binom{n}{k} \, 2^{1 - \binom{k}{2}} < 1,$$
the bad colorings are fewer than all colorings, and some coloring has no $K_k$ of one color.
Then the [[Ramsey number|0K9QVPJYJF]] $R(k, k)$ is greater than $n$; this is the [[probabilistic lower bound|SAZNT80CG5]] in counting form.
For $k = 10$ and $n = 32$, the left side is $\binom{32}{10} \cdot 2^{-44} \approx 3.7 \cdot 10^{-6}$, so $R(10, 10) > 32$.

### When the count proves nothing

The count gives nothing when the bound on the bad objects is at least the number of all objects.
For triangles in $K_6$ the union bound is $5$ times the number of colorings, as [[the K6 count|H8GK0ABYVC]] shows.
There the conclusion is false too, since every coloring of $K_6$ has a triangle of one color, but a failed count alone never proves nonexistence: for $K_5$ the bound is $5/2$ times too large, and a good coloring exists.

Some existence proofs are not counts at all.
Liouville's proof that the [[Liouville number|0PYEZM6CN9]] $\sum_{k \ge 1} 10^{-k!}$ is transcendental proves one specific number transcendental by [[Liouville's theorem on Diophantine approximation|0N3WFZEFPM]].
And a comparison of two infinite sets of the same size gives nothing: the integers and the rationals are both countable, so no count of this kind shows that a non-integer rational exists.

When the bad classes overlap heavily, the sum $\sum_i |B_i|$ is much larger than $|B|$, and two refinements help.
The alteration method removes a few bad parts from a random object, and the [[Lovász local lemma|35YQ94FNV1]] uses limited dependence between the bad events.

### Watch out

The inequality must be strict.
For four vertices and triangles, the union bound equals the number of colorings exactly, and $|B| \le |S|$ allows $B = S$.
The infinite form needs a difference in size, not just "both are infinite".
And the argument does not give an example: after the count, you still do not know a single transcendental number or a single hard Boolean function.

### History

Georg Cantor proved in 1874 that the algebraic numbers are countable and the real numbers are not.
This gave a new proof that transcendental numbers exist, and it showed that they are most of the real numbers.
Paul Erdős proved his lower bound on Ramsey numbers by a count of colorings in 1947.
Claude Shannon proved in 1949 that most Boolean functions of $n$ variables need large circuits.

### Try it

First, show that some binary string of length $10$ is not the output of a fixed rule applied to a shorter binary string.
The shorter strings number $1 + 2 + 4 + \cdots + 512 = 1023$, so the rule has at most $1023$ outputs among the $1024$ strings of length $10$.

Second, show that some $6$-digit number is not the product of two $3$-digit numbers.
There are $900$ three-digit numbers, so at most $\binom{900}{2} + 900 = 405450$ products $ab$ with $a \le b$, and there are $900000$ six-digit numbers.

## Explanations

### L1 human

Suppose a bag holds $100$ balls, and at most $99$ of them are red.
Then at least one ball is not red, even if you cannot see which one.
A counting argument for existence works in this way.
You count all the objects, you count the bad ones, and you show that the bad ones are fewer.
For example, there are more real numbers than roots of whole-number equations, so some real number is not such a root.

### L2 human

Here is a typical problem: color the $15$ edges of $K_6$ red and blue so that no four vertices have all six of their edges in one color.
There are
$$2^{15} = 32768$$
colorings in all.
Fix a set of $4$ vertices, with its $\binom{4}{2} = 6$ edges.
Those edges are all red or all blue in $2 \cdot 2^{15 - 6} = 1024$ colorings.
There are $\binom{6}{4} = 15$ sets of four vertices, so the bad colorings number at most
$$15 \cdot 1024 = 15360 < 32768.$$
So a good coloring exists, and $R(4, 4) > 6$; in fact more than half of all colorings are good.

The problem shows the usual pattern: one bad class for each way to fail, the union bound, and a strict comparison.
Watch out: the count gives only $R(4, 4) > 6$, while the true value is $18$, so the method can be far from sharp for small numbers.

### L3 human

A counting argument for existence is the case of the [[probabilistic method|3B55HNS754]] with a uniform probability space and a bad event of probability less than $1$.
Its strength is that it often proves that almost all objects are good, which is a statement about a typical object.
Its weakness is the gap between existence and construction.
Most Boolean functions need circuits of size of order $2^n/n$, but the best known lower bounds for explicit functions are only linear in $n$.
Most real numbers are transcendental and [[normal|C98T2T5FJS]], but whether a specific number such as $\pi$ is normal is an open problem.

The same idea gives incompressible strings in Kolmogorov complexity, codes with large distance by a greedy count, and graphs with many properties at once.
In set theory, the infinite form is a comparison of cardinal numbers, and its sharpest form is [[diagonalization|V2H30SA654]], which builds the missing object from the list.
The [[averaging argument|HXP9VMXV8S]] is the quantitative relative: it gives an object at least as good as the average, not only an object outside a small set.
