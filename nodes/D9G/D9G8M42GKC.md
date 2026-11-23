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

Logic studies a language with the help of another language, and keeping the two apart prevents confusion and paradox.
Look at the sentence "$p \to p$ is a theorem".
The part $p \to p$ is a string of a [[formal language|5MFZ4VNY6D]], and the words "is a theorem" are English that speaks about that string.

The object language is the language $L$ whose expressions we study.
The metalanguage is the language in which we describe $L$, state its rules and prove facts about it; usually it is mathematical English with some extra symbols.
In the metalanguage the expressions of $L$ are objects: it has names for them (quotations), variables that range over them (metavariables), and predicates about them, such as "is a formula" or "is a theorem".
A theorem of a [[formal system|439M8B4DY2]] is a formula of the object language that has a derivation.
A metatheorem is a statement of the metalanguage about the system, proved by ordinary mathematics.

## Motivation

When the two levels are mixed without care, paradoxes appear.
The [[liar sentence|KBYY281V8T]] "this sentence is false" speaks about its own truth, and it can be neither true nor false.
Tarski showed that such paradoxes disappear when the truth of the sentences of $L$ is defined in a separate metalanguage.
Hilbert's study of formal systems needed the same care for a different reason.
He wanted to prove statements such as "no derivation ends in $0 = 1$", and such a statement is about derivations, so it lives in the metalanguage.

The distinction runs through the whole area.
Soundness, completeness and consistency are metatheorems.
Gödel's [[incompleteness theorems|X9WYNYE29C]] work because arithmetic can serve as a metalanguage for its own syntax, and Tarski's undefinability theorem shows that it cannot serve for its own truth.

## Notation

Metavariables are letters of the metalanguage that range over expressions of $L$.
We use $\varphi, \psi, \chi$ for formulas, $\Gamma, \Delta$ for sets of formulas and $t$ for terms, while $p, q, r$ are propositional variables of the object language.
The turnstiles $\vdash$ and $\models$ belong to the metalanguage, and $\to$, $\neg$, $\forall$ belong to the object language.
Quotation marks name an expression: 'snow' is the name of the word snow.
Quine corners form quasi-quotations, so that $\ulcorner \varphi \to \psi \urcorner$ is the formula made of the value of $\varphi$, then the symbol $\to$, then the value of $\psi$.
Most books let the symbols of $L$ name themselves and write $\varphi \to \psi$ for $\ulcorner \varphi \to \psi \urcorner$; some print object symbols in bold.
Watch out: in [[Gödel numbering|MFJXPAF0R0]], $\ulcorner \varphi \urcorner$ means something else, the numeral of the code of $\varphi$, which is a term of the object language.

## Remarks

### Use and mention

A word is used when it stands for what it means, and mentioned when the sentence speaks about the word itself.
In "Boston is a city" the word Boston is used, and in "'Boston' has six letters" it is mentioned.
The sentence "Boston has six letters" confuses the two, since a city has no letters.
Formulas need the same care: "$(p \to q)$ has five symbols" mentions a formula, while a derivation with $(p \to q)$ as a line uses it.

### Quotation and quasi-quotation

A quotation names exactly the string between the marks.
So '$(\varphi \to \psi)$' names a string of five symbols that contains two Greek letters, and that string is not a formula of $L$.
A quasi-quotation names a formula of $L$ that depends on the values of the metavariables.
If $\varphi$ is $p$ and $\psi$ is $(q \wedge r)$, then
$$\ulcorner (\varphi \to \psi) \urcorner = (p \to (q \wedge r)).$$
This is how we state rules and schemas: "for every formula $\varphi$, the formula $\ulcorner (\varphi \to \varphi) \urcorner$ is a theorem".
The [[worked example|J3JB3N4K4A]] checks such computations symbol by symbol.

### Schemas live in the metalanguage

An axiom [[schema|NYK5HABF3K]] such as $\varphi \to (\psi \to \varphi)$ is not a formula of $L$, because $\varphi$ and $\psi$ are not symbols of $L$.
It describes, in the metalanguage, infinitely many formulas of $L$, its instances, such as $p \to (q \to p)$.
A [[rule of inference|QPD3X471Q1]] such as modus ponens, "from $\varphi$ and $\varphi \to \psi$ infer $\psi$", is a schema in the same sense.

### Theorems and metatheorems

The formula $p \to p$ is a theorem of a [[Hilbert system|1MGMQX43B8]].
The [[deduction theorem|9X08XK5RV2]], "if $\Gamma \cup \{ \varphi \} \vdash \psi$, then $\Gamma \vdash \varphi \to \psi$", is a metatheorem, proved by induction on derivations.
So are the [[soundness|4A84VHDTHV]] of a proof system, [[Gödel's completeness theorem|WQ1ZE255SF]], and the fact that $MU$ is not a theorem of the [[MIU system|PMN32E37BW]].
[[Theorems and metatheorems of a Hilbert system|SKJFMANQTW]] sorts the symbols of each into the two levels.

When the object language is first-order arithmetic studied in set theory, $\forall x\, (x + 0 = x)$ is a sentence of the object language, and "$\mathsf{PA} \vdash \forall x\, (x + 0 = x)$" is a sentence of the metalanguage.
Through Gödel numbering, arithmetic can even express its own syntax: a formula $\mathrm{Prov}(x)$ of the object language says that $x$ codes a sentence provable in $\mathsf{PA}$.

### What does not fit

[[Arithmetic as the metalanguage of its own truth|NJ1RCSBQ27]] fails: by [[Tarski's undefinability theorem|YRV6SYK2BY]], no formula of arithmetic defines the set of true sentences of arithmetic.
Translation is not the same relation either.
"Snow is white" translates "La neige est blanche", but it says nothing about French words, so English is not acting as a metalanguage for French there.
A string such as $p \to {\vdash} q$ belongs to neither language, since $\vdash$ is not a symbol of $L$ and the string is not an English sentence.

### Why truth needs a richer metalanguage

The metalanguage must name each expression of $L$ and speak about finite strings; a small part of arithmetic or set theory is enough for syntax.
Truth is different.
A language with the usual logic that contains its own truth predicate, with every sentence "$\varphi$ is true if and only if $\varphi$", is inconsistent, by the liar argument; this is the problem of a [[semantically closed language|S2MZ6KV3G9]].
So a metalanguage that defines truth for $L$ must be richer than $L$, and repeating the step gives the [[Tarskian hierarchy|Z6MCGB0ZFX]].
A metalanguage can itself be formalized, in set theory or a logical framework, and it then becomes the object language of a new metalanguage.

### Watch out

Do not confuse $\vdash p \to q$ with "if $\vdash p$, then $\vdash q$".
In classical propositional logic the second is true, because $p$ is not a theorem, and the first is false, because $p \to q$ is not a tautology.
Do not put a turnstile inside a formula, and do not read Quine corners as Gödel corners.

### History

Hilbert and his school called the study of formal systems by finitary means metamathematics in the 1920s.
Tarski's work on the concept of truth in formalized languages, first published in Polish in 1933, made the separation of object language and metalanguage precise.
Quine introduced corner quotes in his book *Mathematical Logic* of 1940.

### Try it

Is the schema $\varphi \to \varphi$ a formula of propositional logic?
No: it is a metalanguage description, and its instances, such as $q \to q$ and $(p \wedge r) \to (p \wedge r)$, are the formulas.

If $\varphi$ is $\neg p$, what is $\ulcorner \neg \varphi \urcorner$?
It is $\neg \neg p$, a formula with three symbols.

## Explanations

### L1 human

When we talk about a language, we use a language to do it.
A grammar book for French is written in English: French is the language we study, and English is the language we use to talk about it.
In logic, the formulas form the language we study, called the object language.
The ordinary mathematical language in which we explain and prove things about the formulas is the metalanguage.
Quotation marks show when we talk about a word: Paris is a city, but "Paris" is a word with five letters.

### L2 human

Sort the parts of the sentence "for all formulas $\varphi$ and $\psi$, if $\vdash \varphi$ and $\vdash \varphi \to \psi$, then $\vdash \psi$".
The words "for all", "if", "and" and "then" are English, so they belong to the metalanguage.
The letters $\varphi$ and $\psi$ are metavariables: they range over formulas and are not symbols of the object language.
The turnstile is a predicate of the metalanguage, and "$\vdash \varphi$" says that $\varphi$ is a theorem.
The arrow in "$\vdash \varphi \to \psi$" is a symbol of the object language, and the expression stands for $\vdash \ulcorner \varphi \to \psi \urcorner$.
So the whole sentence is a metatheorem, which says that the set of theorems is closed under modus ponens.
It holds because two derivations can be written one after the other and extended by one step.
Watch out for the typical slip: using a metatheorem inside a derivation as if it were a formula.

### L3 human

Tarski's theory of truth defines "$\varphi$ is true in the structure $\mathcal{M}$" in a metalanguage that speaks about the formulas of $L$ and about $\mathcal{M}$.
His undefinability theorem shows that for arithmetic this metalanguage must be stronger than the object language.
Gödel's method goes the other way: it codes the syntax of $L$ inside $L$, so that the object language expresses syntactic notions such as provability.
Together the two results show that syntax can be internalized and truth cannot.

The same distinction separates a programming language from the language in which its interpreter is written, and a logic from a logical framework that encodes it.
In the Edinburgh logical framework, an object logic is encoded as a signature of a type theory, and metatheorems about it become constructions in the framework; [[abstract logical systems|RQXV7PM2WT]] describes this.
In [[proof theory|N4EDJNMTEF]] the strength of the metatheory matters.
Hilbert's program asked for consistency proofs in a weak finitary metatheory, and Gentzen's proof for arithmetic used induction up to the ordinal $\varepsilon_0$ in the metatheory.
