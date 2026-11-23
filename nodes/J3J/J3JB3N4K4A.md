---
tag: J3JB3N4K4A
kind: example
name: Quotation and quasi-quotation of formulas
aliases: [quine-corners]
msc: ["03B99", "03A05"]
topics: [H8QZY0RZXZ]
audience: ug2
instance_of: [D9G8M42GKC]
uses: [D9G8M42GKC, HYJ10AF6RT, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-quotation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Use%E2%80%93mention_distinction
    locator: lead section
---

## Example

The metalanguage has three ways to speak about expressions: using them, quoting them, and quasi-quoting them with metavariables.
We compare the three, first for words and then for [[formulas|HYJ10AF6RT]] of propositional logic.
The object language $L$ has the variables $p, q, r$, the connectives $\neg, \wedge, \to$ and parentheses.
The metalanguage is English with the metavariables $\varphi, \psi$, quotation marks and Quine corners.

Start with a word.
In "Boston is a city" the word Boston is used, since the sentence speaks about the city.
In "'Boston' has six letters" the word is mentioned, since the quotation names the word, and its letters B, o, s, t, o, n are six.
"Boston has six letters" speaks about the city, which has no letters, so it confuses use and mention.

Now quote formulas.

1. The quotation '$(p \to (q \wedge r))$' names the [[string|1P6EP01HZF]] of nine symbols of $L$: $($, $p$, $\to$, $($, $q$, $\wedge$, $r$, $)$, $)$.
2. The quotation '$(\varphi \to \psi)$' names the string of five symbols $($, $\varphi$, $\to$, $\psi$, $)$.
   Two of them are Greek letters, which are not symbols of $L$, so this string is not a formula of $L$.

Then quasi-quote.

3. Let $\varphi$ be the formula $p$ and $\psi$ the formula $(q \wedge r)$.
4. The quasi-quotation $\ulcorner (\varphi \to \psi) \urcorner$ is the string $($, then the value of $\varphi$, then $\to$, then the value of $\psi$, then $)$.
5. Substituting the values gives $\ulcorner (\varphi \to \psi) \urcorner = (p \to (q \wedge r))$, the formula of step 1.
6. With $\varphi = \neg p$ and $\psi = p$, the same quasi-quotation is $(\neg p \to p)$, a different formula.

Finally, quantify over metavariables.

7. "For every formula $\varphi$, the formula $\ulcorner (\varphi \to \varphi) \urcorner$ has a derivation" is meaningful, since for each value of $\varphi$ it speaks about one formula of $L$.
8. "For every formula $\varphi$, '$(\varphi \to \varphi)$' has a derivation" is false.
   The quotation names one fixed string with Greek letters, whatever $\varphi$ is, and that string is not a formula of $L$.

## Remarks

A plain quotation names one fixed string, so a letter inside it is not a variable at all.
A quasi-quotation is a template: its metavariables are replaced by their values, and the result depends on the values.
Most books drop the corners and write $\varphi \to \psi$ for $\ulcorner \varphi \to \psi \urcorner$, which is safe once the reader knows the convention.
Watch out: in the theory of Gödel numbering, $\ulcorner \varphi \urcorner$ means the numeral of the code of $\varphi$, which is a term of arithmetic and not a formula.

## Explanations

### L1 human

Quotation marks let you talk about a word instead of the thing it names.
London is big, but "London" is short: it has six letters.
A form letter "Dear ___," is like a quasi-quotation, since it becomes a real greeting only after you fill in a name.
In logic, the template "( ___ implies ___ )" becomes a real formula only after you put formulas into the gaps.

### L2 human

Compute $\ulcorner \neg (\varphi \wedge \psi) \urcorner$ for $\varphi = (p \to q)$ and $\psi = \neg r$.
The template is the symbol $\neg$, then $($, then the value of $\varphi$, then $\wedge$, then the value of $\psi$, then $)$.
Filling in gives
$$\neg ((p \to q) \wedge \neg r).$$
Check: the symbols are $\neg$, $($, $($, $p$, $\to$, $q$, $)$, $\wedge$, $\neg$, $r$, $)$, which are eleven.
The typical use of quasi-quotation is to state schemas and rules, such as "every formula $\ulcorner \varphi \to (\psi \to \varphi) \urcorner$ is an axiom".
Watch out when outer parentheses are dropped: if $\varphi$ is written $p \wedge q$, then $\ulcorner \neg \varphi \urcorner$ is $\neg (p \wedge q)$, not the different formula $\neg p \wedge q$.
