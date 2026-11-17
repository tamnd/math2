---
tag: 8FVA1VMBSW
kind: example
name: Self-application is not a formula of higher-order logic
msc: ["03B16"]
topics: [MDHDYV8QZW]
audience: grad
not_instance_of:
  - target: K40YJX8K1G
    note: no type equals the type of relations on it, so a variable cannot be applied to itself
uses: [K40YJX8K1G, 0HESMMSYEG]
sources:
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Russell%27s_paradox
    locator: lead section
---

## Example

In [[higher-order logic|K40YJX8K1G]], the expression $X(X)$ is not a formula, for any variable $X$.
We prove this.

1. An atomic formula $X(t)$ with one argument requires that $X$ has a type $(\tau)$ and that $t$ has the type $\tau$.
2. So $X(X)$ is a formula only if the type $\sigma$ of $X$ satisfies $\sigma = (\sigma)$.
3. Define the rank of a type: $\operatorname{rk}(\iota) = 0$ and $\operatorname{rk}((\tau_1, \ldots, \tau_n)) = 1 + \max_i \operatorname{rk}(\tau_i)$. By the inductive definition of types, each type has exactly one rank.
4. Then $\operatorname{rk}((\sigma)) = 1 + \operatorname{rk}(\sigma) \neq \operatorname{rk}(\sigma)$, so $(\sigma) \neq \sigma$ for every type $\sigma$.
5. By step 2, $X(X)$ is not a formula.

## Remarks

The condition that fails is the typing rule of atomic formulas: a relation applies only to objects of the types that its own type lists.
Because $X(X)$ is not a formula, the comprehension schema cannot form the "set of all sets that do not belong to themselves", $\set{X : \neg X(X)}$.
So [[Russell's paradox|0HESMMSYEG]] cannot be stated in higher-order logic.
In untyped settings, such as naive set theory or the untyped lambda calculus, self-application is allowed, and the paradox or a fixed point appears.
The rank of a type is the order minus $1$, so step 4 also shows that $(\sigma)$ has a higher order than $\sigma$.

## Explanations

### L1 human

In higher-order logic, a collection may only contain objects from the level below it.
The expression "$X$ belongs to $X$" asks a collection to be on its own level and on the level below at the same time.
That is impossible, so the expression is not allowed at all.
This is how the logic avoids the paradox of the set of all sets that do not contain themselves.

### L2 human

We test two candidate expressions.

1. Let $X$ have type $(\iota)$ and $\mathcal{Y}$ type $((\iota))$. Then $\mathcal{Y}(X)$ is a formula, since $\mathcal{Y}$ has type $(\tau)$ with $\tau = (\iota)$, the type of $X$.
2. The expression $X(\mathcal{Y})$ is not a formula: $X$ accepts arguments of type $\iota$, and $\mathcal{Y}$ has type $((\iota)) \neq \iota$.
3. The expression $\mathcal{Y}(\mathcal{Y})$ is not a formula, by the rank argument: $\operatorname{rk}(((\iota))) = 2$ and $\operatorname{rk}((((\iota)))) = 3$.

The typical use of this example is to explain how the type discipline blocks Russell's paradox.
The trap is to think that $X(X)$ is a false formula: it is not a formula at all, so it has no truth value.
