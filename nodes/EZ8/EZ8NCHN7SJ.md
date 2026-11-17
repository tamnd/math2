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

1. The Skolem form of a prenex sentence $\varphi$ is written $\varphi^S$, over the signature $\sigma^S$ of $\sigma$ and the new symbols.
2. Some books call the result of Skolemization the Skolem normal form of $\varphi$, and others call any universal prenex sentence a Skolem normal form.

## Remarks

Let $\varphi = \forall x_1 \cdots \forall x_k \, \exists y \, \chi$ be in prenex normal form, with distinct prefix variables.
Its Skolemization step replaces $\varphi$ by $\forall x_1 \cdots \forall x_k \, \chi[f(x_1, \dots, x_k)/y]$.
Here $f$ is a new function symbol of arity $k$; for $k = 0$ it is a new constant symbol.
Repeating the step gives a sentence in Skolem normal form over a larger signature.
It is satisfiable if and only if $\varphi$ is satisfiable, by the [[Skolem normal form theorem|Q5H7C57VNH]].
For example, $\forall x \, \exists y \, R(x, y)$ becomes $\forall x \, R(x, f(x))$, which is in Skolem normal form.
The sentence $\forall x \, \exists y \, R(x, y)$ itself is not in Skolem normal form, since its prefix contains $\exists$.
The sentence $\forall x \, R(x, f(x))$ implies $\forall x \, \exists y \, R(x, y)$, but not conversely, so the two are not equivalent.

## Explanations

### L1 human

A sentence is in Skolem normal form when it starts with "for all" quantifiers only, and the rest has no quantifiers.
For example, "for all $x$ and $y$, $x + y = y + x$" is in Skolem normal form.

### L2 human

To Skolemize, read the prefix from the left.
Each $\exists y$ is deleted, and $y$ is replaced in the matrix by a new symbol applied to the universal variables read so far.
For $\exists u \, \forall x \, \exists y \, R(u, x, y)$, this gives $\forall x \, R(c, x, g(x))$ with a new constant $c$ and a new unary symbol $g$.
