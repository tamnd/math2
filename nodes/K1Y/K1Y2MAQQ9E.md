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

Four cards lie on a table and show E, K, 4 and 7.
Each card has a letter on one side and a number on the other, and the rule says: if a card has a vowel on one side, then it has an even number on the other side.
Which cards must you turn over to check the rule?
Most people turn E and 4, but the correct answer is E and 7.
The E card could hide an odd number, and the 7 card could hide a vowel, and either would break the rule, while nothing on the back of the 4 can break it.

This puzzle is the [[Wason selection task|7GYZJ2MGY9]], and it shows that reading a [[conditional statement|FA6YZGR2SS]] correctly does not come for free with intelligence or schooling.
The teaching of logic studies how students learn the logical words of mathematics, "not", "and", "or", "if ... then" and "for all", and how a course can help them.
It covers logic as a school topic, logic as the first unit of a transition course, and logic learned only through the practice of proof.

## Motivation

In everyday speech, "if you finish your homework, you can watch television" is usually heard as "if and only if".
In mathematics, "if $n$ is divisible by $4$, then $n$ is even" says nothing about odd numbers, and it does not claim the converse.
A student who reads the mathematical "if" as the everyday "if" will prove the wrong statement or reject a correct proof.
Most errors in early proofs are of this kind: a proof of the converse, a wrong negation, or a wrong order of [[quantifiers|EGTZPA6QH3]].
So logic is not a side topic in learning to prove, and the question is how and when to teach it.

## Notation

Research papers write the conditional as $p \to q$ or $p \Rightarrow q$, and call $p$ the antecedent and $q$ the consequent.
Studies of reasoning test four inferences: modus ponens (from $p$ infer $q$), modus tollens (from not $q$ infer not $p$), and the two invalid ones, affirming the consequent and denying the antecedent.
The "material conditional" is the truth-table reading, in which a conditional with a false antecedent is true.

## Remarks

### Why people choose E and 4

Peter Wason introduced the selection task in 1966 and reported it in detail in 1968 in the Quarterly Journal of Experimental Psychology.
In the abstract form, most participants chose the card that shows the antecedent, often with the card that shows the consequent, and few chose the card that shows the negation of the consequent.
In the 1970s Jonathan Evans and colleagues described one source of the pattern, which they called matching bias: people tend to choose the cards whose symbols are named in the rule.
The 4 is named and the 7 is not, so the 4 attracts attention even though it cannot falsify the rule.

The choice of the 7 is modus tollens: if the back were a vowel, the rule would demand an even number on the front.
That is the same move as a [[proof by contrapositive|0BB5TPGQ1N]], which is why the task matters to teachers of proof.

### Content changes the answer

Richard Griggs and James Cox (1982) gave a version about the drinking age, with cards that showed a drink or an age.
Most participants solved this version, although its logical form matches the abstract task.
So people do have the reasoning in familiar settings, and the difficulty lies in applying it to abstract rules.
Mathematics asks for exactly that application, because its conditionals concern objects that have no everyday meaning for the student.

### Logic as students meet it in proofs

Annie Selden and John Selden (1995) asked undergraduate students to unpack informal mathematical statements into their logical form, and many could not.
They argued that this skill is needed to check whether a proof proves the statement at hand.
Viviane Durand-Guerrier (2003) pointed out that the conditionals of mathematics are usually universally quantified statements about open sentences, such as "for all $n$, if $4 \mid n$, then $2 \mid n$".
She argued that teaching should treat conditionals in that form, not only through truth tables of single propositions.
Susanna Epp (2003) argued in the same direction and collected many examples of student errors with conditionals and quantifiers.

### Does studying mathematics train logic?

Matthew Inglis and Adrian Simpson (2008) found that mathematics undergraduates gave more normatively correct answers on an abstract conditional inference task than students of other subjects.
A comparison at one moment cannot show whether mathematics caused the difference or whether students with this skill choose mathematics.
Nina Attridge and Matthew Inglis (2013) therefore followed students of advanced school mathematics and students of English literature through one year.
The conditional reasoning of the mathematics students changed more, without explicit teaching of logic.
The change was toward the "defective conditional" reading, in which a conditional with a false antecedent counts as irrelevant, not toward the material conditional of logic textbooks.

### History

Logic entered school curricula in France and several other countries with the reforms of the 1960s, together with sets.
After those reforms ended, most school curricula kept little explicit logic, while university transition courses kept a short logic unit.
Research on how logic is learned in mathematics grew from the 1990s, with the work of Selden and Selden, Epp, Durand-Guerrier and Inglis.
In ICMI Study 19 (2012), Durand-Guerrier, Paolo Boero, Nadia Douek, Epp and Denis Tanguay wrote a chapter on the role of logic in teaching proof.

### Watch out

The commonest error is proving the converse: the student reads "if $P$, then $Q$" as "if $Q$, then $P$" or as "$P$ if and only if $Q$".
For "if $4 \mid n$, then $2 \mid n$" the converse fails at $n = 6$.
The second error is negating "for all $x$, $P(x)$" as "for all $x$, not $P(x)$", when the negation is "there exists $x$ with not $P(x)$".
A teacher can also go wrong, by assuming that the truth table of the conditional answers students' questions.
The truth table treats single propositions, and the conditionals of mathematics contain variables and hidden quantifiers.

### Try it

First, the rule is "if a card shows a square on one side, then it is red on the other", and the cards show a square, a circle, red and blue.
Turn the square and the blue card, since only these can hide a counterexample.

Second, [[negate|K930V33BSC]] "every continuous function on $[0, 1]$ is bounded".
The negation is "some continuous function on $[0, 1]$ is unbounded", which is false by the extreme value theorem.

## Explanations

### L1 human

Logic in mathematics is about the small words: "not", "and", "or", "if ... then", "for all" and "there is".
These words have exact meanings in mathematics, and the meanings sometimes differ from everyday speech.
For example, "if a number ends in $0$, then it is even" is true.
It does not say that each even number ends in $0$, and indeed $4$ is even and does not end in $0$.
Many students mix up a statement and its reverse, and teachers of logic look for tasks that make the difference visible.

### L2 human

Here is one task from a logic unit: negate "every integer greater than $1$ has a prime divisor", and decide which version is true.
First write the statement with explicit quantifiers:
$$\forall n \in \mathbb{Z}, \ n > 1 \to \exists p \text{ prime with } p \mid n.$$
The negation of "for all $n$, $A(n)$" is "there exists $n$ with not $A(n)$".
The negation of "$n > 1 \to B(n)$" is "$n > 1$ and not $B(n)$", so the negation of a conditional is not a conditional.
The negation of "some prime divides $n$" is "no prime divides $n$".
Together:
$$\exists n \in \mathbb{Z}, \ n > 1 \wedge \forall p \text{ prime}, \ p \nmid n.$$
The original statement is true, because the smallest divisor $d > 1$ of $n$ exists by the [[well-ordering principle|01BX15HSRR]] and must be prime, so the negation is false.
Tasks like this train [[negating mathematical statements|K930V33BSC]] before students need it in proofs by contradiction.
Watch out for the middle step: many students write "if $n > 1$, then no prime divides $n$", which is a different and stronger statement.

### L3 human

Research on logic in mathematics education draws on the psychology of reasoning, such as the content effects in the Wason task and the dual-process theories.
It also asks whether studying mathematics trains general reasoning, a question as old as the theory of formal discipline.
The studies of Inglis and coauthors suggest a more complex answer than either yes or no: mathematics students change, but toward a reading of the conditional that differs from the material conditional.
Durand-Guerrier's model-theoretic view links the teaching of logic to the [[language of mathematics|661V0DH7V3]], where open sentences and implicit quantifiers are the rule.
[[Student difficulties with proof|5K2969GSWE]] collects the errors that follow from these difficulties.
