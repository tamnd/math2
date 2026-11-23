---
tag: ZE54ABPMJ0
kind: statement
role: theorem
name: Transfinite induction in arithmetic
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: grad
uses: [0QFT7Z76N5, KT50SMH3EC, DXKWBFWCE0, 0ZHQMQ2C1N, 5NVA2JRHPV, 1QD0KDDGYJ]
about: [0QFT7Z76N5, 0ZHQMQ2C1N, KT50SMH3EC]
history:
  posed_by: "Gerhard Gentzen"
  first_stated: "1943"
  notes: "Gentzen proved both parts in a paper on the provability of initial cases of transfinite induction in pure number theory, Mathematische Annalen, 1943."
sources:
  - url: https://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof
    locator: Gentzen's theorem
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
---

## Statement

The theorem says that Peano arithmetic proves transfinite induction up to each fixed ordinal below $\varepsilon_0$, but not up to $\varepsilon_0$ itself.

Let PA be first-order [[Peano arithmetic|0QFT7Z76N5]], with the [[induction schema|1QD0KDDGYJ]] for all formulas.
Fix the standard notation system for the ordinals below [[epsilon nought|KT50SMH3EC]], coded by natural numbers; its set of codes and its order $\prec$ are [[primitive recursive|5NVA2JRHPV]], so PA expresses them by fixed formulas.
The order $\prec$ is the [[comparison of Cantor normal forms|DXKWBFWCE0]], applied recursively, and the variables $x, y, z$ range over codes of notations.
For a formula $\varphi(x)$, possibly with other free variables, define

$$\operatorname{Prog}(\varphi) :\equiv \forall x \, \bigl(\forall y \prec x \; \varphi(y) \to \varphi(x)\bigr), \qquad \operatorname{TI}(a, \varphi) :\equiv \operatorname{Prog}(\varphi) \to \forall x \prec a \; \varphi(x).$$

So $\operatorname{Prog}(\varphi)$ says that $\varphi$ is *progressive*, and $\operatorname{TI}(a, \varphi)$ is [[transfinite induction|0ZHQMQ2C1N]] for $\varphi$ up to $a$.
Write $\operatorname{TI}(\varepsilon_0, \varphi)$ for $\operatorname{Prog}(\varphi) \to \forall x \, \varphi(x)$, induction along the whole order.

**Theorem (Gentzen).**

1. For every notation $a$ and every formula $\varphi(x)$ of the language of PA, $\mathrm{PA} \vdash \operatorname{TI}(a, \varphi)$.
2. If PA is consistent, there is a formula $\varphi(x)$ with $\mathrm{PA} \nvdash \operatorname{TI}(\varepsilon_0, \varphi)$, and $\varphi$ can be taken to express a primitive recursive predicate.

In part 1, $a$ is a fixed notation, written as a numeral, and the proof depends on $a$.
The [[proof by the jump|9072B273Q6]] proves both parts.

## Remarks

### Up to each level, but not to the top

Why can PA reach $\omega^{\omega^\omega}$ but not $\varepsilon_0$?
Ordinary induction already gives induction up to $\omega$, for every formula.
Gentzen's jump turns induction up to $a$ for a more complex formula $\varphi^+$ into induction up to $\omega^a$ for $\varphi$.
So three jumps take PA from $\omega$ to $\omega^\omega$, to $\omega^{\omega^\omega}$, and to $\omega^{\omega^{\omega^\omega}}$, each time with a formula one level more complex.
Each proof uses finitely many jumps, so it reaches some finite stage of the tower, and $\varepsilon_0$ is the limit of all the stages.
To pass the limit, one proof would need unboundedly many jumps, and part 2 says that no proof does this.

### Why each hypothesis is needed

The notation $a$ must be fixed.
The uniform statement $\forall a \, \operatorname{TI}(a, \varphi)$ is equivalent to $\operatorname{TI}(\varepsilon_0, \varphi)$, which part 2 excludes.

Induction for all formulas is needed.
Each jump uses induction for $\varphi^+$, which has more quantifiers than $\varphi$.
Fragments with less induction prove less: $\mathrm{I}\Sigma_1$ has the [[proof-theoretic ordinal|C72RBH0CDR]] $\omega^\omega$, far below $\varepsilon_0$.

The standard notation system is needed.
Along [[an artificial notation system of type ω|PXMATF6B16]], PA fails to prove transfinite induction even though the order type is only $\omega$.

Consistency is needed in part 2, since an inconsistent theory proves every formula.

### What it gives you

The proof-theoretic ordinal of PA is at least $\varepsilon_0$, and with [[Gentzen's consistency proof|QPV0HNP22S]] it is exactly $\varepsilon_0$.
A function defined by recursion along $\prec$ below a fixed notation, with primitive recursive steps, is provably total in PA.
A true statement whose proof needs induction along all of $\varepsilon_0$ can be independent of PA, and [[Goodstein's theorem|XQMNJF241J]] is such a statement.

### The converse

Take a natural system that extends the standard one, such as the notations of the [[Veblen function|JQFAE9S2F4]], where PA proves that the initial segment below $\varepsilon_0$ matches the Cantor normal forms.
Then PA proves transfinite induction for all formulas up to a notation exactly when the notation names an ordinal below $\varepsilon_0$.
The direction "only if" follows from part 2, because induction up to a larger notation gives induction up to $\varepsilon_0$.
For artificial systems this converse fails.

### Generalizations

The same jump works in second-order arithmetic.
Over $\mathrm{RCA}_0$, the statement "if $X$ is a well-order, then $\omega^X$ is a well-order" is equivalent to $\mathrm{ACA}_0$, a result of [[reverse mathematics|7SQS69T17R]] due to Girard and to Hirst.
Stronger theories prove transfinite induction along longer notation systems, and the length they reach is their proof-theoretic ordinal.

### Try it

How many jumps does PA need for induction up to $\omega^{\omega^2}$?
Two: $\omega^2 < \omega^\omega$, and two jumps from $\omega$ give $\omega^{\omega^\omega} > \omega^{\omega^2}$, so induction below $\omega^{\omega^2}$ follows.

Does PA prove "for every notation $a$, $\operatorname{TI}(a, \varphi)$" for every $\varphi$?
No: that sentence implies $\operatorname{TI}(\varepsilon_0, \varphi)$, which fails for some $\varphi$ by part 2.

## History

Gentzen proved both parts in 1943, in a paper in Mathematische Annalen on the provability and unprovability of initial cases of transfinite induction in number theory.
Part 2 can be derived from his consistency proof for PA of 1936, as in the proof given here.

## Explanations

### L1 human

Ordinary induction proves a property for $0, 1, 2, \ldots$ one step at a time.
Transfinite induction does the same along a longer list of ordinals, such as $0, 1, 2, \ldots, \omega, \omega + 1, \ldots, \omega \cdot 2, \ldots$.
The usual axioms of arithmetic can do this along any list that stops before $\varepsilon_0$.
The trick is a "jump": induction along a list of length $\alpha$ gives induction along a list of length $\omega^\alpha$.
Jumping again and again, we reach $\omega$, $\omega^\omega$, $\omega^{\omega^\omega}$, and so on, but never $\varepsilon_0$ itself.

### L2 human

How does PA get $\operatorname{TI}(\omega^\omega, \varphi)$ for a formula $\varphi$?
Ordinary induction gives $\operatorname{TI}(\omega, \psi)$ for every formula $\psi$, since the notations below $\omega$ are the natural numbers.
Apply this to $\psi = \varphi^+$, the jump of $\varphi$, to get $\operatorname{TI}(\omega, \varphi^+)$.
One more step gives $\operatorname{TI}(\omega + 1, \varphi^+)$, and the jump lemma turns this into $\operatorname{TI}(\omega^\omega, \varphi)$.
To reach $\omega^{\omega^\omega}$, start from $\operatorname{TI}(\omega, \varphi^{++})$; each new level of the tower costs one more jump.
This is the typical use: inside PA, show that a function defined by recursion along an ordinal below $\varepsilon_0$ is total.
Watch out: PA proves each instance $\operatorname{TI}(a, \varphi)$, but not the single sentence "for all $a$, $\operatorname{TI}(a, \varphi)$".

### L3 human

The theorem and Gentzen's consistency proof together give the first [[ordinal analysis|C5E5TG8PGP]]: $\varepsilon_0$ is the least ordinal that PA cannot reach by transfinite induction.
The jump $\varphi \mapsto \varphi^+$ is a proof-theoretic form of ordinal exponentiation, and it trades one level of formula complexity for one level of the tower.
This trade explains the ordinals of the fragments of PA with restricted induction.
The same pattern returns in second-order arithmetic, where $\mathrm{ACA}_0$ is the theory that proves that $X \mapsto \omega^X$ preserves well-orders.
