---
tag: CYG8CJ45BM
kind: example
name: Necessity of identity in quantified modal logic
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [D2H3S12V7X]
uses: [D2H3S12V7X, G989VP2NGP, HGR6C3KA34]
sources:
  - url: https://en.wikipedia.org/wiki/Ruth_Barcan_Marcus
    locator: Necessity of identity
  - url: https://en.wikipedia.org/wiki/Rigid_designator
    locator: Necessary identities
---

## Example

The formula of [[quantified modal logic|D2H3S12V7X]]
$$x = y \to \square (x = y)$$
says that objects which are identical are necessarily identical.
We show that it is valid on every Kripke frame with domains, and that it is derivable in $\mathsf{QK}$ with identity.

For the semantic check, let $\mathfrak{M} = (W, R, D, I)$ be any Kripke model with domains, let $w \in W$, and let $\sigma$ be any assignment.

1. Assume $\mathfrak{M}, w \models_\sigma x = y$.
   By the truth condition for identity, $\sigma(x) = \sigma(y)$.
2. Let $v$ be any world with $w R v$.
   The assignment $\sigma$ is the same at $v$ as at $w$, because assignments do not depend on worlds.
3. So $\sigma(x) = \sigma(y)$ still holds, and $\mathfrak{M}, v \models_\sigma x = y$.
4. Step 3 holds for every $v$ with $w R v$, so $\mathfrak{M}, w \models_\sigma \square (x = y)$.
5. Steps 1 to 4 hold for every $\mathfrak{M}$, $w$ and $\sigma$, so the formula is valid.

For the derivation, we use the identity axioms and the [[necessitation rule|G989VP2NGP]].

6. $x = x$ is an axiom of identity.
7. $\square (x = x)$ follows from step 6 by necessitation.
8. The substitution axiom $x = y \to (\varphi(x) \to \varphi(y))$ with $\varphi(z) = \square (x = z)$ gives $x = y \to (\square (x = x) \to \square (x = y))$.
9. From steps 7 and 8, propositional logic gives $x = y \to \square (x = y)$.

## Remarks

The example shows that identity between objects cannot be contingent in the standard semantics, because variables are rigid.
The same check with $\neq$ in place of $=$ shows that $x \neq y \to \square (x \neq y)$ is also valid.
That formula is not obtained by the derivation above, and many presentations derive it with the axiom B or add it as an axiom.

What changes if we allow constants that denote different objects at different worlds?
Then step 2 fails for the constants, and so does the formula, as [[a non-rigid name breaks the necessity of identity|CWGY8F92MH]] shows.
A name that keeps its object at every world is a [[rigid designator|HGR6C3KA34]].
The derivation in steps 6 to 9 goes back to Ruth Barcan Marcus, whose 1947 paper proved the necessity of identity in her system.

## Explanations

### L1 human

If two labels stand for the same thing, there is only one object.
An object is equal to itself in every possible world.
So if $x$ and $y$ are the same object here, they are the same object in every world.
For example, if $x$ and $y$ both label the number $7$, then in every world they both label $7$.

### L2 human

We check the formula in a concrete model with two worlds.
Let $W = \{w, v\}$, $R = \{(w, v)\}$ and $D(w) = D(v) = \{1, 2\}$.
Under $\sigma(x) = \sigma(y) = 1$ the antecedent holds at $w$.
The only successor of $w$ is $v$, and there still $\sigma(x) = \sigma(y) = 1$, so $w \models_\sigma \square (x = y)$.
Under $\sigma'(x) = 1$ and $\sigma'(y) = 2$, the antecedent fails at $w$, so the implication holds.
The typical use of the formula is in arguments about identity across worlds.
Watch out: the formula does not say that the object exists at every world, only that it is identical to itself there.
