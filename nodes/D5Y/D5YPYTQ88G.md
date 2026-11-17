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

Mathematical writing style is the set of conventions that make a text with formulas easy to read and to check.
The main conventions are about sentences and symbols.
Each formula sits inside a grammatical sentence, no sentence starts with a symbol, and words separate two formulas.
Each symbol is defined before its first use, and it keeps one meaning in the whole text.
A displayed formula carries the punctuation of its sentence.
The conventions are advice, not laws, and good authors differ on some of them.
For example, they differ on "we" versus "I" and on logical symbols in prose.
They matter because a reader can check a [[proof|0B94TKFQJX]] only when each sentence says exactly one thing and can be read aloud.

## Motivation

Compare two versions of the same short argument.
The first version is "$n$ odd $\Rightarrow$ $n = 2k+1$, $n^2 = 4k^2+4k+1$, $= 2(2k^2+2k)+1$ odd".
The second version is the following text.

> Let $n$ be an odd integer.
> Then $n = 2k + 1$ for some integer $k$.
> Hence $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, and so $n^2$ is odd.

Both versions contain the same mathematics.
The second version says where $k$ comes from, that $k$ is an integer, which equations are claims, and what the conclusion is.
A reader of the first version must guess these four things.
The conventions of this page remove such guesses, and so they let the reader spend the effort on the mathematics.

## Notation

Consider the symbols $\forall$ ("for all"), $\exists$ ("there exists"), $\Rightarrow$ ("implies"), $\therefore$ ("therefore") and $\in$ ("is an element of").
They belong to formal logic and to blackboard shorthand.
Many style guides, among them the Wikipedia manual of style for mathematics, advise the words in place of $\forall$, $\exists$ and $\in$ in running prose.
Texts on logic and on set theory use the symbols in prose more often, because there the formulas themselves are the objects of study.
The page [[mathematical notation|QKEX4PD029]] gives the general conventions for symbols, and the page [[mathematical abbreviations|4ZNYMYRRY3]] gives the short forms such as "iff" and "wlog".

## Remarks

### Sentences and symbols

1. Do not start a sentence with a symbol. Bad: "$G$ is abelian." Good: "The group $G$ is abelian."
2. A sentence that starts with a formula looks like the end of the last sentence. Bad: "Let $p$ be prime. $p$ divides $ab$." Good: "Let $p$ be prime, and suppose that $p$ divides $ab$."
3. Separate two formulas by a word. Bad: "For $x > 1$, $x^2 > x$." Good: "For $x > 1$ we have $x^2 > x$."
4. Two formulas side by side can read as one formula. Bad: "Each $x$ $\in A$ has an inverse." Good: "Each element $x$ of $A$ has an inverse."
5. Write the logical words in prose. Bad: "$\forall \varepsilon > 0$ $\exists \delta > 0$ with $\lvert x \rvert < \delta \Rightarrow \lvert f(x) \rvert < \varepsilon$." Good: "For each $\varepsilon > 0$ there is $\delta > 0$ such that $\lvert x \rvert < \delta$ implies $\lvert f(x) \rvert < \varepsilon$."
6. Use a symbol when it carries the meaning better than words, for example in a computation. Some authors allow $\Rightarrow$ between two displayed formulas, and others never use it.

### Definitions and notation

1. Define each symbol before its first use, and state its type. Bad: "Then $f(n) = n^2$ is injective." Good: "Let $f \colon \mathbb{N} \to \mathbb{N}$ be the function $f(n) = n^2$. Then $f$ is injective."
2. Say when an equation is a definition and when it is a claim. Bad: "Let $u = v - w$." when $u$ already has a meaning. Good: "We define the vector $u$ by $u = v - w$."
3. Keep one meaning for each symbol in the whole text. Bad: $n$ is the dimension in Section 2 and an index in Section 3. Good: the dimension is $d$ in the whole text, and the index is $n$.
4. Keep one symbol for each object. Bad: the same set is $X$ on one page and $S$ on the next. Good: the set is $X$ on every page.
5. Choose letters that follow the common conventions. The letters $i, j, k, m, n$ usually denote integers, $\varepsilon$ and $\delta$ small positive numbers, and $f, g, h$ functions.
6. Use the standard term and the standard symbol when they exist. A new notation needs a sentence that defines it, as the page [[conflicting conventions|CSFEP56A7D]] explains for symbols with two meanings.

### Displayed formulas

1. A displayed formula is a part of a sentence. The sentence goes on after the display, and the display carries the comma or the full stop that the sentence needs.
2. A correct display: "Adding the two equations, we obtain" then the display $2x = 10,$ then "and so $x = 5$." The comma after $2x = 10$ belongs to the sentence.
3. Display a formula that is long, that is important, or that a later sentence refers to. Keep a short formula in the line.
4. Number only the displays that a later sentence cites. A number on each display makes the reader look for references that do not exist.
5. In a chain of equalities, put the reason of each step in the text before or after the chain. A reason hidden inside the chain is easy to miss.

### Words and voice

1. Most mathematical papers use "we", which means the author and the reader together: "We now show that $f$ is continuous."
2. Some single authors write "I" for personal choices and "we" for the steps of the argument. Other authors prefer the passive voice. The choice is a matter of taste, and the advice of style guides differs.
3. Words such as `clearly`, `obviously` and `it is easy to see` claim that a step is simple, but they do not give the reason. The page [[trivial, obvious and clearly|Y0HXCJRB9B]] treats these words.
4. Phrases such as "note that" and "it should be noted that" add no content. Many style guides advise to remove them and to put the important fact first in the sentence.
5. The word "any" can mean "every" or "some", so a careful writer replaces it by one of the two. The page [[ambiguity in mathematical language|8BZPKYF912]] shows examples.

### Examples

1. The sentence "Since $x > 0$ we have $x^2 > 0$" follows rules 1 and 3 of the list on sentences. It starts with a word, and the words "we have" separate the two formulas.
2. Take the definition "A function $f \colon \mathbb{R} \to \mathbb{R}$ is even if $f(-x) = f(x)$ for every real $x$". It states the type of $f$, defines the term, and quantifies $x$ in words.
3. The display of the formula $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ with a comma at its end, followed by "where $n$ is a positive integer", is correct. The comma ends the formula, and the sentence goes on to define $n$.
4. A paper writes $\mathbb{N}$ for the positive integers and says so in its first section. It follows the rule of defining notation before use, even though some books include $0$ in $\mathbb{N}$.

### Non-examples

1. "$x^2 - 5x + 6 = 0$, $x = 2, 3$." Here a sentence starts with a symbol, and two formulas touch. The reader cannot tell if the second formula is a claim or a definition.
2. "Let $f$ be continuous. Then $f(c) = 0$." The symbol $c$ appears without a definition, so the sentence has no exact meaning.
3. "We show that $A \subseteq B$. Let $a \in A$ ... thus $A = B$." The last sentence claims more than the first sentence promised, so the text uses two different goals for one proof.

### Basic properties

1. Each sentence of a mathematical text, formulas included, can be read aloud as a grammatical English sentence. This is a test that a writer can apply to each line.
2. A formula inside a sentence plays the role of a noun ("the number $n^2$") or of a clause ("$n^2$ is odd"). The punctuation around it follows the role.
3. The rules on symbols serve one goal: the reader must know, at each point, what each symbol means. The reader must also know if each formula is a claim, a definition or an assumption.
4. The rules conflict at times. A long formula written in words becomes hard to read, and then the formula is the better choice.

### History

Paul Halmos wrote the essay "How to write mathematics" in 1970.
In 1973 the American Mathematical Society printed it in a booklet of the same name, with essays by Norman Steenrod, Menahem Schiffer and Jean Dieudonné.
Donald Knuth, Tracy Larrabee and Paul Roberts published the book "Mathematical Writing" in 1989.
Nicholas Higham's "Handbook of Writing for the Mathematical Sciences" appeared in a second edition in 1998, and Franco Vivaldi's "Mathematical Writing" in 2014.
Consider the rule that a sentence ending with a formula ends with a full stop.
It appears in the guides of Halmos and of Higham, and in the house styles of many journals.

### Common errors

1. A student writes a list of formulas without any words between them. The reader cannot tell which formula follows from which, so the student must add "hence", "so" or "since" with a reason.
2. A student uses $=$ to mean "the next step is". For example, "$x^2 = 4 = x = 2$" is false as a chain of equalities, and it should be "$x^2 = 4$, so $x = 2$ or $x = -2$".
3. A student uses $\Rightarrow$ as a general connector between sentences. The symbol means "implies", and a sentence such as "$f$ is continuous $\Rightarrow$ we take $\delta = 1$" misuses it.

## Explanations

### L1 human

A mathematical text mixes words and formulas.
The formulas are short, but they are hard to read when they are not inside sentences.
A good writer puts each formula into a sentence that a person can read aloud.
For example, "the number $7$ is odd, because $7 = 2 \cdot 3 + 1$" reads well.
The line "$7$ $= 2 \cdot 3 + 1$ odd" says the same thing, but the reader must guess the missing words.
Other rules are just as simple: a writer says what a letter means before the first use, and does not change its meaning later.

### L2 human

We rewrite a poor proof that the product of two odd integers is odd.

The poor version is: "$a = 2k+1$, $b = 2l+1$, $ab = 4kl+2k+2l+1$ odd."

1. Introduce the objects with their types. "Let $a$ and $b$ be odd integers."
2. Give the source of each new letter. "By the definition of an odd integer, there are integers $k$ and $l$ with $a = 2k + 1$ and $b = 2l + 1$."
3. Write the computation as a sentence with a display. "Then"
$$ab = (2k+1)(2l+1) = 4kl + 2k + 2l + 1 = 2(2kl + k + l) + 1.$$
4. State the conclusion with its reason. "Since $2kl + k + l$ is an integer, the integer $ab$ is odd."

The typical use of these rules is the last stage of [[writing proofs|8JQHJK94RZ]]: the writer reads the draft once only for style.
The writer fixes each sentence that starts with a symbol, each undefined letter and each display without punctuation.
A trap is to use the same letter $k$ for both $a$ and $b$, as in $a = 2k + 1$ and $b = 2k + 1$.
This proves the claim only when $a = b$.

### L3 human

The rules of style rest on one fact: a mathematical text is a natural language with formulas as embedded phrases.
The page [[the language of mathematics|661V0DH7V3]] describes this language.
A formula is a noun phrase ("the sum $a + b$") or a sentence ("$a + b$ is even").
The grammar of the host sentence fixes which one it is.
Formal languages, such as the input language of a proof assistant, remove the choice: there each line has one parse, which a program checks.
Informal writing keeps the flexibility of English, and the style rules are the discipline that keeps its meaning exact.
The same rules appear in other parts of this site.
The page [[the language of proofs|GKMRQCA8CW]] gives the standard phrases, and [[level of detail in proofs|VYGBV5D8Y4]] tells which steps to write.
The page [[structure of a mathematical paper|XZHACQ74C0]] applies the rules at the level of a whole paper.
