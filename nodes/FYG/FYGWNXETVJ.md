---
tag: FYGWNXETVJ
kind: concept
name: IΔ0 and the linear-time hierarchy
aliases: [rudimentary-sets, delta-zero-definable-sets, linear-time-hierarchy]
msc: ["03F30", "03D15", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [GE43CSZTS9, T70PYM1F36, D8SD54M5PN, PPGD5KW8JC, TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Rudimentary_function
    locator: lead section
---

## Summary

A set $X \subseteq \N^k$ is $\Delta_0$-definable when some [[$\Delta_0$ formula|GE43CSZTS9]] $\theta(\bar x)$ of the [[language of arithmetic|D8SD54M5PN]] defines it in $\N$: $\bar n \in X$ if and only if $\N \models \theta(\bar n)$.
These sets are exactly Smullyan's rudimentary relations, and exactly the sets in the linear-time hierarchy $\mathrm{LinH}$, when a number is given in binary.
Here $\mathrm{LinH}$ is the class of sets decided in time $O(n)$ by alternating Turing machines with a bounded number of alternations, where $n$ is the length of the input.
The theory $\mathsf{I}\Delta_0$ has induction for exactly these sets, so it is the theory of bounded arithmetic that belongs to $\mathrm{LinH}$, as $S^1_2$ belongs to polynomial time.
The match explains both what $\mathsf{I}\Delta_0$ can prove and why some questions about it, such as the pigeonhole principle, are hard.

## Motivation

A bounded quantifier $\exists y < t(x)$ in $\N$ ranges over numbers below a polynomial in $x$.
Such a number has binary length at most a constant times the length of $x$.
So a $\Delta_0$ formula describes a guess of a linear number of bits, then a check of the guess, with a fixed number of alternations of guesses.
This is an alternating computation in linear time, and the converse also holds.
The correspondence turns questions about the [[fragment|T70PYM1F36]] $\mathsf{I}\Delta_0$ into questions about a natural complexity class.

## Notation

- $\Delta_0$ is also written $\Sigma_0$, $\Pi_0$ or $\Sigma^0_0$. The class of rudimentary relations is written $\mathrm{Rud}$.
- $\mathrm{LinH}$ is also written $\mathrm{LTH}$. Its levels are $\Sigma^{\mathrm{lin}}_k$, the sets decided in linear time by alternating machines that start in an existential state and alternate at most $k - 1$ times.
- $\mathrm{NLIN}$ is $\Sigma^{\mathrm{lin}}_1$, nondeterministic linear time.
- $\mathsf{I}\Delta_0(R)$ is $\mathsf{I}\Delta_0$ in the language with a new relation symbol $R$, with induction for $\Delta_0$ formulas that may contain $R$.

## Remarks

### Examples

- The set of perfect squares, defined by $\exists y < x + 1 \, (y \cdot y = x)$; [[this example|3ZQC9WVWRE]] checks it.
- The set of primes; [[this example|BY43KQMK15]] gives the $\Delta_0$ formula.
- The divisibility relation $x \mid y$, defined by $\exists z < y + 1 \, (x \cdot z = y)$.
- The set of powers of $2$, defined by "$x \ge 1$ and every divisor $u > 1$ of $x$ is even". The divisor and the half are below $x + 1$.
- The graph $\set{(x, y) : y = 2^x}$. Bennett showed that it is $\Delta_0$-definable, although the function $x \mapsto 2^x$ is not provably total in $\mathsf{I}\Delta_0$.

### Non-examples

- The halting set is not $\Delta_0$-definable, since every $\Delta_0$-definable set is [[computable|PPGD5KW8JC]]; [[this non-example|P2TG6SR5EN]] gives the details.
- Myhill showed that every $\Delta_0$-definable set can be decided in linear space. The [[space hierarchy theorem|R06DB3S2PV]] gives a computable set that needs more than linear space, and that set is not $\Delta_0$-definable.
- The set of $\Sigma_1$ sentences true in $\N$ is not $\Delta_0$-definable, for the same reason as the halting set: it is not computable.

### Basic properties

- The $\Delta_0$-definable sets are closed under Boolean operations and under bounded quantification $\exists y < t$ and $\forall y < t$.
- $\Delta_0 = \mathrm{Rud} = \mathrm{LinH}$, with numbers written in binary.
- $\mathrm{LinH}$ is contained in the [[polynomial hierarchy|TDQ7AXGM6P]], since linear time is polynomial time, and in linear space, by Myhill's theorem.
- Whether every set decidable in linear space is $\Delta_0$-definable is open.
- $\mathsf{I}\Delta_0$ does not prove that $x \mapsto 2^x$ is total, by [[Parikh's theorem|YPQPC1WJMV]]. Gaifman and Dimitracopoulos showed that $\mathsf{I}\Delta_0$ proves the recursion laws of a $\Delta_0$ definition of its graph.
- Paris, Wilkie and Woods showed that $\mathsf{I}\Delta_0 + \Omega_1$ proves that there are infinitely many primes.
- Whether $\mathsf{I}\Delta_0$ proves the pigeonhole principle for $\Delta_0$ relations is open. For a new relation symbol $R$, $\mathsf{I}\Delta_0(R)$ does not prove it, by Ajtai's theorem. Both questions belong to the [[pigeonhole problem|NJ18EZ5JBC]].

### History

Smullyan introduced the rudimentary relations on strings in 1961.
Bennett proved in his 1962 thesis that they are exactly the $\Delta_0$-definable relations, and that the graph of exponentiation is $\Delta_0$-definable.
In 1978 Wrathall characterized the rudimentary relations by the linear-time hierarchy, and Lipton stated and proved the equality with the $\Delta_0$ sets explicitly.
Paris and Wilkie, and later Paris, Wilkie and Woods, studied counting and the pigeonhole principle in $\mathsf{I}\Delta_0$.

### Common errors

- To measure time in the value of $x$ instead of its length. A bounded quantifier over $y < x$ ranges over $x$ values, which is exponential in the length of $x$, but the alternating machine guesses $y$ in time linear in the length.
- To conclude from the $\Delta_0$-definability of the graph of $2^x$ that $\mathsf{I}\Delta_0$ proves $2^x$ total. The formula defines the graph, but $\mathsf{I}\Delta_0$ cannot prove that each $x$ has a value.

## Explanations

### L1 human

Some properties of numbers can be checked by a search that never goes beyond a fixed size.
For example, "$45$ is not a perfect square" is checked by trying all numbers from $0$ to $45$ and seeing that none of them squares to $45$.
Logicians call such properties bounded.
Computer scientists found the same properties from another side: they are the properties that a machine can check in time proportional to the number of digits of the input, when it may guess and check in a few rounds.
The theory $\mathsf{I}\Delta_0$ is the set of rules for proofs that may use induction only on such bounded properties.

### L2 human

We check that the relation $x \mid y$ is $\Delta_0$ and describe an alternating algorithm.

1. The formula $\exists z < y + 1 \, (x \cdot z = y)$ has one bounded quantifier, so it is $\Delta_0$.
2. It defines divisibility in $\N$: if $x \cdot z = y$ with $y \ge 1$, then $z \le y$; and if $y = 0$, then $z = 0$ works.
3. For $x = 6$ and $y = 42$, the witness is $z = 7$, and $7 < 43$.
4. The machine guesses the bits of $z$, at most the length of $y$ many.
5. Then it checks $x \cdot z = y$. This check is itself in $\mathrm{LinH}$, because the graph of multiplication is $\Delta_0$-definable: it is an atomic formula.

The typical use is to transfer a question: a statement about $\Delta_0$ sets, such as a counting principle, becomes a statement about linear-time computation.
A trap is in step 5: the graph of multiplication is in $\mathrm{LinH}$, but no deterministic linear-time algorithm for multiplication on Turing machines is known.

### L3 human

The correspondence is the bottom level of a family: $\Sigma^b_i$ formulas give the polynomial hierarchy, and $\Delta_0$ formulas give the linear-time hierarchy.
In the two-sorted setting of Cook and Nguyen, $\Sigma^B_0$ formulas define exactly the sets in uniform $\mathrm{AC}^0$, and the theory $V^0$ is conservative over $\mathsf{I}\Delta_0$.
Here a number of $\mathsf{I}\Delta_0$ corresponds to the length of a string, which is why $\mathrm{LinH}$ becomes $\mathrm{AC}^0$ after the change of input.

Many open problems of $\mathsf{I}\Delta_0$ are open problems in complexity in disguise.
A proof in $\mathsf{I}\Delta_0(R)$ of a $\Delta_0(R)$ statement gives short propositional proofs in a bounded-depth Frege system, by the [[Paris-Wilkie translation|ZVD982MVST]].
So lower bounds for bounded-depth Frege proofs give independence results for $\mathsf{I}\Delta_0(R)$, and the unrelativized questions remain open.
