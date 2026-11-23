---
tag: B37TYWXS74
kind: concept
name: Equisatisfiability
aliases: [equisatisfiable]
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
uses: [QN7M1JCGT9, 0JMR2HM2N2, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Equisatisfiability
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Tseitin_transformation
    locator: Approach
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
same_as:
  wikidata: Q2402183
  wikipedia: Equisatisfiability
inventory: [G7XH6MR18A]
---

## Summary

Compare $p \lor q$ with $(p \lor x) \land (\neg x \lor q)$, where $x$ is a new variable.
They are not equivalent: $p = 1$, $q = 0$, $x = 1$ makes the first true and the second false.
But each is [[satisfiable|QN7M1JCGT9]] exactly when the other is, because a model of $p \lor q$ becomes a model of the second formula after we choose $x$ well.

Two formulas, or two sets of formulas, are *equisatisfiable* when both are satisfiable or both are unsatisfiable.
They may contain different variables, and the definition says nothing about which assignments satisfy them.
Equisatisfiability is much weaker than [[logical equivalence|0JMR2HM2N2]].
But it is the property that the conversions to clause form keep, such as the [[Tseitin transformation|S367PDDP61]] and [[Skolemization|GCPQGMJYEV]], and it is all that a satisfiability test needs.

## Motivation

A satisfiability solver takes its input in [[conjunctive normal form|0B3D4C8YF2]].
Every formula is equivalent to a formula in conjunctive normal form, but the equivalent form can be very long.
The formula $(p_1 \land q_1) \lor \cdots \lor (p_n \land q_n)$ has $2n$ variable occurrences, and the distributive law turns it into $2^n$ clauses.

If we only want to know whether the formula is satisfiable, we may add new variables that name subformulas and get a formula of linear size.
The new formula is not equivalent to the old one, because it speaks about more variables, but it is satisfiable exactly when the old one is.
Equisatisfiability names this weaker link, and it tells us what we may and may not conclude from it.

## Notation

There is no standard symbol for equisatisfiability.
Some authors write $\varphi \approx_{\mathrm{sat}} \psi$ or $\varphi \equiv_{\mathrm{sat}} \psi$, and others write the word out.
Compare it with logical equivalence $\varphi \equiv \psi$, which says $\bar v(\varphi) = \bar v(\psi)$ for every truth assignment $v$.

## Remarks

### Equisatisfiable pairs and other pairs

The pair in the Summary is worked out in [[splitting a clause|5ZPK7DC8MK]].
The formulas $p$ and $\neg p$ are equisatisfiable, since both are satisfiable, but no assignment makes both true; see [[a formula and its negation|PW6JP5ZK4D]].
Any two satisfiable formulas are equisatisfiable, such as $p$ and $q \land r$.
Any two unsatisfiable ones are too, such as $p \land \neg p$ and $\{ q, \; \neg q \lor r, \; \neg r \}$.

In first-order logic, $\forall x \, \exists y \, R(x, y)$ and its Skolem form $\forall x \, R(x, f(x))$, with a new function symbol $f$, are equisatisfiable.
They are not equivalent, since a structure can satisfy the first sentence and interpret $f$ as a function that does not pick witnesses.

On the other side, $p$ and $p \land \neg p$ are not equisatisfiable, because only the first is satisfiable; see [[the non-example|M1HY02BDTV]].
Nor are $\{ p, \; p \to q \}$ and $\{ p, \; p \to q, \; \neg q \}$, since $v(p) = v(q) = 1$ satisfies the first and the second is unsatisfiable.

### What it keeps and what it loses

Equisatisfiability is an equivalence relation with exactly two classes: the satisfiable formulas and the unsatisfiable ones.
Equivalent formulas are equisatisfiable, but $p$ and $\neg p$ show that the converse fails.
To decide whether $\varphi$ is satisfiable, we may decide it for any equisatisfiable $\psi$, and that is the whole use of the notion.

It does not keep validity.
The formulas $p \lor \neg p$ and $p$ are equisatisfiable, but only the first is a [[tautology|05006AJ7DZ]].
To test whether $\varphi$ is valid, we test whether a formula equisatisfiable with $\neg \varphi$ is unsatisfiable.

It does not keep [[logical consequence|1HK0VYWTV7]].
We have $p \models p$, and $q$ is equisatisfiable with $p$, but $q \not\models p$.

It is not compatible with the connectives.
The formulas $p$ and $q$ are equisatisfiable, but $p \land \neg p$ is unsatisfiable while $q \land \neg p$ is satisfiable.

### Naming a subformula

The basic step of the Tseitin transformation names a subformula with a new variable.
Let $\chi$ and $\psi$ be formulas, let $x$ be a variable that does not occur in $\psi$, and let $\chi[\psi / x]$ be $\chi$ with every occurrence of $x$ replaced by $\psi$.
Then $\chi[\psi / x]$ and $\chi \land (x \leftrightarrow \psi)$ are equisatisfiable.

The proof uses the substitution property, proved by [[induction on formulas|EDRV3N0SA3]]: if $v(x) = \bar v(\psi)$, then $\bar v(\chi[\psi / x]) = \bar v(\chi)$.

1. Let $v$ satisfy $\chi[\psi / x]$, and let $v'$ agree with $v$ except that $v'(x) = \bar v(\psi)$.
2. Since $x$ does not occur in $\psi$, $\bar v'(\psi) = \bar v(\psi) = v'(x)$, so $v'$ makes $x \leftrightarrow \psi$ true.
3. Since $x$ does not occur in $\chi[\psi / x]$, $v'$ makes $\chi[\psi / x]$ true, and by the substitution property it makes $\chi$ true.
4. Conversely, let $v$ satisfy $\chi \land (x \leftrightarrow \psi)$.
   Then $v(x) = \bar v(\psi)$, so $\bar v(\chi[\psi / x]) = \bar v(\chi) = 1$.

### Naming a subformula, continued

The two formulas need not be equivalent.
For $\chi = x$ and $\psi = p$, the assignment $v(p) = 1$, $v(x) = 0$ makes $p$ true and $x \land (x \leftrightarrow p)$ false.

The proof gives more than equisatisfiability.
Every model of $\chi[\psi / x]$ extends to a model of $\chi \land (x \leftrightarrow \psi)$, and every model of the second restricts to a model of the first.
This stronger link survives repetition with fresh variables, which is why the Tseitin transformation can name all subformulas one after another.

### Watch out

Do not replace a formula by an equisatisfiable one inside a larger formula.
The last example of the previous section shows that this can change the satisfiability of the whole formula.

Do not use an equisatisfiable form to test validity directly.
First negate, then transform, then test for unsatisfiability.

When you do the Tseitin transformation by hand, do not reuse one new variable for two different subformulas.
Each new variable must be fresh.

### History

The word is used mainly in automated reasoning, where the conversion to clause form keeps only satisfiability.
Grigori Tseitin introduced the conversion into an equisatisfiable conjunctive normal form of linear size that carries his name.
Skolemization, named after Thoralf Skolem, plays the same role for the quantifiers of first-order logic.

### Try it

Are $p \land q$ and $(p \lor x) \land \neg x \land q$ equisatisfiable?
Yes: $\neg x$ forces $x = 0$, so the second formula has the value of $p \land q$ for the old variables, and both are satisfiable.
Are they equivalent?
No: with $p = q = x = 1$ the first is true and the second is false.

## Explanations

### L1 human

Two puzzles are equisatisfiable when both have a solution or both have none.
The puzzles may be very different, and their solutions may look nothing alike.
"Pick a number that is even" and "pick a number that is odd" both have solutions, so they are equisatisfiable, even though no number solves both.
If we only want to know whether a puzzle has a solution, we may swap it for an easier equisatisfiable puzzle.

### L2 human

We use new variables to shorten a conjunctive normal form.
Let $\varphi = (p_1 \land q_1) \lor (p_2 \land q_2)$.

1. By distribution, $\varphi$ is equivalent to $(p_1 \lor p_2) \land (p_1 \lor q_2) \land (q_1 \lor p_2) \land (q_1 \lor q_2)$.
2. Take a new variable $x$ for $p_1 \land q_1$ and a new variable $y$ for $p_2 \land q_2$.
3. Let $\psi = (x \lor y) \land (\neg x \lor p_1) \land (\neg x \lor q_1) \land (\neg y \lor p_2) \land (\neg y \lor q_2)$.
4. If $v$ satisfies $\varphi$, set $v(x) = \bar v(p_1 \land q_1)$ and $v(y) = \bar v(p_2 \land q_2)$, and then $v$ satisfies $\psi$.
5. If $v$ satisfies $\psi$, then $v(x) = 1$ or $v(y) = 1$, which forces $p_1 = q_1 = 1$ or $p_2 = q_2 = 1$, so $v$ satisfies $\varphi$.

For $n$ disjuncts, distribution gives $2^n$ clauses, while this method gives $2n + 1$.
A solver gets $\psi$, and a model of $\psi$ restricted to the old variables is a model of $\varphi$.
Check: $\psi$ is not equivalent to $\varphi$, since all $p_i$, $q_i$ true with $x = y = 0$ satisfies $\varphi$ and falsifies $x \lor y$.

### L3 human

Equisatisfiability by itself is a coarse relation with only two classes.
So the useful transformations meet a stronger condition: every model of $\psi$ restricts to a model of $\varphi$, and every model of $\varphi$ extends to a model of $\psi$.
In first-order terms $\psi$ is then a conservative extension of $\varphi$ in a richer language, and this relation is kept when we combine steps that use disjoint sets of new symbols.
Skolemization has the same form, with new function symbols in place of new variables, and in general its extension step uses the axiom of choice to pick the witnesses.
In complexity theory, polynomial-time reductions between satisfiability problems, such as the reduction of SAT to 3-SAT, are maps that keep satisfiability status, and the [[Boolean satisfiability problem|3QKF32ZAKN]] is studied up to such maps.
