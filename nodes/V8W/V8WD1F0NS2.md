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

The axiom $\Omega_1$ says that a number raised to the power of its own length exists.
For $x = 7$, which is $111$ in binary, the length is $3$ and the axiom promises the number $7^3 = 343$.

In exact terms, let $\lvert x \rvert$ be the binary length of $x$ and let $\omega_1(x) = x^{\lvert x \rvert}$.
Fix a [[$\Delta_0$ formula|GE43CSZTS9]] $\Omega(x, y)$ that defines the relation $y = x^{\lvert x \rvert}$ in $\mathbb{N}$.
The axiom $\Omega_1$ is the sentence $\forall x \, \exists y \, \Omega(x, y)$, and the theory is $\mathsf{I}\Delta_0 + \Omega_1$.
We check that it is a theory of [[bounded arithmetic|A2CFPP8JMN]], and that $\omega_1$ grows exactly as fast as the smash function $x \# y = 2^{\lvert x \rvert \cdot \lvert y \rvert}$.

### Checking the conditions

1. The only induction axioms are those of $\mathsf{I}\Delta_0$, which are for $\Delta_0$ formulas, so the induction is bounded.
2. For an upper bound, use $x < 2^{\lvert x \rvert}$, which holds for every $x$.
   Raise both sides to the power $\lvert x \rvert$:
   $$\omega_1(x) = x^{\lvert x \rvert} \le 2^{\lvert x \rvert \cdot \lvert x \rvert} = x \# x.$$
3. For a lower bound, take $x \ge 1$.
   Then $2x \ge 2^{\lvert x \rvert}$ and $\lvert 2x \rvert = \lvert x \rvert + 1$, so we get the following:
   $$\omega_1(2x) = (2x)^{\lvert x \rvert + 1} \ge (2^{\lvert x \rvert})^{\lvert x \rvert} = x \# x.$$
4. Check with numbers.
   For $x = 7$ we have $\omega_1(7) = 343 \le 512 = 2^9 = 7 \# 7$, and for $2x = 14$ we have $\omega_1(14) = 14^4 = 38416 \ge 512$.
5. By step 2, $\lvert \omega_1(x) \rvert \le \lvert x \rvert^2 + 1$.
   So a term built from $+$, $\cdot$ and $\omega_1$ has a length bounded by a polynomial in $\lvert x \rvert$, and its value is at most $2^{p(\lvert x \rvert)}$ for some polynomial $p$.
6. The argument of the [[proof of Parikh's theorem|54SYW2Z3QN]] still works when a function symbol for $\omega_1$ is added.
   So each provably total function of the theory is bounded by such a term, and so by $2^{p(\lvert x \rvert)}$.

So $\mathsf{I}\Delta_0 + \Omega_1$ has bounded induction, and its provably total functions grow at most like $2^{p(\lvert x \rvert)}$.

## Remarks

The two bounds of steps 2 and 3 show that $\omega_1$ and $x \mapsto x \# x$ can each be bounded by the other with a small change of input.
That is the reason why $\mathsf{I}\Delta_0 + \Omega_1$ and Buss's theory $T_2$ can interpret each other's functions, and in fact they prove the same theorems once the languages are translated.

Change the axiom and the picture changes at once.
Without $\Omega_1$, the theory $\mathsf{I}\Delta_0$ has only polynomial growth, and by [[Parikh's theorem|YPQPC1WJMV]] it does not prove that $x \mapsto x \# x$ is total.
If $\Omega_1$ is replaced by the totality of $x \mapsto 2^x$, the theory becomes [[elementary function arithmetic|2JD80TE553]], which is no longer a theory of bounded arithmetic.

## Explanations

### L1 human

The binary length of $7$ is $3$, since $7$ is written $111$ in binary.
The axiom $\Omega_1$ says that the number $7^3 = 343$ exists, and in general that each number raised to its own length exists.
The new number has about the square of the old length in digits: $343$ is $101010111$ in binary, which has $9 = 3^2$ digits.
So the axiom allows numbers whose length is the square of the old length, but never numbers whose length is exponential in it.

### L2 human

We compare $\omega_1(x)$ and $x \# x$ for $x = 5$ and $x = 10$.
Since $\lvert 5 \rvert = 3$, we get $\omega_1(5) = 125$ and $5 \# 5 = 2^9 = 512$.
Since $\lvert 10 \rvert = 4$, we get $\omega_1(10) = 10^4 = 10000$ and $10 \# 10 = 2^{16} = 65536$.
In both cases $\omega_1(x) \le x \# x$, as step 2 predicts.
Step 3 with $x = 5$ predicts $\omega_1(10) \ge 5 \# 5$, and indeed $10000 \ge 512$.

The typical use of $\Omega_1$ is to code sequences and syntax.
A sequence of $\lvert x \rvert$ numbers, each below $x$, is coded by a number of size about $x^{\lvert x \rvert}$, and $\Omega_1$ makes that number exist.
Watch out: $\Omega_1$ does not make exponentiation total, because $2^x$ is far larger than $2^{\lvert x \rvert^2}$ for large $x$.
