---
tag: ~8fccb51d
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

We compare use, quotation and quasi-quotation, first for words and then for [[formulas|HYJ10AF6RT]] of propositional logic.
The object language $L$ has the variables $p, q, r$, the connectives $\neg, \wedge, \to$ and the parentheses.
The metalanguage is English with the metavariables $\varphi, \psi$, quotation marks and Quine corners.

Use and mention of a word.

1. In "Boston is a city", the word Boston is used: the sentence speaks about the city.
2. In "'Boston' has six letters", the word is mentioned: the quotation names the word. The letters are B, o, s, t, o, n, which are six.
3. "Boston has six letters" speaks about the city, which has no letters. So the sentence is false or meaningless, and the error is a confusion of use and mention.

Quotation of a formula.

4. The quotation '$(p \to (q \wedge r))$' names the [[string|1P6EP01HZF]] of the symbols $($, $p$, $\to$, $($, $q$, $\wedge$, $r$, $)$, $)$, which are nine symbols of $L$.
5. The quotation '$(\varphi \to \psi)$' names the string of the five symbols $($, $\varphi$, $\to$, $\psi$, $)$. Two of them are Greek letters, which are not symbols of $L$, so this string is not a formula of $L$.

Quasi-quotation.

6. Let $\varphi$ be the formula $p$ and $\psi$ the formula $(q \wedge r)$.
7. The quasi-quotation $\ulcorner (\varphi \to \psi) \urcorner$ is the string $($, then the value of $\varphi$, then $\to$, then the value of $\psi$, then $)$.
8. Substituting the values gives $(p \to (q \wedge r))$, the formula of step 4.
9. With $\varphi$ equal to $\neg p$ and $\psi$ equal to $p$, the same quasi-quotation is $(\neg p \to p)$, a different formula.

Quantifying into quotations.

10. "For every formula $\varphi$, the formula $\ulcorner (\varphi \to \varphi) \urcorner$ has a derivation" is a meaningful statement. For each value of $\varphi$ it speaks about one formula of $L$.
11. "For every formula $\varphi$, '$(\varphi \to \varphi)$' has a derivation" is false. The quotation names one fixed string with Greek letters, whatever $\varphi$ is, and that string is not a formula of $L$.

## Remarks

The example shows the three tools of the metalanguage for speaking about expressions.
A plain quotation names one fixed string, so a variable inside it is not a variable at all.
A quasi-quotation is a template: its metavariables are replaced by their values, and the result depends on the values.
Most books drop the corners and write $\varphi \to \psi$ for $\ulcorner \varphi \to \psi \urcorner$, which is safe once the reader knows the convention.
In the theory of Gödel numbering the corners $\ulcorner \varphi \urcorner$ mean something else: the numeral of the code of $\varphi$, which is a term of arithmetic.

## Explanations

### L1 human

Quotation marks let us talk about a word instead of the thing it names.
London is big, but "London" is short: it has six letters.
A template such as "Dear ___," is like a quasi-quotation: it becomes a real greeting only after we fill in a name.
In logic, the template "( ___ implies ___ )" becomes a real formula only after we put formulas into the gaps.

### L2 human

We compute $\ulcorner \neg (\varphi \wedge \psi) \urcorner$ for $\varphi = (p \to q)$ and $\psi = \neg r$.

1. The template is the symbol $\neg$, then $($, then the value of $\varphi$, then $\wedge$, then the value of $\psi$, then $)$.
2. Filling in gives $\neg ((p \to q) \wedge \neg r)$.
3. Count the symbols: $\neg$, $($, $($, $p$, $\to$, $q$, $)$, $\wedge$, $\neg$, $r$, $)$. There are eleven.

The typical use of quasi-quotation is the statement of schemas and rules, such as "every formula $\ulcorner \varphi \to (\psi \to \varphi) \urcorner$ is an axiom".
A trap appears when outer parentheses are dropped: if $\varphi$ is written $p \wedge q$, then $\ulcorner \neg \varphi \urcorner$ is $\neg (p \wedge q)$, not the different formula $\neg p \wedge q$.
