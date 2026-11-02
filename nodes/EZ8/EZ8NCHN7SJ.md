---
tag: EZ8NCHN7SJ
kind: definition
name: Skolem normal form
msc: [03B10]
defines: GCPQGMJYEV
uses: [CS82V969DE, DKFGQTRYZE, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
A [[sentence|DKFGQTRYZE]] over $\sigma$ is in *Skolem normal form* if it has the form
$$\forall x_1 \, \forall x_2 \cdots \forall x_n \, \psi,$$
where $n \ge 0$ and $\psi$ is a formula with no quantifiers.
So it is a sentence in [[prenex normal form|CS82V969DE]] whose prefix has only universal quantifiers.

## Remarks

Let $\varphi = \forall x_1 \cdots \forall x_k \, \exists y \, \chi$ be in prenex normal form.
Its Skolemization step replaces $\varphi$ by $\forall x_1 \cdots \forall x_k \, \chi[f(x_1, \dots, x_k)/y]$.
Here $f$ is a new function symbol of arity $k$; for $k = 0$ it is a new constant symbol.
Repeating the step gives a sentence in Skolem normal form over a larger signature.
It is satisfiable if and only if $\varphi$ is satisfiable.
For example, $\forall x \, \exists y \, R(x, y)$ becomes $\forall x \, R(x, f(x))$, which is in Skolem normal form.
The sentence $\forall x \, \exists y \, R(x, y)$ itself is not in Skolem normal form, since its prefix contains $\exists$.
The sentence $\forall x \, R(x, f(x))$ implies $\forall x \, \exists y \, R(x, y)$, but not conversely, so the two are not equivalent.
