---
tag: PSNXBQGWYB
kind: example
name: An identity on the Boolean cube that is not a certificate
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: ZERBQSTZB5
    note: the sum equals 1 at every 0-1 point but is not the polynomial 1, because the Boolean axioms are missing, so it is not a Nullstellensatz refutation
uses: [ZERBQSTZB5]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

Work over a field $\mathbb{F}$ of characteristic other than $2$, for example $\mathbb{Q}$.
Let $F$ be the CNF with the two clauses $x$ and $\neg x$, whose translations are $f_1 = 1 - x$ and $f_2 = x$.
Take $g_1 = 1 - x$ and $g_2 = x$, and no Boolean axioms.

1. The sum is $g_1 f_1 + g_2 f_2 = (1 - x)^2 + x^2 = 1 - 2x + 2x^2$.
2. At $x = 0$, the sum is $1$.
3. At $x = 1$, the sum is $1 - 2 + 2 = 1$.
4. The coefficient of $x^2$ is $2$, which is not $0$ in $\mathbb{F}$. So the sum is not the polynomial $1$.

So the sum equals $1$ at every $0$-$1$ point, but $g_1 f_1 + g_2 f_2 = 1$ is not a polynomial identity.
The list $g_1, g_2$ is not a [[Nullstellensatz refutation|ZERBQSTZB5]], because the definition asks for an identity in $\mathbb{F}[x]$.

## Remarks

The list fails only the identity condition, and one Boolean axiom repairs it.
With $h = -2$ for the Boolean axiom $x^2 - x$:
$$(1 - x)^2 + x^2 - 2 (x^2 - x) = 1 - 2x + 2x^2 - 2x^2 + 2x = 1.$$
This is a Nullstellensatz refutation of degree $2$.

The general fact is the same.
A polynomial that vanishes at every $0$-$1$ point is a combination of Boolean axioms, so an identity on the cube becomes a certificate once the Boolean axioms are added.
But the degree and the size of the certificate count these added terms.

Over $\mathbb{F}_2$, the polynomial $1 - 2x + 2x^2$ is already $1$, so in characteristic $2$ the list is a certificate without Boolean axioms.

## Explanations

### L1 human

A certificate must be correct as a formula, not only at the values $0$ and $1$.
The expression $1 - 2x + 2x^2$ gives $1$ at $x = 0$ and at $x = 1$, but at $x = 2$ it gives $5$.
So it is not the same polynomial as $1$, and the check by expansion fails.

### L2 human

To test a proposed certificate, expand the sum and compare it with $1$ coefficient by coefficient.

1. The expansion is $1 - 2x + 2x^2$.
2. The coefficients of $x$ and $x^2$ are not $0$, so the test fails.
3. The term $-2(x^2 - x)$ removes both of them.

A trap is to test a certificate only on $0$-$1$ points: such a test checks values, not coefficients, and this list passes it without being a certificate.
