---
tag: 367Y9XDMXG
kind: example
name: The real field without order has no quantifier elimination
aliases: [real-field-ring-language-no-quantifier-elimination]
msc: ["03C10", "12D15"]
topics: [1A9JSC5YG8]
audience: grad
not_instance_of:
  - target: 7FDDXV3JK7
    note: in the ring signature the formula saying that x is a square defines the nonnegative reals, which is neither finite nor cofinite, while quantifier-free formulas in one variable define finite or cofinite sets
uses: [RE5TFTDP4D, MCZRXR3SVB, CY1TXHF6KQ, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Real_closed_field
    locator: Decidability and quantifier elimination
  - book: isbn:9780387987606
---

## Example

Let $L_{\mathrm{ring}} = \set{+, -, \cdot, 0, 1}$ and let $T = \operatorname{Th}(\R, +, -, \cdot, 0, 1)$, the [[theory|92SWXST1ZM]] of the real field without the order.
We show that $T$ does not have [[quantifier elimination|RE5TFTDP4D]].
Let $\varphi(x)$ be the formula $\exists y \, (x = y \cdot y)$.

1. In $\R$, a number is a square exactly when it is nonnegative. So $\varphi$ defines the [[set|CY1TXHF6KQ]] $[0, \infty)$.
2. An [[atomic formula|MCZRXR3SVB]] in the variable $x$ has the form $t_1(x) = t_2(x)$ for terms $t_1, t_2$. Every term in $x$ is a polynomial in $x$ with integer coefficients.
3. So an atomic formula in $x$ is equivalent in $\R$ to $p(x) = 0$ for a polynomial $p \in \Z[x]$.
4. If $p \ne 0$, then $p$ has at most $\deg p$ real roots, so $p(x) = 0$ defines a finite set. If $p = 0$, it defines $\R$.
5. The finite and cofinite subsets of $\R$ are closed under complement, finite union and finite intersection. So every quantifier-free formula in $x$ defines a finite or cofinite set.
6. The set $[0, \infty)$ is infinite, and its complement $(-\infty, 0)$ is infinite.
7. So $\varphi(x)$ is not equivalent in $\R$ to a quantifier-free formula, and $T$ does not have quantifier elimination.

## Remarks

The example shows that quantifier elimination depends on the signature.
The theory is the same, but a definable relation, the order, is missing from the atomic formulas.
In the ordered signature $\set{+, -, \cdot, 0, 1, <}$, the theory of $\R$ has quantifier elimination by [[Tarski's theorem|FSJ9NGRRPA]].

When a parameter changes, the result changes in this way.

- Step 5 also holds for quantifier-free formulas with real parameters, since a nonzero polynomial with real coefficients has finitely many roots. So $[0, \infty)$ is not even quantifier-free definable with parameters.
- Over $\C$ the same argument fails: in $\C$ every element is a square, so $\varphi$ is equivalent to $x = x$. The theory of algebraically closed fields has quantifier elimination in $L_{\mathrm{ring}}$.
- The theory $T$ is still [[model complete|YR6HCMABTE]], since the order is defined by an existential formula and by a universal formula.

## Explanations

### L1 human

On the number line, the numbers that are squares are $0$ and the positive numbers.
To say "$x$ is a square" with only plus, minus and times, one must say "there is a $y$ with $y \cdot y = x$".
An equation without "there is", like $x^2 - 2 = 0$, holds only at a few points, here two points.
Half of the number line is not a few points, so the words "there is" cannot be removed.

### L2 human

We test a candidate.
The formula $x \cdot x = x$ has no quantifier.

1. It holds when $x^2 - x = 0$, so at $x = 0$ and $x = 1$ only.
2. Its negation holds everywhere except at $0$ and $1$, including at $-5$, which is not a square.
3. Neither set equals $[0, \infty)$.

The typical use of the example is to explain why the order symbol is part of the signature in Tarski's theorem.
A trap is to think that "no quantifier elimination" means "undecidable": $T$ is decidable, since each $L_{\mathrm{ring}}$-sentence is also a sentence of the ordered signature, and there Tarski's method decides it.
