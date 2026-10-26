---
tag: 0EHWPWGHB2
kind: statement
role: theorem
name: Binomial theorem
msc: [05A10]
uses: [092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_theorem
    locator: Statement
same_as:
  wikidata: Q26708
  wikipedia: Binomial theorem
---

## Statement

Let $R$ be a commutative ring, let $x, y \in R$, and let $n$ be a natural number.
Then
$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}.$$
Here $\binom{n}{k}$ is the [[binomial coefficient|092GEF38YD]], and the integer $\binom{n}{k}$ acts on $R$ by repeated addition.

## Remarks

For $n = 2$ it gives $(x + y)^2 = x^2 + 2xy + y^2$. For $n = 3$ it gives $x^3 + 3x^2 y + 3x y^2 + y^3$.
The formula stays true in a noncommutative ring when $xy = yx$.
With $x = y = 1$ it gives the [[sum of binomial coefficients|0KAMF19NV8]]. With $x = -1$ and $y = 1$ it gives the [[alternating sum|0PQQGFAWSH]].
The [[multinomial theorem|0XFC1VQYEK]] extends it to sums of more than two terms.

## Explanations

### L1 human

When you expand $(x + y)^n$, each term comes from choosing $x$ or $y$ in each of the $n$ factors.
The term $x^k y^{n-k}$ appears once for each choice of the $k$ factors that give $x$, so its coefficient is $\binom{n}{k}$.
