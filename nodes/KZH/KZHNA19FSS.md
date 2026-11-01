---
tag: KZHNA19FSS
kind: statement
role: lemma
name: Borel's lemma
msc: ["26E10"]
uses: [0BE3QDH73A, 084NGSTWM7, 0225QPWRRE, 072W67KFYK, HS65DW0HXH, 0CS42KEM5C, 09RTYYHXKA]
about: [0BE3QDH73A, 0225QPWRRE]
sources:
  - url: https://en.wikipedia.org/wiki/Borel%27s_lemma
same_as:
  wikidata: Q3527022
  wikipedia: Borel's lemma
---

## Statement

Let $(a_n)_{n \ge 0}$ be any sequence of real numbers.
Then there is a [[smooth function|0BE3QDH73A]] $f \colon \R \to \R$ such that $f^{(n)}(0) = a_n$ for every $n \ge 0$.

## Remarks

Idea of the proof: choose a [[bump function|HS65DW0HXH]] $\chi$ equal to $1$ on $[-1/2, 1/2]$ and $0$ outside $[-1, 1]$.
Set $f(x) = \sum_{n \ge 0} \frac{a_n}{n!} x^n \chi(\lambda_n x)$ with numbers $\lambda_n \ge 1$ that grow fast.
The $n$-th term agrees with $\frac{a_n}{n!} x^n$ near $0$.
For $k < n$, its $k$-th derivative has supremum at most $2^{-n}$ when $\lambda_n$ is large enough.
Then every series of derivatives converges uniformly, so [[term-by-term differentiation|0CS42KEM5C]] gives $f^{(n)}(0) = a_n$.

The construction also gives $f$ with compact support.
Example: for $a_n = (n!)^2$, the [[Taylor series|0225QPWRRE]] of $f$ at $0$ is $\sum n! \, x^n$, which converges only at $x = 0$.

## Explanations

### L1 human

Any list of numbers can be the list of derivatives at $0$ of some smooth function.
There is no growth condition, unlike for analytic functions, whose derivatives at a point can grow at most like $C R^n n!$.
So every formal power series is the Taylor series of some smooth function.

### L2 human

The lemma says that the map sending a smooth function to its Taylor series at $0$, a [[formal power series|072W67KFYK]], is onto.
It is far from one-to-one: the [[smooth non-analytic function|09RTYYHXKA]] equal to $e^{-1/x}$ for $x > 0$ and to $0$ for $x \le 0$ has zero Taylor series at $0$.
Together these facts show how loosely the Taylor series controls a smooth function.
The lemma has versions in several variables and with parameters, and it is used in the study of singularities and of partial differential equations.
