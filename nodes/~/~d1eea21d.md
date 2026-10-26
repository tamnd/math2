---
tag: ~d1eea21d
kind: statement
role: theorem
name: Taylor's theorem
msc: [41A58]
uses: [~ef52d2a0]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Statement of the theorem
same_as:
  wikidata: Q1137206
  wikipedia: Taylor's theorem
---

## Statement

Let $k \ge 1$, let $I$ be an open interval, let $a \in I$, and let $f \colon I \to \mathbb{R}$ be $k$ times differentiable at $a$.
Let $P_k$ be the [[Taylor polynomial|~ef52d2a0]] of degree $k$ of $f$ at $a$.
Then there is a function $h_k \colon I \to \mathbb{R}$ with $h_k(x) \to 0$ as $x \to a$ and
$$f(x) = P_k(x) + h_k(x) (x - a)^k \quad \text{for all } x \in I.$$

## Remarks

In [[little o notation|~5480c900]], the conclusion is the [[Peano form|~e9f65ac6]] $f(x) - P_k(x) = o((x - a)^k)$.
Under stronger hypotheses, the remainder has explicit forms: the [[Lagrange form|~98b72424]], the [[Cauchy form|~fecc3241]], and the [[integral form|~7870f42f]].
For $k = 1$, it says that $f(x) = f(a) + f'(a)(x - a) + o(x - a)$.

## Explanations

### L1 human

Near $a$, a function is close to its Taylor polynomial.
The error is small even compared with $(x - a)^k$.
