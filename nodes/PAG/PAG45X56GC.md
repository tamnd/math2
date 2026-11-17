---
tag: PAG45X56GC
kind: example
name: Negation is not expressible in the implicational calculus
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: ZMVBAY7ZZD
    note: the formula ¬p is not a formula of the implicational propositional calculus, and no formula with only → is logically equivalent to it, since every such formula is true when all its variables are true
uses: [ZMVBAY7ZZD, 029JBBF693, 0NMG7W7Q11, EDRV3N0SA3, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Functional (in)completeness
---

## Example

Let $p$ be a propositional variable.
We show that no formula $\varphi$ built from propositional variables with $\to$ only is [[logically equivalent|0JMR2HM2N2]] to the [[negation|029JBBF693]] $\neg p$.
So $\neg p$ is not expressible in the [[implicational propositional calculus|ZMVBAY7ZZD]].
Let $v_1$ be the truth assignment that gives every variable the value $1$.
We prove by [[induction on formulas|EDRV3N0SA3]] that $v_1(\varphi) = 1$ for every formula $\varphi$ with only $\to$.

1. Base case: if $\varphi$ is a variable, then $v_1(\varphi) = 1$ by the definition of $v_1$.
2. Step: if $\varphi = \alpha \to \beta$ and $v_1(\beta) = 1$ by the induction hypothesis, then $v_1(\varphi) = v_1(\alpha) \to 1 = 1$ by the truth table of [[implication|0NMG7W7Q11]].
3. So $v_1(\varphi) = 1$ for every formula with only $\to$.
4. But $v_1(\neg p) = \neg 1 = 0$.
5. So $\varphi$ and $\neg p$ take different values under $v_1$, and they are not logically equivalent.

## Remarks

The example shows that implication alone is not functionally complete.
The same argument rules out every formula that is false when all variables are true, such as $\neg p \lor \neg q$ or the constant false.
A sharper argument also rules out $p \land q$, which is true when $p$ and $q$ are true.
Every formula with only $\to$ is true when its rightmost variable is true, but $p \land q$ is false at $p = 1, q = 0$ and at $p = 0, q = 1$.
If a constant $\bot$ for false is added to the language, the argument fails at the base case, and indeed $\neg p$ becomes expressible as $p \to \bot$.
The Peirce's law axiom does not change this: it adds theorems, not expressive power.

## Explanations

### L1 human

Imagine that every basic statement is true.
Then every "if ... then" sentence built from them is true too, since "if ... then (something true)" is always true.
But "not $p$" is false in this situation.
So no sentence made only with "if ... then" can mean "not $p$".

### L2 human

We test the candidate $\varphi = (p \to q) \to p$, hoping that it means $\neg p$.

1. Under $v(p) = 1$, $v(q) = 1$: $v(p \to q) = 1$, so $v(\varphi) = 1 \to 1 = 1$.
2. Under the same assignment, $v(\neg p) = 0$.
3. So $\varphi$ is not equivalent to $\neg p$, as the general argument predicts.

The typical use of the argument is to prove that a set of connectives is not functionally complete.
For this, find a property of truth values that every connective in the set preserves.
A trap is to test only one or two candidate formulas; the induction is needed to cover all formulas at once.
