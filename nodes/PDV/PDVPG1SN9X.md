---
tag: PDVPG1SN9X
kind: example
name: The tree classes O₁ and O₂ as iterated inductive definitions
msc: ["03F15", "03D70"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [5VNT564Y2W]
uses: [45GQ3KQVT3, WHAP0K600D, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: ID<sub>ν</sub>
  - url: https://en.wikipedia.org/wiki/Kleene%27s_O
    locator: Definition
---

## Example

Let $\{ e \}(n)$ be the result of the $e$-th partial [[computable function|KZSB5E471K]] on input $n$, and let $\langle a, b \rangle$ be a pairing function on $\mathbb{N}$.
We write "$\{ e \}(n) \in X$" for the positive formula $\exists m \, (\{ e \}(n) \text{ halts with output } m \wedge X(m))$.
The operator of the first tree class is
$$A_1(X, x) = (x = 0) \vee \exists y \, (x = \langle 1, y \rangle \wedge X(y)) \vee \exists e \, \big( x = \langle 2, e \rangle \wedge \forall n \, (\{ e \}(n) \in X) \big).$$
The operator of the second tree class has one more clause, which branches over the first class $\mathcal{O}_1$:
$$A_2(X, Y, x) = A_1(X, x) \vee \exists e \, \big( x = \langle 3, e \rangle \wedge \forall a \, (Y(a) \to \{ e \}(a) \in X) \big).$$
We check that these operators define $\mathcal{O}_1$ and $\mathcal{O}_2$ in $\mathrm{ID}_2$, in the sense of the [[definition|45GQ3KQVT3]].

1. Take $\prec$ on $\{ 0, 1 \}$ with $0 \prec 1$, a primitive recursive well-ordering of type $2$.
2. Let $A(X, Y, \mu, x)$ be $A_1(X, x)$ when $\mu = 0$ and $A_2(X, Y(0, \cdot), x)$ when $\mu = 1$, which is one formula by cases on $\mu$.
3. In $A_1$ the variable $X$ stands only under $\exists$, $\forall$, $\wedge$ and $\vee$.
   In the new clause of $A_2$ it stands in the consequent of $\to$, which is a positive place.
4. The predicate $Y$ occurs negatively in $A_2$, in the antecedent $Y(a)$, and the definition of $\mathrm{ID}_\nu$ allows this.
5. So stage $0$ is $\mathcal{O}_1 = P^0_A$, and stage $1$ is $\mathcal{O}_2 = P^1_A$, the least fixed point of $A_2(\cdot, \mathcal{O}_1, \cdot)$.

In the standard model, $\mathcal{O}_1$ is the set of codes of well-founded computable trees that branch over $\mathbb{N}$, and $\mathcal{O}_2$ also contains trees that branch over all members of $\mathcal{O}_1$.

## Remarks

The example shows why the stages are iterated.
The clause $\forall a \, (a \in \mathcal{O}_1 \to \dots)$ uses $\mathcal{O}_1$ negatively, so it cannot be part of the same positive definition as $\mathcal{O}_1$.
In $\mathrm{ID}_2$ the class $\mathcal{O}_1$ is fixed at an earlier stage, and after that it may appear anywhere.
Going on, $\mathcal{O}_{\mu + 1}$ branches over $\mathcal{O}_\mu$, and the theory $\mathrm{ID}^i_\nu(\mathcal{O})$ has exactly these tree classes for $\mu < \nu$, over intuitionistic logic.

The class $\mathcal{O}_1$ is close to [[Kleene's O|WHAP0K600D]], which uses the same three kinds of code but also asks that the sequence $\{ e \}(0), \{ e \}(1), \dots$ increase.
Its trees are a constructive model of the countable ordinals, often called Brouwer ordinals.
The class $\mathcal{O}_2$ plays the role of a higher number class, with branching over $\mathcal{O}_1$ in place of $\mathbb{N}$.

## Explanations

### L1 human

A tree in $\mathcal{O}_1$ is a single point, or a point on top of one smaller tree, or a point on top of an infinite list of smaller trees given by a program.
Every branch of such a tree ends after finitely many steps.
A tree in $\mathcal{O}_2$ may also sit on top of a family of trees, with one tree for each tree of $\mathcal{O}_1$.
To define the second kind we must already know which trees are of the first kind, so we build the classes one after the other.

### L2 human

We check that a code for $\omega$ is in $\mathcal{O}_1$.
Let $s_0 = 0$ and $s_{n+1} = \langle 1, s_n \rangle$, and let $e$ be a program with $\{ e \}(n) = s_n$ for every $n$.
The first clause and the closure axiom give $s_0 \in \mathcal{O}_1$, and the second clause gives $s_{n+1} \in \mathcal{O}_1$ from $s_n \in \mathcal{O}_1$.
By induction on $n$, every $s_n$ is in $\mathcal{O}_1$, so the third clause gives $\langle 2, e \rangle \in \mathcal{O}_1$.
The code $s_n$ stands for the number $n$, and $\langle 2, e \rangle$ stands for their limit $\omega$.

These classes serve in the reduction of subsystems of analysis to theories of inductive definitions.
Watch out: putting the clause with $Y$ into $A_1$ itself would make $\mathcal{O}_1$ occur negatively in its own definition.
