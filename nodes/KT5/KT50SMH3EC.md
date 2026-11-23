---
tag: KT50SMH3EC
kind: object
name: Epsilon nought
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [0YSCSX5YZC]
uses: [0RDJK7EQYY, 01TQB88H4C, KAEDCQ8RM6, 6GD30FGYDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
---

## Description

Start with $\omega$ and keep raising $\omega$ to the power of what you have:

$$\omega, \quad \omega^\omega, \quad \omega^{\omega^\omega}, \quad \omega^{\omega^{\omega^\omega}}, \quad \ldots$$

Each term is much larger than the one before, and the list never ends.
The ordinal $\varepsilon_0$, read "epsilon nought", is the first [[ordinal|0RDJK7EQYY]] past every term of this list.
It is the ordinal that measures the strength of [[Peano arithmetic|0QFT7Z76N5]].

Precisely, define the tower $\tau_0 = 1$ and $\tau_{n+1} = \omega^{\tau_n}$ in [[ordinal arithmetic|KAEDCQ8RM6]], and set

$$\varepsilon_0 = \sup_{n} \tau_n = \sup \{ 1, \omega, \omega^\omega, \omega^{\omega^\omega}, \ldots \}.$$

By the theorem [[epsilon nought is the least fixed point of α ↦ ω^α|9BX0XHX2D5]], $\varepsilon_0$ is also the least ordinal $\varepsilon$ with $\omega^\varepsilon = \varepsilon$, so it is the least [[epsilon number|PQSHBKCE7V]].
It is a [[countable|01TQB88H4C]] limit ordinal, and the ordinals below it are closed under $+$ and $\alpha \mapsto \omega^\alpha$.

Every $\alpha$ with $0 < \alpha < \varepsilon_0$ has a [[Cantor normal form|6GD30FGYDZ]] $\omega^{\beta_1} c_1 + \cdots + \omega^{\beta_k} c_k$ with $\beta_1 > \cdots > \beta_k$, and every exponent is smaller than $\alpha$.
Writing each exponent in normal form again ends after finitely many steps.
So every ordinal below $\varepsilon_0$ has a unique finite name built from $0$, $+$ and $\omega^{(\cdot)}$, and the [[comparison of Cantor normal forms|DXKWBFWCE0]] decides the order of two names.
This is the standard [[ordinal notation system|7MBX59Y7N9]] for $\varepsilon_0$, and with it $\varepsilon_0$ is the [[proof-theoretic ordinal|C72RBH0CDR]] of Peano arithmetic.

## Remarks

### Names below epsilon nought

A notation is $0$ or a string $\omega^{a_1} + \cdots + \omega^{a_k}$ with $k \ge 1$, where the $a_i$ are notations and $a_1 \succeq a_2 \succeq \cdots \succeq a_k$.
Equal neighboring exponents replace coefficients, so $\omega^a \cdot 3$ is written $\omega^a + \omega^a + \omega^a$.
Some values: $\omega^0 = 1$, $\omega^0 + \omega^0 = 2$, $\omega^{\omega^0} = \omega$ and $\omega^{\omega^{\omega^0}} = \omega^\omega$.
The order is the lexicographic comparison of exponents, applied recursively, and with natural numbers as codes it is a [[primitive recursive relation|QQQRJA90EP]].
The full construction is the [[Cantor normal form notation|R3BJR7TM2Z]].

### Fundamental sequences

How do we approach $\omega^2$ from below in a fixed, computable way?
Take $\omega^2[n] = \omega \cdot n$, which gives $0, \omega, \omega \cdot 2, \omega \cdot 3, \ldots$ with supremum $\omega^2$.
A [[fundamental sequence|VB6YXF761M]] for a limit $\lambda$ is in general an increasing sequence $\lambda[0] < \lambda[1] < \cdots$ with supremum $\lambda$.

The standard choice below $\varepsilon_0$ works on the last term of the normal form.
For $\lambda = \gamma + \omega^{\delta + 1}$ we set $\lambda[n] = \gamma + \omega^\delta \cdot n$, and for $\lambda = \gamma + \omega^\beta$ with $\beta$ a limit we set $\lambda[n] = \gamma + \omega^{\beta[n]}$.
So $\omega^\omega[n] = \omega^n$ and $(\omega^2 + \omega)[n] = \omega^2 + n$.
For $\varepsilon_0$ itself a common choice is $\varepsilon_0[0] = 0$ and $\varepsilon_0[n+1] = \omega^{\varepsilon_0[n]}$, which gives $0, 1, \omega, \omega^\omega, \ldots$.
Books differ in small details, for example $\varepsilon_0[n] = \tau_n$, and the fast-growing functions defined from them differ in detail too.

### Role in proof theory

Peano arithmetic proves [[transfinite induction|0ZHQMQ2C1N]] along the notation system up to every ordinal below $\varepsilon_0$; this is [[transfinite induction in arithmetic|ZE54ABPMJ0]].
It does not prove transfinite induction up to $\varepsilon_0$ itself.
One reason is that such induction proves the consistency of PA by [[Gentzen's consistency proof|QPV0HNP22S]], which PA cannot prove by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].

The ordinal also bounds what PA computes.
The functions that PA proves total are those computable in time bounded by a level $f_\alpha$ of the fast-growing hierarchy with $\alpha < \varepsilon_0$.
[[Goodstein's theorem|XQMNJF241J]] is true and unprovable in PA: its proof gives each step an ordinal below $\varepsilon_0$, and these ordinals decrease.
The second-order system [[ACA0|HPA6HX3114]] has the same ordinal, because it is conservative over PA.

### Watch out

The ordinal $\varepsilon_0$ is not the limit of $\omega, \omega^2, \omega^3, \ldots$, which is only $\omega^\omega = \tau_2$.
The tower must grow in the exponent, not in the base.
It is also countable: it is far below the [[first uncountable ordinal|Z92S2GVCX9]] $\omega_1$, and it is not a cardinal.
The symbols $\omega_n$ already mean the initial ordinals $\omega_0 = \omega$, $\omega_1, \ldots$, so do not use them for the stages of the tower.

### Try it

Is $\omega^{\omega^2 + 1}$ below $\varepsilon_0$?
Yes: $\omega^2 + 1 < \omega^\omega = \tau_2$, so $\omega^{\omega^2 + 1} < \omega^{\tau_2} = \tau_3 < \varepsilon_0$.

Give the first three terms of the fundamental sequence of $\omega^3$.
They are $\omega^3[0] = 0$, $\omega^3[1] = \omega^2$ and $\omega^3[2] = \omega^2 \cdot 2$, by the rule $\gamma + \omega^{\delta+1} \mapsto \gamma + \omega^\delta \cdot n$ with $\gamma = 0$, $\delta = 2$.

## Explanations

### L1 human

Count $0, 1, 2, \ldots$ and then $\omega$, the first infinite ordinal.
Keep going: $\omega + 1$, $\omega \cdot 2$, $\omega^2$, $\omega^\omega$, $\omega^{\omega^\omega}$.
The ordinal $\varepsilon_0$ is the first ordinal past all the towers $\omega^{\omega^{\cdots}}$ of finite height.
Every smaller ordinal has a short written name made from $0$, plus signs and powers of $\omega$.
In logic, $\varepsilon_0$ measures exactly how strong the usual axioms for the natural numbers are.

### L2 human

Write $\omega^{\omega + 1} + \omega^3 \cdot 2 + 5$ as a notation, and check that it is below $\varepsilon_0$.
The exponents are $\omega + 1$, $3$ and $0$, and they decrease, so the sum is a normal form.
The exponent $\omega + 1$ is $\omega^{\omega^0} + \omega^0$, and $3$ is $\omega^0 + \omega^0 + \omega^0$.
The full notation is therefore:

$$\omega^{\omega^{\omega^0} + \omega^0} + \omega^{\omega^0 + \omega^0 + \omega^0} + \omega^{\omega^0 + \omega^0 + \omega^0} + \omega^0 + \omega^0 + \omega^0 + \omega^0 + \omega^0.$$

Each exponent is less than $\omega^\omega = \tau_2$, so by the comparison of normal forms the ordinal is less than $\omega^{\tau_2} = \tau_3 < \varepsilon_0$.
This is the typical use: a termination proof gives each state a notation below $\varepsilon_0$ and shows that each step lowers it.

### L3 human

The ordinal $\varepsilon_0$ is the first point where the closure of $\{ 0 \}$ under $+$ and $\alpha \mapsto \omega^\alpha$ stops.
To go further, we add a function that names fixed points, such as $\varepsilon_\alpha = \varphi_1(\alpha)$ for the [[Veblen function|JQFAE9S2F4]], and repeat the step.
The proof-theoretic meaning comes from Gentzen: PA proves induction along each initial segment of the standard order below $\varepsilon_0$, and induction along the whole order proves the consistency of PA.
So $\varepsilon_0$ is the model case of [[ordinal analysis|C5E5TG8PGP]].
The same ordinal measures intuitionistic [[Heyting arithmetic|CK8ZQRN183]] and the second-order system $\mathrm{ACA}_0$.
