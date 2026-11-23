---
tag: FFAWTY9TBE
kind: example
name: Double exponentiation is provably total in elementary function arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
instance_of: [2JD80TE553]
uses: [2JD80TE553, SXYZP1DNJJ, RJ3MCAAZSV, 69234Z1V00]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: Definition
---

## Example

Two uses of the axiom "every power of $2$ exists" give a power of a power.
Let $d(x) = 2^{2^x}$.
We show that [[elementary function arithmetic|2JD80TE553]] proves that $d$ is total, in the form $\mathsf{I}\Delta_0 + \mathsf{exp}$ of the [[definition|SXYZP1DNJJ]].
Let $\delta(x, z)$ be the formula
$$\exists y \le z \, (\mathrm{Exp}(x, y) \land \mathrm{Exp}(y, z)).$$
It is $\Delta_0$, and in $\mathfrak{N}$ it holds exactly when $z = d(x)$, because the middle value $2^x$ is at most $2^{2^x}$.

1. Fix $x$.
   The axiom $\mathsf{exp}$ gives some $y$ with $\mathrm{Exp}(x, y)$.
2. The axiom $\mathsf{exp}$ applied to $y$ gives some $z$ with $\mathrm{Exp}(y, z)$.
3. $\mathsf{I}\Delta_0$ proves $\mathrm{Exp}(u, v) \to u < v$, by $\Delta_0$ induction on $u$ with the recursion laws of $\mathrm{Exp}$.
   So $y < z$ for the numbers of step 2.
4. By steps 1 to 3, $y$ is a witness below $z$ for $\delta(x, z)$, so $\mathsf{EFA} \vdash \forall x \, \exists z \, \delta(x, z)$.
5. $\mathsf{I}\Delta_0$ proves $\mathrm{Exp}(u, v) \land \mathrm{Exp}(u, v') \to v = v'$, by $\Delta_0$ induction on $u$.
   Two uses of this give $\delta(x, z) \land \delta(x, z') \to z = z'$.

So $\mathsf{EFA} \vdash \forall x \, \exists! z \, \delta(x, z)$, and $d$ is provably total in $\mathsf{EFA}$.

## Remarks

The same argument with $k$ uses of $\mathsf{exp}$ shows that the tower of $k$ twos topped by $x$ is provably total, for each fixed $k$.
This agrees with the theorem that the provably total functions of $\mathsf{EFA}$ are the [[elementary recursive functions|RJ3MCAAZSV]], since each such tower is elementary.

The argument does not reach a tower of variable height $x$.
That would need $x$ uses of $\mathsf{exp}$, which is an induction on a formula with an unbounded $\exists$.
In $\mathsf{I}\Delta_0$ without $\mathsf{exp}$, steps 1 and 2 fail, and $d$ is not provably total there at all.

What the example proves is the uniform statement with $\forall x$.
Each single instance $\exists z \, \delta(\overline{n}, z)$ is a true $\Sigma_1$ sentence, so even $\mathsf{Q}$ proves it, by [[Σ1-completeness|69234Z1V00]].

## Explanations

### L1 human

The number $2^{2^x}$ is a power of $2$ whose exponent is itself a power of $2$.
For $x = 3$ it is $2^8 = 256$, and for $x = 4$ it is $2^{16} = 65536$.
The theory has an axiom saying that $2^y$ exists for each $y$.
Using this axiom twice, first for $x$ and then for $2^x$, shows that $2^{2^x}$ exists for every $x$.

### L2 human

We follow the proof for $x = 2$ in $\mathfrak{N}$.
Step 1 gives $y = 2^2 = 4$, with $\mathrm{Exp}(2, 4)$, and step 2 gives $z = 2^4 = 16$, with $\mathrm{Exp}(4, 16)$.
Step 3 gives $4 < 16$, so $y = 4$ is a witness below $z$, and $\delta(2, 16)$ holds.
Check: $d(2) = 2^{2^2} = 2^4 = 16$.

A typical use is to bound codes.
A sequence of $x$ numbers below $2^x$ has a code below $2^{x \cdot x}$, written as $x$ blocks of $x$ binary digits.
That code is below $d(x)$ as soon as $x^2 < 2^x$, which holds for $x \ge 5$.
Check at $x = 5$: $x^2 = 25 < 32 = 2^5$.

Watch out for the bound $\exists y \le z$ in $\delta$.
Without it, $\delta$ is $\Sigma_1$ but not $\Delta_0$, and it could not be used inside a $\Delta_0$ induction.
