---
tag: D5YPYTQ88G
kind: concept
name: Mathematical writing style
aliases: [mathematical-writing-style]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug1
uses: [0B94TKFQJX, QKEX4PD029, 8JQHJK94RZ]
sources:
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Writing style in mathematics
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Punctuation after formulae
  - url: https://en.wikipedia.org/wiki/Paul_Halmos
    locator: Books
---

## Summary

Mathematical writing style is a set of habits that make a text with formulas easy to read aloud and to check.
Here is a short argument written badly, followed by the same argument rewritten.

> $n$ odd $\Rightarrow$ $n = 2k+1$, $n^2 = 4k^2+4k+1$, $= 2(2k^2+2k)+1$ odd

> Let $n$ be an odd integer.
> Then $n = 2k + 1$ for some integer $k$.
> Hence $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, and so $n^2$ is odd.

Both versions hold the same mathematics.
The rewrite says that $k$ is an integer and where it comes from, which equations are claims, and what the conclusion is, while a reader of the first version has to guess all four.
The habits behind the rewrite are few: every formula sits inside a grammatical sentence, no sentence starts with a symbol, words separate formulas, and every symbol is defined before use and keeps one meaning.
These are advice, not laws, and good authors disagree on some of them, such as "we" versus "I" and logical symbols in prose.

## Motivation

A reader can check a [[proof|0B94TKFQJX]] only when each sentence says exactly one thing.
Formulas are dense, so a small ambiguity in the words around them costs the reader a lot of time.
The habits of style move that effort from the reader back to the writer, who knows what was meant.
A quick test for any line is to read it aloud as an English sentence, formulas included.

## Notation

The symbols $\forall$, $\exists$, $\Rightarrow$, $\therefore$ and $\in$ belong to formal logic and to blackboard shorthand.
Many guides advise words in their place in running prose: "for every", "there is", "implies", "therefore", "is an element of".
Texts on logic and set theory use the symbols in prose more often, because there the formulas are themselves the objects of study, so this is a point where good writers differ.
General conventions for symbols are in [[mathematical notation|QKEX4PD029]], and short forms such as "iff" and "wlog" are in [[mathematical abbreviations|4ZNYMYRRY3]].

## Remarks

### Sentences and symbols

A sentence that starts with a symbol looks like the end of the last sentence.
"Let $p$ be prime, and suppose that $p$ divides $ab$" reads better than two sentences of which the second begins with $p$.
A noun in front of the symbol fixes it: "the group $G$ is abelian".

Two formulas side by side can read as one formula.
"For $x > 1$, $x^2 > x$" makes the reader stop at the comma, while "for $x > 1$ we have $x^2 > x$" does not.

Logical words are usually clearer than logical symbols in prose.
Compare "for each $\varepsilon > 0$ there is $\delta > 0$ such that $\lvert x \rvert < \delta$ implies $\lvert f(x) \rvert < \varepsilon$" with the same line in $\forall$, $\exists$ and $\Rightarrow$.
A symbol earns its place when it carries the meaning better than words, as in a computation, and some authors allow $\Rightarrow$ between two displayed formulas while others never use it.

### Definitions and notation

Define each symbol before its first use, and say what kind of object it is.
"Let $f \colon \mathbb{N} \to \mathbb{N}$ be given by $f(n) = n^2$" tells the reader the domain, which "$f(n) = n^2$ is injective" leaves open.
Say whether an equation is a definition or a claim, for example "we define the vector $u$ by $u = v - w$".

Keep one meaning for each symbol and one symbol for each object in the whole text.
If $n$ is the dimension in one section and an index in the next, or the same set is $X$ on one page and $S$ on another, the reader has to track the change.
Common conventions help: $i, j, k, m, n$ for integers, $\varepsilon$ and $\delta$ for small positive numbers, and $f, g, h$ for functions.
A symbol with two common meanings, such as $\mathbb{N}$ with or without $0$, needs one sentence that settles it, as [[conflicting conventions|CSFEP56A7D]] explains.

### Displayed formulas

A displayed formula is part of a sentence, and it carries the comma or the period that the sentence needs.
For example, after "adding the two equations, we obtain" comes the display
$$2x = 10,$$
and the sentence goes on: "and so $x = 5$".

Display a formula that is long, important, or cited later, and keep a short one in the line.
Number only the displays that a later sentence cites, since numbers on every display send the reader looking for references that do not exist.
In a chain of equalities, put the reason for each step in the text before or after the chain, where it is easy to find.

### Person and voice

Most mathematical papers use "we", meaning the author and the reader together: "we now show that $f$ is continuous".
Some single authors write "I" for their own choices and "we" for the steps of the argument, and some prefer impersonal or passive forms.
Guides disagree here, and the custom of a journal often decides.

Phrases such as "note that" add no content, and many guides advise cutting them and putting the important fact first.
The word "any" can mean "every" or "some", so a careful writer replaces it with one of the two, as [[ambiguity in mathematical language|8BZPKYF912]] shows.
Words such as `clearly` and `obviously` claim that a step is easy without giving the reason, as [[trivial, obvious and clearly|Y0HXCJRB9B]] explains.

### Watch out

The equals sign is not a word for "the next step is".
"$x^2 = 4 = x = 2$" is false as a chain of equalities, and the intended sentence is "$x^2 = 4$, so $x = 2$ or $x = -2$".

The arrow $\Rightarrow$ means "implies", so it cannot connect actions.
"$f$ is continuous $\Rightarrow$ we take $\delta = 1$" misuses it.

The habits sometimes conflict.
A long formula spelled out in words becomes hard to read, and then the formula is the better choice.

### History

Paul Halmos wrote the essay "How to Write Mathematics" in 1970.
In 1973 the American Mathematical Society reprinted it in a booklet of the same name, together with essays by Norman Steenrod, Menahem Schiffer and Jean Dieudonné.
Donald Knuth, Tracy Larrabee and Paul Roberts published "Mathematical Writing" in 1989, based on a course at Stanford.
Later guides include Nicholas Higham's "Handbook of Writing for the Mathematical Sciences", second edition 1998, and Franco Vivaldi's "Mathematical Writing" of 2014.

### Try it

Rewrite "$x^2 - 5x + 6 = 0$, $x = 2, 3$" as a sentence.
One answer: "The roots of $x^2 - 5x + 6 = 0$ are $x = 2$ and $x = 3$, since $x^2 - 5x + 6 = (x - 2)(x - 3)$."

What is wrong with "Let $f$ be continuous; then $f(c) = 0$"?
The letter $c$ is never defined, so the sentence has no exact meaning.

## Explanations

### L1 human

A mathematical text mixes words and formulas.
The formulas are short, but they are hard to read when they are not inside sentences.
A good writer puts each formula into a sentence that a person can read aloud.
For example, "the number $7$ is odd, because $7 = 2 \cdot 3 + 1$" reads well, while "$7$ $= 2 \cdot 3 + 1$ odd" makes the reader guess the missing words.
A good writer also says what a letter means before using it, and does not change its meaning later.

### L2 human

We rewrite a poor proof that the product of two odd integers is odd.
The poor version reads "$a = 2k+1$, $b = 2l+1$, $ab = 4kl+2k+2l+1$ odd".

> Let $a$ and $b$ be odd integers.
> By the definition of an odd integer, there are integers $k$ and $l$ with $a = 2k + 1$ and $b = 2l + 1$.
> Then
> $$ab = (2k+1)(2l+1) = 4kl + 2k + 2l + 1 = 2(2kl + k + l) + 1.$$
> Since $2kl + k + l$ is an integer, $ab$ is odd.
> $\square$

The first line gives the objects their type, the second gives each new letter its source, the display is part of a sentence, and the last line gives the conclusion with its reason.
Check: $a = 3$ and $b = 5$ give $k = 1$, $l = 2$ and $ab = 15 = 2 \cdot 7 + 1$.

This rewrite is the last stage of [[writing proofs|8JQHJK94RZ]], a reading of the draft for style alone.
Watch out: the same letter for both numbers, as in $a = 2k + 1$ and $b = 2k + 1$, proves the claim only when $a = b$.

### L3 human

A mathematical text is a natural language with formulas as embedded phrases, as [[the language of mathematics|661V0DH7V3]] describes.
A formula is a noun phrase ("the sum $a + b$") or a sentence ("$a + b$ is even"), and the grammar of the host sentence decides which.
Formal languages, such as the input language of a proof assistant, remove the choice: each line has one parse, which a program checks.
Informal writing keeps the flexibility of English, and the habits of style are the discipline that keeps its meaning exact.
[[The language of proofs|GKMRQCA8CW]] gives the standard phrases, [[level of detail in proofs|VYGBV5D8Y4]] says which steps to write, and [[structure of a mathematical paper|XZHACQ74C0]] applies the same habits to a whole paper.
