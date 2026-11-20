---
tag: D9G8M42GKC
kind: concept
name: Object language and metalanguage
aliases: [object-language, metalanguage]
msc: ["03B99", "03A05"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [5MFZ4VNY6D, 439M8B4DY2, HYJ10AF6RT]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section O
    note: adopted
    mention: wikipedia://en/76765067#J4FJ
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Metalanguage
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Use%E2%80%93mention_distinction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quasi-quotation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Metatheorem
    locator: lead section
  - book: isbn:9780122384523
inventory: [6V6WBDQV3Y]
---

## Summary

When we study a [[formal language|5MFZ4VNY6D]] $L$, two languages are at work.
The object language is $L$ itself, the language whose expressions we study.
The metalanguage is the language in which we describe $L$, state its rules and prove facts about it; usually it is mathematical English with extra symbols.
In the metalanguage the expressions of $L$ are objects: the metalanguage has names for them (quotations), variables that range over them (metavariables), and predicates about them, such as "is a formula" or "is a theorem".
A theorem of a [[formal system|439M8B4DY2]] is a formula of the object language with a derivation, while a metatheorem is a statement of the metalanguage about the system, proved by ordinary mathematics.
The distinction matters because it keeps statements about formulas apart from the formulas themselves, which avoids confusions and paradoxes such as the liar.

## Motivation

The sentence "$p \to p$ is a theorem" mixes two levels.
The part $p \to p$ is a string of the object language, and the part "is a theorem" is English that speaks about this string.
When the two levels are mixed without care, paradoxes appear.
The [[liar sentence|KBYY281V8T]] "this sentence is false" is a sentence that speaks about its own truth, and it can be neither true nor false.
Alfred Tarski showed that such paradoxes disappear when the truth of sentences of $L$ is defined in a separate metalanguage.
In the same way, David Hilbert's study of formal systems needed a clear metalanguage in which to prove statements such as "no derivation ends in $0 = 1$".

## Notation

- Quotation marks name an expression: 'snow' is the name of the word snow.
- Metavariables are letters of the metalanguage that range over expressions of $L$. On these pages $\varphi, \psi, \chi$ range over formulas, $\Gamma, \Delta$ over sets of formulas, and $t$ over terms. The letters $p, q, r$ are propositional variables of the object language.
- Quine corners form quasi-quotations: $\ulcorner \varphi \to \psi \urcorner$ is the formula made of the value of $\varphi$, then the symbol $\to$, then the value of $\psi$.
- The turnstiles $\vdash$ and $\models$ are symbols of the metalanguage, while $\to$, $\neg$, $\forall$ are symbols of the object language.
- Most books use the symbols of $L$ as names of themselves, and write $\varphi \to \psi$ for $\ulcorner \varphi \to \psi \urcorner$. Some books print object symbols in bold type instead.
- In the theory of [[Gödel numbering|MFJXPAF0R0]], $\ulcorner \varphi \urcorner$ has another meaning: the numeral of the code of $\varphi$, which is a term of the object language.

## Remarks

### Use and mention

A word is used when it stands for the thing it means, and it is mentioned when the sentence speaks about the word itself.
In "Boston is a city" the word Boston is used, and in "'Boston' has six letters" it is mentioned.
The sentence "Boston has six letters" confuses the two: a city has no letters.
In logic the same care applies to formulas: "$(p \to q)$ has five symbols" mentions a formula, while a derivation that has $(p \to q)$ as a line uses it.

### Quotation and quasi-quotation

A quotation names the exact string between the marks.
So '$(\varphi \to \psi)$' names a string of five symbols that contains Greek letters, and this string is not a formula of $L$.
A quasi-quotation $\ulcorner (\varphi \to \psi) \urcorner$ names a formula of $L$ that depends on the values of the metavariables.
If $\varphi$ is $p$ and $\psi$ is $(q \wedge r)$, then $\ulcorner (\varphi \to \psi) \urcorner$ is the formula $(p \to (q \wedge r))$.
Quasi-quotation lets us state rules and schemas, such as "for all formulas $\varphi$, the formula $\ulcorner (\varphi \to \varphi) \urcorner$ is a theorem".
The [[worked example|J3JB3N4K4A]] checks these computations symbol by symbol.

### Metavariables and schemas

An axiom [[schema|NYK5HABF3K]] such as $\varphi \to (\psi \to \varphi)$ is not a formula of $L$, because $\varphi$ and $\psi$ are not symbols of $L$.
It is a description, in the metalanguage, of infinitely many formulas of $L$, its instances.
The same holds for a [[rule of inference|QPD3X471Q1]] such as modus ponens, "from $\varphi$ and $\varphi \to \psi$ infer $\psi$".

### Theorems and metatheorems

A theorem of a formal system $S$ is a formula of $L$, for example $p \to p$ in a [[Hilbert system|1MGMQX43B8]].
A metatheorem is a statement about $S$, proved in the metalanguage, usually by induction on formulas or on derivations.
The [[deduction theorem|9X08XK5RV2]] is a metatheorem: if $\Gamma \cup \set{\varphi} \vdash \psi$, then $\Gamma \vdash \varphi \to \psi$.
Other metatheorems are the [[soundness|4A84VHDTHV]] of a proof system, [[Gödel's completeness theorem|WQ1ZE255SF]], the consistency of a system, and the fact that $MU$ is not a theorem of the [[MIU system|PMN32E37BW]].
The [[example of a Hilbert system|SKJFMANQTW]] sorts the symbols of a theorem and of a metatheorem into the two levels.

### Examples

- [[Theorems and metatheorems of a Hilbert system|SKJFMANQTW]]: the object language is propositional logic, and the metalanguage is English with Greek metavariables and the turnstile.
- [[Quotation and quasi-quotation of formulas|J3JB3N4K4A]]: the corners build formulas of $L$ from the values of metavariables.
- First-order arithmetic studied in set theory: the sentence $\forall x\, (x + 0 = x)$ belongs to the object language, and "$\mathsf{PA} \vdash \forall x\, (x + 0 = x)$" belongs to the metalanguage.
- Arithmetic as a metalanguage of its own syntax: by [[Gödel numbering|MFJXPAF0R0]], the property "$\varphi$ is provable in $\mathsf{PA}$" is expressed by a formula $\mathrm{Prov}(x)$ of the object language.

### Non-examples

- [[Arithmetic as the metalanguage of its own truth|NJ1RCSBQ27]] fails: no formula of arithmetic defines the true sentences of arithmetic, by [[Tarski's undefinability theorem|YRV6SYK2BY]].
- A translation from French into English is not a pair of object language and metalanguage. "Snow is white" translates "La neige est blanche", but it says nothing about French words.
- A string that mixes the levels, such as $p \to {\vdash} q$, belongs to neither language: $\vdash$ is not a symbol of $L$, and the string is not a sentence of the metalanguage.

### Basic properties

- The metalanguage must be able to name each expression of $L$ and to speak about finite strings. A small part of arithmetic or of set theory suffices for the syntax.
- A language that contains its own truth predicate and the usual logic, with all sentences "$\varphi$ is true if and only if $\varphi$", is inconsistent, by the liar argument. This is the content of the [[semantically closed language|S2MZ6KV3G9]] problem.
- So a metalanguage that defines truth for $L$ must be richer than $L$, and this gives the [[Tarskian hierarchy|Z6MCGB0ZFX]] of languages.
- The metalanguage can itself be formalized, for example in set theory or in a logical framework, and it then becomes the object language of a new metalanguage.

### History

Hilbert and his school spoke of metamathematics in the 1920s, the study of formal systems by finitary means.
Tarski's work on the concept of truth in formalized languages, first published in Polish in 1933, made the separation of object language and metalanguage precise.
Willard Van Orman Quine introduced corner quotes in his book *Mathematical Logic* of 1940.

### Common errors

- Writing a turnstile inside a formula, as in $p \to {\vdash} q$. The turnstile belongs to the metalanguage.
- Confusing $\vdash p \to q$ with "if $\vdash p$, then $\vdash q$". In classical propositional logic the second statement is true, because $p$ is not a theorem, while the first is false, because $p \to q$ is not a tautology.
- Reading Quine corners and Gödel corners as the same thing. Quine corners name formulas, while Gödel corners give numerals, which are terms of arithmetic.

## Explanations

### L1 human

When we talk about a language, we use a language to do it.
A grammar book for French is written in English: French is the language we study, and English is the language we use to talk about it.
In logic, the formulas form the studied language, called the object language.
The ordinary mathematical language in which we explain and prove things about the formulas is the metalanguage.
Quotation marks show when we talk about a word: Paris is a city, but "Paris" is a word with five letters.

### L2 human

We sort the parts of the sentence "for all formulas $\varphi$ and $\psi$, if $\vdash \varphi$ and $\vdash \varphi \to \psi$, then $\vdash \psi$".

1. "For all", "if", "and", "then" are English words of the metalanguage.
2. $\varphi$ and $\psi$ are metavariables: they range over formulas, and they are not symbols of the object language.
3. $\vdash$ is a predicate of the metalanguage: "$\vdash \varphi$" says that $\varphi$ is a theorem.
4. In "$\vdash \varphi \to \psi$" the arrow $\to$ is a symbol of the object language, and the expression stands for $\vdash \ulcorner \varphi \to \psi \urcorner$.
5. So the sentence is a metatheorem: the set of theorems is closed under modus ponens. It holds because two derivations can be joined and extended by one step.

The typical use of the distinction is to state rules, schemas and metatheorems without ambiguity.
A trap is to apply a metatheorem inside a derivation as if it were a formula, or to quantify over formulas inside the object language.

### L3 human

Tarski's theory of truth defines "$\varphi$ is true in the structure $\mathcal{M}$" in a metalanguage that speaks about the formulas of $L$ and about $\mathcal{M}$.
His undefinability theorem shows that for arithmetic this metalanguage must be stronger than the object language.
Gödel's method goes the other way: it codes the syntax of $L$ inside $L$, so that the object language can express syntactic metalanguage notions such as provability, and this leads to the [[incompleteness theorems|X9WYNYE29C]].
The two results together show that syntax can be internalized and truth cannot.

The distinction is the same as the one between a programming language and the language in which its interpreter is written, and between a logic and a logical framework that encodes it.
In a framework such as the Edinburgh logical framework, the object logic is encoded as a signature of a type theory.
Metatheorems of the object logic then become constructions in the framework, as described on the page on [[abstract logical systems|RQXV7PM2WT]].
In [[proof theory|N4EDJNMTEF]] the strength of the metatheory matters: Hilbert's program asked for consistency proofs in a weak finitary metatheory, and Gentzen's proof for arithmetic used induction up to the ordinal $\varepsilon_0$ in the metatheory.
