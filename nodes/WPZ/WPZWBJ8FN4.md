---
tag: WPZWBJ8FN4
kind: example
name: Skolem functions for the group axioms
msc: ["03B10", "20A05"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [GCPQGMJYEV]
uses: [GCPQGMJYEV, EZ8NCHN7SJ, Q5H7C57VNH, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Definition
---

## Example

Take the signature $\{ \cdot \}$ with one binary function symbol.
A [[group|G5S1M9]] can be axiomatized in it by associativity and the sentence
$$\varphi = \exists e \, \forall x \, \exists y \, (e \cdot x = x \land x \cdot e = x \land x \cdot y = e \land y \cdot x = e).$$
We compute the [[Skolem normal form|GCPQGMJYEV]] of $\varphi$ and interpret the new symbols.

1. The sentence $\varphi$ is prenex with prefix $\exists e \, \forall x \, \exists y$, distinct variables and a quantifier-free matrix.
2. The leftmost $\exists e$ has no universal quantifier before it.
   So $e$ becomes a new constant symbol $c$, by the [[Skolemization step|EZ8NCHN7SJ]].
3. The next $\exists y$ follows $\forall x$.
   So $y$ becomes $i(x)$ for a new unary symbol $i$.
4. The result is
   $$\varphi^S = \forall x \, \big( c \cdot x = x \land x \cdot c = x \land x \cdot i(x) = c \land i(x) \cdot x = c \big).$$
5. In a group $G$, the sentence $\varphi$ is true, with $e$ the identity and $y = x^{-1}$.
6. The expansion with $c$ the identity and $i(x) = x^{-1}$ satisfies $\varphi^S$, because these are the identity and inverse laws.
7. The identity and the inverses of a group are unique, so here the expansion is unique and no choice is needed.

So the Skolem symbols for the group axioms are the identity and the inverse map, as the [[Skolem normal form theorem|Q5H7C57VNH]] predicts in this case.

## Remarks

This explains why groups are often given in the signature $\{ \cdot, e, {}^{-1} \}$: there all the axioms are universal.
In that signature every substructure of a group is a subgroup, because universal sentences are preserved in substructures.
In the signature $\{ \cdot \}$ the axiom $\varphi$ is not universal, and a substructure need not be a group.
For example, $\mathbb{N}$ is closed under addition, so it is a substructure of $(\mathbb{Z}, +)$, but it has no inverses.

## Explanations

### L1 human

The group axiom "there is an identity, and every element has an inverse" has two "there is" parts.
Skolemization names them: a constant $c$ for the identity and a function $i$ for taking inverses.
The new axiom says only "for every $x$", and it describes the identity and the inverse directly.

### L2 human

We compare Skolem functions with unique and with non-unique witnesses.
In a group the witness $y$ for $x$ is unique, so the Skolem function $i$ is forced.
For $\forall x \, \exists y \, (y + y = x)$ in $\mathbb{Z}/5\mathbb{Z}$, each $x$ has exactly one witness, since $2$ is invertible modulo $5$; for $x = 1$ it is $y = 3$.
In the positive reals under multiplication, the witness of $y \cdot y = x$ is $\sqrt{x}$, and it is again unique.
In the nonzero complex numbers under multiplication, each $x$ has two square roots, so there are many Skolem functions.
The typical use is to turn an axiom system into a universal one by adding the Skolem symbols to the signature.
Watch out: when the witness is not unique, different Skolem functions give different expansions of the same structure.
