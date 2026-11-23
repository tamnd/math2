---
tag: ME9J33BFNC
kind: statement
role: theorem
name: Prenex normal form theorem
aliases: [prenex-normal-form-theorem]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
about: [CS82V969DE]
uses: [CS82V969DE, HYJ10AF6RT, 9CNGDRAMGC, 0JMR2HM2N2, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Conversion to prenex form
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Intuitionistic logic
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Statement

Every formula of classical first-order logic can be rewritten, without change of meaning, with all its quantifiers at the front.

Let $\sigma$ be a signature, and let every $\sigma$-structure have a nonempty domain.
For every $\sigma$-[[formula|HYJ10AF6RT]] $\varphi$ there is a $\sigma$-formula $\psi$ in [[prenex normal form|CS82V969DE]] such that:

1. $\psi$ is [[logically equivalent|0JMR2HM2N2]] to $\varphi$, that is, in every [[structure|983GZBQYT4]] and under every assignment, $\psi$ is true exactly when $\varphi$ is true;
2. $\psi$ has the same [[free variables|9CNGDRAMGC]] as $\varphi$, that is, $\operatorname{FV}(\psi) = \operatorname{FV}(\varphi)$;
3. $\psi$ is computed from $\varphi$ by an algorithm.

## Remarks

### Why each hypothesis is needed

The domains must be nonempty.
The proof uses $(\forall x \, \varphi) \to \chi \equiv \exists x \, (\varphi \to \chi)$ for $x$ not free in $\chi$.
In the empty structure, $(\forall x \, P(x)) \to \forall y \, (y = y)$ is true, since both sides are true, but $\exists x \, (P(x) \to \forall y \, (y = y))$ is false, since there is no $x$ at all.

The logic must be classical.
The proof uses $\neg \forall x \, \varphi \equiv \exists x \, \neg \varphi$, and that equivalence fails in [[intuitionistic logic|Q11N8X99FK]].
There, not every formula is equivalent to a prenex formula.

Equivalence is asked under every assignment, not only for sentences.
This is what lets the proof replace a subformula by an equivalent one inside a larger formula.

### What it gives you

Every formula has a prefix type, such as $\forall \exists \forall$, and this gives the classes $\Sigma_n$ and $\Pi_n$ of the [[arithmetical hierarchy|7CVJCQKY41]].
Every sentence has a [[Skolem normal form|GCPQGMJYEV]], by the [[Skolem normal form theorem|Q5H7C57VNH]] applied to a prenex form.
The matrix is quantifier-free, so propositional rules can put it into [[conjunctive normal form|0B3D4C8YF2]], which is the input format of resolution provers.

For a worked use, take $\neg \forall x \, P(x) \lor \exists x \, Q(x)$.
The negation rule turns it into $\exists x \, \neg P(x) \lor \exists x \, Q(x)$.
Rename the second bound variable to $y$, then pull out $\exists x$ and $\exists y$, since neither variable is free in the other disjunct:
$$\exists x \, \exists y \, \big( \neg P(x) \lor Q(y) \big).$$
The prefix type is $\exists \exists$, so the formula is $\Sigma_1$.

### The converse and uniqueness

The converse asks whether every prenex formula is a formula, and it is, by definition.
The interesting fact is that the prenex form is not unique.
For example, $\forall x \, P(x) \land \exists y \, Q(y)$ is equivalent to $\forall x \, \exists y \, (P(x) \land Q(y))$ and also to $\exists y \, \forall x \, (P(x) \land Q(y))$.

### Generalizations

The theorem holds in [[many-sorted logic|7TDHDN8P96]], with the same proof, when every sort has a nonempty domain.
Modulo a theory $T$ with quantifier elimination, every formula is $T$-equivalent to a quantifier-free formula, that is, to a prenex formula with an empty prefix.
The proof also gives a prenex form whose prefix variables are distinct from each other and from the free variables.

## History

Skolem used prenex formulas in his 1920 work on the Löwenheim-Skolem theorem.
Hilbert and Ackermann's textbook of 1928 presented the conversion to prenex form as a standard tool of the predicate calculus.

## Explanations

### L1 human

Every formula can be rewritten so that all the quantifiers stand at the front, and the new formula means the same in every situation.
For example, "if everyone is happy, then Ann is happy" becomes "there is someone such that, if that person is happy, then Ann is happy".
Both sentences are true in every situation with at least one person.
In the first, either someone is unhappy, or Ann is happy.
In the second, pick the unhappy person if there is one, and anyone otherwise.

### L2 human

We put $\varphi = \forall x \, P(x) \land \exists x \, Q(x, z)$ in prenex form and watch the free variable $z$.
Rename the second bound variable, since $x$ is bound twice:
$$\varphi \equiv \forall x \, P(x) \land \exists y \, Q(y, z).$$
Now $x$ is not free in $\exists y \, Q(y, z)$, so $\forall x$ moves out, and then $y$ is not free in $P(x)$, so $\exists y$ moves out:
$$\varphi \equiv \forall x \, \exists y \, \big( P(x) \land Q(y, z) \big).$$
Check: the free variables of both sides are $\{ z \}$, as part 2 of the theorem promises.
The typical use is to read off the prefix type, here $\forall \exists$.
Watch out for the shortcut of merging two quantifiers.
Merging is correct for $\exists$ over $\lor$, but $\exists x \, P(x) \land \exists x \, Q(x)$ is not $\exists x \, (P(x) \land Q(x))$, as an even number and an odd number show.

### L3 human

The theorem shows that classical first-order formulas are, up to equivalence, a quantifier prefix over a propositional matrix.
The prefix can be read as a game: the $\forall$ player and the $\exists$ player choose elements in turn, and the matrix decides who wins.
Skolem functions are the strategies of the $\exists$ player.
The number of alternations is the measure behind the arithmetical and polynomial hierarchies.
The prenex form given by the proof can be exponentially longer than $\varphi$, because each $\leftrightarrow$ is written out with two copies of each side.
Intuitionistically, the rules that move a quantifier out of an antecedent or out of a negation fail, so constructive logic has no prenex theorem.
