---
tag: 4M1FGQ0HNZ
kind: concept
name: Mathematical jargon
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [QKEX4PD029, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
---

## Summary

Mathematical jargon is the set of words and phrases that mathematicians use with a special meaning that is not a formal definition, such as "nice", "well-behaved", "vanish", "upstairs", "folklore" and "morally true".
A jargon word is different from a defined term: a defined term, such as "normal subgroup", has an exact definition, while a jargon word has a meaning that the community shares and that the context makes precise.
Some jargon words are short names for exact ideas ("$f$ vanishes at $a$" means $f(a) = 0$), and others express a judgement or a guess ("this is morally true").
Jargon matters because it fills lectures, papers and conversations, and a reader who takes it literally, or ignores it, misreads the argument.

## Motivation

A [[mathematical proof|0B94TKFQJX]] is written in a mix of formulas, defined terms and ordinary words.
Some ordinary words acquire a fixed meaning among mathematicians that differs from their everyday meaning.
For example, a "nice" function is not a pleasant function; it is a function with the properties that the current argument needs.
These words help experts talk fast, because one word replaces a list of conditions that both sides know.
A student meets them without a definition, so this page lists the common ones and says what each one means and how to make it precise.

## Notation

Jargon has no symbols of its own.
The site uses jargon words only when it also states the exact condition that the word stands for.
When a page writes "$f$ vanishes on $A$", it means $f(x) = 0$ for every $x \in A$.

## Remarks

### A list of common jargon

| Word | Meaning among mathematicians |
|---|---|
| nice, well-behaved | has the regularity that the current argument needs, such as continuity, smoothness or finiteness; the opposite of [[pathological|WMBZPYPN2D]] |
| natural | defined without arbitrary choices; see [[canonical and natural|F8WNADZFMM]] |
| structure | the extra data on a set, such as operations, an order or a topology, together with their axioms |
| vanish | to be equal to zero: $f$ vanishes at $a$ when $f(a) = 0$ |
| vanish identically | to be zero at every point: $f(x) = 0$ for all $x$ |
| upstairs, downstairs | the larger and the smaller object of a pair, such as a ring and a subring, a covering space and its base, or the numerator and the denominator of a fraction |
| folklore | a result that experts know and use, but that has no standard published source or no known first author |
| morally true | true in spirit: true in a simple model case, or true after technical conditions are added |
| on the nose | equal exactly, not only up to an isomorphism or an approximation |
| for free | follows with no extra work from what is already proved |
| in general | either "in every case" or "in most cases"; see [[almost all, generic and in general|N1XSAXCQY3]] |
| the obvious map | the map that a reader would write down first; in good writing it is also given by a formula |

Some jargon words have their own pages: [[trivial, obvious and clearly|Y0HXCJRB9B]], [[sharp|KWQV0G0VJ3]], [[elementary|84SZZBACP3]], and [[elegant and deep|STHWD1K9AN]].

### Examples

1. [[The function x^2 - 4 vanishes at 2 and at -2|ZT7JBHZFHF]]. The word "vanish" is a short name for $f(a) = 0$.
2. [[Upstairs and downstairs in the Gaussian integers|X49VTBJ08Z]]. The prime $5$ of $\mathbb{Z}$ downstairs factors upstairs as $(2 + i)(2 - i)$, while $3$ stays prime upstairs.
3. "Let $f$ be a nice function on $[0, 1]$." In a first course on integrals this often means "continuous", so that the integral of $f$ exists. The writer should say which property is meant.
4. "For a finite-dimensional vector space $V$, the isomorphism $V \cong V^{**}$ is natural." The map $v \mapsto (\varphi \mapsto \varphi(v))$ uses no choice of basis, as the [[canonical isomorphism with the double dual|0ZJM9D7NPS]] shows.
5. "The result is folklore." The writer knows of no first published proof and treats the result as common knowledge, so the reader should look for a proof or prove it.

### Non-examples

1. [[The word normal in "normal subgroup" is a defined term|EZVF6MJEH9]]. It has an exact definition, so it is not jargon, although the everyday word "normal" is vague.
2. "Continuous" is not jargon. It has the exact $\varepsilon$-$\delta$ definition, and a claim that a function is continuous can be proved or refuted.
3. The abbreviation `iff` is not jargon. It is a short written form with one fixed expansion, "if and only if"; see [[mathematical abbreviations|4ZNYMYRRY3]].

### Basic properties

1. A jargon word depends on context. "Nice" means "continuous" in one lecture and "smooth with compact support" in another.
2. A jargon word can always be replaced by an exact condition, and a careful writer does this at least once in each text.
3. Some jargon words name exact relations: "vanish", "upstairs" and "on the nose" have a precise meaning once the setting is fixed.
4. Other jargon words express judgement: "nice", "morally true" and "folklore" are claims about the state of knowledge or the taste of the writer, and they cannot be proved.
5. A defined term can be built from a jargon word. The informal "natural" became the defined term "natural transformation" in category theory.

### History

Many jargon words began as informal speech in lectures and seminars and then entered print.
The word "natural" is an example: Samuel Eilenberg and Saunders Mac Lane gave it an exact meaning in their 1945 paper that founded category theory.
Lists of jargon, such as the Wikipedia glossary of mathematical jargon, collect the words with their usual meanings.

### Common errors

1. A student takes "nice" or "well-behaved" as a hypothesis that needs no checking. The theorem holds only under the exact conditions that the word hides.
2. A student reads "in general" as "always" when the writer meant "usually", or the reverse. The two readings give different theorems.
3. A student cites a "folklore" result as proved. A folklore result may have no complete proof in print, so the student should give a proof or a source.

## Explanations

### L1 human

Mathematicians use some everyday words in a special way.
When they say that a function "vanishes" at a point, they mean that its value there is zero.
For example, the function that sends $x$ to $x - 3$ vanishes at $3$, because $3 - 3 = 0$.
When they call a function "nice", they mean that it has no strange behaviour, such as jumps, that would break the argument.
These words help experts talk quickly, but a careful text always says exactly what they mean.

### L2 human

We make a jargon sentence precise: "The polynomial $p(x) = x^3 - x$ vanishes at three points, and it does not vanish identically."

1. "Vanishes at $a$" means $p(a) = 0$.
2. We factor: $p(x) = x(x - 1)(x + 1)$.
3. A product of real numbers is $0$ exactly when one factor is $0$, so $p(a) = 0$ exactly when $a \in \{-1, 0, 1\}$.
4. So $p$ vanishes at exactly three points, $-1$, $0$ and $1$.
5. "Vanishes identically" means $p(x) = 0$ for every $x$. Since $p(2) = 6 \neq 0$, the polynomial does not vanish identically.

The typical use of jargon is to compress a standard condition into one word in a talk or a proof sketch.
A trap: a polynomial that is zero as a function need not be the zero polynomial over a finite field.
Over $\mathbb{Z}/2\mathbb{Z}$, the polynomial $x^2 + x$ vanishes at $0$ and at $1$, so it vanishes identically as a function, but its coefficients are not all zero.

### L3 human

Jargon is the informal layer of the language of mathematics, and much of it marks a structure that is formalised elsewhere.
"Natural" became the theory of natural transformations, and "upstairs" and "downstairs" describe a morphism $Y \to X$ viewed from its source and its target.
"On the nose" separates strict equality from equality up to isomorphism, a distinction that higher category theory makes central.
"Morally true" often points to a statement that holds in a model case, such as a finite-dimensional or a smooth case, and the work is to find the hypotheses under which it holds in general.
Other words, such as "folklore", describe the sociology of the field and not mathematics.
The later pages of this sub-area treat the most frequent families of jargon: triviality, canonicity, genericity, size ("sufficiently large"), strength, sharpness, elementarity, pathology and elegance.
