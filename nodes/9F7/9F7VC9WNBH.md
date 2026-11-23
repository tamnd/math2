---
tag: 9F7VC9WNBH
kind: example
name: A disjunction of two variables is not a Horn clause
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: QR92EZDTKF
    note: the clause p ∨ q has two positive literals, and no set of Horn clauses is equivalent to it, because its models {p} and {q} have the intersection ∅, which is not a model
uses: [T3SXVH3ZZC, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
---

## Example

Let $p$ and $q$ be distinct propositional variables, and let $C = \{ p, q \}$, the [[clause|T3SXVH3ZZC]] $p \lor q$.
We show that $C$ is not a [[Horn clause|QR92EZDTKF]], and that no set of Horn clauses is even equivalent to it.

1. The literals $p$ and $q$ are both positive, so $C$ has two positive literals and is not a Horn clause.
2. Suppose that a set $S$ of Horn clauses, in any variables, has the same models as $C$.
3. Let $v_1$ make $p$ true and every other variable false, and let $v_2$ make $q$ true and every other variable false.
   Both make $p \lor q$ true, so both are models of $S$.
4. By the intersection property of Horn clauses, the assignment $u$ with
$$u(x) = \min(v_1(x), v_2(x))$$
   for each variable $x$ is also a model of $S$.
5. But $u(p) = \min(1, 0) = 0$ and $u(q) = \min(0, 1) = 0$, so $u$ makes $p \lor q$ false, which contradicts step 2.

So no set of Horn clauses is equivalent to $p \lor q$.

## Remarks

The example shows that Horn formulas are not closed under disjunction, although $p$ and $q$ are each Horn formulas.
One sign makes the difference.
The clause $\neg p \lor q$ is a Horn clause, and replacing a variable by its negation everywhere can turn some non-Horn sets into Horn sets; such sets are called renamable Horn.

The failure also shows up in the models.
A set of definite clauses has a least model, but $p \lor q$ has two minimal models, $\{ p \}$ and $\{ q \}$, and no least one.
This is why logic programs whose rules have disjunctive heads need a different semantics.

## Explanations

### L1 human

"Pia comes or Quin comes" leaves a choice.
A Horn rule never leaves a choice: from what is known, it either forces one more thing or forbids a combination.
So no list of Horn rules can say exactly "Pia or Quin".
Such rules would have to allow "only Pia" and "only Quin" and forbid "nobody", and that needs a choice.

### L2 human

We find the minimal models of $p \lor q$ over the variables $p$ and $q$.
The models are $\{ p \}$, $\{ q \}$ and $\{ p, q \}$.
The model $\{ p, q \}$ is not minimal, since $\{ p \}$ is a smaller model.
The models $\{ p \}$ and $\{ q \}$ are minimal, since their only proper subset, $\emptyset$, is not a model.
So there are two minimal models and no least model.
The method is general: to show that a property cannot be written with Horn clauses, find two models whose intersection is not a model.
Watch out: $p \lor q$ is still easy to satisfy; the point is only that the marking algorithm and the least-model semantics do not apply to it.
