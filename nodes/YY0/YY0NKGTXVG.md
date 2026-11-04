---
tag: YY0NKGTXVG
kind: statement
role: proposition
name: Well-formed formulas (wffs)
sources:
  - wikipedia: en:1557634@r1345686870
    locator: Propositional formula, section Well-formed formulas (wffs)
    note: adopted
    mention: wikipedia://en/1557634#9LZG
    sections: [Statement]
inventory: [5K9WYPXDNF]
---

## Statement

A key property of formulas is that they can be uniquely parsed to determine the structure of the formula in terms of its propositional variables and logical connectives. When formulas are written in infix notation, as above, unique readability is ensured through an appropriate use of parentheses in the definition of formulas. Alternatively, formulas can be written in Polish notation or reverse Polish notation, eliminating the need for parentheses altogether.

The inductive definition of infix formulas in the previous section can be converted to a formal grammar in Backus-Naur form:

```bnf
<formula> ::= <propositional variable>
| ( ¬ <formula> )
| ( <formula> ∧ <formula>)
| ( <formula> ∨ <formula> )
| ( <formula> → <formula> )
| ( <formula> ↔ <formula> )
```

It can be shown that any expression matched by the grammar has a balanced number of left and right parentheses, and any nonempty initial segment of a formula has more left than right parentheses. This fact can be used to give an algorithm for parsing formulas. For example, suppose that an expression *x* begins with $( \lnot$. Starting after the second symbol, match the shortest subexpression *y* of *x* that has balanced parentheses. If *x* is a formula, there is exactly one symbol left after this expression, this symbol is a closing parenthesis, and *y* itself is a formula. This idea can be used to generate a recursive descent parser for formulas.
