---
tag: SXYZP1DNJJ
kind: definition
name: Elementary function arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
defines: 2JD80TE553
uses: [D8SD54M5PN, 3K1AKGXF8A, 1QD0KDDGYJ, GE43CSZTS9]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: Definition
---

## Definition

Elementary function arithmetic is Robinson arithmetic with a symbol for exponentiation and induction for all bounded formulas in the enlarged language.

Let $L_{\exp}$ be the [[language of arithmetic|D8SD54M5PN]] $L_A$ with one more binary function symbol, written $x^y$.
A formula of $L_{\exp}$ is $\Delta_0(\exp)$ when every quantifier in it is bounded, of the form $\forall x < t$ or $\exists x < t$ with $t$ a term of $L_{\exp}$ that does not contain $x$.

Elementary function arithmetic $\mathsf{EFA}$ is the first-order theory in $L_{\exp}$ with the following axioms.

1. The axioms $\mathsf{Q}1$ to $\mathsf{Q}8$ of [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$.
2. The exponentiation axioms $\forall x \, (x^0 = S0)$ and $\forall x \, \forall y \, (x^{Sy} = x^y \cdot x)$.
3. The [[induction schema|1QD0KDDGYJ]] for $\Delta_0(\exp)$ formulas.
   For every $\Delta_0(\exp)$ formula $\varphi(x, \vec z)$ this is the axiom below.

$$\forall \vec z \, \big( \varphi(0, \vec z) \land \forall x \, (\varphi(x, \vec z) \to \varphi(Sx, \vec z)) \to \forall x \, \varphi(x, \vec z) \big)$$

The standard model is $\mathfrak{N}$ with $x^y$ read as ordinary exponentiation on $\mathbb{N}$, with $0^0 = 1$.

## Notation

A second formulation stays in $L_A$.
Fix a [[$\Delta_0$ formula|GE43CSZTS9]] $\mathrm{Exp}(x, y)$ of $L_A$ that defines $y = 2^x$ in $\mathfrak{N}$, and for which $\mathsf{I}\Delta_0$ proves the laws $\mathrm{Exp}(0, S0)$ and $\mathrm{Exp}(x, y) \to \mathrm{Exp}(Sx, y + y)$.
Such a formula exists, but its construction is technical, and we cite it rather than give it.
Then $\mathsf{I}\Delta_0 + \mathsf{exp}$ is $\mathsf{I}\Delta_0$ with the one extra axiom $\mathsf{exp}$, which is $\forall x \, \exists y \, \mathrm{Exp}(x, y)$.
The two theories prove the same sentences of $L_A$, so the name $\mathsf{EFA}$ is used for both.

## Remarks

Each axiom group has a job.
The axioms of $\mathsf{Q}$ fix $0$, successor, $+$, $\cdot$ and $<$.
The two exponentiation axioms compute powers by recursion on the exponent, for example $2^3 = 2^2 \cdot 2 = (2^1 \cdot 2) \cdot 2 = ((2^0 \cdot 2) \cdot 2) \cdot 2 = 8$.
The induction schema may use $x^y$ inside the formula and inside the bounds, and that is what lets the theory prove general laws about powers, as L2 shows.

The bound on each quantifier is the condition that keeps the theory weak.
The formula $x < 2^x$ is $\Delta_0(\exp)$, since it has no quantifiers.
The formula $\exists y \, (y = 2^{2^x})$ is not, since its quantifier has no bound, and induction on such formulas is not an axiom.

The [[concept page|2JD80TE553]] explains the provably total functions and Friedman's grand conjecture.

## Explanations

### L1 human

The definition lists the starting facts of the theory.
There are the basic facts about $0$, successor, addition, multiplication and order, as in Robinson arithmetic.
There are two rules that compute powers, such as $2^3 = 2^2 \cdot 2 = 8$.
And there is induction, but only for statements whose quantifiers range below a given bound, such as "every $d < x^2$ has some property".

### L2 human

We show that $\mathsf{EFA}$ proves $\forall x \, (x < 2^x)$, where $2$ is the numeral $SS0$.
Let $\varphi(x)$ be $x < 2^x$.
It has no quantifiers, so it is $\Delta_0(\exp)$ and induction applies to it.

1. Base case: $2^0 = S0$ by the first exponentiation axiom, and $\mathsf{Q}$ proves $0 < S0$.
2. Step: assume $x < 2^x$.
   Then $Sx \le 2^x$, and $2^x \ge 1$ by a separate induction of the same kind.
3. So $Sx \le 2^x < 2^x + 2^x = 2^x \cdot 2 = 2^{Sx}$, by the second exponentiation axiom.
4. Induction for $\varphi$ gives $\forall x \, (x < 2^x)$.

Check at $x = 3$: $3 < 8$.
Watch out: item 3 of the definition is induction for bounded formulas only, and an unbounded quantifier inside $\varphi$ is not allowed.
