---
tag: Q0H5CJGCAY
kind: example
name: The type of an infinite natural number
msc: ["03C07", "03C62"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [9V71Q3SD1G]
not_instance_of:
  - target: A0VNTN725W
    note: "no single formula consistent with the theory of the natural numbers implies all formulas of the type"
  - target: ZGEXNRHC9M
    note: "the standard model omits this recursive type, so it is not recursively saturated"
uses: [9V71Q3SD1G, 1NR3HAWG9D, 655K8Y7VS8, X9HV9C6X4F, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $\mathcal{N} = (\N, 0, 1, +, \cdot, <)$ and let $T = \operatorname{Th}(\mathcal{N})$ be its [[theory|X9HV9C6X4F]].
For $k \in \N$ let $\underline{k}$ be the term $1 + \cdots + 1$ with $k$ terms, and $\underline{0} = 0$.
Let $p(x) = \set{\underline{k} < x : k \in \N}$.

1. A finite subset of $p$ is contained in $\set{\underline{k} < x : k \le m}$ for some $m$, and $m + 1$ satisfies it in $\mathcal{N}$.
2. So every finite subset of $p$ is realized in $\mathcal{N}$, and by the [[compactness theorem|1NR3HAWG9D]] $T \cup p$ is satisfiable.
3. So $p$ is a $1$-[[type|9V71Q3SD1G]] of $T$.
4. The model $\mathcal{N}$ omits $p$: the number $n$ fails the formula $\underline{n} < x$.
5. The type $p$ is not isolated. Let $\varphi(x)$ be consistent with $T$; since $T$ is [[complete|655K8Y7VS8]], $\mathcal{N} \models \exists x \, \varphi(x)$, say $\mathcal{N} \models \varphi(n)$.
6. Then $\varphi(x) \wedge \neg(\underline{n} < x)$ holds of $n$ in $\mathcal{N}$, so $\varphi$ does not imply the formula $\underline{n} < x$ of $p$.
7. The set $p$ is a [[computable set|PPGD5KW8JC]] of formulas, since $\underline{k} < x$ is computed from $k$.
8. So $\mathcal{N}$ omits a computable type without parameters, and $\mathcal{N}$ is not recursively saturated.

## Remarks

Every model of $T$ other than $\mathcal{N}$ realizes $p$.
Indeed $T$ contains, for each $k$, the sentence $\forall x \, (x \le \underline{k} \to x = \underline{0} \vee \dots \vee x = \underline{k})$, so an element outside the copy of $\N$ is above every $\underline{k}$.
The type $p$ is not complete: the formula "$x$ is even" and its negation are both consistent with $p$.
Its completions are the types of the nonstandard elements, and there are $2^{\aleph_0}$ of them, one or more for each set of primes that divide $x$.

## Explanations

### L1 human

The list "$x > 0$, $x > 1$, $x > 2$, and so on" describes an infinitely large natural number.
Each finite part of the list is met by an ordinary number, so the list is consistent.
No ordinary number meets the whole list, but every nonstandard model of arithmetic has such elements.

### L2 human

We show why no single formula forces an element to be infinite.

1. Suppose $\varphi(x)$ is a formula that some element of some model of $T$ satisfies.
2. Then $\exists x \, \varphi(x)$ is true in that model, so it is in the complete theory $T$ and true in $\mathcal{N}$.
3. A standard witness $n$ of $\varphi$ is not infinite.

The typical use of $p$ is to build nonstandard models by realizing it.
The trap is to think that "$x$ is larger than every number" is a formula: it is an infinite list of formulas.
