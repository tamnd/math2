---
tag: CWGY8F92MH
kind: example
name: A non-rigid name breaks the necessity of identity
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: D2H3S12V7X
    note: the structure interprets the constant b by different objects at different worlds, so it is not a Kripke model with rigid terms, and the necessity of identity fails for b
uses: [D2H3S12V7X, HGR6C3KA34, CYG8CJ45BM]
sources:
  - url: https://en.wikipedia.org/wiki/Rigid_designator
    locator: Necessary identities
---

## Example

Add two constants $a$ and $b$ to the language of [[quantified modal logic|D2H3S12V7X]], and let a structure interpret each constant $c$ world by world, by an object $c^u$ at each world $u$.
Take $W = \{w, v\}$, $R = W \times W$ and $D(w) = D(v) = \{1, 2\}$.
Let $a^w = a^v = 1$, so $a$ names the same object at both worlds.
Let $b^w = 1$ and $b^v = 2$, so $b$ names different objects at the two worlds.

First we check that $a = b \to \square (a = b)$ fails at $w$.

1. At $w$, $a^w = 1 = b^w$, so $w \models a = b$.
2. At $v$, $a^v = 1$ and $b^v = 2$, so $v \not\models a = b$.
3. Since $w R v$, step 2 gives $w \not\models \square (a = b)$.
4. By steps 1 and 3, the antecedent is true and the consequent false at $w$, so the implication fails.

Then we check which condition of the standard semantics fails.

5. In Kripke models with domains the only terms are variables, and their values do not depend on the world.
6. The constant $b$ has two values, $1$ at $w$ and $2$ at $v$, so $b$ is not rigid, and the structure is not a model of that kind.

## Remarks

The example shows that rigidity is exactly what the proof of [[the necessity of identity|CYG8CJ45BM]] uses.
In that proof, the step "the assignment is the same at $v$ as at $w$" fails for $b$.
A name that keeps its object at every world is a [[rigid designator|HGR6C3KA34]].
If we change $b^v$ to $1$, then $b$ becomes rigid, and the implication holds at both worlds.
Definite descriptions such as "the number of planets" behave like $b$: they can pick out different objects at different worlds.

## Explanations

### L1 human

The phrase "the winner of the race" names a person, but which person depends on how the race went.
In our world it names Ana, and in another possible world it names Ben.
So "Ana is the winner" is true here, but it is not necessary.
A proper name like "Ana" names Ana in every world, and that is why identities between proper names are necessary.

### L2 human

We check that the necessity of identity still holds for the rigid constant $a$ and a variable $x$.
Let $\sigma(x) = 1$.
At $w$ we have $a^w = 1 = \sigma(x)$, and at $v$ we have $a^v = 1 = \sigma(x)$, so $a = x$ holds at both worlds.
Both worlds are successors of $w$, so $w \models_\sigma \square (a = x)$, and the implication $a = x \to \square(a = x)$ holds at $w$.
The typical use of the non-rigid structure is to model descriptions and contingent identities.
Watch out: the failure comes from the term $b$, not from the logic $\mathsf{S5}$ of the frame.
