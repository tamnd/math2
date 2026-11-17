---
tag: MFJXPAF0R0
kind: concept
name: Gödel numbering
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
uses: [HYJ10AF6RT, KZSB5E471K, PPGD5KW8JC, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_numbering
    locator: lead section
  - book: isbn:9780521857840
  - url: https://builds.openlogicproject.org/
    locator: "Part: Incompleteness"
same_as:
  wikidata: Q1451046
  wikipedia: Gödel numbering
---

## Summary

A Gödel numbering of a formal language is a map from the strings of symbols, and from finite sequences of strings, to natural numbers.
It must be injective and [[computable|KZSB5E471K]], its set of codes must be a [[computable set|PPGD5KW8JC]], and decoding must be computable.
The precise definition is the node [[Gödel numbering (definition)|7RP93F2W47]].
With a Gödel numbering, statements about [[formulas|HYJ10AF6RT]] and proofs become statements about numbers, and a theory of arithmetic can speak about its own syntax.

## Motivation

A theory of arithmetic speaks only about numbers.
To ask whether arithmetic can describe its own proofs, we must first make formulas and proofs into numbers.
Gödel did this with prime powers in 1931.
Then "the formula with code $n$ is provable" becomes a property of the number $n$, and the methods of arithmetic apply to it.

## Notation

We fix the language $\set{0, S, +, \cdot}$ of arithmetic with the logical symbols $\neg, \to, \forall, =$, parentheses and variables $v_0, v_1, \ldots$.
The other connectives and $\exists$ are abbreviations.
Our symbol codes are the odd numbers below.

| symbol | $\neg$ | $\to$ | $\forall$ | $=$ | $($ | $)$ | $0$ | $S$ | $+$ | $\cdot$ | $v_i$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| code | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | $21 + 2i$ |

1. A string $s_1 \cdots s_n$ has code $\# (s_1 \cdots s_n) = 2^{c(s_1)} 3^{c(s_2)} \cdots p_n^{c(s_n)}$, where $p_n$ is the $n$-th prime.
2. A finite sequence of strings $w_1, \ldots, w_k$, such as a proof, has code $2^{\# w_1} 3^{\# w_2} \cdots p_k^{\# w_k}$.
3. The code of a formula $\varphi$ is $\# \varphi$, and the [[numeral|VK6WWSDMXK]] of this code is written $\ulcorner \varphi \urcorner$.
4. A string code has odd exponents, and a sequence code has even exponents, so no number is both.

## Remarks

### Examples

1. The prime-power numbering of the table is a Gödel numbering. The worked case is [[the Gödel number of 0 = S0|GEHMF7T5FX]].
2. The bijective base-$k$ numbering of strings is a Gödel numbering onto all of $\N$. It is the example [[bijective base-k numbering of strings|4QSK8112QQ]].
3. A program stores a text file as a sequence of bytes, which is one number in base $256$; with a leading byte $1$ this coding is injective and computable.
4. The Lean library Mathlib has the class `Encodable`: an injective map into $\N$ with a partial inverse. Lean does not ask for computability, so this is a weaker notion.

### Non-examples

1. The map that sends a string to its length is computable but not injective, so it fails the first condition.
2. [[Coding sentences by their truth value|Y4VRPDEV6K]] gives an injective map that is not computable, so it fails the second condition.
3. Any map onto $\N$ that treats the symbols $v_0, v_1, \ldots$ as one symbol fails injectivity, because it identifies different formulas.

### Basic properties

1. Any two Gödel numberings are related by a computable bijection between their sets of codes.
2. With the prime-power numbering, the relations "$x$ codes a term", "$x$ codes a formula", "$x$ codes a sentence" and "$x$ codes an axiom of logic" are [[primitive recursive|5NVA2JRHPV]] relations.
3. The functions $\mathrm{num}(n) = \# \underline{n}$ and $\mathrm{sub}(x, y) = $ the code of the result of putting the numeral $\underline{y}$ for the free variable $v_0$ in the formula with code $x$ are primitive recursive.
4. If a theory has a decidable set of axioms, the relation "$y$ codes a proof of the formula with code $x$" is decidable. This is the subject of [[arithmetization of syntax|6M12VR1GT6]].
5. Primitive recursiveness holds because each check is a search bounded by the number itself: the parts of a string have smaller codes than the string.

### History

Kurt Gödel introduced the numbering in his 1931 paper on formally undecidable propositions, with codes by prime powers.
Later authors used other codings, such as the coding of sequences by the [[β-function|BM6P0C2AC2]], which needs only addition and multiplication.

### Common errors

1. A student thinks that the theory proves facts about formulas directly. The theory proves facts about numbers, and the numbering gives these facts their reading.
2. A student confuses the code $\# \varphi$, a number, with $\ulcorner \varphi \urcorner$, a closed term of the language.
3. A student forgets that the choice of numbering is free. Results such as the incompleteness theorems hold for every Gödel numbering, with the same proofs.

## Explanations

### L1 human

Give each symbol a number, for example $13$ for "0", $7$ for "=" and $15$ for "S".
A formula is a list of symbols, so it becomes a list of numbers.
A list of numbers can be packed into one number by prime powers: the list $13, 7, 13$ becomes $2^{13} \cdot 3^{7} \cdot 5^{13}$.
Because each number splits into primes in only one way, the list can be read back from the number.
Then "this formula is provable" becomes a property of a number, and arithmetic can talk about it.

### L2 human

1. The formula $0 = 0$ is the string of symbols $0, =, 0$ with codes $13, 7, 13$.
2. Its Gödel number is $2^{13} \cdot 3^{7} \cdot 5^{13} = 21870000000000000$.
3. To decode, divide by $2$ as often as possible: $13$ times. Then divide by $3$: $7$ times. Then by $5$: $13$ times.
4. The exponents $13, 7, 13$ read back as $0, =, 0$.

The typical use is to turn a syntactic relation, such as "$y$ is a proof of $x$", into a relation between numbers that a formula of arithmetic can express.
A trap: the code of a formula and the formula are different objects, and a formula $\varphi(x)$ applied to $\ulcorner \psi \urcorner$ speaks about $\psi$ only through the numbering.

### L3 human

A Gödel numbering is an effective injection of a countable free structure, the strings or the terms, into $\N$.
Any two such injections differ by a computable bijection, so the computability theory of syntax does not depend on the choice.
In type theory the same role is played by a class like Mathlib's `Encodable`, and in computer science by any serialization format.
The numbering is the first step of [[arithmetization of syntax|6M12VR1GT6]], which leads to the [[diagonal lemma|3PRW76471J]] and the [[incompleteness theorems|X9WYNYE29C]].
