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

The sets that bounded formulas of arithmetic can define are exactly the sets that a guessing machine can decide in linear time, with a fixed number of rounds of guesses.
Take "$x$ is composite", written as a formula with bounded quantifiers:
$$\exists u < x \, \exists v < x \, (u \cdot v = x).$$
A machine decides it on the binary input $x$ by guessing the bits of $u$ and $v$, at most $2 \lvert x \rvert$ bits, and then checking one product.

In exact terms, a set $X \subseteq \mathbb{N}^k$ is $\Delta_0$-definable when some [[$\Delta_0$ formula|GE43CSZTS9]] $\theta(\bar x)$ of the [[language of arithmetic|D8SD54M5PN]] defines it, so that $\bar n \in X$ if and only if $\mathbb{N} \models \theta(\bar n)$.
These sets are exactly Smullyan's rudimentary relations, and exactly the sets in the linear-time hierarchy $\mathrm{LinH}$, when numbers are written in binary.
Here $\mathrm{LinH}$ is the class of sets decided in time $O(n)$ by alternating Turing machines with a bounded number of alternations, where $n$ is the length of the input.
The theory $\mathsf{I}\Delta_0$ has induction for exactly these sets, so $\mathsf{I}\Delta_0$ is to $\mathrm{LinH}$ what $S^1_2$ is to polynomial time.

## Motivation

Why should bounded formulas and linear time match?
A bounded quantifier $\exists y < t(x)$ ranges over numbers below a polynomial in $x$, and such a number has binary length at most a constant times $\lvert x \rvert$.
So a $\Delta_0$ formula describes a guess of linearly many bits, then a check, with a fixed number of alternations between "some" and "all".
This is an alternating computation in linear time, and the converse translation also works.

The match turns questions about the [[fragment|T70PYM1F36]] $\mathsf{I}\Delta_0$ into questions about a natural complexity class.
It explains what $\mathsf{I}\Delta_0$ can define and prove, and it explains why some questions about it, such as the pigeonhole principle, are as hard as open problems of complexity theory.
The same pattern returns one level up, where Buss's $\Sigma^b_i$ formulas match the [[polynomial hierarchy|TDQ7AXGM6P]], on the [[main page on bounded arithmetic|A2CFPP8JMN]].

## Notation

Books write $\Delta_0$ also as $\Sigma_0$, $\Pi_0$ or $\Sigma^0_0$, and the class of rudimentary relations as $\mathrm{Rud}$.
The linear-time hierarchy is $\mathrm{LinH}$ or $\mathrm{LTH}$, and its level $\Sigma^{\mathrm{lin}}_k$ holds the sets decided in linear time by alternating machines that start in an existential state and alternate at most $k - 1$ times.
So $\Sigma^{\mathrm{lin}}_1$ is $\mathrm{NLIN}$, nondeterministic linear time.
The theory $\mathsf{I}\Delta_0(R)$ is $\mathsf{I}\Delta_0$ in a language with a new relation symbol $R$, with induction for the $\Delta_0$ formulas that may contain $R$.
Watch out: the "linear" refers to the length of the input in binary, not to its value.

## Remarks

### A formula and a machine

Take the composite numbers again, with $x = 91$.
In binary $91 = 1011011_2$, so $\lvert 91 \rvert = 7$.
The machine guesses $u = 7$ and $v = 13$, each with at most $7$ bits, and then checks the product:
$$7 \cdot 13 = 91.$$
Check: both guesses are below $91$, so the bounded formula holds, and $91$ is composite.

Each bounded $\exists$ becomes an existential guess and each bounded $\forall$ becomes a universal guess.
Each guess has linearly many bits, because the bound is a term in $x$, and terms of the language $\{0, S, +, \cdot\}$ are polynomials.
The atomic check at the end compares two polynomials in the guessed numbers, and it fits in the linear-time hierarchy as well.
So the number of alternations of the formula becomes the number of alternations of the machine.

### Sets you can define

The [[perfect squares|3ZQC9WVWRE]] and the [[primes|BY43KQMK15]] have short $\Delta_0$ definitions, which the example pages check.
Divisibility $x \mid y$ is defined by $\exists z < y + 1 \, (x \cdot z = y)$.
The powers of $2$ are the numbers $x \ge 1$ whose divisors $u > 1$ are all even, and each divisor lies below $x + 1$.

A deeper example is the graph $\{ (x, y) : y = 2^x \}$.
Bennett showed that it is $\Delta_0$-definable, although the function $x \mapsto 2^x$ is not provably total in $\mathsf{I}\Delta_0$.
The formula has to encode the computation of $2^x$ inside numbers no larger than $y$, which is the hard part.

### Sets you cannot define

[[The halting set is not $\Delta_0$-definable|P2TG6SR5EN]], because every $\Delta_0$-definable set is [[computable|PPGD5KW8JC]]: bounded quantifiers give finite searches.
Computability is not enough, though.
Alternating linear time fits in deterministic linear space, so every $\Delta_0$-definable set is decidable in linear space.
The [[space hierarchy theorem|R06DB3S2PV]] gives a computable set that needs more than linear space, and that set is not $\Delta_0$-definable.
The set of codes of true $\Sigma_1$ sentences is not $\Delta_0$-definable either, since it is not computable.

### The rules you can use

The $\Delta_0$-definable sets are closed under Boolean operations and under bounded quantification, directly from the definition of a $\Delta_0$ formula.
The main fact is $\Delta_0 = \mathrm{Rud} = \mathrm{LinH}$, with numbers in binary.
Since linear time is polynomial time, $\mathrm{LinH}$ is contained in the polynomial hierarchy, and it is also contained in linear space.
Whether every set decidable in linear space lies in $\mathrm{LinH}$ is an open problem.

### What IΔ0 cannot prove

The theory $\mathsf{I}\Delta_0$ can define the graph of $2^x$, but it cannot prove that $2^x$ exists for every $x$, by [[Parikh's theorem|YPQPC1WJMV]].
The reason is size: a proof in $\mathsf{I}\Delta_0$ of $\forall x \, \exists y \, \theta$ gives a polynomial bound on $y$, and $2^x$ has no polynomial bound.
The $\Delta_0$ formula for the graph can be chosen so that $\mathsf{I}\Delta_0$ proves the recursion laws $2^0 = 1$ and $2^{x+1} = 2 \cdot 2^x$, whenever the values exist.

Counting is the other weak point.
Paris, Wilkie and Woods showed that $\mathsf{I}\Delta_0 + \Omega_1$ proves that there are infinitely many primes, and whether $\mathsf{I}\Delta_0$ alone proves it is open.
For a new relation symbol $R$, the theory $\mathsf{I}\Delta_0(R)$ does not prove the pigeonhole principle for $R$, by Ajtai's theorem.
Whether $\mathsf{I}\Delta_0$ proves the pigeonhole principle for $\Delta_0$ relations is open, and the [[pigeonhole problem|NJ18EZ5JBC]] tells that story.

### Watch out

Do not measure time in the value of $x$.
The bounded quantifier $\exists y < x$ ranges over $x$ values, exponentially many in $\lvert x \rvert$, so trying them one by one is slow.
The alternating machine does not try them: it guesses one $y$, and the guess has only $\lvert x \rvert$ bits.

Do not conclude from the $\Delta_0$ graph of $2^x$ that $\mathsf{I}\Delta_0$ proves $2^x$ total.
Defining a graph says what a value would be, and totality says that every input has one.
Every polynomial bound is passed by $2^x$ for large $x$: for example $2^x > x^3$ for all $x \ge 10$, since $2^{10} = 1024 > 1000$ and the left side doubles while the right side grows by a factor of at most $1.331$.

### History

Smullyan introduced the rudimentary relations on strings in 1961.
Bennett proved in his 1962 thesis that they are exactly the $\Delta_0$-definable relations, and that the graph of exponentiation is $\Delta_0$-definable.
Wrathall showed in 1978 that the rudimentary sets, and so the $\Delta_0$ sets, form the linear-time hierarchy.
Paris and Wilkie, and then Paris, Wilkie and Woods in 1988, studied counting and the pigeonhole principle in $\mathsf{I}\Delta_0$.

### Try it

First, write a $\Delta_0$ formula for "$x$ is even".
One answer is $\exists y < x + 1 \, (y + y = x)$, with a single bounded quantifier.

Second, how many bits does the machine guess for the formula $\exists u < x \, \exists v < x \, (u \cdot v = x)$ when $x = 1000$?
Since $\lvert 1000 \rvert = 10$, it guesses at most $10$ bits for each of $u$ and $v$, so $20$ bits.

## Explanations

### L1 human

Some properties of numbers can be checked by a search that never goes beyond a fixed size.
For example, "$45$ is not a perfect square" is checked by trying all numbers from $0$ to $45$ and seeing that none of them squares to $45$.
Logicians call such properties bounded.
Computer scientists found the same properties from another side: a machine can check them in time proportional to the number of digits of the input, if it may guess and check in a few rounds.
The theory $\mathsf{I}\Delta_0$ is a set of rules for proofs that may use induction only on such bounded properties.

### L2 human

Here is a typical problem: show that divisibility is $\Delta_0$, and describe the machine.
The formula is $\exists z < y + 1 \, (x \cdot z = y)$, with one bounded quantifier, so it is $\Delta_0$.
It defines divisibility, because a witness $z$ of $x \mid y$ can always be chosen at most $y$: if $y \ge 1$ then $z \le x \cdot z = y$, and if $y = 0$ then $z = 0$ works.
For $x = 6$ and $y = 42$ the witness is $z = 7$:
$$6 \cdot 7 = 42.$$
The machine guesses the bits of $z$, at most $\lvert 42 \rvert = 6$ of them, and then checks the product.
The problem shows the typical use: a statement about $\Delta_0$ sets, such as a counting principle, becomes a statement about linear-time computation, and back.

### L3 human

The correspondence is the bottom level of a family: $\Delta_0$ formulas give the linear-time hierarchy, and Buss's $\Sigma^b_i$ formulas give the levels of the polynomial hierarchy.
In the two-sorted setting of Cook and Nguyen, the $\Sigma^B_0$ formulas over strings define exactly the sets in uniform $\mathrm{AC}^0$, and the theory $V^0$ is conservative over $\mathsf{I}\Delta_0$.

Many open problems about $\mathsf{I}\Delta_0$ are open problems of complexity theory in disguise.
A proof in $\mathsf{I}\Delta_0(R)$ of a $\Delta_0(R)$ statement gives short proofs of propositional translations in a bounded-depth Frege system, by the [[Paris-Wilkie translation|ZVD982MVST]].
So lower bounds for bounded-depth Frege proofs give independence results for $\mathsf{I}\Delta_0(R)$, while the questions without $R$ remain open.
