---
tag: RDFA0SYHEQ
kind: definition
name: Self-avoiding walk
msc: [82B41, 60K35, 05A16]
defines: E2BVEB570S
uses: [04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Self-avoiding_walk
---

## Definition

Let $d \ge 1$ and $n \ge 0$ be integers, and let $\abs{\cdot}$ be the Euclidean norm on $\R^d$.
An $n$-step *self-avoiding walk* on $\Z^d$ starting at $0$ is a sequence $\omega = (\omega_0, \omega_1, \ldots, \omega_n)$ of points of $\Z^d$ such that:

1. $\omega_0 = 0$;
2. $\abs{\omega_i - \omega_{i-1}} = 1$ for $1 \le i \le n$;
3. $\omega_i \ne \omega_j$ for $0 \le i < j \le n$.

Let $c_n$ be the number of $n$-step self-avoiding walks.
The uniform probability measure on these $c_n$ walks is also called the self-avoiding walk with $n$ steps.

## Remarks

Example: in $\Z^2$, the walk $(0,0), (1,0), (1,1), (0,1)$ satisfies all three clauses, and it is one of the $c_3 = 36$ walks with three steps.
Non-example: $(0,0), (1,0), (0,0)$ satisfies clauses 1 and 2 but not clause 3, since it returns to $0$.
Cutting an $(n + m)$-step walk after $n$ steps gives $c_{n+m} \le c_n c_m$, so by Fekete's lemma the connective constant $\mu_d = \lim_{n \to \infty} c_n^{1/n}$ exists.
Walks that only move in positive coordinate directions are self-avoiding, and walks that never reverse their last step include all self-avoiding walks, so $d \le \mu_d \le 2d - 1$.
