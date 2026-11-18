---
tag: S09CTN8JZ4
kind: example
name: Elementary function arithmetic is not a theory of bounded arithmetic
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
not_instance_of:
  - target: A2CFPP8JMN
    note: EFA has only bounded induction, but it proves that the function 2^x is total, and 2^x is not bounded by 2^{p(|x|)} for any polynomial p
uses: [A2CFPP8JMN, 2JD80TE553, SXYZP1DNJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: lead section
---

## Example

Let $\mathsf{EFA} = \mathsf{I}\Delta_0 + \forall x \, \exists y \, \mathrm{Exp}(x, y)$ be [[elementary function arithmetic|2JD80TE553]], where $\mathrm{Exp}(x, y)$ is a $\Delta_0$ formula that defines $y = 2^x$ in $\N$.
We show that it is not a theory of [[bounded arithmetic|A2CFPP8JMN]], although its induction is bounded.

1. Induction. The induction axioms of $\mathsf{EFA}$ are those of $\mathsf{I}\Delta_0$, so this condition holds.
2. Totality of $2^x$. The axiom $\forall x \, \exists y \, \mathrm{Exp}(x, y)$ is a theorem of $\mathsf{EFA}$, and $\mathrm{Exp}$ defines the function $x \mapsto 2^x$ in $\N$.
3. Growth. Let $p$ be a polynomial. Since $\abs{n} \le \log_2 n + 1$ for $n \ge 1$, there is an $n_0$ with $p(\abs{n}) < n$ for all $n \ge n_0$.
4. So $2^n > 2^{p(\abs{n})}$ for $n \ge n_0$. For example, with $p(m) = m^2$ and $n = 64$, $p(\abs{64}) = 49 < 64$.
5. By steps 2 to 4, $\mathsf{EFA}$ has a provably total function that is not bounded by $2^{p(\abs{x})}$ for any polynomial $p$. The growth condition fails.

## Remarks

The example shows that bounded induction alone does not make a theory weak: the growth rate of the provably total functions comes from the axioms that assert totality.
The provably total functions of $\mathsf{EFA}$ are the [[elementary recursive functions|RJ3MCAAZSV]], which include every tower $2^{2^{x}}$ of fixed height.
If the axiom for $2^x$ is replaced by the axiom $\Omega_1$ for $x^{\abs{x}}$, the theory becomes [[a theory of bounded arithmetic|V8WD1F0NS2]].

## Explanations

### L1 human

A theory of bounded arithmetic must not allow numbers that are too large compared with the input.
Elementary function arithmetic has an axiom that says that $2^x$ exists for every $x$.
For the input $64$, which has $7$ binary digits, the number $2^{64}$ has $65$ binary digits.
For larger inputs the gap grows without limit, far faster than any polynomial in the number of digits.
So this theory is too strong to count as bounded arithmetic.

### L2 human

We compare $2^n$ with the bound $2^{\abs{n}^3}$ for growing $n$.

1. For $n = 64$, $\abs{n} = 7$ and $\abs{n}^3 = 343 > 64$, so $2^{64}$ is still below the bound.
2. For $n = 2^{12} = 4096$, $\abs{n} = 13$ and $\abs{n}^3 = 2197 < 4096$, so $2^n$ exceeds the bound.
3. For every larger power of two $n = 2^k$, $\abs{n}^3 = (k + 1)^3 < 2^k$ once $k \ge 12$, so the gap grows.

The typical use of this non-example is as the upper end of weak arithmetic: $\mathsf{EFA}$ is the weakest standard theory in which exponentiation is total.
A trap is to call every theory with bounded induction a theory of bounded arithmetic.
