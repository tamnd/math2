---
tag: 9EAHDX44B2
kind: definition
name: Internal set theory
msc: ["03H05", "03E70", "26E35"]
defines: V0PGBXYJ9R
uses: [0HE5WDQ9FJ, 0BBTH3YSZA]
sources:
  - url: https://en.wikipedia.org/wiki/Internal_set_theory
---

## Definition

*Internal set theory* (IST) is the first-order theory in the language of set theory with one extra unary predicate $\operatorname{st}$, read "is standard".
A formula is *internal* if it does not contain $\operatorname{st}$, and *external* otherwise.
Write $\forall^{\mathrm{st}} x$ for "for all standard $x$", $\exists^{\mathrm{st}} x$ for "there is a standard $x$", and $\forall^{\mathrm{st\,fin}} z$ for "for all standard [[finite|0BBTH3YSZA]] sets $z$".
The axioms of IST are the following.

1. The axioms of [[ZFC|0HE5WDQ9FJ]], where the schemes of separation and replacement are taken only for internal formulas.
2. Idealization: for each internal formula $B(x, y)$, possibly with other free variables,
$$\forall^{\mathrm{st\,fin}} z \, \exists x \, \forall y \in z \; B(x, y) \;\leftrightarrow\; \exists x \, \forall^{\mathrm{st}} y \; B(x, y).$$
3. Standardization: for each formula $C(z)$, internal or external, possibly with other free variables,
$$\forall^{\mathrm{st}} x \, \exists^{\mathrm{st}} y \, \forall^{\mathrm{st}} z \, \bigl(z \in y \leftrightarrow (z \in x \wedge C(z))\bigr).$$
4. Transfer: for each internal formula $A(x, t_1, \dots, t_k)$ with no other free variables,
$$\forall^{\mathrm{st}} t_1 \cdots \forall^{\mathrm{st}} t_k \, \bigl(\forall^{\mathrm{st}} x \, A(x, t_1, \dots, t_k) \to \forall x \, A(x, t_1, \dots, t_k)\bigr).$$

## Remarks

Example: there is a nonstandard natural number.
Apply idealization to the internal formula $B(x, y)$: "$x \in \N$, and if $y \in \N$ then $y < x$".
The left side holds, since every finite set $z$ has only finitely many natural numbers, and some natural number exceeds them all.
So some $\nu \in \N$ is larger than every standard natural number, and $\nu$ is not standard.

Non-example: the collection of standard natural numbers is not given by separation, because the formula "$n$ is standard" is external, so clause 1 does not apply to it.
In fact no such set exists: its complement in $\N$ would have a least element $m > 0$, and then $m - 1$ would be standard, so $m$ would be standard by transfer.

By transfer, every object uniquely defined by an internal formula without parameters, such as $0$, $\N$, $\R$ or $\pi$, is standard.
