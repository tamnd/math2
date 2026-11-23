---
tag: XZF94M3GFF
kind: example
name: A formula that begins with a quantifier need not be prenex
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: CS82V969DE
    note: the quantifier exists y stands inside the scope of the implication, so the part after the first quantifier is not quantifier-free
uses: [CS82V969DE, 1NKD8P3PS0, ME9J33BFNC]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: lead section
---

## Example

Let $P$ be a unary and $R$ a binary relation symbol, and let
$$\varphi = \forall x \, \big( P(x) \to \exists y \, R(x, y) \big).$$
We check that $\varphi$ is not in [[prenex normal form|CS82V969DE]], and then we find a prenex form.

1. By the [[definition|1NKD8P3PS0]], a prenex formula is a string of quantifiers followed by a quantifier-free matrix.
2. The prefix of $\varphi$ can only be $\forall x$, because the next symbol is a bracket, not a quantifier.
3. What follows, $P(x) \to \exists y \, R(x, y)$, contains the quantifier $\exists y$.
   So it is not quantifier-free, and $\varphi$ is not prenex.
4. The variable $y$ is not free in $P(x)$, so the consequent rule gives
   $$P(x) \to \exists y \, R(x, y) \;\equiv\; \exists y \, \big( P(x) \to R(x, y) \big).$$
5. Hence $\varphi \equiv \forall x \, \exists y \, (P(x) \to R(x, y))$, which is prenex, as the [[prenex normal form theorem|ME9J33BFNC]] predicts.

So a leading quantifier does not make a formula prenex.

## Remarks

What matters is whether some quantifier sits under a connective.
The formula $\exists x \, P(x) \land \exists y \, Q(y)$ also starts with a quantifier, but $\exists y$ stands inside the conjunction.
Its prenex form is $\exists x \, \exists y \, (P(x) \land Q(y))$.
The formula $\neg \forall x \, P(x)$ fails for the opposite reason: its quantifier comes after a negation, so its prefix is empty.

Step 4 is safe here because $y$ does not occur in $P(x)$.
If the antecedent were $P(y)$, with $y$ free, you would first rename the bound $y$ to a fresh $z$ and get $\exists z \, (P(y) \to R(x, z))$.

## Explanations

### L1 human

"Every $x$ with property $P$ is related to some $y$" starts with "every", but a "some" sits inside the condition.
So not all the quantifiers are at the front.
Moving "some $y$" forward gives "for every $x$ there is a $y$ such that, if $P(x)$, then $R(x, y)$".

### L2 human

We check step 4 in a structure with a nonempty domain, for a fixed value of $x$.
If $P(x)$ is false, both sides are true: the left side because its antecedent is false, the right side because any $y$ works, and there is at least one.
If $P(x)$ is true, both sides say that some $y$ satisfies $R(x, y)$.
So the two sides agree in every case.
The typical use of this non-example is in exercises that ask for the prefix type of a formula.
Watch out: the prefix type of $\varphi$ is $\forall \exists$, not $\forall$, so $\varphi$ is a $\Pi_2$ formula and not a $\Pi_1$ formula.
