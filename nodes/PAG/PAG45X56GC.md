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

When every letter is true, every formula built with "if ... then" is true, so no such formula can mean "not $p$".
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

### What the example shows

Implication alone is not functionally complete.
The same argument rules out every formula that is false when all variables are true, such as $\neg p \lor \neg q$ or the constant false.

### A sharper argument for conjunction

The formula $p \land q$ is true when $p$ and $q$ are true, so the argument above does not rule it out.
A sharper one does: every formula with only $\to$ is true when its rightmost variable is true.
Let $r$ be the rightmost variable of a formula $\varphi$ with only $\to$.
If $r$ is $p$, take $p = 1$ and $q = 0$; otherwise take $r = 1$ and $p = 0$.
In both cases $\varphi$ is true and $p \land q$ is false, so no formula with only $\to$ is equivalent to $p \land q$.

### What changes with a constant

If a constant $\bot$ for false is added to the language, the argument fails at the base case, and $\neg p$ becomes expressible as $p \to \bot$.
Peirce's law as an axiom does not change this: it adds theorems, not expressive power.

## Explanations

### L1 human

Imagine that every basic statement is true.
Then every "if ... then" sentence built from them is true too, since "if ... then (something true)" is always true.
But "not $p$" is false in this situation.
So no sentence made only with "if ... then" can mean "not $p$".

### L2 human

We test the candidate $\varphi = (p \to q) \to p$, hoping that it means $\neg p$.
Under $v(p) = 1$ and $v(q) = 1$ we get $v(p \to q) = 1$, so $v(\varphi) = 1 \to 1 = 1$.
Under the same assignment, $v(\neg p) = 0$.
So $\varphi$ is not equivalent to $\neg p$, as the general argument predicts.

The typical use of the argument is to prove that a set of connectives is not functionally complete.
For this, find a property of truth values that every connective in the set preserves.
Watch out: testing one or two candidate formulas proves nothing, and the induction is needed to cover all formulas at once.
