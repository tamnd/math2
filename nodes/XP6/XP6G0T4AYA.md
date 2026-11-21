---
tag: XP6G0T4AYA
kind: example
name: Real closed fields in the ring signature eliminate quantifiers relative to squares
aliases: [real-closed-fields-relative-to-squares, rcf-ring-signature-relative-elimination]
msc: ["03C10", "12D15"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [WMC3J66FAY]
uses: [FSJ9NGRRPA, DDY3Q3PJ6W, 0P3VCBDEE2, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
    locator: Model theory
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L_r = \set{+, -, \cdot, 0, 1}$ and $L = L_r \cup \set{<}$.
Let $T_r$ be the $L_r$-[[theory|92SWXST1ZM]] of [[real closed fields|DDY3Q3PJ6W]].
Let $\Delta$ consist of the atomic $L_r$-formulas and the formulas $\exists z \, (t = z \cdot z)$, for $L_r$-terms $t$.
We show that $T_r$ has elimination relative to $\Delta$.

1. A real closed field $R$ has exactly one [[ordering|0P3VCBDEE2]]: the nonnegative elements are the squares. So $R$ expands in one way to a model of $\mathrm{RCF}$ in $L$, and in it $s \le t$ holds if and only if $\exists z \, (t - s = z \cdot z)$ holds.
2. Let $\varphi(\bar x)$ be an $L_r$-formula. It is also an $L$-formula. By [[quantifier elimination for RCF|FSJ9NGRRPA]], $\varphi$ is equivalent modulo $\mathrm{RCF}$ to a quantifier-free $L$-formula $\psi(\bar x)$.
3. In $\psi$, replace each atomic formula $s < t$ by $\neg \exists z \, (s - t = z \cdot z)$. Call the result $\psi_0$. It is a Boolean combination of formulas in $\Delta$.
4. In each model of $T_r$, with its unique ordering, $s < t$ and $\neg \exists z \, (s - t = z \cdot z)$ define the same set, by step 1. So $\varphi$ and $\psi_0$ are equivalent in each model of $T_r$.

So every $L_r$-formula is equivalent modulo $T_r$ to a Boolean combination of formulas in $\Delta$.

## Remarks

The theory $T_r$ has no quantifier elimination in $L_r$.
A quantifier-free $L_r$-formula in one variable $x$ is a Boolean combination of polynomial equations $p(x) = 0$, so it defines a finite or cofinite set.
The formula $\exists z \, (x = z \cdot z)$ defines the nonnegative elements, which form an infinite set with infinite complement.

## Explanations

### L1 human

In the real numbers, "$x$ is at most $y$" can be said with multiplication alone: "$y - x$ is a square".
So once the order is known to be removable from the quantifiers, every statement about real numbers with $+$ and $\cdot$ becomes a combination of equations and of statements "this number is a square".

### L2 human

We see the elimination on the formula $\exists y \, (x = y^4 + 1)$, which says $x \ge 1$ in a real closed field.

1. In $L$, quantifier elimination gives the quantifier-free formula $1 < x \lor x = 1$.
2. Replacing $1 < x$ by $\neg \exists z \, (1 - x = z \cdot z)$ gives a formula in $\Delta$.

The typical use is to transfer results proved for ordered fields back to the ring signature.
A trap is to apply this to fields that are only formally real: such a field can have several orderings, and the squares need not be the nonnegative elements.
