---
tag: N5YVK89ZQ9
kind: example
name: The standard translation of a modal formula is guarded
aliases: [standard-translation-into-the-guarded-fragment]
msc: ["03B45", "03B25"]
topics: [E4AVTNWE9E]
audience: grad
instance_of: [Y7YS1C3GAE]
uses: [Y7YS1C3GAE, C3RZY20ETK, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Guarded_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

Let the modal language have propositional letters $p, q, \ldots$, the connectives $\neg$ and $\wedge$, and the operators $\Diamond$ and $\Box$.
The first-order signature has a binary relation symbol $R$ and a unary relation symbol $P$ for each letter $p$.
The standard translation $\mathrm{ST}_x$ maps each [[modal formula|C3RZY20ETK]] to a first-order formula with one free variable $x$.
It uses only the two variables $x$ and $y$, and it swaps their roles at each modal operator.

- $\mathrm{ST}_x(p) = P(x)$.
- $\mathrm{ST}_x(\neg \varphi) = \neg \mathrm{ST}_x(\varphi)$ and $\mathrm{ST}_x(\varphi \wedge \psi) = \mathrm{ST}_x(\varphi) \wedge \mathrm{ST}_x(\psi)$.
- $\mathrm{ST}_x(\Diamond \varphi) = \exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi))$.
- $\mathrm{ST}_x(\Box \varphi) = \forall y \, (R(x, y) \to \mathrm{ST}_y(\varphi))$.

The clauses for $\mathrm{ST}_y$ are the same with $x$ and $y$ exchanged.
In a [[Kripke model|NGHWZ9Y7ZV]], read as a first-order structure, $\mathrm{ST}_x(\varphi)$ holds at a world $w$ exactly when $\varphi$ is true at $w$.

We claim that $\mathrm{ST}_x(\varphi)$ is in the [[guarded fragment|Y7YS1C3GAE]] for every modal formula $\varphi$, and that its only free variable is $x$.
We prove both claims together by induction on $\varphi$, for $\mathrm{ST}_x$ and $\mathrm{ST}_y$ at the same time.

1. Letters. $P(x)$ is atomic, so it is guarded, and its only free variable is $x$.
2. Negation and conjunction. The guarded fragment is closed under $\neg$ and $\wedge$, and these connectives add no free variable.
3. Diamond. By induction, $\mathrm{ST}_y(\varphi)$ is guarded with the free variable $y$ only. The guard $R(x, y)$ is atomic and contains $y$. So $\exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi))$ is a guarded quantification, with the free variable $x$ only.
4. Box. The same argument applies to $\forall y \, (R(x, y) \to \mathrm{ST}_y(\varphi))$.

As a concrete case, take $\varphi = \Box (p \to \Diamond q)$, where $p \to \chi$ abbreviates $\neg (p \wedge \neg \chi)$.
Its translation is
$$\mathrm{ST}_x(\varphi) = \forall y \, \bigl( R(x, y) \to (P(y) \to \exists x \, (R(y, x) \wedge Q(x))) \bigr).$$

5. The innermost quantifier $\exists x$ has guard $R(y, x)$, and its body $Q(x)$ has the free variable $x$, which occurs in the guard.
6. The outer quantifier $\forall y$ has guard $R(x, y)$. Its body has the free variable $y$ only, since the inner $x$ is bound. The variable $y$ occurs in the guard.
7. So the translation is guarded, and its only free variable is $x$.

## Remarks

The example shows that basic modal logic sits inside the guarded fragment.
The decidability of the guarded fragment therefore gives a second proof that basic modal logic is decidable.
The translation also lies in the [[two-variable fragment|S7C3C7DJRF]], because it uses only $x$ and $y$.
For a modal operator of higher arity, such as a binary operator interpreted by a ternary relation $S$, the clause $\exists y \, \exists z \, (S(x, y, z) \wedge \mathrm{ST}_y(\varphi) \wedge \mathrm{ST}_z(\psi))$ needs three variables; it is guarded by $S(x, y, z)$, but it is not in two-variable logic.
For the modal language with the universal modality, the clause $\exists y \, \mathrm{ST}_y(\varphi)$ is guarded by the equality $y = y$, written $\exists y \, (y = y \wedge \mathrm{ST}_y(\varphi))$.

## Explanations

### L1 human

Modal logic talks about "possible worlds" and says things like "in some world that we can reach, it rains".
Written in ordinary logic, this becomes "there is a world $y$ that $x$ can reach, and it rains in $y$".
The phrase "that $x$ can reach" is the guard: it limits the search to worlds that are directly connected to $x$.
Every modal statement translates in this way, so every modal statement lands in the guarded fragment.

### L2 human

We translate $\Diamond \Box p$ and check the guards.

1. $\mathrm{ST}_x(\Diamond \Box p) = \exists y \, (R(x, y) \wedge \mathrm{ST}_y(\Box p))$.
2. $\mathrm{ST}_y(\Box p) = \forall x \, (R(y, x) \to P(x))$, with the roles of $x$ and $y$ exchanged.
3. The full translation is $\exists y \, (R(x, y) \wedge \forall x \, (R(y, x) \to P(x)))$.
4. The inner guard $R(y, x)$ contains the quantified variable $x$ and the free variable $x$ of $P(x)$.
5. The outer guard $R(x, y)$ contains $y$, the only free variable of the body.

The typical use is to transfer a result on the guarded fragment, such as the finite model property, to a modal logic.
A trap is to reuse a fresh variable at each level; the translation is still guarded, but then it is no longer in two-variable logic.
