---
tag: BCTD7FZTSK
kind: example
name: A sentence and its Skolem form are not logically equivalent
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: GCPQGMJYEV
    note: the sentence forall x exists y R(x, y) has an existential quantifier in its prefix, and its Skolem form is equisatisfiable with it but not equivalent to it
uses: [GCPQGMJYEV, Q5H7C57VNH, 0JMR2HM2N2, B37TYWXS74]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
---

## Example

Let $R$ be a binary relation symbol, and let $\varphi = \forall x \, \exists y \, R(x, y)$.
Its Skolem form is $\varphi^S = \forall x \, R(x, f(x))$, with a new unary function symbol $f$.
We show that $\varphi$ is not in [[Skolem normal form|GCPQGMJYEV]], and that $\varphi$ and $\varphi^S$ are not [[logically equivalent|0JMR2HM2N2]].

1. The prefix of $\varphi$ contains $\exists y$, so $\varphi$ is not in Skolem normal form.
2. Let $\mathcal{N}$ have the domain $\set{0, 1}$, with $R^{\mathcal{N}}$ the equality relation and $f^{\mathcal{N}}$ the constant map with value $0$.
3. In $\mathcal{N}$, $\varphi$ is true: for each $x$, take $y = x$.
4. In $\mathcal{N}$, $\varphi^S$ is false: for $x = 1$, $f^{\mathcal{N}}(1) = 0$, and $R(1, 0)$ fails.
5. So one $\sigma^S$-structure satisfies $\varphi$ but not $\varphi^S$, and the two sentences are not equivalent.
6. The two are still [[equisatisfiable|B37TYWXS74]]. Changing $f^{\mathcal{N}}$ to the identity gives a model of $\varphi^S$, as the [[Skolem normal form theorem|Q5H7C57VNH]] says.

So Skolemization keeps satisfiability but not truth in a fixed structure.

## Remarks

The direction $\varphi^S \models \varphi$ always holds: the value $f(x)$ is a witness for $\exists y$.
The failure is only in the other direction, because the interpretation of $f$ in a given structure need not choose witnesses.
For this reason, Skolemization is used for refutation: $\varphi$ is unsatisfiable exactly when $\varphi^S$ is.
It is not used to prove that $\varphi$ is valid, where the dual Herbrand form is the right tool.

## Explanations

### L1 human

"Everyone has a friend" does not mean the same as "everyone is a friend of $f(\text{them})$", for some fixed rule $f$.
The rule $f$ might point to the wrong person.
But if everyone has a friend, then some rule $f$ does point to a friend, and the second sentence then becomes true.

### L2 human

We see why the two sentences have the same models up to the choice of $f$.

1. A model of $\varphi^S$ is a model of $\varphi$ after forgetting $f$.
2. A model of $\varphi$ becomes a model of $\varphi^S$ when $f$ is chosen to pick a witness for each $x$.
3. In step 2 of the example, the structure fixed $f$ badly, so the expansion was not a model.

The typical use is in resolution, where only unsatisfiability matters.
A trap: the claim "$\varphi \models \varphi^S$" looks plausible, but $\varphi^S$ makes a promise about the symbol $f$, and $\varphi$ says nothing about $f$.
