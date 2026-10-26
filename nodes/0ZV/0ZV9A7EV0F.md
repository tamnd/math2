---
tag: 0ZV9A7EV0F
kind: definition
name: Complex power
msc: [33B10]
defines: 0RNGDMHT7M
uses: [054VXHMCA3, 0X2FY491PF, 0YKY4M3KRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Exponentiation
    locator: Complex exponentiation
  - url: https://en.wikipedia.org/wiki/Exponentiation
    locator: Principal value
---

## Definition

Let $z, w \in \mathbb{C}$ with $z \neq 0$.
The complex powers of $z$ with exponent $w$ are the numbers $e^{w \ell}$, where $\ell$ runs through the [[complex logarithms|0X2FY491PF]] of $z$.
The principal value of $z^w$ is
$$z^w = e^{w \operatorname{Log} z},$$
where $\operatorname{Log}$ is the [[principal branch|0YKY4M3KRQ]] of the logarithm and $e^u$ is the [[complex exponential|054VXHMCA3]] of $u$.

## Remarks

The powers of $z$ with exponent $w$ are the numbers $e^{w \operatorname{Log} z} e^{2 \pi i k w}$ with $k \in \mathbb{Z}$. There is one value if $w$ is an integer, there are $q$ values if $w = p/q$ in lowest terms with $q \ge 2$, and there are infinitely many values otherwise.
For an integer $w = n$, $z^n$ is the usual product of $n$ factors $z$, or of $-n$ factors $1/z$.
For example, $i^i = e^{i \cdot i \pi/2} = e^{-\pi/2}$, a positive real number.
The usual rules can fail: with principal values, $(z^a)^b \neq z^{ab}$ for some $z, a, b$. A common convention for $z = 0$ is $0^0 = 1$ and $0^w = 0$ for $w \neq 0$.

## Explanations

### L1 human

For real numbers, $a^b = e^{b \ln a}$ when $a > 0$. The complex power uses the same formula with a complex logarithm.
Because the logarithm has many values, the power can have many values too, and the principal value picks one of them.
