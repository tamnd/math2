---
tag: BYNV84PF86
kind: statement
role: theorem
name: Dominated convergence theorem
msc: [28A25, 26A42]
uses: [DWJF7ABPR1, X7GTF3D98F, RARTMA0ZEC, S95TR54TCG]
about: [DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Dominated_convergence_theorem
same_as:
  wikidata: Q1067156
  wikipedia: Dominated convergence theorem
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space.
Let $f_1, f_2, \dots$ and $f$ be real or complex measurable functions on $X$ with $f_n \to f$ [[almost everywhere|RARTMA0ZEC]].
Suppose there is an [[integrable function|X7GTF3D98F]] $g \colon X \to [0, \infty]$ with $\abs{f_n} \le g$ almost everywhere for every $n$.
Then $f$ and each $f_n$ are integrable, and
$$\lim_{n \to \infty} \int_X \abs{f_n - f} \, d\mu = 0, \qquad \lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu,$$
where the integrals are [[Lebesgue integrals|DWJF7ABPR1]].

## Remarks

Proof idea: $\abs{f} \le g$ almost everywhere, so $f$ is integrable.
The functions $2g - \abs{f_n - f}$ are non-negative almost everywhere and tend to $2g$.
[[Fatou's lemma|S95TR54TCG]] gives $\int 2g \le \int 2g - \limsup_n \int \abs{f_n - f}$, so $\limsup_n \int \abs{f_n - f} = 0$.
The second limit follows from $\abs{\int f_n - \int f} \le \int \abs{f_n - f}$.

Example: $\int_0^1 x^n \, dx \to 0$, since $x^n \to 0$ for $x \in [0, 1)$ and $\abs{x^n} \le 1$, which is integrable on $[0, 1]$.

The dominating function is needed.
For $f_n = n \mathbf{1}_{(0, 1/n)}$ on $\R$, $f_n \to 0$ everywhere but $\int f_n = 1$.
Here $\sup_n f_n$ behaves like $1/x$ near $0$ and is not integrable.

## Explanations

### L1 human

Suppose a sequence of functions converges at almost every point, and all of them stay below one fixed function of finite integral.
Then their integrals converge to the integral of the limit.
The fixed bound stops mass from escaping to infinity or piling up in a spike.

### L2 human

This is the most used convergence theorem of analysis.
It justifies differentiating under the integral sign, exchanging sums and integrals, and passing to the limit in many approximation arguments.
For finite measure spaces, a constant bound is enough, which gives the bounded convergence theorem.
The Vitali convergence theorem replaces domination by the weaker uniform integrability and gives a necessary and sufficient condition.
