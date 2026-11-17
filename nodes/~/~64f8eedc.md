---
tag: ~64f8eedc
kind: example
name: The non-self-membered sets form a plurality but not a set
msc: ["03A05", "03E30"]
topics: [MDHDYV8QZW]
audience: research
uses: [~8cf214d8, 0HESMMSYEG, 0HE5WDQ9FJ, NFQ9FVCP31]
instance_of: [~8cf214d8]
sources:
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Russell%27s_paradox
    locator: lead section
---

## Example

We work in [[plural logic|~8cf214d8]] over the domain of all sets of [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]], with the membership relation $\in$.
Plural comprehension gives, for each formula $\varphi(y)$ in which $xx$ is not free,
$$\exists y \, \varphi(y) \to \exists xx \, \forall y \, \big( y \prec xx \leftrightarrow \varphi(y) \big).$$
We apply it to $\varphi(y) = y \notin y$, the formula of [[Russell's paradox|0HESMMSYEG]].

1. The empty set $\emptyset$ has no members, so $\emptyset \notin \emptyset$. So $\exists y \, (y \notin y)$ is true.
2. By comprehension there are some sets $rr$ with $\forall y \, (y \prec rr \leftrightarrow y \notin y)$: they are exactly the sets that are not members of themselves.
3. By the [[axiom of regularity|NFQ9FVCP31]], no set is a member of itself. So every set is one of $rr$.
4. Suppose that some set $r$ has exactly $rr$ as its members: $\forall y \, (y \in r \leftrightarrow y \prec rr)$.
5. Then $r \in r \iff r \prec rr \iff r \notin r$, by step 4 and then step 2 with $y = r$. This is a contradiction.
6. So there are some sets that are exactly the non-self-membered sets, and no set has exactly them as members.

## Remarks

The example shows how plural logic avoids Russell's paradox: comprehension produces some things, and no axiom produces an object whose members are these things.
Russell's argument in step 5 needs such an object, and it proves only that none exists.
The formula $rr \prec rr$ is not even well formed, because the left place of $\prec$ takes a singular term.
In naive set theory, the step from step 2 to an object is the unrestricted comprehension axiom, and it is that axiom that fails.
The plurality $rr$ is what [[von Neumann–Bernays–Gödel set theory|JTPZ1HZ9KK]] treats as a proper class, here without a class object.
If we replace $\varphi(y)$ by $y \notin y \land y \in a$ for a set $a$, the separation axiom gives a set with these members.
The argument then shows only that this set is not in $a$.

## Explanations

### L1 human

Some collections are too large to be a single set, such as "all sets that are not members of themselves".
Russell showed that treating this collection as one set leads to a contradiction.
Plural logic lets us still talk about these sets together: "there are some sets that are exactly the sets not members of themselves".
The sentence is about many sets at once, and it does not claim that they form one new set.
So the contradiction does not arise.

### L2 human

We run the same argument for $\varphi(y) = (y \notin y \land y \in a)$ with $a = \{ \emptyset, \{\emptyset\} \}$.

1. Both members of $a$ are not members of themselves, so the sets satisfying $\varphi$ are $\emptyset$ and $\{\emptyset\}$.
2. Comprehension gives some sets $xx$ that are exactly $\emptyset$ and $\{\emptyset\}$.
3. Here a set with exactly these members exists, namely $a$ itself.
4. The Russell argument for $r = a$ gives: $a \in a$ if and only if $a \notin a \land a \in a$. Since $a \notin a$, both sides are false, and there is no contradiction.

The typical use of the example is the plural reading of proper classes in set theory.
A trap is to think that plural comprehension is unrestricted set comprehension in disguise: it never asserts that a set or class exists.
