---
tag: EZ8NCHN7SJ
kind: definition
name: Skolem normal form
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
defines: GCPQGMJYEV
uses: [CS82V969DE, DKFGQTRYZE, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
A [[sentence|DKFGQTRYZE]] over $\sigma$ is in *Skolem normal form* if it has the form
$$\forall x_1 \, \forall x_2 \cdots \forall x_n \, \psi,$$
where $n \ge 0$ and $\psi$ is a formula with no quantifiers.
So it is a sentence in [[prenex normal form|CS82V969DE]] whose prefix has only universal quantifiers.

## Notation

The Skolem form of a prenex sentence $\varphi$ is written $\varphi^S$, over the signature $\sigma^S$ made of $\sigma$ and the new symbols.
Some books call the result of Skolemization the Skolem normal form of $\varphi$, and others call any universal prenex sentence a Skolem normal form.

## Remarks

The sentence $\forall x \, \forall y \, (x + y = y + x)$ is in Skolem normal form, and so is every quantifier-free sentence, with $n = 0$.
The sentence $\forall x \, \exists y \, R(x, y)$ is not, since its prefix contains $\exists$.

Skolemization produces sentences of this form.
Let $\varphi = \forall x_1 \cdots \forall x_k \, \exists y \, \chi$ be in prenex normal form, with distinct prefix variables.
One Skolemization step replaces $\varphi$ by
$$\forall x_1 \cdots \forall x_k \, \chi[f(x_1, \dots, x_k)/y],$$
where $f$ is a new function symbol of arity $k$, and a new constant symbol when $k = 0$.
Repeating the step until no $\exists$ is left gives a sentence in Skolem normal form over a larger signature.
It is satisfiable if and only if $\varphi$ is satisfiable, by the [[Skolem normal form theorem|Q5H7C57VNH]].

For example, $\forall x \, \exists y \, R(x, y)$ becomes $\forall x \, R(x, f(x))$.
The new sentence implies the old one, but not conversely, so the two are not equivalent.

## Explanations

### L1 human

A sentence is in Skolem normal form when it starts with "for all" quantifiers only, and the rest has no quantifiers.
For example, "for all $x$ and $y$, $x + y = y + x$" is in Skolem normal form.
"For every $x$ there is a $y$ with $x < y$" is not, because of the "there is".

### L2 human

To Skolemize, read the prefix from the left.
Each $\exists y$ is deleted, and $y$ is replaced in the matrix by a new symbol applied to the universal variables read so far.
For $\exists u \, \forall x \, \exists y \, R(u, x, y)$, this gives $\forall x \, R(c, x, g(x))$, with a new constant $c$ and a new unary symbol $g$.
Check: the constant $c$ has no arguments because no $\forall$ stands before $\exists u$.
Watch out that a sentence with only universal quantifiers but not in prenex form, such as $P(c) \land \forall x \, Q(x)$, is not in Skolem normal form until its quantifier is moved to the front.
