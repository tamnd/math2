---
tag: KAA92JQ7TH
kind: example
name: Grzegorczyk's theory of concatenation TC
msc: ["03F30", "03B25"]
topics: [QHCRN4JVG0]
audience: research
instance_of: [Q5MT8WY7JM]
uses: [92SWXST1ZM, MVCH6N9SNW, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/Concatenation_theory
    locator: lead section
---

## Example

A theory about gluing strings, with no numbers in its language, is already essentially undecidable.
The theory of concatenation $\mathsf{TC}$ has a binary function symbol $\frown$ and two constant symbols $\alpha$ and $\beta$.
Its axioms are the universal closures of these five formulas:

- $\mathsf{TC}1$: $x \frown (y \frown z) = (x \frown y) \frown z$;
- $\mathsf{TC}2$: $x \frown y = u \frown v \to \bigl((x = u \land y = v) \lor \exists w\,((u = x \frown w \land w \frown v = y) \lor (x = u \frown w \land w \frown y = v))\bigr)$;
- $\mathsf{TC}3$: $\alpha \ne x \frown y$;
- $\mathsf{TC}4$: $\beta \ne x \frown y$;
- $\mathsf{TC}5$: $\alpha \ne \beta$.

Axiom $\mathsf{TC}2$ is called the editor axiom: if two splittings of one string differ, then one left part is an initial segment of the other.
### The standard model of strings

The standard model $\mathfrak{S}$ has as domain the set $\{ \mathtt{a}, \mathtt{b} \}^+$ of nonempty finite strings over the letters $\mathtt{a}$ and $\mathtt{b}$.
In it, $\frown$ is concatenation, $\alpha$ is the string $\mathtt{a}$, and $\beta$ is the string $\mathtt{b}$.
We check that $\mathfrak{S} \models \mathsf{TC}$, writing $|s|$ for the length of a string $s$.

1. $\mathsf{TC}1$: both sides are the string $x$ followed by $y$ followed by $z$.
2. $\mathsf{TC}2$: let $x y = u v$.
   If $|x| = |u|$, then $x$ and $u$ are the same prefix of $x y$, so $x = u$, and then $y = v$.
3. If $|x| < |u|$, then $x$ is a proper prefix of $u$.
   So $u = x w$ for a nonempty string $w$, and $x y = x w v$ gives $y = w v$.
4. If $|x| > |u|$, then by the same argument $x = u w$ with $w$ nonempty, and $u w y = u v$ gives $v = w y$.
5. $\mathsf{TC}3$ and $\mathsf{TC}4$: $|\mathtt{a}| = |\mathtt{b}| = 1$, while $|x y| \ge 2$ for nonempty $x$ and $y$.
6. $\mathsf{TC}5$: the strings $\mathtt{a}$ and $\mathtt{b}$ differ.

In steps 3 and 4 the string $w$ is nonempty, so it lies in the domain.
This is why the domain has no empty string.
So $\mathsf{TC}$ is consistent.
Grzegorczyk proved that $\mathsf{TC}$ is undecidable, and Grzegorczyk and Zdanowski proved that it is essentially undecidable.
So $\mathsf{TC}$ is one of the [[weak theories of arithmetic|Q5MT8WY7JM]], although its language has no numbers.

## Remarks

The example shows that the incompleteness phenomenon does not need numbers.
Gödel coded formulas by numbers because his theory spoke about numbers.
$\mathsf{TC}$ speaks about strings, and formulas are strings already.

The number $n \ge 1$ can be represented by the string $\mathtt{a}^n$ of $n$ letters $\mathtt{a}$, and then $\mathtt{a}^n \frown \mathtt{a}^m = \mathtt{a}^{n + m}$.
Multiplication is harder to express, and an interpretation of [[Robinson arithmetic|3K1AKGXF8A]] in $\mathsf{TC}$ needs real work.
Such an interpretation exists, so $\mathsf{TC}$ and $\mathsf{Q}$ are mutually interpretable.

Without $\mathsf{TC}5$, the one-letter structure with domain $\{ \mathtt{a} \}^+$ and $\alpha = \beta = \mathtt{a}$ satisfies the other four axioms.
That structure is isomorphic to $(\mathbb{N} \setminus \{ 0 \}, +)$, and its theory is decidable, by Presburger's method.

## Explanations

### L1 human

The theory of concatenation talks about words made of two letters, $\mathtt{a}$ and $\mathtt{b}$.
Its only operation glues two words together, so $\mathtt{ab}$ glued to $\mathtt{ba}$ is $\mathtt{abba}$.
The five rules say that gluing is associative, that a word can be cut in a consistent way, and that single letters cannot be cut.
Grzegorczyk showed that these five rules already give an undecidable theory, with no numbers in sight.

### L2 human

We test the editor axiom on the string $\mathtt{abba}$, split as $x = \mathtt{a}$, $y = \mathtt{bba}$ and as $u = \mathtt{abb}$, $v = \mathtt{a}$.

1. Both splittings give $x y = u v = \mathtt{abba}$.
2. Since $|x| = 1 < 3 = |u|$, we are in the case $u = x \frown w$.
3. Take $w = \mathtt{bb}$.
   Then $x \frown w = \mathtt{abb} = u$.
4. Also $w \frown v = \mathtt{bba} = y$, so the second disjunct of $\mathsf{TC}2$ holds.

The typical use of $\mathsf{TC}$ is to prove undecidability of theories of strings, words or trees, by interpreting $\mathsf{TC}$ in them.
A trap is the empty string: with it in the domain, $\alpha = \alpha \frown \varepsilon$ violates $\mathsf{TC}3$.
