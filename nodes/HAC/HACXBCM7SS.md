---
tag: HACXBCM7SS
kind: concept
name: Peano arithmetic
aliases: [first-order-peano-arithmetic]
msc: ["03F30", "03H15"]
topics: [QHCRN4JVG0]
audience: grad
uses: [D8SD54M5PN, 3K1AKGXF8A, 1QD0KDDGYJ, 0QFT7Z76N5, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9781482237726
  - url: https://builds.openlogicproject.org/
    locator: Models of Arithmetic
---

## Summary

Peano arithmetic is what you get when you give [[Robinson arithmetic|3K1AKGXF8A]] the power to prove general laws by induction.
Here is the smallest case.
Robinson arithmetic $\mathsf{Q}$ proves $0 + \overline{n} = \overline{n}$ for each numeral $\overline{n}$, one at a time, but it cannot prove the general law $\forall x\,(0 + x = x)$.
Peano arithmetic proves that law with one induction: the base is $0 + 0 = 0$, and the step turns $0 + x = x$ into $0 + S x = S(0 + x) = S x$.

Exactly, Peano arithmetic $\mathsf{PA}$ is the first-order [[theory|92SWXST1ZM]] in the [[language of arithmetic|D8SD54M5PN]] whose axioms are the axioms of $\mathsf{Q}$ together with the [[induction schema|1QD0KDDGYJ]], one induction axiom for every formula.
The [[definition|Z8YDBW2857]] writes the axioms out.

## Motivation

Mathematicians prove laws about all numbers by [[induction|0ASJVEFA9J]].
Induction speaks about every property of numbers, and a first-order theory cannot quantify over properties.
So $\mathsf{PA}$ takes one induction axiom for each property that a formula can express.
The result formalizes nearly all of elementary number theory, from commutativity of addition to unique factorization and the infinitude of primes.

Because $\mathsf{PA}$ is first-order, it has a complete proof system, and it also has non-standard models and true sentences that it cannot prove.
That mix makes $\mathsf{PA}$ the standard test case of logic.
Hilbert asked whether arithmetic can prove its own consistency, and Gödel answered the question for $\mathsf{PA}$.
The later pages on the [[fragments of PA|T70PYM1F36]] and on [[finite axiomatizability|M5WNB181T7]] cut $\mathsf{PA}$ into layers by the complexity of induction.

## Notation

Books write $\mathsf{PA}$ or $\mathrm{PA}$.
The induction axiom for a formula $\varphi(x, \vec{y})$ is $\mathrm{Ind}_\varphi$.
For a class $\Gamma$ of formulas, $\mathsf{I}\Gamma$ is $\mathsf{Q}$ plus $\mathrm{Ind}_\varphi$ for each $\varphi \in \Gamma$, so $\mathsf{PA}$ is $\mathsf{I}\Gamma$ for the class of all formulas.
Some books write $x'$ for $S x$, and some leave out $<$ and define it, which gives the same theory.
We write $\mathfrak{N}$ for the standard model and $\mathfrak{M}$ for an arbitrary model of $\mathsf{PA}$.

## Remarks

### A first proof by induction

Let us prove $\forall x\,(0 + x = x)$ in full, with $\varphi(x)$ the formula $0 + x = x$.
The base $\varphi(0)$ is $0 + 0 = 0$, an instance of axiom $\mathsf{Q}4$.
For the step, assume $0 + x = x$ and compute with $\mathsf{Q}5$:
$$0 + S x = S(0 + x) = S x.$$
So $\forall x\,(\varphi(x) \to \varphi(S x))$ holds, and the axiom $\mathrm{Ind}_\varphi$ gives $\forall x\, \varphi(x)$.
Check: in [[a model of Q|PR8Z1YPJDK]] with two extra elements $a$ and $b$, $0 + a = b$, so $\mathsf{Q}$ alone cannot prove this law.

The same pattern, with lemmas feeding later inductions, proves that [[addition is commutative|DE8YZ5SDH3]], and one induction proves that [[no number is its own successor|855J8368AM]].

### What Peano arithmetic proves

Inside $\mathsf{PA}$ you can prove that $+$ and $\cdot$ are associative and commutative, that $\cdot$ distributes over $+$, and that $<$ is a discrete linear order with least element $0$.
You can prove the least number principle and strong induction for every formula, and division with remainder.
With the [[β-function lemma|BM6P0C2AC2]] you can code finite sequences, so you can define exponentiation and the factorial and prove their recursion equations.
Since $\mathsf{PA}$ contains $\mathsf{Q}$, it proves every true $\Sigma_1$ sentence, by [[Σ1-completeness|69234Z1V00]].
The [[standard model|MPSCREYC3M]] satisfies every axiom, since each induction axiom speaks about a subset of $\mathbb{N}$, and ordinary induction holds for every subset.

### What Peano arithmetic cannot prove

If $\mathsf{PA}$ is consistent, then it does not prove its own consistency statement $\mathrm{Con}(\mathsf{PA})$, by Gödel's [[incompleteness theorems|X9WYNYE29C]].
Gentzen proved $\mathrm{Con}(\mathsf{PA})$ in a weak theory with induction along the ordinal [[ε0|KT50SMH3EC]]; see [[Gentzen's consistency proof|QPV0HNP22S]].
There are also statements of ordinary combinatorics that are true and unprovable in $\mathsf{PA}$.
Two of them are [[Goodstein's theorem|XQMNJF241J]] and the [[Paris-Harrington principle|509ZWA0R26]], both $\Pi_2$ sentences.

### Models

$\mathsf{PA}$ has models of every infinite cardinality, by compactness and the Löwenheim-Skolem theorem.
A model that is not isomorphic to $\mathfrak{N}$ is a [[non-standard model of arithmetic|1QWN5CV4CG]].
Every such model starts with a copy of $\mathfrak{N}$ as an initial segment, and then has elements above every numeral.
By [[Tennenbaum's theorem|W6D5ZJAY9D]], in a countable non-standard model the operations $+$ and $\cdot$ are not computable.

### What it is not

The second-order Peano axioms are not $\mathsf{PA}$.
Their single induction axiom quantifies over all subsets, and every model of them is isomorphic to $\mathfrak{N}$.
The first-order schema covers only the sets that a formula defines, and [[the compactness argument|Y2S28SPR3R]] gives a model of $\mathsf{PA}$ that is not standard.
Nor is $\mathsf{PA}$ the set of all true sentences: that set is [[true arithmetic|DX0KPMH4QZ]], which is not recursively axiomatizable, while the axioms of $\mathsf{PA}$ form a decidable set.

### Watch out

A non-standard model does not break induction.
Let $A$ be the set of standard elements of a non-standard model $\mathfrak{M}$.
Then $0 \in A$ and $A$ is closed under $S$, but $A \ne M$.
This is no contradiction, because no formula defines $A$ in $\mathfrak{M}$, so no induction axiom speaks about $A$.
The wrong move is to apply an induction axiom to a set that you have described in words outside the language.

### History

Dedekind in 1888 and Peano in 1889 gave axioms for the natural numbers, with induction as a statement about all sets.
Gödel's theorems of 1931 apply to $\mathsf{PA}$, so it is incomplete and cannot prove its own consistency.
Skolem built a non-standard model of first-order arithmetic in 1934.
Gentzen proved the consistency of $\mathsf{PA}$ by transfinite induction up to $\varepsilon_0$ in 1936.

### Try it

First, which axiom of $\mathsf{Q}$ becomes unnecessary in $\mathsf{PA}$?
Axiom $\mathsf{Q}3$, "every nonzero number is a successor", follows by induction on $x = 0 \lor \exists y\,(x = S y)$, as [[this example|855J8368AM]] shows.

Second, write the induction axiom you need to prove $\forall x\,(x \cdot 0 = 0 \cdot x)$.
Take $\varphi(x)$ to be $0 \cdot x = 0$; the base is $\mathsf{Q}6$, and the step is $0 \cdot S x = 0 \cdot x + 0 = 0$ by $\mathsf{Q}7$, $\mathsf{Q}4$ and the hypothesis, and $\mathsf{Q}6$ gives $x \cdot 0 = 0$.

## Explanations

### L1 human

Peano arithmetic is a list of rules for the whole numbers.
It has the rules of Robinson arithmetic for "next", plus and times.
It adds the rule of induction: if a property holds for $0$, and it passes from each number to the next, then it holds for all numbers.
With induction it proves general laws, such as $x + y = y + x$ for all $x$ and $y$.
Gödel showed that some true statements about numbers still escape these rules.

### L2 human

We prove in $\mathsf{PA}$ that every number is even or odd.
Let $\varphi(x)$ be the $\Sigma_1$ formula $\exists y\,(x = y + y \lor x = S(y + y))$.
For the base, $y = 0$ works, since $0 + 0 = 0$ by $\mathsf{Q}4$.
For the step, assume $\varphi(x)$ with witness $y$.
If $x = y + y$, then $S x = S(y + y)$, and the same $y$ is a witness for $\varphi(S x)$.
If $x = S(y + y)$, the witness is $S y$, because $\mathsf{Q}5$ and [[Lemma B of the commutativity proof|DE8YZ5SDH3]] give
$$S y + S y = S(S y + y) = S(S(y + y)) = S x.$$
So $\varphi(x) \to \varphi(S x)$, and $\mathrm{Ind}_\varphi$ gives $\forall x\, \varphi(x)$.

The example shows the typical shape of number theory in $\mathsf{PA}$: an induction whose step calls on earlier lemmas.
The trap is the identity $S y + y = S(y + y)$, which looks like an axiom but needs an induction of its own.

### L3 human

$\mathsf{PA}$ is the union of the increasing chain of theories $\mathsf{I}\Sigma_n$, the [[fragments of PA|T70PYM1F36]].
Each $\mathsf{I}\Sigma_n$ with $n \ge 1$ is finitely axiomatizable, and $\mathsf{PA}$ proves the consistency of each one, so $\mathsf{PA}$ is [[not finitely axiomatizable|M5WNB181T7]].
The provably total recursive functions of $\mathsf{PA}$ are those computable by recursion along ordinals below $\varepsilon_0$.
$\mathsf{PA}$ and set theory with the axiom of infinity replaced by its negation interpret each other, so $\mathsf{PA}$ is a theory of finite mathematics in general.
The order type of every countable non-standard model is $\omega + \zeta \cdot \eta$, where $\zeta$ is the order type of $\mathbb{Z}$ and $\eta$ that of $\mathbb{Q}$.
The [[incompleteness theorems|X9WYNYE29C]] and the independence results of [[Goodstein|XQMNJF241J]] and Paris and Harrington take $\mathsf{PA}$ as their main example.
