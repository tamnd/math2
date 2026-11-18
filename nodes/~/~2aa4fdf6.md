---
tag: ~2aa4fdf6
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

The formula
$$x = y \to \square (x = y)$$
is a formula of [[quantified modal logic|D2H3S12V7X]].
We show that it is valid on every Kripke frame with domains, and that it is derivable in $\mathsf{QK}$ with identity.

First the semantic check.
Let $\mathfrak{M} = (W, R, D, I)$ be any Kripke model with domains, let $w \in W$, and let $\sigma$ be any assignment.

1. Assume $\mathfrak{M}, w \models_\sigma x = y$. By the truth condition for identity, $\sigma(x) = \sigma(y)$.
2. Let $v$ be any world with $w R v$.
3. The assignment $\sigma$ is the same at $v$ as at $w$, because assignments do not depend on worlds.
4. So $\sigma(x) = \sigma(y)$ still holds, and $\mathfrak{M}, v \models_\sigma x = y$.
5. Step 4 holds for every $v$ with $w R v$, so $\mathfrak{M}, w \models_\sigma \square (x = y)$.
6. Steps 1 to 5 hold for every $\mathfrak{M}$, $w$ and $\sigma$, so the formula is valid.

Now the derivation.

7. $x = x$ is an axiom of identity.
8. $\square (x = x)$ follows from step 7 by the [[necessitation rule|G989VP2NGP]].
9. $x = y \to (\square (x = x) \to \square (x = y))$ is an instance of the substitution axiom $x = y \to (\varphi(x) \to \varphi(y))$ with $\varphi(z) = \square (x = z)$.
10. From steps 8 and 9, propositional logic gives $x = y \to \square (x = y)$.

## Remarks

The example shows that identity between objects cannot be contingent in the standard semantics.
The reason is that variables are rigid: their value does not change from world to world.
The same check, with "$\neq$" in place of "$=$", shows that $x \neq y \to \square (x \neq y)$ is also valid.
If we allow constants that denote different objects at different worlds, step 3 fails for the constants, and so does the formula.
This is the case of a name that is not a [[rigid designator|HGR6C3KA34]].
The derivation in steps 7 to 10 goes back to Ruth Barcan Marcus, whose 1947 paper proved the necessity of identity in her system.

## Explanations

### L1 human

If two names stand for the same thing, then that thing is one object.
An object is equal to itself in every possible world.
So if $x$ and $y$ are the same object, they are the same object in every world.
For example, if $x$ and $y$ both name the number $7$, then in every world they both name $7$.

### L2 human

We check the formula in a concrete model with two worlds.

1. Let $W = \{w, v\}$, $R = \{(w, v)\}$, $D(w) = D(v) = \{1, 2\}$.
2. Let $\sigma(x) = 1$ and $\sigma(y) = 1$. Then $w \models_\sigma x = y$.
3. The only world with $w R v$ is $v$, and $\sigma(x) = \sigma(y) = 1$ there, so $v \models_\sigma x = y$ and $w \models_\sigma \square (x = y)$.
4. Let $\sigma'(x) = 1$ and $\sigma'(y) = 2$. Then $w \not\models_{\sigma'} x = y$, so the implication holds at $w$ under $\sigma'$ because its antecedent is false.

The typical use of the formula is in arguments about identity across worlds.
A trap: the formula does not say that the object exists at every world, only that it is identical to itself there.
