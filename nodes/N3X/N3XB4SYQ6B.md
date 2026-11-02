---
tag: N3XB4SYQ6B
kind: definition
name: Pochhammer symbol
msc: [05A10, 33C20, 33B15]
defines: YZHM3HSM0F
uses: [0XWG0JGDFW]
sources:
  - url: https://en.wikipedia.org/wiki/Falling_and_rising_factorials
---

## Definition

Let $a$ be an element of a commutative ring, for example a complex number, and let $n$ be a natural number.
The *Pochhammer symbol* (or *rising factorial*) of $a$ of order $n$ is
$$(a)_n = a (a + 1) (a + 2) \cdots (a + n - 1) = \prod_{i=0}^{n-1} (a + i).$$
For $n = 0$ the product is empty, and $(a)_0 = 1$.

## Remarks

Example: $(1)_n = 1 \cdot 2 \cdots n = n!$, the [[factorial|0XWG0JGDFW]]; and $(2)_3 = 2 \cdot 3 \cdot 4 = 24$.
For a negative integer $a = -m$ and $n > m$, one factor is $0$, so $(-m)_n = 0$; this is why hypergeometric series with such a parameter terminate.
Other notations are $a^{\overline{n}}$ and $a^{(n)}$.
The rising factorial of $a$ is $(-1)^n$ times the [[falling factorial|0SJNCJCCQG]] of $-a$: $(a)_n = (-1)^n (-a)(-a-1)\cdots(-a-n+1)$.
If $a \in \C$ is not in $\set{0, -1, -2, \ldots}$, then $(a)_n = \Gamma(a + n)/\Gamma(a)$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
In Mathlib the rising factorial as a polynomial in $a$ is `ascPochhammer`.

## Explanations

### L1 human

The Pochhammer symbol is a factorial that may start at any number and goes up in steps of $1$.
For example $(5)_3 = 5 \cdot 6 \cdot 7 = 210$.
