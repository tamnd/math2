---
tag: GCX3RQVXXY
kind: example
name: The equality quotient in a Henkin term model
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
instance_of: [RY8KRKR097]
uses: [RY8KRKR097, SC0BSJ3GT6, FMZMD0GGYK, 6D3WA7N2W4, RGNF33GVHX]
sources:
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
---

## Example

A theory that says "there is only one thing" still has infinitely many names, and the term model must glue all of them into one element.

Let $L$ have one constant symbol $a$ and one unary function symbol $f$.
Let $\Gamma = \{ \forall x \, \forall y \, (x = y) \}$, which says that the universe has exactly one element.
We follow the [[Henkin construction|RY8KRKR097]] and look at the term model.

1. We add the new constants $c_0, c_1, \dots$ and the witness axioms, and let $\Delta$ be a maximal consistent extension, as in the [[proof of model existence|FMZMD0GGYK]].
2. The closed [[terms|6D3WA7N2W4]] of $L(C)$ are $f^n(a)$ and $f^n(c_i)$ for $n, i \ge 0$.
   They are infinitely many different strings.
3. For closed terms $t$ and $u$, we instantiate $\forall x \, \forall y \, (x = y)$ twice with axiom group 2, first at $t$ and then at $u$.
   This gives $\Gamma \vdash t = u$, so $(t = u) \in \Delta$ by property 1 of [[Lindenbaum's lemma|SC0BSJ3GT6]].
4. So $t \sim u$ for all closed terms, and the quotient of the set of closed terms has exactly one element, $[a]$.
5. The function $f^{\mathcal{M}}$ sends $[a]$ to $[f(a)] = [a]$, and every constant denotes $[a]$.
6. The one-element structure satisfies $\forall x \, \forall y \, (x = y)$, so the term model is a model of $\Gamma$, as the truth lemma predicts.

## Remarks

Why take a quotient at all?
Suppose the universe were the set of closed terms, with $=$ read as identity of strings.
Then $a$ and $f(a)$ would be two different elements, and $\forall x \, \forall y \, (x = y)$ would be false.
The relation $t \sim u$, defined by $(t = u) \in \Delta$, is an [[equivalence relation|RGNF33GVHX]] and a congruence for $f$ and for every relation symbol, by axiom groups 5 and 6, so the quotient structure is well defined.
In a language without $=$, no quotient is needed, and the universe is the set of closed terms itself.

Change $\Gamma$ to "there are exactly two elements", and the closed terms fall into at most two classes.
Which terms share a class depends on $\Delta$: for example, $\Delta$ may contain $f(a) = a$, or it may contain $\neg (f(a) = a)$.

## Explanations

### L1 human

The facts say "there is only one thing".
We have infinitely many names, such as $a$, $f(a)$ and $c_0$.
All of these names must be names of the same thing.
So the model has one element with many names.

### L2 human

In a term model, an element is a class of closed terms that the theory proves equal.
Here every pair of closed terms is provably equal, so there is exactly one class.
This is the step "take the quotient by provable equality" in the proof of the [[model existence theorem|G0DTR159RN]].
Watch out: counting the closed terms does not count the elements.
There are infinitely many terms here, and the model has one element.

### L3 human

The term model is the quotient of the term algebra by the congruence that $\Delta$ defines.
The term algebra is the free algebra on the constants, and the quotient is the initial model of the equations in $\Delta$.
The example shows that a Henkin model has at most as many elements as there are closed terms, and can have far fewer.
