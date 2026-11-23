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
We compute a [[prenex form|CS82V969DE]] of $\varphi$ and then check it by hand.

1. The bound variables $x$ and $y$ are different, and $\varphi$ has no [[free variables|9CNGDRAMGC]], so no renaming is needed.
2. The variable $x$ is not free in $\exists y \, Q(y)$.
   The antecedent rule $(\forall x \, \alpha) \to \beta \equiv \exists x \, (\alpha \to \beta)$ gives
   $$\varphi \equiv \exists x \, \big( P(x) \to \exists y \, Q(y) \big).$$
3. The variable $y$ is not free in $P(x)$.
   The consequent rule $\alpha \to \exists y \, \beta \equiv \exists y \, (\alpha \to \beta)$ gives
   $$\varphi \equiv \exists x \, \exists y \, \big( P(x) \to Q(y) \big).$$
4. The result has the prefix $\exists x \, \exists y$ and the quantifier-free matrix $P(x) \to Q(y)$, so it is prenex.

Now we check the equivalence directly in a structure $\mathcal{M}$ with a nonempty domain $M$.

5. Suppose $\varphi$ is true in $\mathcal{M}$.
   If some $a \in M$ is not in $P^{\mathcal{M}}$, take $x = a$ and any $y$; the implication holds because its antecedent is false.
   Otherwise $\forall x \, P(x)$ holds, so some $b$ is in $Q^{\mathcal{M}}$, and $y = b$ works with any $x$.
6. Conversely, suppose $P(a) \to Q(b)$ holds for some $a, b \in M$.
   If $\forall x \, P(x)$ holds, then $P(a)$ holds, so $Q(b)$ holds, and $\exists y \, Q(y)$ is true.
   So $\varphi$ is true.

So $\varphi$ and $\exists x \, \exists y \, (P(x) \to Q(y))$ are [[logically equivalent|0JMR2HM2N2]], as the [[prenex normal form theorem|ME9J33BFNC]] says.

## Remarks

The universal quantifier of $\varphi$ became existential, because it stood on the left of $\to$.
Moving $\exists y$ out first gives $\exists y \, \exists x \, (P(x) \to Q(y))$, another prenex form with the same prefix type.
Step 5 uses the nonempty domain in the case where every $a$ is in $P^{\mathcal{M}}$: the witness for $x$ is then any element, and there must be one.

Change the consequent and the picture changes.
For $(\forall x \, P(x)) \to \forall y \, Q(y)$ the same two rules give $\exists x \, \forall y \, (P(x) \to Q(y))$, and the prefix type becomes $\exists \forall$.

## Explanations

### L1 human

The sentence says: "if everything has property $P$, then something has property $Q$".
It means the same as: "there are things $a$ and $b$ such that, if $a$ has $P$, then $b$ has $Q$".
To find $a$, pick a thing without $P$ if there is one, and otherwise pick anything.

### L2 human

We test both forms in the structure with domain $M = \{ 1, 2 \}$, $P = \{ 1, 2 \}$ and $Q = \emptyset$.
Here $\forall x \, P(x)$ is true and $\exists y \, Q(y)$ is false, so $\varphi$ is false.
For each pair $(a, b)$, $P(a)$ is true and $Q(b)$ is false, so $P(a) \to Q(b)$ is false, and the prenex form is false too.
Check: both forms agree, as they must.
The typical use of this example is to see why the quantifier changes in step 2.
Watch out for the guess $\forall x \, \exists y \, (P(x) \to Q(y))$, which keeps $\forall$.
With $M = \{ 1, 2 \}$, $P = \{ 1 \}$ and $Q = \emptyset$, $\varphi$ is true because its antecedent fails, but the guess fails at $x = 1$.
