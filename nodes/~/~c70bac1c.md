---
tag: ~c70bac1c
kind: example
name: A square root symbol over the theory of fields is not a definition
msc: ["03B10", "12L12"]
topics: [H8QZY0RZXZ]
audience: grad
not_instance_of:
  - target: GCK0NN60E4
    note: "The formula y*y = x does not define a function in every field: square roots need not exist (2 in Q) and need not be unique (1 and -1 in Q); the extension proves a new field-theoretic sentence."
uses: [GCK0NN60E4, N238J43XNE, 04C5ZBG1WT, 0F7FQS6XY6, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Extension_by_definition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: lead section
---

## Example

Let $T$ be the theory of [[fields|04C5ZBG1WT]] in the language $L = \set{0, 1, +, \cdot}$.
Let $s$ be a new unary function symbol, and let $T' = T \cup \set{\forall x \, (s(x) \cdot s(x) = x)}$, which says that $s$ picks a [[square root|0F7FQS6XY6]] of each element.
We show that $T'$ is not an [[extension by definitions|GCK0NN60E4]] of $T$, and not even a [[conservative extension|N238J43XNE]].

1. The instance $x = 1 + 1$ of the axiom gives $T' \vdash s(1 + 1) \cdot s(1 + 1) = 1 + 1$, and so $T' \vdash \exists y \, (y \cdot y = 1 + 1)$. This is an $L$-sentence.
2. The field $\mathbb{Q}$ is a model of $T$. Suppose $(a/b)^2 = 2$ with integers $a, b$, $b > 0$, and the fraction in lowest terms.
3. Then $a^2 = 2b^2$, so $a^2$ is even and $a$ is even. Write $a = 2c$; then $4c^2 = 2b^2$, so $b^2 = 2c^2$ and $b$ is even.
4. Then $2$ divides both $a$ and $b$, which contradicts lowest terms. So $\mathbb{Q} \not\models \exists y \, (y \cdot y = 1 + 1)$.
5. By soundness, $T \nvdash \exists y \, (y \cdot y = 1 + 1)$. With step 1, $T'$ proves a new $L$-sentence, so $T'$ is not conservative over $T$.
6. The condition for a definition of $s$ by $\psi(x, y) = (y \cdot y = x)$ fails in two ways. Existence fails in $\mathbb{Q}$ at $x = 1 + 1$, by step 4.
7. Uniqueness fails in $\mathbb{Q}$ at $x = 1$: both $1$ and $-1$ satisfy $y \cdot y = 1$, and $1 \neq -1$ because $1 + 1 = 2 \neq 0$ in $\mathbb{Q}$.
8. $T'$ is consistent. In $\mathbb{C}$ each number $r e^{i\theta}$ with $r \ge 0$ has the square root $\sqrt{r} \, e^{i\theta/2}$, so a choice of one square root for each element gives a model of $T'$.

## Remarks

The example shows that an axiom that looks like a definition can be a new assumption.
The situation changes over the theory ACF of [[algebraically closed fields|0PF6TM8TWT]].
There every element has a square root, so every model of ACF expands to a model of the axiom for $s$, and the extension is conservative over ACF.
It is still not an extension by definitions, because uniqueness fails, and $s$ cannot be eliminated.
Suppose some $L$-formula $\chi(x)$ had $\forall x \, (\chi(x) \leftrightarrow \exists y \, (y + 1 = 0 \land x = s(y)))$ in this extension; take the model $\mathbb{C}$ with $s(-1) = i$.
Then $\chi$ defines the set $\set{i}$ in the field $\mathbb{C}$, but [[complex conjugation|0FTH2E9TAS]] is a field automorphism that fixes $0$ and $1$, so it maps this set to $\set{-i}$, a contradiction.

## Explanations

### L1 human

A definition must describe exactly one object.
"The square root of $x$" does not do this in the rational numbers.
The number $2$ has no rational square root, and the number $1$ has two square roots, $1$ and $-1$.
Adding a symbol for "the square root" therefore adds a new claim, that square roots exist.

### L2 human

We see the failure in a finite field.

1. In the field $\mathbb{F}_5 = \set{0, 1, 2, 3, 4}$ the squares are $0^2 = 0$, $1^2 = 1$, $2^2 = 4$, $3^2 = 9 = 4$, $4^2 = 16 = 1$.
2. So $2$ and $3$ have no square root in $\mathbb{F}_5$, and $\mathbb{F}_5$ does not expand to a model of $T'$.
3. The element $1$ has the two square roots $1$ and $4$, so even where square roots exist, the choice is not unique.

The typical use of this example is as a warning: before a new function symbol is introduced, existence and uniqueness must be proved in the theory.
A trap is to check only existence, for example in $\mathbb{C}$, where every element has a square root.
Uniqueness fails there, since $i$ and $-i$ both square to $-1$.
