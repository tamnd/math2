---
tag: 1GQEQHQ57F
kind: example
name: Subformulas and modal depth of a modal formula
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [C3RZY20ETK]
uses: [C3RZY20ETK, G8VGTW9P4F, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

We list the subformulas and compute the modal depth of the following [[modal formula|G8VGTW9P4F]]:
$$\varphi = \square(p \to \lozenge q) \to \lozenge\square p.$$
For this count we treat $\neg$ and $\lozenge$ as primitive symbols, so $\lozenge\psi$ has the single immediate subformula $\psi$.
The modal depth is defined by recursion on formulas:
$$\operatorname{md}(p) = \operatorname{md}(\bot) = 0, \quad \operatorname{md}(\alpha \to \beta) = \max(\operatorname{md}(\alpha), \operatorname{md}(\beta)), \quad \operatorname{md}(\square\alpha) = \operatorname{md}(\lozenge\alpha) = \operatorname{md}(\alpha) + 1.$$

We first collect the subformulas.

1. The main connective of $\varphi$ is $\to$, with left part $\square(p \to \lozenge q)$ and right part $\lozenge\square p$.
2. The subformulas of the left part are $p$, $q$, $\lozenge q$, $p \to \lozenge q$ and $\square(p \to \lozenge q)$.
3. The subformulas of the right part are $p$, $\square p$ and $\lozenge\square p$.
4. With $\varphi$ itself, the distinct subformulas are $p$, $q$, $\lozenge q$, $p \to \lozenge q$, $\square(p \to \lozenge q)$, $\square p$, $\lozenge\square p$ and $\varphi$.
   There are $8$ of them, because $p$ occurs in both parts and is counted once.

Then we compute the depth from the inside out.

5. The variables give $\operatorname{md}(p) = \operatorname{md}(q) = 0$.
6. One modal operator gives $\operatorname{md}(\lozenge q) = 1$ and $\operatorname{md}(\square p) = 1$.
7. The implication gives $\operatorname{md}(p \to \lozenge q) = \max(0, 1) = 1$.
8. The outer operators give $\operatorname{md}(\square(p \to \lozenge q)) = 2$ and $\operatorname{md}(\lozenge\square p) = 2$.
9. So $\operatorname{md}(\varphi) = \max(2, 2) = 2$.

## Remarks

The depth counts the longest chain of nested modal operators, not the number of operators.
The formula $\varphi$ has $4$ modal operators, but its depth is only $2$.

The count of subformulas depends on the primitive symbols, and the depth does not.
With the official primitives of [[modal logic|C3RZY20ETK]], $\lozenge q$ is $\neg\square\neg q$, that is $\square(q \to \bot) \to \bot$.
Then $\lozenge q$ adds the subformulas $\bot$, $\neg q$ and $\square\neg q$, and $\lozenge\square p$ adds $\neg\square p$ and $\square\neg\square p$.
The official count is $8 + 5 = 13$, but every depth stays the same, because $\neg$ adds no box.

The depth has a meaning in models.
The truth of a formula of depth $d$ at a world $w$ depends only on the worlds that we reach from $w$ in at most $d$ steps.
The reason is a [[structural induction|12MQ2NJ29A]]: the truth of $\square\psi$ at $w$ depends on the truth of $\psi$ at the successors of $w$, and $\psi$ has depth $d - 1$.
If we replace $p$ by $\square p$ in $\varphi$, the depth becomes $3$, and the formula looks one step further from $w$.

## Explanations

### L1 human

A modal formula is built from letters with "if then", "necessarily" and "possibly".
Its subformulas are the pieces that appear while we build it.
The modal depth is the largest number of "necessarily" and "possibly" that sit inside each other.
In "necessarily (if $p$ then possibly $q$)", the word "possibly" is inside "necessarily", so the depth is 2.
The formula "necessarily $p$ and necessarily $q$" has two boxes side by side, so its depth is only 1.

### L2 human

Take a second formula, $\psi = \square p \to \square\square q$.
Its subformulas are $p$, $q$, $\square p$, $\square q$, $\square\square q$ and $\psi$, so there are $6$.
Their depths are $0$, $0$, $1$, $1$, $2$ and $\max(1, 2) = 2$.
The typical use of such a count is in induction proofs and in [[filtration|6ZZSHAKG5F]], which works with the finite set of subformulas of one formula.
Watch out: a book that takes $\lozenge$ as primitive gives a smaller count of subformulas, so always say which symbols are primitive.
