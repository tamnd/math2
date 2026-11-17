---
tag: V8WD1F0NS2
kind: example
name: The theory IΔ0 + Ω1
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
instance_of: [A2CFPP8JMN]
uses: [A2CFPP8JMN, T70PYM1F36, GE43CSZTS9, YPQPC1WJMV]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: lead section
---

## Example

Let $\abs{x}$ be the binary length of $x$, and let $\omega_1(x) = x^{\abs{x}}$.
Fix a $\Delta_0$ formula $\Omega(x, y)$ that defines the relation $y = x^{\abs{x}}$ in $\N$.
The axiom $\Omega_1$ is $\forall x \, \exists y \, \Omega(x, y)$, and the theory is $\mathsf{I}\Delta_0 + \Omega_1$.
We check that it is a theory of [[bounded arithmetic|A2CFPP8JMN]], and that $\omega_1$ has the growth rate of the smash function $x \# y = 2^{\abs{x} \cdot \abs{y}}$.

1. Induction. The only induction axioms are those of $\mathsf{I}\Delta_0$, which are for [[$\Delta_0$ formulas|GE43CSZTS9]], so for bounded formulas.
2. Upper bound for $\omega_1$. Every $x$ satisfies $x < 2^{\abs{x}}$. So $\omega_1(x) = x^{\abs{x}} \le 2^{\abs{x} \cdot \abs{x}} = x \# x$.
3. Lower bound for $\omega_1$. For $x \ge 1$, $2x \ge 2^{\abs{x}}$ and $\abs{2x} = \abs{x} + 1$. So $\omega_1(2x) \ge (2^{\abs{x}})^{\abs{x}} = x \# x$.
4. Numbers. For $x = 7$: $\abs{7} = 3$, $\omega_1(7) = 343$ and $7 \# 7 = 2^9 = 512$. For $x = 14$: $\abs{14} = 4$ and $\omega_1(14) = 38416 \ge 512$.
5. Growth of provably total functions. Parikh's argument in the [[proof of Parikh's theorem|54SYW2Z3QN]] works with a function symbol for $\omega_1$ added. So each provably total function is bounded by a term in $+$, $\cdot$ and $\omega_1$.
6. Such a term is at most $2^{p(\abs{x})}$ for a polynomial $p$, by step 2, since $\abs{\omega_1(x)} \le \abs{x}^2 + 1$. For $p(n) = n^2$ and $x = 7$, this bound is $2^9 = 512$.

So $\mathsf{I}\Delta_0 + \Omega_1$ has bounded induction and provably total functions of growth at most $2^{p(\abs{x})}$.

## Remarks

The example shows why $\mathsf{I}\Delta_0 + \Omega_1$ and Buss's theory $T_2$ prove the same theorems up to the change of language: both have exactly the growth rate of $\#$.
Without $\Omega_1$, the theory $\mathsf{I}\Delta_0$ has only polynomial growth, and $x \# x$ is not provably total in it, by [[Parikh's theorem|YPQPC1WJMV]].
If $\Omega_1$ is replaced by the totality of $x \mapsto 2^x$, the theory becomes [[elementary function arithmetic|2JD80TE553]], which is no longer a theory of bounded arithmetic.

## Explanations

### L1 human

The binary length of $7$ is $3$, since $7$ is written $111$ in binary.
The axiom $\Omega_1$ says that the number $7^3 = 343$ exists, and in general a number raised to its own length.
This number has about the square of the length of the original number in digits.
For $7$, the length is $3$, and $343$ has $9$ binary digits.
So the axiom allows numbers with polynomially many more digits, but not exponentially many.

### L2 human

We compare $\omega_1(x)$ and $x \# x$ for $x = 5$ and $x = 10$.

1. $\abs{5} = 3$, so $\omega_1(5) = 125$ and $5 \# 5 = 2^9 = 512$.
2. $\abs{10} = 4$, so $\omega_1(10) = 10^4 = 10000$, and $10 \# 10 = 2^{16} = 65536$.
3. In both cases $\omega_1(x) \le x \# x$, as step 2 of the example predicts.
4. Step 3 predicts $\omega_1(10) \ge 5 \# 5$, and indeed $10000 \ge 512$.

The typical use of $\Omega_1$ is to code sequences and syntax: a sequence of $\abs{x}$ numbers below $x$ is a number of size about $x^{\abs{x}}$.
A trap is to think that $\Omega_1$ makes exponentiation total: $2^x$ is far larger than $2^{\abs{x}^2}$ for large $x$.
