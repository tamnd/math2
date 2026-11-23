---
tag: YPQPC1WJMV
kind: statement
role: theorem
name: Parikh's theorem
aliases: [parikhs-theorem-bounded-arithmetic]
msc: ["03F30", "03C62"]
topics: [RA380RWEC0]
audience: research
uses: [GE43CSZTS9, T70PYM1F36, 3K1AKGXF8A, 1QD0KDDGYJ, 6D3WA7N2W4]
about: [A2CFPP8JMN, T70PYM1F36]
proofs: [54SYW2Z3QN]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: lead section
history:
  first_stated: "1971"
  notes: "R. Parikh, Existence and feasibility in arithmetic, Journal of Symbolic Logic 36 (1971), 494-508."
---

## Statement

Parikh's theorem says that when $\mathsf{I}\Delta_0$ proves that a witness exists for a bounded property, it also proves that a witness exists below a polynomial.
So $\mathsf{I}\Delta_0$ cannot prove that $2^x$ exists for every $x$, because no polynomial bounds $2^x$.

Let $L_A = \{ 0, S, +, \cdot, < \}$ be the [[language of arithmetic|D8SD54M5PN]].
Let $\mathsf{I}\Delta_0$ be [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ together with the [[induction schema|1QD0KDDGYJ]] for all [[$\Delta_0$ formulas|GE43CSZTS9]].
A $\Pi_1$ sentence is a sentence $\forall \bar w \, \chi(\bar w)$ with $\chi$ a $\Delta_0$ formula.

**Theorem.** Let $T$ be a theory in $L_A$ whose axioms are the axioms of $\mathsf{I}\Delta_0$ together with any set of $\Pi_1$ sentences.
Let $\varphi(\bar x, y)$ be a $\Delta_0$ formula of $L_A$.
If $T \vdash \forall \bar x \, \exists y \, \varphi(\bar x, y)$, then there is a [[term|6D3WA7N2W4]] $t(\bar x)$ of $L_A$ such that the following holds:
$$T \vdash \forall \bar x \, \exists y < t(\bar x) \, \varphi(\bar x, y).$$

A term of $L_A$ in the variables $\bar x$ takes the same values in $\mathbb{N}$ as a polynomial in $\bar x$ with coefficients in $\mathbb{N}$.
So, in the standard model, the theorem gives a polynomial bound on a witness $y$.
The same proof works when $y$ is a tuple $\bar y$, and then each component gets the bound $t(\bar x)$.

## Remarks

### A first use: exponentiation

Fix a $\Delta_0$ formula $\mathrm{Exp}(x, y)$ that defines the relation $y = 2^x$ in $\mathbb{N}$.
Suppose $\mathsf{I}\Delta_0$ proved $\forall x \, \exists y \, \mathrm{Exp}(x, y)$.
Then Parikh's theorem would give a term $t(x)$, a polynomial, with $2^n < t(n)$ for every $n$ in $\mathbb{N}$.
That is false for every polynomial: for $t(x) = x^2 + 3x + 1$ we get the numbers below, and the exponential wins for good from $n = 6$ on:
$$2^5 = 32 < 41 = t(5), \qquad 2^6 = 64 > 55 = t(6).$$
So $\mathsf{I}\Delta_0 \nvdash \forall x \, \exists y \, \mathrm{Exp}(x, y)$, although $\mathsf{I}\Delta_0$ can define the graph of $2^x$.

The same argument proves more.
Every function that is $\Delta_0$-definable and [[provably total|Z742YPHPNS]] in $\mathsf{I}\Delta_0$ is bounded by a polynomial in $\mathbb{N}$.
The theorem is a tool for unprovability: to show that $\mathsf{I}\Delta_0$ does not prove $\forall x \, \exists y \, \varphi$, show that the witnesses grow too fast.

### Why each hypothesis is needed

The formula $\varphi$ must be bounded.
Let $\psi(x, y)$ be $\forall w \, \neg \mathrm{Exp}(x, w) \lor \mathrm{Exp}(x, y)$, a $\Pi_1$ formula.
By pure logic, $\mathsf{I}\Delta_0 \vdash \forall x \, \exists y \, \psi(x, y)$: take $y = w$ when some $w$ satisfies $\mathrm{Exp}(x, w)$, and $y = 0$ otherwise.
But in $\mathbb{N}$ the only witness for $x = n$ is $2^n$, so no term bounds it.

The extra axioms must be $\Pi_1$.
The theory [[elementary function arithmetic|2JD80TE553]], $\mathsf{EFA} = \mathsf{I}\Delta_0 + \forall x \, \exists y \, \mathrm{Exp}(x, y)$, adds one $\Pi_2$ axiom.
It proves $\forall x \, \exists y \, \mathrm{Exp}(x, y)$, and $\mathbb{N}$ is a model of it, so no term bounds the witness.

### The converse and the size of the bound

The converse holds by pure logic, since $\exists y < t(\bar x) \, \varphi(\bar x, y)$ implies $\exists y \, \varphi(\bar x, y)$.
A bound that does not depend on $\bar x$ does not exist in general: for $\varphi(x, y)$ equal to $y = x$, every bound must grow with $x$.

### Generalizations

The proof works in a larger language when the theory proves that each function symbol is monotone, and when the axioms are $\Pi_1$ sentences of that language together with induction or polynomial induction for bounded formulas.
This covers Buss's theories $S^i_2$ and $T^i_2$ of [[bounded arithmetic|A2CFPP8JMN]], and $\mathsf{I}\Delta_0 + \Omega_1$ with a function symbol for $x \mapsto x^{\lvert x \rvert}$.
In Buss's language the terms contain the smash function $x \# y = 2^{\lvert x \rvert \cdot \lvert y \rvert}$, so the binary length of the bound is a polynomial in the binary lengths of $\bar x$.
That is the size of an answer to a polynomial-time search problem, and [[Buss's witnessing theorem|RH4R7GTTAX]] goes on to show that the answer can also be found in polynomial time.

### Watch out

Do not apply the theorem to a formula $\varphi$ that is $\Pi_1$ or $\Sigma_1$: the formula $\psi$ above is a $\Pi_1$ counterexample.
Do not forget the form of the extra axioms either, since the theorem fails for $\mathsf{EFA}$.
Finally, the theorem gives a bound that $T$ proves, which is stronger than a bound that is only true in $\mathbb{N}$.

## History

Rohit Parikh proved the theorem in *Existence and feasibility in arithmetic*, Journal of Symbolic Logic 36 (1971).
He used it to show that $\mathsf{I}\Delta_0$ does not prove that exponentiation is total.
The proof by cuts in a nonstandard model is a model-theoretic proof of the same result.

## Explanations

### L1 human

Some proofs show that a number exists, for example a number that has some property and is bigger than a given number.
Parikh's theorem is about a weak system of rules for whole numbers.
When the system proves that such a number always exists, and the property only looks at numbers up to fixed limits, the system also gives a size limit for the number.
The limit is a polynomial, for example $x^2 + 3x + 1$.
So the system cannot prove that $2^x$ always exists, because $2^x$ outgrows every polynomial: already $2^{10} = 1024$ is far above $10^2 + 3 \cdot 10 + 1 = 131$.

### L2 human

Here is a typical problem: show that $\mathsf{I}\Delta_0$ does not prove that every $x$ has a power $x^x$.
Let $\mathrm{Pow}(x, y)$ be a $\Delta_0$ formula that defines $y = x^x$ in $\mathbb{N}$, which exists since the graph of exponentiation is $\Delta_0$.
If $\mathsf{I}\Delta_0 \vdash \forall x \, \exists y \, \mathrm{Pow}(x, y)$, Parikh's theorem gives a polynomial $t$ with $n^n < t(n)$ for all $n$.
A polynomial of degree $d$ is at most $c \, n^d$ for some constant $c$ and all $n \ge 1$, and $n^n = n^{d} \cdot n^{n - d}$ exceeds $c \, n^d$ once $n^{n - d} > c$.
For $t(n) = n^2$, the case $n = 3$ already gives the comparison below:
$$3^3 = 27 > 9 = t(3).$$
So no polynomial bounds $x^x$, and $\mathsf{I}\Delta_0$ does not prove $\forall x \, \exists y \, \mathrm{Pow}(x, y)$.
The problem shows the typical use: the theorem is negative, and it reduces an unprovability question to a growth comparison.

### L3 human

The model-theoretic proof shows a general principle: in a model of $\mathsf{I}\Delta_0$, the elements below the values of all terms at fixed parameters form an initial segment that is again a model.
Initial segments of this kind are cuts, and $\Delta_0$ formulas mean the same in a model and in its cuts.
Cuts are also the main tool behind [[indicators|JWTZ8NVVGK]] and many independence results for weak theories.

In bounded arithmetic the theorem turns every $\forall \exists$ theorem with a bounded matrix into a bounded one, and so into a statement about search problems with short answers.
Buss's witnessing theorem and the [[Krajíček-Pudlák-Takeuti theorem|YP7KE8E6DC]] start from this bound and then analyze the proof further.
The proof-theoretic proof uses [[cut elimination|AYRZ98Y0NW]] and works for all bounded theories in the same way.
