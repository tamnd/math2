---
tag: 5YGHNNRVFW
kind: example
name: Signaling in independence-friendly logic
msc: ["03B60", "03C80"]
topics: [MDHDYV8QZW]
audience: research
instance_of: [DPMKT2KRB8]
uses: [DPMKT2KRB8, Y3WXJP6FMB, GCPQGMJYEV]
sources:
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Model-theoretic properties
---

## Example

In [[independence-friendly logic|DPMKT2KRB8]], a slash hides a variable, but a player may still learn its value from another move.
Consider this sentence in a structure $\mathcal{M}$ with domain $M$ and empty vocabulary:
$$\psi := \forall x \, \exists z \, (\exists y / \set{x}) \, x = y.$$
We show that $\psi$ is true in every structure.

1. In the game for $\psi$, Abelard chooses $a$ for $x$, then Eloise chooses $c$ for $z$, and then Eloise chooses $b$ for $y$.
   She wins if $a = b$.
2. At $\exists z$ nothing is hidden, so Eloise may choose $c = a$.
3. At $(\exists y / \set{x})$ the value of $x$ is hidden, but the value of $z$ is not, since $z \notin \set{x}$.
   So Eloise may choose $b = c$.
4. The strategy "$z := x$, then $y := z$" respects the slash, because the choice of $y$ depends only on the value of $z$.
5. In every play it gives $b = c = a$, so Eloise wins, and $\psi$ is true in $\mathcal{M}$.

The same proof works with Skolem functions.
The Skolem function of $z$ takes $x$, and the Skolem function of $y$ takes the variables in scope other than $x$, which is only $z$.
So the [[Skolem form|GCPQGMJYEV]] is this sentence:
$$\exists f \, \exists g \, \forall x \, x = g(f(x)).$$
The witnesses are $f = g = \mathrm{id}_M$.

## Remarks

### What signaling is

The example shows signaling: a player passes hidden information to her later self through an earlier move.
The slash hides the value of $x$, but not the value of $z$, which encodes it.
Compare the [[undetermined sentence|Y3WXJP6FMB]] $\forall x \, (\exists y / \set{x}) \, x = y$.
It has no $\exists z$, so Eloise has nothing to read, and the sentence is not true in any structure with at least two elements.

Signaling depends on the convention that the slash hides only the listed variables.
Under this convention, IF logic allows dependence that is not transitive.
Here $y$ depends on $z$, and $z$ depends on $x$, but $y$ does not depend on $x$ directly.

### Blocking the signal

The result changes with the slash set.
With $(\exists y / \set{x, z})$ the Skolem function of $y$ has no arguments.
Then $\psi$ becomes true exactly in the one-element structures, like the undetermined sentence.
This is why the Henkin quantifier in IF form slashes both $x_1$ and $y_1$.

## Explanations

### L1 human

A player must guess a hidden number, and the rules say that she may not look at it.
But one step earlier she was allowed to write a note, and she copied the number into the note.
The rules do not forbid reading the note, so she reads it and wins.
In this logic, hiding one piece of information is not enough when another piece carries the same information.

### L2 human

We play $\psi$ on $M = \set{0, 1}$.

1. Abelard chooses $x = 1$.
2. Eloise sees $x = 1$ and chooses $z = 1$.
3. At $y$, Eloise sees $z = 1$ but not $x$, and she chooses $y = 1$.
4. The atomic formula $x = y$ reads $1 = 1$, so Eloise wins this play.

Check: the play with $x = 0$ gives $z = 0$ and $y = 0$, and $0 = 0$, so Eloise wins both plays.
The typical use of this example is to check a proposed translation of a pattern of dependence into IF logic.
Watch out: to make $y$ independent of $x$, slash $x$ and also every existential variable that can carry the value of $x$.
