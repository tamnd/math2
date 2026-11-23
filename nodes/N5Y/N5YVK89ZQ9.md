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

"In some world that we can reach, it rains" becomes, in first-order logic, "there is a world $y$ with $R(x, y)$ in which it rains", and the atom $R(x, y)$ is a guard.
We show that every modal formula translates in this way into the [[guarded fragment|Y7YS1C3GAE]].

### The translation

Let the modal language have propositional letters $p, q, \ldots$, the connectives $\neg$ and $\wedge$, and the operators $\Diamond$ and $\Box$.
The first-order signature has a binary relation symbol $R$ and a unary relation symbol $P$ for each letter $p$.
The standard translation $\mathrm{ST}_x$ maps each [[modal formula|C3RZY20ETK]] to a first-order formula with the free variable $x$, by four clauses:

- $\mathrm{ST}_x(p) = P(x)$;
- $\mathrm{ST}_x(\neg \varphi) = \neg \mathrm{ST}_x(\varphi)$ and $\mathrm{ST}_x(\varphi \wedge \psi) = \mathrm{ST}_x(\varphi) \wedge \mathrm{ST}_x(\psi)$;
- $\mathrm{ST}_x(\Diamond \varphi) = \exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi))$;
- $\mathrm{ST}_x(\Box \varphi) = \forall y \, (R(x, y) \to \mathrm{ST}_y(\varphi))$.

The clauses for $\mathrm{ST}_y$ are the same with $x$ and $y$ exchanged, so only two variables are ever used.
In a [[Kripke model|NGHWZ9Y7ZV]], read as a first-order structure, $\mathrm{ST}_x(\varphi)$ holds at a world $w$ exactly when $\varphi$ is true at $w$.

### Every translation is guarded

We claim that $\mathrm{ST}_x(\varphi)$ is guarded for every modal formula $\varphi$, and that its only free variable is $x$.
We prove both claims together by induction on $\varphi$, for $\mathrm{ST}_x$ and $\mathrm{ST}_y$ at the same time.

1. Letters.
   $P(x)$ is atomic, so it is guarded, and its only free variable is $x$.
2. Negation and conjunction.
   The guarded fragment is closed under $\neg$ and $\wedge$, and these connectives add no free variable.
3. Diamond.
   By induction, $\mathrm{ST}_y(\varphi)$ is guarded, with the free variable $y$ only.
   The guard $R(x, y)$ is atomic and contains $y$.
   So $\exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi))$ is a guarded quantification, with the free variable $x$ only.
4. Box.
   The same argument applies to $\forall y \, (R(x, y) \to \mathrm{ST}_y(\varphi))$.

### A worked case

As a concrete case, take $\varphi = \Box (p \to \Diamond q)$, where $p \to \chi$ abbreviates $\neg (p \wedge \neg \chi)$.
Its translation is the following formula:
$$\mathrm{ST}_x(\varphi) = \forall y \, \bigl( R(x, y) \to (P(y) \to \exists x \, (R(y, x) \wedge Q(x))) \bigr).$$

5. The inner quantifier $\exists x$ has the guard $R(y, x)$, and its body $Q(x)$ has the free variable $x$, which occurs in the guard.
6. The outer quantifier $\forall y$ has the guard $R(x, y)$.
   Its body has the free variable $y$ only, since the inner $x$ is bound, and $y$ occurs in the guard.
7. So the translation is guarded, and its only free variable is $x$.

## Remarks

The example shows that basic modal logic sits inside the guarded fragment.
So the decidability of the guarded fragment gives a second proof that basic modal logic is decidable.
The translation also lies in [[two-variable logic|S7C3C7DJRF]], because it uses only $x$ and $y$.

Change the modal language, and the two fragments part ways.
A binary modal operator interpreted by a ternary relation $S$ has the clause $\exists y \, \exists z \, (S(x, y, z) \wedge \mathrm{ST}_y(\varphi) \wedge \mathrm{ST}_z(\psi))$.
It is guarded by $S(x, y, z)$, but it needs three variables, so it leaves two-variable logic.
For the universal modality, the clause $\exists y \, \mathrm{ST}_y(\varphi)$ is guarded by an equality, in the form $\exists y \, (y = y \wedge \mathrm{ST}_y(\varphi))$.

## Explanations

### L1 human

Modal logic talks about "possible worlds" and says things like "in some world that we can reach, it rains".
Written in ordinary logic, this becomes "there is a world $y$ that $x$ can reach, and it rains in $y$".
The phrase "that $x$ can reach" is the guard, since it limits the search to worlds that are directly connected to $x$.
Every modal statement translates in this way, so every modal statement lands in the guarded fragment.

### L2 human

We translate $\Diamond \Box p$ and check the guards.
The outer diamond gives $\exists y \, (R(x, y) \wedge \mathrm{ST}_y(\Box p))$.
The box, translated at $y$ with the roles of $x$ and $y$ exchanged, gives $\forall x \, (R(y, x) \to P(x))$.
So the full translation is the following formula:
$$\exists y \, \bigl( R(x, y) \wedge \forall x \, (R(y, x) \to P(x)) \bigr).$$
The inner guard $R(y, x)$ contains the quantified $x$, which is also the free variable of $P(x)$.
The outer guard $R(x, y)$ contains $y$, the only free variable of its body.
Check: each quantifier has an atom that covers its variables, so the formula is guarded.

The typical use is to transfer a result on the guarded fragment, such as the finite model property, to a modal logic.
Watch out: if you take a fresh variable at each modal depth, the result is still guarded, but it is no longer in two-variable logic.
