---
tag: 1C6CGH1G6A
kind: example
name: The quantifier most is not first-order definable
msc: ["03C80", "03C13"]
topics: [MDHDYV8QZW]
audience: grad
uses: [MFV98WTF4G, 2RE7YAZK8R, 086QKPF0A6]
instance_of: [MFV98WTF4G]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Conservativity
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht–Fraïssé_game
    locator: lead section
---

## Example

"Most $A$ are $B$" compares two counts, and a first-order sentence can only count up to its quantifier rank.
So no first-order sentence can say "most", even on finite structures.
The quantifier $\mathrm{most}$ is the class of all structures $(M, A, B)$ with $A, B \subseteq M$ and $|A \cap B| > |A \setminus B|$.
We check that it is a [[generalized quantifier|MFV98WTF4G]] of type $\langle 1, 1 \rangle$, and that it is conservative.
Then we show that no [[first-order|086QKPF0A6]] sentence defines it on finite structures.

1. First we check isomorphism invariance.
   Let $f \colon M \to M'$ be a bijection with $f[A] = A'$ and $f[B] = B'$.
   Then $f$ maps $A \cap B$ onto $A' \cap B'$, and $A \setminus B$ onto $A' \setminus B'$, so both counts stay the same.
2. Next we check conservativity, which says that only the elements of $A$ matter.
   If we replace $B$ by $A \cap B$, the two sets that we count do not change:
   $$A \cap (A \cap B) = A \cap B, \qquad A \setminus (A \cap B) = A \setminus B.$$
   So $\mathrm{most}_M(A, B)$ holds exactly when $\mathrm{most}_M(A, A \cap B)$ holds.
3. Now suppose that a first-order sentence $\varphi$ defines $\mathrm{most}$ on finite structures.
   Its vocabulary has two unary predicates $A$ and $B$.
   Let $k$ be the quantifier rank of $\varphi$.
4. We build two finite structures $\mathcal{M}_1 = (M_1, M_1, B_1)$ and $\mathcal{M}_2 = (M_2, M_2, B_2)$, so $A$ is the whole domain in both.
   The sizes of the parts are these:
   $$|B_1| = k + 1, \quad |M_1 \setminus B_1| = k, \qquad |B_2| = k, \quad |M_2 \setminus B_2| = k + 1.$$
5. Since $A$ is the whole domain, $A \cap B$ is $B_i$ and $A \setminus B$ is $M_i \setminus B_i$.
   So $\varphi$ is true in $\mathcal{M}_1$ and false in $\mathcal{M}_2$.
   Check: $k + 1 > k$ is true, and $k > k + 1$ is false.
6. We give a winning strategy for the duplicator in the $k$-round [[Ehrenfeucht–Fraïssé game|2RE7YAZK8R]] on $\mathcal{M}_1$ and $\mathcal{M}_2$.
   If the spoiler picks an element that was picked before, the duplicator answers with its partner.
7. If the spoiler picks a new element of $B_i$, the duplicator picks a new element of $B_{3-i}$.
   The same rule holds outside $B_i$ and $B_{3-i}$.
   Each of the four parts has at least $k$ elements, and at most $k - 1$ elements were picked before, so a new element exists.
8. After $k$ rounds the picked pairs form a partial isomorphism.
   Equal picks match equal picks, distinct picks match distinct picks, and membership in $A$ and in $B$ agrees.
9. By the Ehrenfeucht-Fraïssé theorem, $\mathcal{M}_1$ and $\mathcal{M}_2$ satisfy the same sentences of quantifier rank at most $k$.
   This contradicts step 5, so no such $\varphi$ exists.

## Remarks

The two structures differ only by a count, and a sentence of quantifier rank $k$ can only count up to $k$ in each part.
That is the whole idea of the proof.

Steps 4 to 9 use only the case where $A$ is the whole domain.
So they also show that the Rescher quantifier $Q^R$, "more than half of the elements", is not first-order definable on finite structures.

Not every generalized quantifier escapes first-order logic.
The quantifier $\exists^{\geq 3}$, "at least three", is first-order definable, because a sentence with three existential quantifiers can count to $3$.
The difference is that $3$ is a fixed number, while $\mathrm{most}$ compares two counts that can both grow without bound.

Step 2 shows conservativity.
Barwise and Cooper proposed this property for all determiners of natural language.

## Explanations

### L1 human

"Most balls are red" asks whether the red balls outnumber the other balls.
Take a bag with $4$ red balls and $3$ blue balls, and another bag with $3$ red balls and $4$ blue balls.
A player who may look at only $3$ balls at a time cannot tell the two bags apart.
Each bag has at least $3$ balls of each color, so each choice of $3$ balls in one bag has a copy in the other.
First-order logic sees a structure in the same limited way, as a fixed number of looks.
So no first-order sentence says "most".

### L2 human

We play the game with $k = 2$.
In $\mathcal{M}_1$ let $B_1 = \{a, b, c\}$ and $M_1 \setminus B_1 = \{d, e\}$.
In $\mathcal{M}_2$ let $B_2 = \{p, q\}$ and $M_2 \setminus B_2 = \{r, s, t\}$.

1. The spoiler picks $a \in B_1$, and the duplicator answers $p \in B_2$.
2. The spoiler picks $q \in B_2$, and the duplicator answers $b \in B_1$, a new element of $B_1$.
3. The picks are $(a, p)$ and $(b, q)$.
   Both pairs lie in $B$, and $a \neq b$ and $p \neq q$.
   So the map $a \mapsto p$, $b \mapsto q$ is a partial isomorphism, and the duplicator wins.

Check: each part has at least $k = 2$ elements, since $|B_2| = 2$ and $|M_1 \setminus B_1| = 2$, so the duplicator never runs out of new elements.

The typical use of this argument is to prove that a counting property is not first-order.
Watch out: the structures must have at least $k$ elements in each part.
With $|B_2| = 1$, the spoiler wins in $2$ rounds by picking two different elements of $B_1$.
