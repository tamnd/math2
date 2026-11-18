---
tag: FWW3GSKV70
kind: example
name: An unbounded existential formula has no Paris-Wilkie translation
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
not_instance_of:
  - target: ZVD982MVST
    note: the quantifier in the formula has no bound, and no propositional formula expresses its truth value
uses: [ZVD982MVST, GE43CSZTS9, 7CVJCQKY41]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Correspondence to propositional proof systems
  - url: https://en.wikipedia.org/wiki/Arithmetic_hierarchy
    locator: lead section
---

## Example

Let $\alpha$ be a new unary relation symbol, and let $E := \exists y \, \alpha(y)$.
The sentence $E$ is closed, but its quantifier has no bound, so $E$ is not a [[$\Delta_0(\alpha)$ formula|GE43CSZTS9]].
We show that $E$ has no [[Paris-Wilkie translation|ZVD982MVST]], and that no propositional formula can serve as one.

1. The clauses of the translation cover atoms, connectives and bounded quantifiers. No clause applies to $\exists y$ without a bound.
2. The obvious extension would be the disjunction $p_0 \lor p_1 \lor p_2 \lor \cdots$ over all $i \in \N$. It has infinitely many disjuncts, so it is not a propositional formula.
3. Suppose a propositional formula $\varphi$ expressed $E$: for every $X \subseteq \N$, $\varphi$ is true under the assignment of $X$ if and only if $E$ holds with $\alpha$ read as $X$.
4. The formula $\varphi$ has finitely many variables. Let $m$ be larger than every index of a variable in $\varphi$.
5. The sets $X_1 = \emptyset$ and $X_2 = \set{m}$ agree on every variable of $\varphi$, so $\varphi$ has the same truth value under both.
6. $E$ is false for $X_1$ and true for $X_2$. This contradicts step 3, so no such $\varphi$ exists.

## Remarks

The example shows why the translation is defined only for bounded formulas: the truth of a bounded formula depends on finitely many values of $\alpha$.
With a bound, the sentence $(\exists y \le n)\, \alpha(y)$ translates to $p_0 \lor \dots \lor p_n$, and step 5 fails because $m$ would exceed $n$.
The same argument applies to every sentence of the [[arithmetical hierarchy|7CVJCQKY41]] whose truth depends on infinitely many values of $\alpha$.
This is one reason why the theories with a propositional translation, such as $\mathsf{I}\Delta_0(\alpha)$ and $T_2(\alpha)$, have induction only for bounded formulas.

## Explanations

### L1 human

The statement "some number is in the set" speaks about all numbers.
To check it, one may need to look arbitrarily far.
A formula of propositional logic has only finitely many switches, so it looks only at finitely many numbers.
A set that contains only one very large number fools every such formula.

### L2 human

We test a candidate translation and watch it fail.

1. Candidate: $\varphi = p_0 \lor p_1 \lor \dots \lor p_{99}$.
2. Take $X = \set{100}$. Then $E$ is true, since $100 \in X$.
3. Every variable $p_0, \dots, p_{99}$ is false under $X$, so $\varphi$ is false.
4. So $\varphi$ does not express $E$, and the same happens for every finite candidate with a larger number in place of $100$.

The typical use is as a test: before one applies the Paris-Wilkie theorem, one checks that every quantifier of the formula is bounded.
A trap is to reject $\forall x \, (\exists y \le x)\, \alpha(y)$ as well: its matrix is bounded, so each instance at $x = n$ has a translation, and the family of these translations is the object of study.
