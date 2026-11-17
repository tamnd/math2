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

The ordinal $\varepsilon_0$, read "epsilon nought", is the least [[ordinal|0RDJK7EQYY]] $\varepsilon$ with $\omega^\varepsilon = \varepsilon$, in [[ordinal arithmetic|KAEDCQ8RM6]].
It is the supremum of the tower
$$\tau_0 = 1, \quad \tau_{n+1} = \omega^{\tau_n},$$
so that $\varepsilon_0 = \sup \set{1, \omega, \omega^\omega, \omega^{\omega^\omega}, \ldots}$.
The two descriptions agree by the theorem [[epsilon nought is the least fixed point of α ↦ ω^α|9BX0XHX2D5]].
The same theorem shows that $\varepsilon_0$ is a [[countable|01TQB88H4C]] limit ordinal, and that the ordinals below it are closed under $+$ and $\alpha \mapsto \omega^\alpha$.
It is the least [[epsilon number|PQSHBKCE7V]].

Each ordinal $\alpha$ with $0 < \alpha < \varepsilon_0$ has a [[Cantor normal form|6GD30FGYDZ]] $\omega^{\beta_1} c_1 + \cdots + \omega^{\beta_k} c_k$, and every exponent satisfies $\beta_i < \alpha$.
Writing each exponent in normal form again, and so on, ends after finitely many steps.
So every ordinal below $\varepsilon_0$ has a unique finite name built from $0$, $+$ and $\omega^{(\cdot)}$.
The [[comparison of Cantor normal forms|DXKWBFWCE0]] decides the order of two names.
This is the standard [[ordinal notation system|7MBX59Y7N9]] for $\varepsilon_0$.

The ordinal $\varepsilon_0$ is the [[proof-theoretic ordinal|C72RBH0CDR]] of [[Peano arithmetic|0QFT7Z76N5]].

## Remarks

### The notation system

A notation is either $0$ or a string $\omega^{a_1} + \cdots + \omega^{a_k}$ with $k \ge 1$, where the $a_i$ are notations and $a_1 \succeq a_2 \succeq \cdots \succeq a_k$.
Equal exponents next to each other replace the coefficients: $\omega^a \cdot 3$ is written $\omega^a + \omega^a + \omega^a$.
The order $\prec$ on notations is the lexicographic comparison of the theorem on normal forms, applied recursively to the exponents.
With natural numbers as codes, the set of notations and the relation $\prec$ are [[primitive recursive relations|QQQRJA90EP]].
The map that sends each notation to the ordinal that it names is an isomorphism onto $\varepsilon_0$.
Some values: $\omega^0 = 1$, $\omega^0 + \omega^0 = 2$, $\omega^{\omega^0} = \omega$, and $\omega^{\omega^{\omega^0}} = \omega^\omega$.

### Fundamental sequences

A [[fundamental sequence|VB6YXF761M]] for a limit ordinal $\lambda$ is an increasing sequence $\lambda[0] < \lambda[1] < \cdots$ with supremum $\lambda$.
A common choice for $\varepsilon_0$ is $\varepsilon_0[0] = 0$ and $\varepsilon_0[n+1] = \omega^{\varepsilon_0[n]}$, which gives $0, 1, \omega, \omega^\omega, \ldots$.
For a limit $\lambda < \varepsilon_0$ with normal form $\gamma + \omega^\beta$, one sets $(\gamma + \omega^{\delta + 1})[n] = \gamma + \omega^\delta \cdot n$, and $(\gamma + \omega^\beta)[n] = \gamma + \omega^{\beta[n]}$ when $\beta$ is a limit.
For example, $\omega^\omega[n] = \omega^n$ and $\omega^2[n] = \omega \cdot n$.
Books use slightly different conventions, for example $\varepsilon_0[n] = \tau_n$, and the fast-growing functions defined from them differ in detail.

### Role in proof theory

- [[Peano arithmetic|0QFT7Z76N5]] proves [[transfinite induction|0ZHQMQ2C1N]] along the notation system for every ordinal below $\varepsilon_0$. This is the theorem [[transfinite induction in arithmetic|ZE54ABPMJ0]].
- Peano arithmetic does not prove transfinite induction up to $\varepsilon_0$ itself, by [[Gentzen's consistency proof|QPV0HNP22S]] and [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
- The provably total computable functions of Peano arithmetic are the functions computable in time bounded by a level $f_\alpha$, $\alpha < \varepsilon_0$, of the fast-growing hierarchy.
- [[Goodstein's theorem|XQMNJF241J]] is true and unprovable in Peano arithmetic. Its proof assigns to each step an ordinal below $\varepsilon_0$, and the ordinals strictly decrease.
- The second-order system [[ACA0|HPA6HX3114]] has the same ordinal $\varepsilon_0$, because it is conservative over Peano arithmetic.

### Common errors

- The ordinal $\varepsilon_0$ is countable. It is far below the [[first uncountable ordinal|Z92S2GVCX9]] $\omega_1$, and it is not a cardinal.
- The notation $\omega_n$ is reserved for the initial ordinals $\omega_0 = \omega$, $\omega_1$, and so on. It must not be used for the stages of the tower.
- The statement "the ordinal of Peano arithmetic is $\varepsilon_0$" refers to the standard notation system. For an artificial notation system of a small order type, Peano arithmetic can fail to prove well-foundedness. For ordinals above $\varepsilon_0$, the choice of the notation system matters even more; see [[ordinal notation system|7MBX59Y7N9]].

## Explanations

### L1 human

Count $0, 1, 2, \ldots$ and then $\omega$, the first infinite ordinal.
Keep going: $\omega + 1$, $\omega \cdot 2$, $\omega^2$, $\omega^\omega$, $\omega^{\omega^\omega}$.
The ordinal $\varepsilon_0$ is the first ordinal past all the towers $\omega^{\omega^{\cdots}}$ of finite height.
Every smaller ordinal has a short written name made from $0$, plus signs and powers of $\omega$.
In logic, $\varepsilon_0$ measures exactly how strong the usual axioms for the natural numbers are.

### L2 human

We write the ordinal $\omega^{\omega + 1} + \omega^3 \cdot 2 + 5$ as a notation, and we check that it is below $\varepsilon_0$.

1. The exponents are $\omega + 1$, $3$ and $0$, and they decrease, so the sum is a normal form.
2. The exponent $\omega + 1$ is $\omega^{\omega^0} + \omega^0$, and $3$ is $\omega^0 + \omega^0 + \omega^0$.
3. So the full notation is $\omega^{\omega^{\omega^0} + \omega^0} + \omega^{\omega^0 + \omega^0 + \omega^0} + \omega^{\omega^0 + \omega^0 + \omega^0} + \omega^0 + \omega^0 + \omega^0 + \omega^0 + \omega^0$.
4. Each exponent is less than $\omega^\omega = \tau_2$. By the comparison of normal forms, the ordinal is less than $\omega^{\tau_2} = \tau_3 < \varepsilon_0$.

The typical use: a proof that a process ends assigns to each state a notation below $\varepsilon_0$, and shows that each step lowers it.
The trap: $\varepsilon_0$ is not $\omega^\omega$, and it is not the limit of $\omega, \omega^2, \omega^3, \ldots$, which is only $\omega^\omega$.

### L3 human

The ordinal $\varepsilon_0$ is the first point where the closure of $\set{0}$ under $+$ and $\alpha \mapsto \omega^\alpha$ stops.
To go further, one adds a function that names fixed points, as in $\varepsilon_\alpha = \varphi_1(\alpha)$ for the [[Veblen function|JQFAE9S2F4]], and repeats the step.
The proof-theoretic meaning comes from Gentzen: Peano arithmetic proves induction along each initial segment of the standard order below $\varepsilon_0$, and induction along the whole order proves the consistency of Peano arithmetic.
So $\varepsilon_0$ is the [[proof-theoretic ordinal|C72RBH0CDR]] of Peano arithmetic, and the model case of [[ordinal analysis|C5E5TG8PGP]].
The same ordinal measures intuitionistic [[Heyting arithmetic|CK8ZQRN183]] and the second-order system ACA0.
