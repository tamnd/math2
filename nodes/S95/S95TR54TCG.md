---
tag: S95TR54TCG
kind: statement
role: lemma
name: Fatou's lemma
msc: [28A25]
uses: [DG76G5Z6XW, 0H4R3RESGV, G2S6H789RG]
about: [DG76G5Z6XW]
sources:
  - url: https://en.wikipedia.org/wiki/Fatou%27s_lemma
same_as:
  wikidata: Q1068118
  wikipedia: Fatou's lemma
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space.
Let $f_1, f_2, \dots \colon X \to [0, \infty]$ be measurable functions.
Then $\liminf_{n} f_n$ is measurable, and
$$\int_X \liminf_{n \to \infty} f_n \, d\mu \le \liminf_{n \to \infty} \int_X f_n \, d\mu,$$
where $\liminf$ is the [[limit inferior|0H4R3RESGV]] and the integrals are [[integrals of non-negative functions|DG76G5Z6XW]].

## Remarks

Proof idea: let $g_k = \inf_{n \ge k} f_n$.
The functions $g_k$ increase to $\liminf_n f_n$, and $\int g_k \le \int f_n$ for every $n \ge k$.
The [[monotone convergence theorem|G2S6H789RG]] gives $\int \liminf_n f_n = \lim_k \int g_k \le \liminf_n \int f_n$.

The inequality can be strict.
For $f_n = n \mathbf{1}_{(0, 1/n)}$ on $\R$ with Lebesgue measure, $f_n \to 0$ pointwise but $\int f_n = 1$ for all $n$.

Non-negativity is needed.
For $f_n = -\mathbf{1}_{[n, n+1]}$ on $\R$, the left side is $0$ and the right side is $-1$.

## Explanations

### L1 human

When a sequence of non-negative functions converges, mass can escape, but it cannot appear from nowhere.
So the integral of the limit is at most the limit of the integrals.
A tall thin spike that keeps its area while it shrinks is the typical way mass escapes.

### L2 human

Fatou's lemma is the step between the monotone convergence theorem and the dominated convergence theorem.
It is often used to show that a limit function is integrable: if $\int f_n \le C$ for all $n$, then $\int \liminf f_n \le C$.
It also shows that the $L^p$ norm is lower semicontinuous under pointwise convergence almost everywhere.
