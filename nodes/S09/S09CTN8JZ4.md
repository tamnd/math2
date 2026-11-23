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

Bounded induction alone does not make a theory weak.
[[Elementary function arithmetic|2JD80TE553]] has the same induction as $\mathsf{I}\Delta_0$, and one extra axiom: for every $x$ the number $2^x$ exists.
For the input $x = 64$, which has $7$ binary digits, that axiom promises a number with $65$ binary digits.

In exact terms, $\mathsf{EFA} = \mathsf{I}\Delta_0 + \forall x \, \exists y \, \mathrm{Exp}(x, y)$, where $\mathrm{Exp}(x, y)$ is a $\Delta_0$ formula that defines $y = 2^x$ in $\mathbb{N}$.
We check that it fails the growth condition of [[bounded arithmetic|A2CFPP8JMN]], although its induction is bounded.

1. The induction axioms of $\mathsf{EFA}$ are those of $\mathsf{I}\Delta_0$, so the induction condition holds.
2. The axiom $\forall x \, \exists y \, \mathrm{Exp}(x, y)$ is a theorem of $\mathsf{EFA}$, and $\mathrm{Exp}$ defines the function $x \mapsto 2^x$ in $\mathbb{N}$.
   So $x \mapsto 2^x$ is a provably total function of $\mathsf{EFA}$.
3. Let $p$ be a polynomial.
   Since $\lvert n \rvert \le \log_2 n + 1$ for $n \ge 1$, the value $p(\lvert n \rvert)$ grows like a polynomial in $\log n$, so there is an $n_0$ with $p(\lvert n \rvert) < n$ for all $n \ge n_0$.
4. For such $n$ we get $2^n > 2^{p(\lvert n \rvert)}$.
   For example, with $p(m) = m^2$ and $n = 64$, we have $p(\lvert 64 \rvert) = 7^2 = 49 < 64$.
5. By steps 2 to 4, $\mathsf{EFA}$ has a provably total function that is not bounded by $2^{p(\lvert x \rvert)}$ for any polynomial $p$, so the growth condition fails.

## Remarks

The example shows where the growth of a theory comes from: from the axioms that assert that functions are total, not from the shape of the induction.
The provably total functions of $\mathsf{EFA}$ are the [[elementary recursive functions|RJ3MCAAZSV]], which include every tower $2^{2^{\cdot^{\cdot^{x}}}}$ of fixed height.

Change one axiom and the theory moves back into bounded arithmetic.
If the axiom for $2^x$ is replaced by the axiom $\Omega_1$ for $x^{\lvert x \rvert}$, the result is [[the theory $\mathsf{I}\Delta_0 + \Omega_1$|V8WD1F0NS2]], whose functions grow only like $2^{p(\lvert x \rvert)}$.
Watch out: do not call every theory with bounded induction a theory of bounded arithmetic, since the growth condition is a separate condition.

## Explanations

### L1 human

A theory of bounded arithmetic must not promise numbers that are too large compared with the input.
Elementary function arithmetic has an axiom that says that $2^x$ exists for every $x$.
For the input $64$, which has $7$ binary digits, the number $2^{64}$ has $65$ binary digits.
For larger inputs the gap grows without limit, far faster than any polynomial in the number of digits.
So this theory is too strong to count as bounded arithmetic.

### L2 human

We compare $2^n$ with the bound $2^{\lvert n \rvert^3}$ for growing $n$, so we compare $n$ with $\lvert n \rvert^3$.
For $n = 64$ we have $\lvert n \rvert = 7$ and $7^3 = 343 > 64$, so $2^{64}$ is still below the bound.
For $n = 2^{11} = 2048$ we have $\lvert n \rvert = 12$ and $12^3 = 1728 < 2048$, so $2^n$ is above the bound.

From there on the gap only grows.
For $n = 2^k$ the comparison is between $(k + 1)^3$ and $2^k$.
When $k$ goes up by one, the right side doubles, and the left side grows by the factor below, which is less than $2$ for $k \ge 11$:
$$\left(\frac{k + 2}{k + 1}\right)^3 \le \left(\frac{13}{12}\right)^3 \approx 1.27.$$
So $(k + 1)^3 < 2^k$ for all $k \ge 11$.

The typical use of this non-example is as the upper end of weak arithmetic: $\mathsf{EFA}$ is the standard weak theory in which exponentiation is total, and bounded arithmetic lives strictly below it.
