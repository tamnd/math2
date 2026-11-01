---
tag: F8XD8CDB0H
kind: statement
role: theorem
name: Borel–Carathéodory theorem
msc: [30A10, 30D20]
uses: [0DG0Z72CQD, 0MB48XDBY3]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Borel%E2%80%93Carath%C3%A9odory_theorem
same_as:
  wikidata: Q3229335
  wikipedia: Borel–Carathéodory theorem
---

## Statement

Let $R > 0$ and let $f$ be [[holomorphic|0DG0Z72CQD]] on an open set containing the closed disc $\set{z : \abs{z} \le R}$.
Let $A(R) = \max_{\abs{z} = R} \operatorname{Re} f(z)$.
Then for each $r$ with $0 < r < R$,
$$\max_{\abs{z} = r} \abs{f(z)} \le \frac{2r}{R - r} A(R) + \frac{R + r}{R - r} \abs{f(0)}.$$

## Remarks

Proof idea: first let $f(0) = 0$ and $f$ not constant, so that $A(R) > 0$ by the mean value property of $\operatorname{Re} f$.
Then $g = f / (2A(R) - f)$ maps the disc of radius $R$ into the unit disc with $g(0) = 0$.
The [[Schwarz lemma|0MB48XDBY3]] gives $\abs{g(z)} \le \abs{z}/R$, and solving for $f$ gives $\abs{f(z)} \le \frac{2r A(R)}{R - r}$ on $\abs{z} = r$.
In general, apply this to $f - f(0)$, whose real part is at most $A(R) + \abs{f(0)}$ on $\abs{z} = R$.
Example: a real constant $f = c \le 0$ gives equality.
The left side is $\abs{c}$, and the right side is $\frac{2rc + (R + r)\abs{c}}{R - r} = \abs{c}$.

## Explanations

### L1 human

Usually one needs a bound on $\abs{f}$ to control $\abs{f}$.
This theorem says that an upper bound on the real part alone is enough, on a slightly smaller disc.
The price is a factor that blows up as the smaller radius approaches the larger one.

### L2 human

The theorem is a standard tool for entire functions and in analytic number theory.
A typical use is to bound $\log f$ when $f$ has no zeros in a disc.
There $\operatorname{Re} \log f = \log \abs{f}$ is easy to bound from above.
The theorem then bounds $\abs{\log f}$ and, through Cauchy's estimates, its derivatives.
This is a step in the proof of the [[Hadamard factorization theorem|KYSR7NHNFQ]] and in zero-free region arguments for the Riemann zeta function.
