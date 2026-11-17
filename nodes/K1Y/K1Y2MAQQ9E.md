---
tag: K1Y2MAQQ9E
kind: concept
name: Teaching logic
aliases: [logic-in-mathematics-education, teaching-of-logic]
msc: ["97E30", "97C30"]
topics: [VHGA6J4NZK]
audience: research
uses: [FA6YZGR2SS, EGTZPA6QH3, K930V33BSC, 7GYZJ2MGY9]
sources:
  - url: https://en.wikipedia.org/wiki/Wason_selection_task
    locator: Policing social rules
  - url: https://doi.org/10.1080/14640746808400161
    locator: pages 273-281
  - url: https://doi.org/10.1111/j.2044-8295.1982.tb01823.x
    locator: pages 407-420
  - url: https://doi.org/10.1007/BF01274210
    locator: pages 123-151
  - url: https://doi.org/10.1080/00029890.2003.11920029
    locator: pages 886-899
  - url: https://doi.org/10.1023/A:1024661004375
    locator: pages 5-34
  - url: https://doi.org/10.1007/978-94-007-2129-6_16
    locator: pages 369-389
  - url: https://doi.org/10.1007/s10649-007-9098-9
    locator: pages 187-204
  - url: https://doi.org/10.1371/journal.pone.0069399
    locator: whole article
---

## Summary

The teaching of logic is the study of how students learn to use the logical words of mathematics, "not", "and", "or", "if ... then" and "for all", and how a course can help them.
It covers logic as a school topic, logic as the first unit of a transition course, and logic learned only through the practice of proof.
A central object of research is the [[conditional statement|FA6YZGR2SS]], because everyday language and mathematics use "if" in different ways.
The field matters because most errors in early proofs are errors of logic: a proof of the converse, a wrong negation, or a wrong order of [[quantifiers|EGTZPA6QH3]].

## Motivation

In everyday speech, "if you finish your homework, you can watch television" is usually heard as "if and only if".
In mathematics, "if $n$ is divisible by $4$, then $n$ is even" says nothing about the odd numbers, and it does not claim the converse.
A student who reads the mathematical "if" as the everyday "if" will prove the wrong statement or will reject a correct proof.
The [[Wason selection task|7GYZJ2MGY9]] shows that most adults do not test a conditional rule correctly when the rule is abstract.
So logic does not come for free with intelligence or with general education, and the question is how to teach it.

## Remarks

### Examples

1. A logic unit at the start of a [[transition-to-proof course|HQDCSJG379]] teaches truth tables, the conditional, the contrapositive, the negation of quantified statements and De Morgan's laws.
2. A teacher asks students to [[negate|K930V33BSC]] the definition of a continuous function. Students must change each "for all" to "there exists" and each "there exists" to "for all", in the right order.
3. A teacher gives the Wason task in an abstract form and in a social form, for example "if a person drinks beer, then the person is over $18$". Students compare their answers and find the logical form that both versions share.
4. A teacher asks students to unpack an informal statement such as "a function is increasing when larger inputs give larger outputs" into a statement with explicit quantifiers.

### Non-examples

1. The study of formal systems, soundness and completeness is [[mathematical logic|DYJ0KGTPMR]]. It is the subject of logic, not of its teaching.
2. The psychology of reasoning in general, without a link to mathematics or teaching, belongs to cognitive psychology. The Wason task is a result of that field, and this page uses it only as evidence about learners.

### Research findings

1. Peter Wason introduced the selection task in 1966 and reported it in 1968. Most people chose the card that shows the hypothesis, and few chose the card that shows the negation of the conclusion.
2. Richard Griggs and James Cox (1982) gave a version of the task about drinking age, which people know from their lives. Most people solved this version, although its logical form is the same.
3. Annie Selden and John Selden (1995) found that undergraduate students had difficulty unpacking informal mathematical statements into their logical form. They argued that this skill is needed to check proofs.
4. Viviane Durand-Guerrier (2003) argued that the conditionals of mathematics are usually universally quantified statements about open sentences, such as "for all $n$, if $n$ is divisible by $4$, then $n$ is even". She argued that teaching should treat conditionals in this form, not only through truth tables of propositions.
5. Matthew Inglis and Adrian Simpson (2008) found that mathematics undergraduates gave more normatively correct answers on abstract conditional inference than comparable students of other subjects.
6. Nina Attridge and Matthew Inglis (2013) followed students of advanced school mathematics and students of English literature for one year. The conditional reasoning of the mathematics students changed more, without explicit teaching of logic.
7. In the same study, the change was toward the "defective conditional" reading, not toward the material conditional of logic. In the defective reading, a conditional with a false hypothesis is seen as irrelevant, not as true.

### History

Logic entered school curricula in France and in several other countries with the reforms of the 1960s, together with sets.
After the end of these reforms, most school curricula kept little explicit logic.
University transition courses kept a short logic unit before the work on proofs.
Research on the learning of logic in mathematics grew after the 1990s, with the work of Selden and Selden, Epp, Durand-Guerrier and Inglis.
In the ICMI Study 19 (2012), Durand-Guerrier, Paolo Boero, Nadia Douek, Epp and Denis Tanguay wrote a chapter on the role of logic in teaching proof.

### Common errors

1. A student proves the converse of the statement. The student reads "if $P$, then $Q$" as "if $Q$, then $P$", or as "$P$ if and only if $Q$".
2. A student negates "for all $x$, $P(x)$" as "for all $x$, not $P(x)$". The correct negation is "there exists $x$ with not $P(x)$".
3. A teacher assumes that the truth table of the conditional answers the questions of students. The truth table treats propositions, and the conditionals of mathematics contain variables and hidden quantifiers.

## Explanations

### L1 human

Logic in mathematics is about the small words: "not", "and", "or", "if ... then", "for all" and "there is".
These words have exact meanings in mathematics, and the meanings are sometimes different from everyday speech.
For example, "if a number ends in $0$, then it is even" is true.
It does not say that each even number ends in $0$, and indeed $4$ is even and does not end in $0$.
Many students mix up a statement and its reverse.
Teachers of logic look for tasks that make this difference visible.

### L2 human

We work through one task from a logic unit.
The task: negate the statement "every integer greater than $1$ has a prime divisor", and decide which of the two statements is true.

1. We write the statement with explicit quantifiers: for all integers $n$, if $n > 1$, then there exists a prime $p$ with $p \mid n$.
2. The negation of "for all $n$, $A(n)$" is "there exists $n$ with not $A(n)$".
3. The negation of "if $n > 1$, then $B(n)$" is "$n > 1$ and not $B(n)$". The negation of a conditional is not a conditional.
4. The negation of "there exists a prime $p$ with $p \mid n$" is "for all primes $p$, $p \nmid n$".
5. So the negation reads: there exists an integer $n > 1$ such that no prime divides $n$.
6. The original statement is true, because the smallest divisor $d > 1$ of $n$ is a prime, as the page on the [[well-ordering principle|01BX15HSRR]] shows. So the negation is false.

The typical use of such a task is to train the steps of [[negating mathematical statements|K930V33BSC]] before students need them in proofs by contradiction.
A trap is step 3: many students write the negation of a conditional as "if $n > 1$, then not $B(n)$".
That statement is stronger than the negation, and it is not the negation.

### L3 human

The research on logic in mathematics education uses results of the psychology of reasoning, such as the dual-process theories and the content effects of the Wason task.
It asks whether the study of mathematics trains general reasoning, a question that goes back to the old theory of formal discipline.
The studies of Inglis and coauthors suggest a more complex answer: mathematics students differ from others in conditional reasoning, but the change is toward a reading of the conditional that differs from the material conditional of logic textbooks.
The model-theoretic view of Durand-Guerrier links the teaching of logic to the [[language of mathematics|661V0DH7V3]], where open sentences and implicit quantifiers are the rule.
The page on [[student difficulties with proof|5K2969GSWE]] collects the errors that follow from these difficulties.
