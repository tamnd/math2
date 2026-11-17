---
tag: ZVR8TNBHNH
kind: example
name: Prenex form of an implication between quantified formulas
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [CS82V969DE]
uses: [CS82V969DE, ME9J33BFNC, 0JMR2HM2N2, 9CNGDRAMGC]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Conversion to prenex form
---

## Example

Let $P$ and $Q$ be unary relation symbols, and let
$$\varphi = (\forall x \, P(x)) \to \exists y \, Q(y).$$
We compute a [[prenex form|CS82V969DE]] of $\varphi$ and check it.

1. The bound variables $x$ and $y$ are distinct, and $\varphi$ has no free variables. So no renaming is needed.
2. The variable $x$ is not free in $\exists y \, Q(y)$. The rule $(\forall x \, \alpha) \to \beta \equiv \exists x \, (\alpha \to \beta)$ gives $\varphi \equiv \exists x \, (P(x) \to \exists y \, Q(y))$.
3. The variable $y$ is not free in $P(x)$. The rule $\alpha \to \exists y \, \beta \equiv \exists y \, (\alpha \to \beta)$ gives $\varphi \equiv \exists x \, \exists y \, (P(x) \to Q(y))$.
4. The result has the prefix $\exists x \, \exists y$ and the quantifier-free matrix $P(x) \to Q(y)$. So it is prenex.
5. Direct check in a structure $\mathcal{M}$ with a nonempty domain $M$. Suppose that $\varphi$ is true. If some $a \in M$ is not in $P^{\mathcal{M}}$, take $x = a$ and any $y$. Otherwise $\forall x \, P(x)$ holds, so some $b$ is in $Q^{\mathcal{M}}$, and $y = b$ works.
6. Conversely, suppose that $P(a) \to Q(b)$ holds for some $a, b \in M$. If $\forall x \, P(x)$ holds, then $P(a)$ holds, so $Q(b)$ holds, and $\exists y \, Q(y)$ is true. So $\varphi$ is true.

So $\varphi$ and $\exists x \, \exists y \, (P(x) \to Q(y))$ are [[logically equivalent|0JMR2HM2N2]], as the [[prenex normal form theorem|ME9J33BFNC]] says.

## Remarks

The universal quantifier of $\varphi$ became an existential one, because it stood on the left of $\to$.
Moving $\exists y$ out first gives $\exists y \, \exists x \, (P(x) \to Q(y))$, another prenex form with the same prefix type.
Step 5 uses the nonempty domain: when every $a$ is in $P^{\mathcal{M}}$, the witness $x$ is any element.
In an empty structure both formulas would be false, but for other formulas the rules of step 2 fail there.

## Explanations

### L1 human

The sentence says: "if everything has property $P$, then something has property $Q$".
It is the same as: "there are things $a$ and $b$ such that if $a$ has $P$, then $b$ has $Q$".
To find $a$, pick a thing without $P$ if there is one, and otherwise pick anything.

### L2 human

We test the two forms in the structure with $M = \set{1, 2}$, $P = \set{1, 2}$ and $Q = \emptyset$.

1. $\forall x \, P(x)$ is true and $\exists y \, Q(y)$ is false, so $\varphi$ is false.
2. For each pair $(a, b)$, $P(a)$ is true and $Q(b)$ is false, so $P(a) \to Q(b)$ is false.
3. So $\exists x \, \exists y \, (P(x) \to Q(y))$ is false too, as it must be.

The typical use is to see the role of the dual quantifier in step 2 of the example.
A trap: the guess $\forall x \, \exists y \, (P(x) \to Q(y))$ is not equivalent.
With $M = \set{1, 2}$, $P = \set{1}$ and $Q = \emptyset$, $\varphi$ is true but the guess fails at $x = 1$.
