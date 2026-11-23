---
tag: GBG2F2PWJ3
kind: example
name: Defining the order relation in Peano arithmetic
msc: ["03F30", "03B10"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [GCK0NN60E4]
uses: [GCK0NN60E4, 0QFT7Z76N5, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Extension_by_definition
    locator: lead section
---

## Example

We know that $3 \le 5$ because $3 + 2 = 5$.
Peano arithmetic has no symbol for $\le$, but this observation turns into a definition, and the definition adds nothing but notation.

Let PA be [[Peano arithmetic|0QFT7Z76N5]] in the language $L = \{ 0, S, +, \cdot \}$, with the axioms $x + 0 = x$ and $x + S(y) = S(x + y)$ for addition and the induction schema.
Let $L' = L \cup \{ \le \}$, and let $T' = \mathsf{PA} \cup \{ \delta \}$ with the defining axiom
$$\delta: \quad \forall x\, \forall y\, \big( x \le y \leftrightarrow \exists z\, (x + z = y) \big).$$
We check that $T'$ is an [[extension by definitions|GCK0NN60E4]] and translate one theorem.

1. The definiens $\exists z\, (x + z = y)$ is an $L$-formula with free variables $x$ and $y$, and $\le$ is a relation symbol.
   So no existence or uniqueness condition is needed, and $T'$ is an extension by definitions.
2. The sentence $\forall x\, (0 \le x)$ of $L'$ has the translation $\forall x\, \exists z\, (0 + z = x)$.
   We get it by replacing the atomic formula $0 \le x$ by its definiens.
3. We prove $\forall x\, (0 + x = x)$ in PA by [[induction|0ASJVEFA9J]] on $x$.
   Base case: $0 + 0 = 0$ by the axiom $x + 0 = x$.
4. Induction step: assume $0 + x = x$.
   Then $0 + S(x) = S(0 + x)$ by the axiom $x + S(y) = S(x + y)$, and $S(0 + x) = S(x)$ by the assumption.
5. So $\mathsf{PA} \vdash \forall x\, (0 + x = x)$.
   For each $x$, the witness $z = x$ gives $\exists z\, (0 + z = x)$.
6. So PA proves the translation, and $T' \vdash \forall x\, (0 \le x)$ by the defining axiom.
7. In the same way $\forall x\, (x \le x)$ translates to $\forall x\, \exists z\, (x + z = x)$.
   PA proves it with the witness $z = 0$ and the axiom $x + 0 = x$.

## Remarks

### Models

In the standard model $\mathbb{N}$ the only expansion that satisfies $\delta$ reads $\le$ as the usual order, as the unique expansion theorem predicts.
In a nonstandard model of PA, $\le$ is read as the order of that model, in which every nonstandard element lies above all standard numbers.

### More abbreviations

The strict order comes next, by $x < y \leftrightarrow \exists z\, (x + S(z) = y)$.
Then the bounded quantifiers $\forall x \le t$ and $\exists x \le t$ are abbreviations as well.
These abbreviations define the levels of the arithmetical hierarchy, so every text on formal arithmetic uses the theorem on extensions by definitions.

### Watch out

Over a theory without induction, the same definition is still an extension by definitions.
But the translated sentence of step 2 may stop being a theorem, since step 3 used induction.
A definition is always harmless, but it does not make old facts easier to prove.

## Explanations

### L1 human

The symbol "$\le$" is not one of the basic symbols of arithmetic in Peano's axioms.
We can define it: "$a \le b$" means "some number added to $a$ gives $b$".
For example $3 \le 5$, because $3 + 2 = 5$.
Every statement with "$\le$" can be rewritten with addition instead, so the new symbol adds no new facts.

### L2 human

We translate and check the sentence $\forall x\, \forall y\, \forall w\, (x \le y \land y \le w \to x \le w)$.

1. Replace each atomic formula with $\le$ by its definiens, with a new bound variable each time.
   The result is $\forall x\, \forall y\, \forall w\, (\exists z_1\, (x + z_1 = y) \land \exists z_2\, (y + z_2 = w) \to \exists z_3\, (x + z_3 = w))$.
2. Given $z_1$ and $z_2$, take $z_3 = z_1 + z_2$.
3. Then $x + (z_1 + z_2) = (x + z_1) + z_2 = y + z_2 = w$, by the associativity of addition, which PA proves by induction.

The typical use is to work with $\le$ as if it were basic, and to know that each result is a theorem of PA in the original language.
Watch out: if you use the same bound variable $z$ for the three definientia in step 1, you can confuse the three witnesses.
