---
tag: S7C3C7DJRF
kind: statement
role: theorem
name: Decidability of two-variable logic
aliases: [two-variable-logic, two-variable-fragment, fo2-decidability, mortimer-theorem]
msc: ["03B25", "03C13", "68Q17"]
topics: [E4AVTNWE9E]
audience: research
uses: [086QKPF0A6, QN7M1JCGT9, AS0NHQMAKA, ZF79MZRQ8V, ESPYW94XGR]
about: [086QKPF0A6, QN7M1JCGT9]
history:
  first_stated: "1975"
  notes: Mortimer proved the finite model property of two-variable logic in 1975; Grädel, Kolaitis and Vardi proved the exponential model property and NEXPTIME-completeness in 1997.
sources:
  - url: https://en.wikipedia.org/wiki/Two-variable_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finite_model_property
    locator: lead section
---

## Statement

First-order sentences that use only two variable names can always be tested for a model, and a satisfiable one always has a finite model of exponential size.
For example, $\forall x \, \exists y \, (R(x, y) \wedge \exists x \, (R(y, x) \wedge P(x)))$ speaks about chains of three elements, but it reuses $x$, so it needs only two names.

Let $L$ be a finite signature of unary and binary relation symbols.
The two-variable fragment $\mathrm{FO}^2$ is the set of first-order $L$-formulas, with equality, that use only the two variables $x$ and $y$.
A variable may be quantified again inside its own scope.

1. Scott normal form.
   From each $\mathrm{FO}^2$ sentence $\varphi$ one computes in polynomial time a sentence $\psi = \forall x \, \forall y \, \chi \wedge \bigwedge_{i=1}^m \forall x \, \exists y \, \chi_i$, with $\chi$ and each $\chi_i$ quantifier-free, over $L$ plus new unary symbols.
   Every model of $\psi$ satisfies $\varphi$, and every model of $\varphi$ expands to a model of $\psi$.
2. Exponential model property.
   If an $\mathrm{FO}^2$ sentence $\varphi$ has a model, then it has a finite model with at most $2^{c \lvert \varphi \rvert}$ elements, where $c$ is a constant and $\lvert \varphi \rvert$ is the length of $\varphi$.
3. Consequently, [[satisfiability|QN7M1JCGT9]] of $\mathrm{FO}^2$ sentences is decidable, and it lies in the [[complexity class|ESPYW94XGR]] NEXPTIME of problems solved in nondeterministic exponential time.

The [[proof|96TBEPJTKG]] proves parts 1 to 3 in full.
The matching lower bound, that satisfiability of $\mathrm{FO}^2$ is NEXPTIME-hard, is cited and not proved.

## Remarks

### Two names go a long way

The sentence of the opening says that every element has an $R$-successor, which in turn has an $R$-successor in $P$.
After the inner $\exists x$, the name $x$ points to a new element, and the old value of $x$ is no longer needed.
So $\mathrm{FO}^2$ can describe paths of any length, one step at a time.

A small model shows the sentence is satisfiable.
Take the domain $\{a, b\}$ with $R = \{ (a, b), (b, a) \}$ and $P = \{ a, b \}$.
Check: $a$ has the successor $b$, and $b$ has the successor $a$ in $P$; the same holds with $a$ and $b$ exchanged.

What two variables cannot say is a property of three elements at once.
Transitivity, $\forall x \, \forall y \, \forall z \, (R(x, y) \wedge R(y, z) \to R(x, z))$, needs all three values at the same moment.
The sentence [[with only infinite models|KH3ZG4RXAW]] uses transitivity, and it has no finite model.
By part 2, no $\mathrm{FO}^2$ sentence is equivalent to it.

### Why each hypothesis is needed

The bound of two variables is sharp.
The prefix class $[\forall \exists \forall]$ is undecidable by the classification of [[decidable prefix classes|ZF79MZRQ8V]], and its sentences use three variables, so $\mathrm{FO}^3$ is undecidable.

Function symbols are excluded.
With one unary function symbol and two variables, the sentence $\forall x \, \forall y \, (f(x) = f(y) \to x = y) \wedge \exists y \, \forall x \, (f(x) \neq y)$ says that $f$ is injective and not onto, so it has only infinite models.

Counting quantifiers break the finite model property.
In the extension $\mathrm{C}^2$, the quantifier $\exists^{\le 1} y$ means "for at most one $y$".
The sentence $\forall x \, \exists^{\le 1} y \, R(y, x) \wedge \forall x \, \exists y \, R(x, y) \wedge \exists x \, \forall y \, \neg R(y, x)$ gives every element a successor and at most one predecessor, and some element has none.
Choosing one successor for each element gives an injective map that is not onto, which needs an infinite domain.

### What it gives you

Many modal and description logics translate into $\mathrm{FO}^2$, so their satisfiability problems are decidable.
For example, the standard translation of basic [[modal logic|C3RZY20ETK]] uses only two variables.

Every satisfiable $\mathrm{FO}^2$ sentence has a finite model, so for $\mathrm{FO}^2$ satisfiability and finite satisfiability are the same problem.
Validity is decidable too, because $\varphi$ is valid exactly when $\neg \varphi$, also a sentence of $\mathrm{FO}^2$, has no model.

### The converse

Part 3 follows from part 2, but decidability does not give the finite model property in general.
The counting extension $\mathrm{C}^2$ is decidable, by the results cited under Generalizations, but the $\mathrm{C}^2$ sentence above has only infinite models.

### Watch out

Count the variable names, not the quantifiers.
The sentence $\forall x \, \exists y \, (R(x, y) \wedge \exists x \, R(y, x))$ has three quantifiers and is in $\mathrm{FO}^2$.
The sentence $\exists x \, \exists y \, \exists z \, (x \neq y \wedge y \neq z \wedge x \neq z)$, "there are three elements", has three names, and in fact no $\mathrm{FO}^2$ sentence says it.
Rewriting is not always possible, so a sentence with three names needs an argument before you treat it as $\mathrm{FO}^2$.

### Generalizations

The two-variable logic with counting quantifiers $\exists^{\ge n}$, written $\mathrm{C}^2$, is decidable.
Grädel, Otto and Rosen proved this in 1997, and Pacholski, Szwast and Tendera proved it independently.
Pratt-Hartmann proved in 2005 that satisfiability of $\mathrm{C}^2$ is in NEXPTIME, also with the numbers $n$ written in binary.
The [[guarded fragment|Y7YS1C3GAE]] extends the modal side of $\mathrm{FO}^2$ in another direction, by restricting quantifiers instead of variables.

### Try it

Is $\forall x \, \forall y \, (R(x, y) \to R(y, x))$ in $\mathrm{FO}^2$, and is it satisfiable?
Yes to both: it uses only $x$ and $y$, and the one-element structure with $R$ empty is a model.

Put $\forall x \, \exists y \, R(x, y)$ in Scott normal form.
It is already in that form, with $\chi$ true and $m = 1$, $\chi_1 = R(x, y)$.

## History

Scott introduced the normal form in 1962 and reduced the two-variable fragment without equality to the Gödel class.
Mortimer proved in 1975 that two-variable logic with equality has the finite model property, so it is decidable.
Grädel, Kolaitis and Vardi proved in 1997 that every satisfiable sentence has a model of exponential size, and that satisfiability is NEXPTIME-complete.

## Explanations

### L1 human

A logical statement uses names such as $x$ and $y$ for the objects it talks about.
If a statement may use only two names, and may reuse them, it can still say a lot, for example "everyone has a friend who has a friend".
Such statements are always decidable by a computer.
The reason is that a statement with two names cannot force an infinite world.
Whenever it has a world, it has a finite one, and the computer can search for it.

### L2 human

We put $\varphi = \forall x \, \exists y \, (R(x, y) \wedge \exists x \, (R(y, x) \wedge P(x)))$ in Scott normal form.
The innermost quantified part is $\exists x \, (R(y, x) \wedge P(x))$, with free variable $y$, so we name it with a new unary symbol $A$ and write $A(y)$ instead.
The outer part becomes a sentence of the shape $\forall x \, \exists y \, \chi_1$:
$$\forall x \, \exists y \, (R(x, y) \wedge A(y)).$$
Next we write down what $A$ means.
The direction "if $y$ has a successor in $P$, then $A(y)$" becomes a universal condition on pairs, and the direction "if $A(x)$, then $x$ has a successor in $P$" becomes a witness demand:
$$\forall x \, \forall y \, (R(y, x) \wedge P(x) \to A(y)), \qquad \forall x \, \exists y \, (A(x) \to R(x, y) \wedge P(y)).$$
The normal form $\psi$ is the conjunction of these three sentences.
Check: in the model with domain $\{a, b\}$, $R = \{ (a, b), (b, a) \}$ and $P = \{ a, b \}$, put $A = \{ a, b \}$, and all three conjuncts hold.

The typical use of the normal form is to reduce every question about $\mathrm{FO}^2$ to the simple shape $\forall \forall \wedge \forall \exists$.
Watch out: the new symbols must get the meaning that their definitions give, or the expansion fails.

### L3 human

Two-variable logic is the first-order counterpart of modal logic.
The standard translation of modal formulas uses two variables, and both logics have a small model property.
The proof of the exponential model property is surgery on models, with "kings", elements whose 1-type occurs once, and three levels of copies of the other elements that serve as witnesses for each other in a cycle.
Extensions with counting, with two equivalence relations, or with a linear order have been studied in detail, and some remain decidable while others do not.
The [[guarded fragment|Y7YS1C3GAE]] and the [[decidable prefix classes|ZF79MZRQ8V]] are the other main families of decidable fragments in the classical decision problem.
