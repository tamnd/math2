---
tag: 9J3RXB9HJG
kind: example
name: First-order logic as an institution
msc: ["03B22", "03C95", "03B10"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [RQXV7PM2WT]
uses: [RQXV7PM2WT, 086QKPF0A6, WDVVEYD6AT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Institution_(computer_science)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reduct
    locator: lead section
  - book: isbn:9780122384523
---

## Example

Take the integers with order and addition, $(\mathbb{Z}, <, +)$, and forget the addition.
What remains is the ordered set $(\mathbb{Z}, <)$, and every sentence about $<$ alone has the same truth value in both.
This is the heart of [[first-order logic|086QKPF0A6]] with equality as an institution, one of the [[abstract logical systems|RQXV7PM2WT]].
A [[signature|WDVVEYD6AT]] $\Sigma$ is a set of function symbols and relation symbols, each with an arity.
A morphism $\sigma \colon \Sigma \to \Sigma'$ sends each function symbol to a function symbol of the same arity, and each relation symbol to a relation symbol of the same arity.
The sentences $\mathrm{Sen}(\Sigma)$ are the first-order sentences over $\Sigma$.
The map $\mathrm{Sen}(\sigma)$ replaces each symbol $f$ or $R$ by $\sigma(f)$ or $\sigma(R)$, and leaves variables, connectives and quantifiers unchanged.

The models $\mathrm{Mod}(\Sigma)$ form the category of $\Sigma$-[[structures|983GZBQYT4]] with homomorphisms.
For $\sigma \colon \Sigma \to \Sigma'$ and a $\Sigma'$-structure $M'$, the reduct $M'|_\sigma$ has the same universe as $M'$.
It interprets each symbol $f$ of $\Sigma$ as $M'$ interprets $\sigma(f)$, and likewise for relation symbols.
Satisfaction $M \models_\Sigma \varphi$ is the usual truth of a sentence in a structure.

We check the satisfaction condition $M' \models_{\Sigma'} \sigma(\varphi) \iff M'|_\sigma \models_\Sigma \varphi$.
Since $M'$ and $M'|_\sigma$ have the same universe, an assignment $s$ of the variables serves for both.
So we prove the claim for all formulas and all assignments, by induction.

1. Terms.
   For every $\Sigma$-term $t$, the value of $\sigma(t)$ in $M'$ under $s$ equals the value of $t$ in $M'|_\sigma$ under $s$.
   For a variable both are $s(x)$.
   For $f(t_1, \dots, t_n)$, both apply the interpretation of $\sigma(f)$ in $M'$ to the same values, by the induction hypothesis.
2. Atomic formulas.
   We have $\sigma(R(t_1, \dots, t_n)) = \sigma(R)(\sigma(t_1), \dots, \sigma(t_n))$.
   By step 1 the arguments have the same values, and $\sigma(R)$ in $M'$ is $R$ in $M'|_\sigma$.
   Equations $t_1 = t_2$ work the same way.
3. Connectives.
   We have $\sigma(\neg \psi) = \neg \sigma(\psi)$ and $\sigma(\psi \wedge \chi) = \sigma(\psi) \wedge \sigma(\chi)$, so the claim passes from the parts to the whole.
4. Quantifiers.
   $M', s \models \exists x\, \sigma(\psi)$ holds iff $M', s[x \mapsto a] \models \sigma(\psi)$ for some $a$ in the universe.
   By the induction hypothesis this holds iff $M'|_\sigma, s[x \mapsto a] \models \psi$ for some $a$, that is, iff $M'|_\sigma, s \models \exists x\, \psi$.
   The same universe is used on both sides.
5. For sentences the assignment does not matter, which gives the satisfaction condition.

Now a concrete check.

6. Let $\Sigma = \{ E \}$ with $E$ binary, and $\Sigma' = \{ <, + \}$ with $<$ a binary relation and $+$ a binary function.
   Let $\sigma(E) = {<}$.
7. Let $M' = (\mathbb{Z}, <, +)$.
   Its reduct is $M'|_\sigma = (\mathbb{Z}, E)$ with $E$ read as $<$, and the addition is forgotten.
8. Take $\varphi = \forall x\, \neg E(x, x)$.
   Then $\sigma(\varphi) = \forall x\, \neg (x < x)$, which is true in $M'$ since no integer is less than itself.
9. In the reduct, $E$ is irreflexive for the same reason, so $M'|_\sigma \models \varphi$, and both sides agree.
10. Take $\varphi_2 = \forall x\, \exists y\, E(x, y)$.
    In $M'$, $\sigma(\varphi_2) = \forall x\, \exists y\, (x < y)$ holds with $y = x + 1$, and in the reduct $\varphi_2$ holds with the same witness.

## Remarks

Step 4 uses that a reduct keeps the universe.
A notion of reduct that shrank the universe would break the satisfaction condition.
In algebraic specification one uses many-sorted first-order logic, where signatures also have sorts and a morphism maps sorts to sorts.
The proof is the same, sort by sort.

If $\sigma$ sends two constants $c, d$ to one constant $e$, then the sentence $c \neq d$, which has models over $\Sigma$, translates to $e \neq e$, which has none.
This repeats the [[propositional case|4Y5D1JY6RV]], where merging variables also creates new consequences.
For an injective $\sigma$, every $\Sigma$-structure is a reduct of a $\Sigma'$-structure, obtained by interpreting the new symbols arbitrarily.
So translation along an injective $\sigma$ also reflects consequence.

## Explanations

### L1 human

A first-order sentence speaks about a structure through symbols such as "less than" and "plus".
If we rename "less than" to "E", and read "E" in the integers as "less than", every sentence keeps its truth value.
Forgetting symbols that a sentence does not use also changes nothing.
The satisfaction condition of an institution states these two facts in one rule.

### L2 human

We check the satisfaction condition for a sentence with two symbols.

1. Let $\Sigma = \{ c, F \}$ with a constant $c$ and a unary relation $F$.
   Let $\Sigma' = \{ 0, P, Q \}$ with a constant $0$ and unary relations $P, Q$.
2. Let $\sigma(c) = 0$ and $\sigma(F) = P$.
3. Let $M'$ have universe $\mathbb{N}$, with $0$ read as zero, $P$ as "is even" and $Q$ as "is odd".
4. Let $\varphi = F(c) \wedge \exists x\, \neg F(x)$, so $\sigma(\varphi) = P(0) \wedge \exists x\, \neg P(x)$.
   It is true in $M'$, since $0$ is even and $1$ is not.
5. The reduct has universe $\mathbb{N}$, with $c$ read as zero and $F$ as "is even", and $Q$ is forgotten.
   Then $\varphi$ is true in it for the same reasons.

The typical use of this institution is to move theories along renamings, for example to reuse a specification of orders for the integers.
A trap is to forget arities.
A morphism may not send a binary relation symbol to a unary one, since then $\mathrm{Sen}(\sigma)$ would produce ill-formed formulas.
