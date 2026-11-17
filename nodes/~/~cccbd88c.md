---
tag: ~cccbd88c
kind: example
name: The definition of an injective function in logical form
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
instance_of: [~5a296a2e]
uses: [~5a296a2e, 09NWETVTNY, 0GHS47PDAQ, 05SZQKH75K, 0P3A06QNDP]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_function
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

We translate the definition "a function $f \colon X \to Y$ is injective if different inputs give different outputs" into a formula, with the method of [[translating statements into logical form|~5a296a2e]], and then we negate it.

1. Dictionary. The domain of the variables $a$ and $b$ is $X$, and $f$ is a fixed function. We use the equality predicate on $X$ and on $Y$.
2. Hidden quantifiers. "Different inputs" means any two inputs $a$ and $b$, so the sentence is about all pairs: $\forall a \in X \; \forall b \in X$.
3. Connective. "Different inputs give different outputs" means "if $a \neq b$, then $f(a) \neq f(b)$".
4. Formula: $\forall a \in X \; \forall b \in X \; \bigl( a \neq b \to f(a) \neq f(b) \bigr)$.
5. Equivalent form, by the contrapositive $p \to q \equiv \neg q \to \neg p$: $\forall a \in X \; \forall b \in X \; \bigl( f(a) = f(b) \to a = b \bigr)$. This is the usual form of the definition of an [[injective function|09NWETVTNY]].
6. Negation, by the [[negation of a universal statement|0P3A06QNDP]] twice and $\neg (p \to q) \equiv p \land \neg q$: $\exists a \in X \; \exists b \in X \; \bigl( f(a) = f(b) \land a \neq b \bigr)$.
7. Test on $f(x) = x^2$ on $\mathbb{R}$: $a = 1$ and $b = -1$ give $f(a) = f(b) = 1$ and $a \neq b$. So the negation holds, and $f$ is not injective.
8. Test on $g(x) = 2x + 1$ on $\mathbb{R}$: if $2a + 1 = 2b + 1$, then $a = b$. So the formula of step 5 holds, and $g$ is injective.

## Remarks

The example shows the three typical hidden parts of a definition: the universal quantifiers on the variables, the implication inside, and the domain of each variable.
The domain changes the truth value: $x^2$ on $[0, \infty)$ is injective, since $a^2 = b^2$ with $a, b \geq 0$ gives $a = b$.
The form of step 5 is better for proofs, because it starts from an equation, and the form of step 6 tells what a counterexample must contain.
A definition written with "if" uses "if" in the sense of "if and only if", so "$f$ is injective" is equivalent to the formula, not only implied by it.

## Explanations

### L1 human

A function is injective when two different inputs never give the same output.
For example, "add $1$" is injective: $3$ gives $4$, $5$ gives $6$, and two different numbers always give two different answers.
"Square the number" is not injective: $2$ and $-2$ both give $4$.
To show that a function is not injective, it is enough to find two different inputs with the same output.

### L2 human

To translate a definition, do three things in order.

1. Find the letters that are not fixed. Each of them gets a quantifier, here $\forall a$ and $\forall b$.
2. Find the condition and the conclusion. Here the condition is $a \neq b$ and the conclusion is $f(a) \neq f(b)$.
3. Find the domain of each letter. Here it is $X$, the domain of $f$.

The typical use is to obtain the negation, which tells what to look for in a counterexample.
A trap is to write the negation in step 6 as $\exists a \, \exists b \, (f(a) = f(b) \to a \neq b)$.
This formula is true for every function with at least two inputs, because any pair with $a \neq b$ makes it true.
