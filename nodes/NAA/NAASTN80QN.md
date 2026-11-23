---
tag: NAASTN80QN
kind: concept
name: ACA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [DC60FYCSPM, XQENB067R3, 60P2XWY5QX, HACXBCM7SS]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Arithmetical comprehension
---

## Summary

The Bolzano-Weierstrass theorem says that every sequence in $[0, 1]$ has a convergent subsequence, and over the computable base system it is [[equivalent to ACA0|HV153Y95MQ]].
So $\mathsf{ACA}_0$ measures exactly the strength of sequential compactness: the power to decide the halting problem, and more generally to form the [[Turing jump|60P2XWY5QX]] of any given set.
Its axioms are the basic axioms of [[second-order arithmetic|DC60FYCSPM]], the set induction axiom, and comprehension for every arithmetical formula $\varphi$, that is, every formula with number quantifiers only, as in the [[formal definition|K9XG0Z2N9V]]:
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \varphi(n)\big).$$
Over [[RCA0|XQENB067R3]] the scheme is equivalent to the single statement that every set has a Turing jump.
$\mathsf{ACA}_0$ is the third of the big five systems, and it proves exactly the same arithmetical sentences as [[Peano arithmetic|HACXBCM7SS]].

## Motivation

Many theorems of analysis and algebra have computable instances whose solutions compute the halting problem.
A computable bounded increasing sequence of rationals can have a limit that computes $\emptyset'$, and a computable vector space over $\mathbb{Q}$ can have no computable basis.
Such theorems cannot be proved in $\mathsf{RCA}_0$, whose least model is the computable sets.

Arithmetical comprehension is the natural cure, since it gives every set that number quantifiers define.
It is also enough for most of the analysis of sequences and series in a first course, and Weyl's [[predicative analysis|43BSXNWQBG]] already worked at about this level.
The next system, [[ATR0|MKB74TX3Z8]], is needed only when a construction iterates the jump transfinitely often.

## Notation

The name abbreviates "arithmetical comprehension axiom", and the subscript $0$ marks the restriction of induction to the single set induction axiom.
$\mathsf{ACA}$ without the subscript has the induction scheme for all formulas of $L_2$.
$\mathsf{ACA}_0^+$ adds the axiom that the $\omega$-th jump $X^{(\omega)}$ of every set $X$ exists.

## Remarks

### Why Bolzano-Weierstrass needs the halting problem

Take a one-to-one function $f$, say with $f(0) = 3$, $f(1) = 0$, $f(2) = 5$ and $f(3) = 1$, and add up $2^{-f(i) - 1}$:
$$c_0 = \tfrac{1}{16}, \quad c_1 = \tfrac{1}{16} + \tfrac{1}{2} = \tfrac{9}{16}, \quad c_2 = \tfrac{9}{16} + \tfrac{1}{64} = \tfrac{37}{64}, \quad c_3 = \tfrac{37}{64} + \tfrac{1}{4} = \tfrac{53}{64}.$$
The sequence increases and stays below $1$, so the theorem gives a limit $L$.
Since $f$ is one-to-one, $L = \sum_{m \in \operatorname{ran} f} 2^{-m-1}$.

Now suppose we know $c_n$ with $L - c_n < 2^{-m-1}$.
If $m = f(i)$ for some $i > n$, then the term $2^{-m-1}$ is still missing from $c_n$, and $L - c_n \ge 2^{-m-1}$.
So $m$ is in the range of $f$ exactly when $f(i) = m$ for some $i \le n$, a finite check.
For $f$ listing the halting set, the limit therefore decides the halting set, and this is the whole idea of the reversal.

### König's lemma and the bound on branching

[[König's lemma|3P2J5NWCM1]] for infinite finitely branching trees is also equivalent to $\mathsf{ACA}_0$.
The classical proof always steps to a child with infinitely many nodes above it, and "infinitely many nodes above" is an arithmetical property.
For binary trees the same statement is only weak König's lemma, the axiom of [[WKL0|7W9EG02T79]].
The difference is that a binary tree tells us its possible children in advance, while a general finitely branching tree does not.

### Models

The [[arithmetical sets|9KPCZ6NA32]] form the least $\omega$-model of $\mathsf{ACA}_0$.
Every $\omega$-model of $\mathsf{ACA}_0$ is a Turing ideal closed under the jump, and conversely every such ideal is an $\omega$-model.

Two models of weaker systems fail it.
The [[ω-model of low sets|8B045KSKW5]] satisfies $\mathsf{WKL}_0$, but it omits $\emptyset'$.
The [[sets computable from the halting set|7KCGVY6XJM]] satisfy $\mathsf{RCA}_0$, but they omit $\emptyset''$, the jump of their largest set.

### Equivalents and strength

Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to $\Sigma^0_1$ comprehension and to the [[existence of ranges of one-to-one functions|3MQ39PRCYJ]], and these are the usual targets of reversals.
The [[existence of Turing jumps|10NR4PGXHW]] is another form of the same axiom.
In analysis it is equivalent to the convergence of bounded increasing sequences and to the Cauchy completeness of the reals.
In algebra it is equivalent to the existence of a basis of every countable vector space over $\mathbb{Q}$ and of a maximal ideal in every countable commutative ring.
In combinatorics it is equivalent to Ramsey's theorem for triples and two colors.

For arithmetical sentences $\mathsf{ACA}_0$ [[is conservative over Peano arithmetic|HPA6HX3114]], and its proof-theoretic ordinal is $\varepsilon_0$, the ordinal of Peano arithmetic.
It proves weak König's lemma, and the low model shows that it is strictly stronger than $\mathsf{WKL}_0$.

### Watch out

$\mathsf{ACA}_0$ proves that each finite jump $\emptyset^{(n)}$ exists, but it does not prove that the sequence of all of them exists as one set.
The wrong move is an induction on $n$ that builds $\emptyset^{(n)}$ step by step and then collects the steps.
The arithmetical sets are a model of $\mathsf{ACA}_0$ that contains every $\emptyset^{(n)}$ and not $\emptyset^{(\omega)}$, so no such proof exists.
The collected sequence needs $\mathsf{ACA}_0^+$, which [[ATR0 proves|MF6AG57W3W]].

The conservation over Peano arithmetic also needs the subscript.
With the full induction scheme, $\mathsf{ACA}$ proves the consistency of Peano arithmetic, so it is not conservative over it.

### History

Hermann Weyl's book *Das Kontinuum* (1918) developed analysis with sets defined by number quantifiers, which is close in spirit to $\mathsf{ACA}_0$.
Harvey Friedman's program of reverse mathematics, announced at the International Congress of Mathematicians in Vancouver in 1974, placed $\mathsf{ACA}_0$ among its main systems.

### Try it

First, does $\mathsf{ACA}_0$ prove that the set of indices $e$ such that the $e$-th program halts on every input exists?
Yes: "for every $x$ there is a stage $s$ at which program $e$ halts on $x$" is an arithmetical formula.

Second, for the function above, how large can $L - c_3$ be if $f$ takes no further values below $6$?
Then all later terms are at most $2^{-7}$ and distinct, so $L - c_3 \le 2^{-7} + 2^{-8} + \cdots = \tfrac{1}{64}$.

## Explanations

### L1 human

$\mathsf{ACA}_0$ lets a set exist whenever we can describe it with "for every number" and "there is a number".
That is enough to prove most theorems about sequences of real numbers, such as the fact that a bounded increasing sequence has a limit.
It is also exactly what these theorems need, because their limits can encode a list of all programs that halt.

### L2 human

Here is a reversal of the monotone convergence theorem, the special case of Bolzano-Weierstrass for increasing sequences.
Given a one-to-one $f$, form $c_n = \sum_{i \le n} 2^{-f(i) - 1}$, which exists in $\mathsf{RCA}_0$ and increases below $1$.
The theorem gives the limit $L$, and from a code of $L$ we can find, for each $m$, an index $n$ with $L - c_n < 2^{-m-1}$ by a search that always ends.
Then $m$ is in the range of $f$ exactly when it appears among $f(0), \ldots, f(n)$, as in the first remark.
So the range of $f$ exists, and by the [[range lemma|3MQ39PRCYJ]] this gives all of $\mathsf{ACA}_0$.
The trap is to think that the limit of an increasing sequence comes with a rate of convergence: the rate is exactly what the proof extracts from the limit.

### L3 human

The $\omega$-models of $\mathsf{ACA}_0$ are the jump ideals, which connects the system with degree theory.
In proof theory, $\mathsf{ACA}_0$ has the same ordinal $\varepsilon_0$ as Peano arithmetic.
Between $\mathsf{ACA}_0$ and $\mathsf{ATR}_0$ lie systems such as $\mathsf{ACA}_0^+$, and Hindman's theorem is provable in $\mathsf{ACA}_0^+$ and implies $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$, with its exact strength still open.
The [[reverse mathematics zoo|E3X5B175ZR]] collects the many principles below $\mathsf{ACA}_0$ that do not reach it, such as [[Ramsey's theorem for pairs|ZT5KV6KJ3E]].
