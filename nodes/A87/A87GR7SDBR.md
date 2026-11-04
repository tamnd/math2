---
tag: A87GR7SDBR
kind: statement
role: proposition
name: Axiom of choice in type theory
msc: ["03E25"]
sources:
  - wikipedia: en:840@r1375106187
    locator: Axiom of choice, section Axiom of choice in type theory
    note: adopted
    mention: wikipedia://en/840#TVQV
    sections: [Statement]
inventory: [FKDX1K9M8D]
---

## Statement

In type theory, a different kind of statement is known as the axiom of choice. This form begins with two types, σ and τ, and a relation *R* between objects of type σ and objects of type τ. The axiom of choice states that if for each *x* of type σ there exists a *y* of type τ such that *R*(*x*,*y*), then there is a function *f* from objects of type σ to objects of type τ such that *R*(*x*,*f*(*x*)) holds for all *x* of type σ:

$$(\forall x^\sigma)(\exists y^\tau) R(x,y) \to (\exists f^{\sigma \to \tau})(\forall x^\sigma) R(x,f(x)).$$

Unlike in set theory, the axiom of choice in type theory is typically stated as an axiom scheme, in which *R* varies over all formulas or over all formulas of a particular logical form.
