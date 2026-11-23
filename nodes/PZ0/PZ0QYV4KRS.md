---
tag: PZ0QYV4KRS
kind: example
name: A derivation of 0 + x = x in primitive recursive arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [WCXH72T8D8]
uses: [WCXH72T8D8, 330YAP9Y4Q, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: Language and axioms
  - book: isbn:9780521857840
---

## Example

Addition is defined by recursion on the right argument, so $x + 0 = x$ is an axiom but $0 + x = x$ must be proved.
We work in [[primitive recursive arithmetic|WCXH72T8D8]], where the defining equations of $+$ in the [[definition|330YAP9Y4Q]] give the two theorems
$$x + 0 = x \qquad \text{and} \qquad x + Sy = S(x + y).$$
We derive $0 + x = x$ with $x$ free.
Let $\varphi(x)$ be the quantifier-free formula $0 + x = x$.

1. The base case $\varphi(0)$ is $0 + 0 = 0$.
   It is the equation $x + 0 = x$ with the term $0$ for $x$, by the substitution rule.
2. The equation $x + Sy = S(x + y)$ with $0$ for $x$ and then $x$ for $y$ gives $0 + Sx = S(0 + x)$, by the substitution rule twice.
3. The equality axiom for $S$ gives $0 + x = x \to S(0 + x) = Sx$.
4. Steps 2 and 3, with the transitivity of equality and propositional logic, give $0 + x = x \to 0 + Sx = Sx$.
5. Step 4 is the formula $\varphi(x) \to \varphi(Sx)$.
   The induction rule, applied to steps 1 and 5, gives $\varphi(x)$, that is, $0 + x = x$.

So $0 + x = x$ is a theorem of $\mathsf{PRA}$, and by soundness it holds in $\mathfrak{N}$ for every value of $x$.

## Remarks

The derivation uses the induction rule once, on an atomic formula, and no quantifiers at all.
In [[Robinson arithmetic|3K1AKGXF8A]] the same formula is not a theorem, because $\mathsf{Q}$ has no induction.
$\mathsf{Q}$ proves each instance $0 + \overline{n} = \overline{n}$, but a nonstandard model of $\mathsf{Q}$ falsifies $\forall x \, (0 + x = x)$.

The same method continues.
Induction on $x$ gives $Sy + x = S(y + x)$, and then induction on $y$ gives $x + y = y + x$, with $0 + x = x$ as the base case.
Each of these is an equation, so the laws of a commutative semiring all live inside $\mathsf{PRA}$.

If we define $+$ by recursion on the left argument instead, the roles swap.
Then $0 + x = x$ is an axiom, and $x + 0 = x$ needs the induction.

## Explanations

### L1 human

The rule $x + 0 = x$ is part of the definition of addition, but the rule $0 + x = x$ is not.
We prove the second rule in two steps.
First, $0 + 0 = 0$ by the definition.
Second, if $0 + x = x$ for some $x$, then $0 + (x + 1) = (0 + x) + 1 = x + 1$.
For example, from $0 + 3 = 3$ we get $0 + 4 = 4$.
The induction rule then gives the law for every $x$.

### L2 human

We follow the step of the induction on the instance $x = \overline{2}$.
Suppose $0 + SS0 = SS0$.
Step 2 with $SS0$ for $x$ gives
$$0 + SSS0 = S(0 + SS0),$$
and by the hypothesis and the equality axiom for $S$, the right side equals $SSS0$.
So $0 + SSS0 = SSS0$, which is $\varphi(\overline{3})$.

The typical use of such derivations is to build the algebra of $+$ and $\cdot$ before syntax is coded inside $\mathsf{PRA}$.
Watch out for the order of the lemmas.
If you try to prove $x + y = y + x$ by induction on $y$ first, the base case is $x + 0 = 0 + x$, which is exactly the law of this example.
