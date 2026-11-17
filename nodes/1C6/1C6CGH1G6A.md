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

The quantifier $\mathrm{most}$ is the class of all structures $(M, A, B)$ with $A, B \subseteq M$ and $|A \cap B| > |A \setminus B|$.
We check that it is a [[generalized quantifier|MFV98WTF4G]] of type $\langle 1, 1 \rangle$, that it is conservative, and that no [[first-order|086QKPF0A6]] sentence defines it on finite structures.

1. Isomorphism invariance. Let $f \colon M \to M'$ be a bijection with $f[A] = A'$ and $f[B] = B'$. Then $f$ maps $A \cap B$ onto $A' \cap B'$ and $A \setminus B$ onto $A' \setminus B'$, so both cardinalities are preserved.
2. Conservativity. We have $A \cap (A \cap B) = A \cap B$ and $A \setminus (A \cap B) = A \setminus B$, so $\mathrm{most}_M(A, B)$ holds exactly when $\mathrm{most}_M(A, A \cap B)$ holds.
3. Suppose that a first-order sentence $\varphi$ in the vocabulary of two unary predicates $A, B$ is true in a finite $(M, A, B)$ exactly when $|A \cap B| > |A \setminus B|$. Let $k$ be the quantifier rank of $\varphi$.
4. Let $\mathcal{M}_1 = (M_1, M_1, B_1)$ with $|B_1| = k + 1$ and $|M_1 \setminus B_1| = k$. Let $\mathcal{M}_2 = (M_2, M_2, B_2)$ with $|B_2| = k$ and $|M_2 \setminus B_2| = k + 1$. In both, $A$ is the whole domain.
5. Then $\varphi$ is true in $\mathcal{M}_1$, since $k + 1 > k$, and false in $\mathcal{M}_2$, since $k \not> k + 1$.
6. We give a winning strategy for the duplicator in the $k$-round [[Ehrenfeucht–Fraïssé game|2RE7YAZK8R]] on $\mathcal{M}_1$ and $\mathcal{M}_2$. If the spoiler picks an element that was picked before, the duplicator answers with its partner.
7. If the spoiler picks a new element of $B_i$, the duplicator picks a new element of $B_{3-i}$. The same rule holds outside $B_i$ and $B_{3-i}$. Each part has at least $k$ elements, and at most $k - 1$ elements were picked before, so a new element exists.
8. After $k$ rounds the picked elements form a partial isomorphism. Equal picks match equal picks, distinct picks match distinct picks, and membership in $A$ and $B$ agrees.
9. By the Ehrenfeucht-Fraïssé theorem, $\mathcal{M}_1$ and $\mathcal{M}_2$ satisfy the same sentences of quantifier rank at most $k$. This contradicts step 5, so no such $\varphi$ exists.

## Remarks

Steps 4 to 9 use only the case $A = M$.
So they also show that the Rescher quantifier $Q^R$ ("more than half of the elements") is not first-order definable on finite structures.
The two structures differ by a count, and a sentence of quantifier rank $k$ can only count up to $k$ in each part.
In contrast, $\exists^{\geq 3}$ is a generalized quantifier that is first-order definable, since it needs only three variables and the count $3$.
If $k$ is replaced by a larger number in step 4, the argument works for every sentence of rank at most that number.
Step 2 shows conservativity, the property that Barwise and Cooper proposed for all determiners of natural language.

## Explanations

### L1 human

"Most balls are red" asks whether the red balls outnumber the other balls.
Take a bag with $4$ red balls and $3$ blue balls, and another with $3$ red balls and $4$ blue balls.
A player who may look at only $3$ balls at a time cannot tell the two bags apart.
Each bag has at least $3$ balls of each color, so each choice of $3$ balls in one bag has a copy in the other.
First-order logic sees a structure in the same limited way, as a fixed number of looks.
So no first-order sentence says "most".

### L2 human

We play the $2$-round game with $k = 2$ on $\mathcal{M}_1$ with $B_1 = \{a, b, c\}$, $M_1 \setminus B_1 = \{d, e\}$, and $\mathcal{M}_2$ with $B_2 = \{p, q\}$, $M_2 \setminus B_2 = \{r, s, t\}$.

1. The spoiler picks $a \in B_1$. The duplicator answers $p \in B_2$.
2. The spoiler picks $q \in B_2$. The duplicator answers $b \in B_1$, a new element of $B_1$.
3. The picks are $(a, p)$ and $(b, q)$. Both pairs are in $B$, and $a \neq b$, $p \neq q$. So the map $a \mapsto p$, $b \mapsto q$ is a partial isomorphism, and the duplicator wins.

The typical use of the argument is to prove that a counting property is not first-order.
A trap is to choose structures with too few elements in one part.
With $|B_2| = 1$ the spoiler wins in $2$ rounds by picking two different elements of $B_1$.
