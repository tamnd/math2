---
tag: GE43CSZTS9
kind: concept
name: Δ0, Σn and Πn formulas
aliases: [arithmetical-formula-classes, bounded-formulas, sigma-n-formulas, pi-n-formulas]
msc: ["03F30", "03D55"]
topics: [QHCRN4JVG0]
audience: grad
uses: [D8SD54M5PN, HYJ10AF6RT, CS82V969DE, 7CVJCQKY41, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: The arithmetical hierarchy of formulas
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: Arithmetization of Syntax
---

## Summary

The classes $\Delta_0$, $\Sigma_n$ and $\Pi_n$ sort the formulas of arithmetic by how much searching it takes to check them.
Take the formula that says "$x$ is prime":
$$\mathrm{Prime}(x) := \overline{1} < x \land \forall y \le x\; \forall z \le x\; \bigl(y \cdot z = x \to (y = \overline{1} \lor z = \overline{1})\bigr).$$
Every quantifier in it is bounded by $x$, so for $x = 7$ you check the $64$ pairs $(y, z)$ with $y, z \le 7$ and stop.
Such a formula is $\Delta_0$.

Exactly, a [[formula|HYJ10AF6RT]] of the [[language of arithmetic|D8SD54M5PN]] is $\Delta_0$ when all its quantifiers are bounded, of the form $\forall x < t$ or $\exists x < t$.
A $\Sigma_n$ formula is a block of $n$ alternating unbounded quantifiers, starting with $\exists$, in front of a $\Delta_0$ formula, and a $\Pi_n$ formula is the same with $\forall$ first.
The [[definition|Y0JTZXBRT5]] gives the exact clauses, which also allow each block to have several quantifiers of the same kind.

## Motivation

The classes measure how hard it is to check a formula in the standard model $\mathfrak{N}$.
A $\Delta_0$ sentence is checked by a finite search, since every quantifier ranges below a known number.
A true $\Sigma_1$ sentence is confirmed by a search that finds a witness, but for a false one the search never ends.
So $\Sigma_1$ sentences are those whose truth a finite computation can confirm, and $\Pi_1$ sentences are those whose falsity it can.

The same scale organizes provability and induction.
[[Robinson arithmetic|3K1AKGXF8A]] proves every true $\Sigma_1$ sentence, by [[Σ1-completeness|69234Z1V00]], but not every true $\Pi_1$ sentence.
The [[fragments|T70PYM1F36]] $\mathsf{I}\Sigma_n$ of [[Peano arithmetic|HACXBCM7SS]] allow induction only on $\Sigma_n$ formulas.
On the side of sets, the classes give the [[arithmetical hierarchy|7CVJCQKY41]].

## Notation

We put $\Sigma_0 = \Pi_0 = \Delta_0$.
We keep $\Sigma_n$ for the class of formulas and write $\Sigma^0_n$ for the class of sets that a $\Sigma_n$ formula defines in $\mathfrak{N}$; many books use $\Sigma^0_n$ for both.
A formula is $\Sigma_n$ in a theory $T$ when $T$ proves it equivalent to a $\Sigma_n$ formula, and $\Delta_n$ in $T$ when it is both $\Sigma_n$ and $\Pi_n$ in $T$.
"In $\mathfrak{N}$" means the same with truth in $\mathfrak{N}$ in place of provability in $T$.
Some books bound quantifiers by $\le$ and some by $<$, and the two choices give the same class $\Delta_0$ up to equivalence.

## Remarks

### Classifying sentences

Goldbach's conjecture says that every even number above $2$ is a sum of two primes.
The primes are at most the number, so after the first quantifier all quantifiers are bounded:
$$\forall x\,\bigl((\overline{2} < x \land \mathrm{Even}(x)) \to \exists p \le x\, \exists q \le x\,(\mathrm{Prime}(p) \land \mathrm{Prime}(q) \land p + q = x)\bigr).$$
One unbounded $\forall$ in front of a $\Delta_0$ formula makes it $\Pi_1$, as [[this example|HTTAH8PY38]] explains.
A counterexample, if one exists, is found by a finite check, which is what $\Pi_1$ means.

"There are infinitely many primes" is $\forall x\, \exists y\,(x < y \land \mathrm{Prime}(y))$.
Here the $\exists y$ is not bounded by anything in the formula, so the sentence is $\Pi_2$.

"$x$ is a square" is $\exists y\,(y \cdot y = x)$, which is $\Sigma_1$ as written.
Since $y \le y \cdot y$ for every $y \in \mathbb{N}$, it is equivalent in $\mathfrak{N}$ to the $\Delta_0$ formula $\exists y \le x\,(y \cdot y = x)$.

### Shapes that are not in the hierarchy as written

The formula $\forall u < y\, \exists z\, \theta(u, z, y)$, with $\theta$ in $\Delta_0$, has an unbounded quantifier inside a bounded one.
It lies in no class as written, but [[this non-example|HJEZHW1YQ2]] shows that it is $\Sigma_1$ in $\mathfrak{N}$, because finitely many witnesses have a common bound.

The formula $\exists x\, \delta_1 \land \forall y\, \delta_2$, with $\delta_1, \delta_2$ in $\Delta_0$, has quantifiers that are not in front.
If $y$ is not free in $\delta_1$ and $x$ is not free in $\delta_2$, its [[prenex form|CS82V969DE]] $\exists x\, \forall y\,(\delta_1 \land \delta_2)$ is $\Sigma_2$.

### The rules you can use

Every formula is logically equivalent to a prenex formula, and so to a $\Sigma_n$ or $\Pi_n$ formula for some $n$.
The negation of a $\Sigma_n$ formula is equivalent to a $\Pi_n$ formula, by pushing $\neg$ through the quantifiers.
Several existential quantifiers in a row can be [[merged into one|4WCR2JXT4S]] in $\mathfrak{N}$, with a bound $w$ on all the witnesses.
For $n \ge 1$, in $\mathfrak{N}$, $\Sigma_n$ is closed under $\land$, $\lor$, $\exists x$ and bounded quantifiers, up to equivalence, and $\Pi_n$ in the same way with $\forall x$.
Both $\Sigma_n$ and $\Pi_n$ lie inside $\Delta_{n+1}$, since a quantifier block may be empty.

### What the classes compute

A $\Delta_0$ formula defines a decidable relation on $\mathbb{N}$, by a finite search on the bounds.
A relation is defined in $\mathfrak{N}$ by a $\Sigma_1$ formula exactly when it is [[computably enumerable|TN9G24VABN]].
The search for a witness gives one direction, and the arithmetization of computations gives the other.
By [[Post's theorem|NYJX5QXX1T]], the sets $\Sigma^0_n$ form a strictly increasing chain.

### Watch out

Do not confuse the formula class with the set class.
The formula $\exists y\,(y \cdot y = x)$ is $\Sigma_1$ and not $\Delta_0$ by its shape, but the set of squares it defines is $\Delta^0_0$ as well, since a $\Delta_0$ formula also defines it.

Do not read "true $\Sigma_1$ sentence" as "provable": true means true in $\mathfrak{N}$.
And do not call a formula $\Sigma_1$ in a theory $T$ because it is equivalent to one in $\mathfrak{N}$.
The proof of that equivalence may use facts, such as the common bound of finitely many witnesses, that $T$ cannot prove.

### History

Kleene in 1943 and Mostowski in 1947 classified the arithmetical sets by quantifier prefixes.
Smullyan's rudimentary relations of 1961 and the later study of bounded arithmetic made the bounded formulas central.

### Try it

First, classify $\forall x\, \exists y\, \forall z\,(x \cdot z < y)$.
The prefix is $\forall \exists \forall$ in front of an atomic formula, so the formula is $\Pi_3$.

Second, the formula $\forall y \le x\,(y \mid x \to y = \overline{1} \lor \mathrm{Even}(y))$ says that $x$ is $0$ or a power of $2$.
Why is it $\Delta_0$?
The relations $\mid$ and $\mathrm{Even}$ are defined by bounded formulas, so every quantifier in the whole formula is bounded.

## Explanations

### L1 human

Some statements about numbers can be checked by looking at finitely many cases: "$91$ is prime" needs only a check of the numbers up to $91$.
Formulas of this kind are called $\Delta_0$.
A statement like "there is a number with property $P$" can be confirmed by finding one example, but a failed search never ends.
Such statements are $\Sigma_1$.
A statement like "every number has property $P$" can be refuted by one counterexample, and it is $\Pi_1$.
More alternations of "there is" and "for all" in front give the higher classes $\Sigma_2$, $\Pi_2$ and so on.

### L2 human

We classify the sentence $\forall x\, \exists y\,(x < y \land \mathrm{Prime}(y))$ step by step.
The formula $\mathrm{Prime}(y)$ is $\Delta_0$, since its quantifiers are bounded by $y$.
The atomic formula $x < y$ is $\Delta_0$, so the conjunction $x < y \land \mathrm{Prime}(y)$ is $\Delta_0$.
One unbounded $\exists y$ in front makes it $\Sigma_1$, and the $\forall x$ in front of that makes the sentence $\Pi_2$.
Check: with $x = 10$, the inner $\Sigma_1$ formula has the witness $y = 11$.
The typical use of the classification is to know which theorem applies, for example that $\mathsf{Q}$ proves every true $\Sigma_1$ sentence.
The trap is to count bounded quantifiers, since $\forall y \le x$ inside $\mathrm{Prime}$ does not raise the class.

### L3 human

The classes interact with theories in two ways.
First, every true $\Sigma_1$ sentence is provable in $\mathsf{Q}$, and a theory is $\Sigma_1$-sound when every $\Sigma_1$ sentence it proves is true.
Second, the schemas $\mathsf{I}\Sigma_n$ and $\mathsf{B}\Sigma_n$ decide which closure properties hold provably, and collection $\mathsf{B}\Sigma_n$ is the principle that pulls an unbounded quantifier out of a bounded one.
By the theorem of Matiyasevich, Robinson, Davis and Putnam, every $\Sigma_1$ formula is equivalent in $\mathfrak{N}$ to one of the form $\exists \vec{y}\,(p(\vec{x}, \vec{y}) = q(\vec{x}, \vec{y}))$ with polynomials $p$ and $q$.
So the $\Delta_0$ part can shrink to a single equation, at the price of more existential quantifiers.
The [[incompleteness theorems|X9WYNYE29C]] rest on the fact that provability is $\Sigma_1$.
