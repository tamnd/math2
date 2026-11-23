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

The sentence "some number is in the set" cannot be written as a propositional formula, because a set can hide its only element beyond every variable of the formula.
Let $\alpha$ be a new unary relation symbol, and let $E := \exists y \, \alpha(y)$.
The sentence $E$ is closed, but its quantifier has no bound, so $E$ is not a [[$\Delta_0(\alpha)$ formula|GE43CSZTS9]].
We show that $E$ has no [[Paris-Wilkie translation|ZVD982MVST]], and that no propositional formula can serve as one.

1. The clauses of the translation cover atoms, connectives and bounded quantifiers.
   No clause applies to $\exists y$ without a bound.
2. The obvious extension would be the disjunction $p_0 \lor p_1 \lor p_2 \lor \cdots$ over all natural numbers.
   It has infinitely many disjuncts, so it is not a propositional formula.
3. Suppose that a propositional formula $\varphi$ expressed $E$.
   That is, for every $X \subseteq \mathbb{N}$, the formula $\varphi$ is true under the assignment of $X$ if and only if $E$ holds with $\alpha$ read as $X$.
4. The formula $\varphi$ has finitely many variables, so we can choose $m$ larger than every index of a variable in $\varphi$.
5. The sets $X_1 = \emptyset$ and $X_2 = \{m\}$ agree on every variable of $\varphi$, so $\varphi$ has the same truth value under both.
6. But $E$ is false for $X_1$ and true for $X_2$.
   This contradicts step 3, so no such $\varphi$ exists.

## Remarks

The example shows why the translation is defined only for bounded formulas: the truth of a bounded formula depends on finitely many values of $\alpha$.
With a bound, the sentence $(\exists y \le n)\, \alpha(y)$ translates to $p_0 \lor \dots \lor p_n$, and the argument breaks at step 6.
For $m > n$ both $X_1$ and $X_2$ make the bounded sentence false, so there is no contradiction.
The same argument applies to every sentence of the [[arithmetical hierarchy|7CVJCQKY41]] whose truth depends on infinitely many values of $\alpha$.

Watch out: do not reject $\forall x \, (\exists y \le x)\, \alpha(y)$ for the same reason.
Its outer quantifier is unbounded, but the translation is applied to each instance at $x = n$, and the family $p_0 \lor \dots \lor p_n$ of these translations is the object of study.

## Explanations

### L1 human

The statement "some number is in the set" speaks about all numbers.
To check it, you may need to look arbitrarily far.
A formula of propositional logic has only finitely many switches, so it looks only at finitely many numbers.
A set that contains only one very large number fools every such formula.

### L2 human

We test a candidate translation and watch it fail.
Take the candidate $\varphi = p_0 \lor p_1 \lor \dots \lor p_{99}$, and the set $X = \{100\}$.
Then $E$ is true, since $100 \in X$.
But every variable $p_0, \dots, p_{99}$ is false under $X$, so $\varphi$ is false.
So $\varphi$ does not express $E$, and the same happens for every finite candidate, with a number beyond its largest index in place of $100$.
The problem shows the typical use: before you apply the Paris-Wilkie theorem, check that every quantifier inside the instance is bounded.
