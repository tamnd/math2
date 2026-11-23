---
tag: XQENB067R3
kind: concept
name: RCA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [DC60FYCSPM, Y92NXGEQBD, PA4PYQ1PZ0, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Base system RCA0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Recursive comprehension
---

## Summary

Take a continuous function $f$ on $[0, 1]$ with $f(0) < 0 < f(1)$, and look for a zero by bisection: test the sign at the midpoint, keep the half where the sign changes, and repeat.
Each step is a computation from the code of $f$, and the system $\mathsf{RCA}_0$ is the theory of exactly such computable constructions.
It proves the [[intermediate value theorem|66WH4PQ392]] this way, and it is the base theory over which [[reverse mathematics|7SQS69T17R]] measures all other theorems.

$\mathsf{RCA}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] with the basic axioms, induction for $\Sigma^0_1$ formulas, and comprehension for $\Delta^0_1$ formulas, as in its [[definition|DNXCKXZZ08]].
The $\Delta^0_1$ comprehension scheme says that a set exists when it has both a $\Sigma^0_1$ and a $\Pi^0_1$ definition.
In an $\omega$-model this means that the sets are closed under [[Turing reducibility|PA4PYQ1PZ0]] and join, and the least $\omega$-model consists of the [[computable sets|PPGD5KW8JC]].

## Motivation

A base theory must be strong enough to code reals, functions and countable structures, and to prove their simple properties.
It must also be weak enough that the theorems under study are not already provable.
$\Delta^0_1$ comprehension gives exactly the sets that are computable from given sets, so it can build everything that an algorithm can build.
$\Sigma^0_1$ induction is what makes definitions by primitive recursion work, so the sequence of intervals in a bisection, or the partial sums of a series, exist as sets.

The result is a picture of computable mathematics inside a classical theory.
A theorem that fails for computable objects, such as weak König's lemma, cannot be a theorem of $\mathsf{RCA}_0$.
The next system, [[WKL0|7W9EG02T79]], adds exactly that lemma.

## Notation

The name abbreviates "recursive comprehension axiom", and the subscript $0$ marks the restriction of induction to $\Sigma^0_1$ formulas.
Some texts write $\mathsf{RCA}$ for the system with the full induction scheme.
The statement "$\mathsf{RCA}_0 \vdash \tau \leftrightarrow \sigma$" is the usual form of a result of reverse mathematics.

## Remarks

### Models made of computable sets

The [[computable sets form the least ω-model|F5T3F7E0H1]] of $\mathsf{RCA}_0$.
A larger example is the family of the [[sets computable from the halting set|7KCGVY6XJM]], which is a model of $\mathsf{RCA}_0$ but not of $\mathsf{ACA}_0$.
In general, the [[ω-models of RCA0 are the Turing ideals|Y6D27XJT3H]]: the nonempty families closed under join and under Turing reducibility.

A family can fail to be a model.
The [[computable sets together with the halting set|ZMVX86T0XK]] do not form a model, since the complement of the halting set, which is computable from it, is missing.
In the other direction, the computable sets are a model of $\mathsf{RCA}_0$ but [[not of full second-order arithmetic|W4J2H41PB7]].

### What RCA0 proves

$\mathsf{RCA}_0$ proves that every function defined by primitive recursion from given functions exists.
It proves the [[infinite pigeonhole principle for two colors|9EB4DXQMWK]], and it proves that $\sqrt{2}$ and every other computable real have [[codes|QY29R8PF9Z]].
In analysis it proves the intermediate value theorem and the Baire category theorem for complete separable metric spaces.
In algebra it proves that every countable field has an algebraic closure.
It does not prove weak König's lemma, because there is a computable infinite binary tree with no computable path, and so the lemma fails in the model of the computable sets.

### What RCA0 knows about numbers

The first-order part of $\mathsf{RCA}_0$ is $\mathrm{I}\Sigma_1$: the arithmetical sentences that $\mathsf{RCA}_0$ proves are exactly those that $\mathrm{I}\Sigma_1$ proves.
So its provably total functions are the primitive recursive functions, and its proof-theoretic ordinal is $\omega^\omega$.
In models with non-standard numbers, $\Sigma^0_2$ induction can fail, and much current work asks which combinatorial principles imply $\Sigma^0_2$ induction or the weaker bounding scheme $\mathrm{B}\Sigma^0_2$ over $\mathsf{RCA}_0$.

### Continuous functions

A continuous function $f \colon \mathbb{R} \to \mathbb{R}$ is coded by a set $\Phi$ of quintuples $(n, a, r, b, s)$ with $a, b$ rational and $r, s$ positive rational.
Write $(a, r) \Phi (b, s)$ for $\exists n \, (n, a, r, b, s) \in \Phi$.
It says that $f$ maps the open interval with center $a$ and radius $r$ into the closed interval with center $b$ and radius $s$.
The code must satisfy three conditions.

1. If $(a, r) \Phi (b, s)$ and $(a, r) \Phi (b', s')$, then $\lvert b - b' \rvert \le s + s'$.
2. If $(a, r) \Phi (b, s)$ and $\lvert a' - a \rvert + r' < r$, then $(a', r') \Phi (b, s)$.
3. If $(a, r) \Phi (b, s)$ and $\lvert b - b' \rvert + s < s'$, then $(a, r) \Phi (b', s')$.

A real $x$ is in the domain of $f$ when for each $\varepsilon > 0$ there is $(a, r) \Phi (b, s)$ with $\lvert x - a \rvert < r$ and $s < \varepsilon$.
Then $f(x)$ is the unique real $y$ with $\lvert y - b \rvert \le s$ for all $(a, r) \Phi (b, s)$ with $\lvert x - a \rvert < r$.
Every coded function is continuous, and the [[Heaviside function|5W961M41F5]] has no code.

### Watch out

$\mathsf{RCA}_0$ does not prove $\Sigma^0_1$ comprehension.
For a function $f$, the range $\{ n : \exists k \, f(k) = n \}$ need not exist: in the computable sets, a computable one-to-one function can have the halting set as its range.
Next, the subscript $0$ does not mean "without induction", since $\Sigma^0_1$ induction is an axiom.
Last, a proof in $\mathsf{RCA}_0$ may use classical logic, so a proof can split into cases that no computer can decide, as the proof of the intermediate value theorem does.

### History

Harvey Friedman introduced the system in the 1970s, as part of the program that he began in 1974.
With $\Sigma^0_1$ induction it became the standard base theory of reverse mathematics, and Simpson's book of 1999 uses it in this form.

### Try it

First, does $\mathsf{RCA}_0$ prove that the set of prime numbers exists?
Yes: "$n$ is prime" is defined by a formula with bounded quantifiers only, so $\Delta^0_1$ comprehension gives the set.

Second, let $f$ be strictly increasing.
Does $\mathsf{RCA}_0$ prove that the range of $f$ exists?
Yes: $f(k) \ge k$ for all $k$, so $n$ is in the range exactly when $f(k) = n$ for some $k \le n$, and this condition is bounded.

## Explanations

### L1 human

$\mathsf{RCA}_0$ is the theory of computable mathematics.
It allows a set to exist when a computer, given the sets that exist already, can decide which numbers belong to it.
It allows induction for statements of the form "some number has a property that we can check".
For example, the even numbers form a set, since a computer decides evenness.

### L2 human

Here is a typical construction in $\mathsf{RCA}_0$: the sum of the series $\sum_{k} 2^{-k} / (k + 1)$.
The partial sums $s_n$ are rationals, computed from $n$ by a primitive recursion, so the sequence $(s_n)$ exists.
The tail after $n$ is at most the sum below.
$$\sum_{k > n} \frac{2^{-k}}{k + 1} \le \sum_{k > n} 2^{-k} = 2^{-n}$$
So $(s_n)$ is a code of a real, and $\mathsf{RCA}_0$ proves that the sum exists.
This is the typical use: an object with a computable approximation and a computable error bound exists in $\mathsf{RCA}_0$.
The trap is a series with no computable error bound, such as $\sum_{n \in K} 2^{-n}$ for the halting set $K$, whose sum $\mathsf{RCA}_0$ cannot form.

### L3 human

$\mathsf{RCA}_0$ is $\Pi^0_2$-conservative over primitive recursive arithmetic, and it is $\Pi^1_1$-conservative over $\mathrm{I}\Sigma_1$.
The weaker system $\mathsf{RCA}^*_0$ replaces $\Sigma^0_1$ induction by $\Sigma^0_0$ induction and adds the totality of exponentiation, and it is used to study theorems that need even less induction.
Constructive reverse mathematics replaces classical logic in the base instead, and it then separates theorems that $\mathsf{RCA}_0$ proves by case splits.
Above $\mathsf{RCA}_0$ the scale continues with [[WKL0|7W9EG02T79]], [[ACA0|NAASTN80QN]], [[ATR0|MKB74TX3Z8]] and [[Π¹₁-CA0|T21WETAHN5]].
