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

The formula $0 = 0$ is a string of three symbols, and a Gödel numbering turns it into one number, for example $2^{13} \cdot 3^{7} \cdot 5^{13}$.
Once every formula and every proof is a number, questions about proofs become questions about numbers, and a theory of arithmetic can talk about its own syntax.
Exactly, a Gödel numbering of the strings over an alphabet is a map into the natural numbers that is injective and [[computable|KZSB5E471K]], whose set of codes is a [[computable set|PPGD5KW8JC]], and whose inverse on that set is computable.
The [[formal definition|7RP93F2W47]] states these conditions, and proofs are coded as finite sequences of [[formulas|HYJ10AF6RT]] in the same way.

## Motivation

Peano arithmetic speaks only about numbers.
Its variables range over $0, 1, 2, \ldots$, and its symbols are $0$, $S$, $+$ and $\cdot$.
So if we want to ask whether arithmetic can describe its own proofs, we must first turn formulas and proofs into numbers.
Gödel did this with prime powers in his paper of 1931.
After the coding, "the formula with code $n$ has a proof" is a property of the number $n$, and the ordinary methods of arithmetic apply to it.

The same idea runs every computer.
A text file is a list of bytes, and a list of bytes is one large number written in base $256$.
A compiler that checks a program is a function on such numbers.
Gödel numbering is the mathematical version of this fact, and it is the first step toward the [[diagonal lemma|3PRW76471J]] and the [[incompleteness theorems|X9WYNYE29C]].

## Notation

We fix the language of arithmetic with the logical symbols $\neg$, $\to$, $\forall$, $=$, parentheses and the variables $v_0, v_1, \ldots$.
The other connectives and $\exists$ are abbreviations.
Each symbol gets an odd code.

| symbol | $\neg$ | $\to$ | $\forall$ | $=$ | $($ | $)$ | $0$ | $S$ | $+$ | $\cdot$ | $v_i$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| code | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | $21 + 2i$ |

A string $s_1 \cdots s_n$ gets the code $\#(s_1 \cdots s_n) = 2^{c(s_1)} 3^{c(s_2)} \cdots p_n^{c(s_n)}$, where $c(s)$ is the code of the symbol $s$ and $p_n$ is the $n$-th prime.
A sequence of strings $w_1, \ldots, w_k$, such as a proof, gets the code $2^{\# w_1} 3^{\# w_2} \cdots p_k^{\# w_k}$.
Books write the code of $\varphi$ as $\# \varphi$, $\mathrm{gn}(\varphi)$ or $\ulcorner \varphi \urcorner$.
Watch the last one: inside a formula, $\ulcorner \varphi \urcorner$ is the [[numeral|VK6WWSDMXK]] of the code, a closed term, not the number itself.

## Remarks

### A first computation

Take the formula $0 = 0$.
Its symbols are $0$, $=$, $0$ with codes $13$, $7$, $13$.
Put these codes as exponents on the first three primes:
$$\#(0 = 0) = 2^{13} \cdot 3^{7} \cdot 5^{13} = 21870000000000000.$$
To decode, divide by $2$ until the result is odd, which takes $13$ divisions, then by $3$, which takes $7$, then by $5$, which takes $13$.
The exponents $13, 7, 13$ give back $0, =, 0$.
Unique factorization is what makes this work: a number has only one list of prime exponents, so two different strings never get the same code.
[[The Gödel number of 0 = S0|GEHMF7T5FX]] does the same for a formula of four symbols.

### Other numberings

Prime powers are not the only choice.
The [[bijective base-k numbering of strings|4QSK8112QQ]] reads a string over $k$ symbols as a number in base $k$ with digits $1$ to $k$.
It is a Gödel numbering onto all of $\mathbb{N}$, and its codes are much smaller.
A computer uses bytes, which is base $256$ with a leading byte $1$ added so that leading zero bytes are not lost.
The Lean library Mathlib has the class `Encodable`, which asks for a map `encode` into $\mathbb{N}$ and a partial inverse `decode`.
That class does not by itself demand computability in the sense of computability theory, so it is a weaker notion.

Any two Gödel numberings are linked by a computable bijection between their sets of codes: decode with one, then encode with the other.
So every statement of the form "this set of formulas is computable" has the same answer for every Gödel numbering.

### What fails to be a numbering

The map that sends a string to its length is computable, but it is not injective, since $0 = 0$ and $0 = v_0$ both have length $3$.
So the length forgets the formula.
[[Coding sentences by their truth value|Y4VRPDEV6K]] can be made injective, but it is not computable, because truth in $\mathbb{N}$ is not computable.
A numbering of that kind is of no use, since arithmetic cannot compute with it.

### The syntax becomes arithmetic

With prime-power codes, "$x$ codes a term", "$x$ codes a formula" and "$x$ codes a sentence" are [[primitive recursive|5NVA2JRHPV]] relations.
The reason is that every part of a string has a smaller code than the string itself, so each check is a search below $x$.
Joining strings is a primitive recursive function of the codes, as [[concatenation of codes|YZHC2B7YT5]] shows.
The same holds for substitution: the function that puts the numeral $\underline{y}$ for $v_0$ in the formula with code $x$ is primitive recursive.
When a theory has a decidable set of axioms, "$y$ codes a proof of the formula with code $x$" is decidable too.
[[Arithmetization of syntax|6M12VR1GT6]] develops this.

### Watch out

A theory never proves facts about formulas directly.
It proves facts about numbers, and the numbering lets us read some of them as facts about formulas.
A second slip is to confuse the number $\# \varphi$ with the term $\ulcorner \varphi \urcorner$.
For $0 = 0$ the number has $17$ digits, while the term is the symbol $S$ written $21870000000000000$ times in front of $0$.
Finally, the choice of numbering is free, and the incompleteness theorems hold for every Gödel numbering with the same proofs.

### History

Kurt Gödel introduced the numbering in his 1931 paper "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", with codes by prime powers.
In the same paper he coded finite sequences by the Chinese remainder theorem, the device now called the [[β-function|BM6P0C2AC2]].
It lets formulas that use only addition and multiplication express definitions by recursion.

### Try it

Which string has the code $2^{15} \cdot 3^{13}$?
The exponents are $15$ and $13$, so the string is $S0$, the term for the number $1$.

Is $10$ a code?
No: $10 = 2^1 \cdot 5^1$ skips the prime $3$, and a code uses the first $n$ primes with no gaps.

## Explanations

### L1 human

Give each symbol a number, for example $13$ for "0", $7$ for "=" and $15$ for "S".
A formula is a list of symbols, so it becomes a list of numbers.
Pack the list into one number by using the numbers as powers of $2, 3, 5, \ldots$.
The list $13, 7, 13$ becomes $2^{13} \cdot 3^{7} \cdot 5^{13}$.
Each whole number splits into primes in only one way, so the list can be read back.
Now "this formula can be proved" is a property of a number, and arithmetic can talk about it.

### L2 human

We find the formula with the code $2^{9} \cdot 3^{13} \cdot 5^{7} \cdot 7^{13} \cdot 11^{11}$.
The exponents, in the order of the primes, are $9, 13, 7, 13, 11$.
The table reads them as $($, $0$, $=$, $0$, $)$, so the string is $(0 = 0)$.
Now we go back the other way to check.
The five symbols of $(0 = 0)$ have codes $9, 13, 7, 13, 11$, and these are the exponents we started with.
The calculation shows the typical use: each syntactic question, such as "is this a formula", becomes a computation with exponents.

### L3 human

A Gödel numbering is an effective injection of a countable free structure, the strings or the terms, into $\mathbb{N}$.
Since any two such injections differ by a computable bijection, the computability theory of syntax does not depend on the choice.
In type theory a class such as `Encodable` plays the same role, and in computing any serialization format does.
The numbering is the first step of [[arithmetization of syntax|6M12VR1GT6]], which gives the [[provability predicate|NB2BCZR40F]], the [[diagonal lemma|3PRW76471J]] and the [[incompleteness theorems|X9WYNYE29C]].
