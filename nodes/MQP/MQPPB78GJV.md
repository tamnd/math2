---
tag: MQPPB78GJV
kind: statement
role: theorem
name: Sensitivity theorem
msc: [68Q17, "06E30", 05C50]
uses: [0X05GS525E, 0EREPBVG2G, 0FJY6G7FNA, 0BQAA2BK3Q, 8QQPVNR80F, 8ZVN9X9WEC]
about: [0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Sensitivity_theorem
same_as:
  wikidata: Q125935416
  wikipedia: Sensitivity theorem
---

## Statement

Let $n \ge 1$ and let $f \colon \set{0, 1}^n \to \set{0, 1}$ be a [[Boolean function|0X05GS525E]].
For $x \in \set{0, 1}^n$ and $1 \le i \le n$, let $x^{(i)}$ be $x$ with its $i$-th coordinate changed.
The *sensitivity* of $f$ is $s(f) = \max_{x} \abs{\set{i : f(x^{(i)}) \ne f(x)}}$.
The *degree* $\deg(f)$ is the degree of the unique real polynomial $p(x_1, \dots, x_n)$, of degree at most $1$ in each variable, with $p(x) = f(x)$ for all $x \in \set{0, 1}^n$.
Then
$$\deg(f) \le s(f)^2.$$

## Remarks

The proof, by Hao Huang in 2019, shows that every [[induced subgraph|0EREPBVG2G]] of the $n$-dimensional hypercube graph on more than $2^{n-1}$ vertices has [[maximum degree|0FJY6G7FNA]] at least $\sqrt{n}$.
For this, Huang signs the edges of the hypercube so that the signed adjacency matrix $A$ satisfies $A^2 = nI$, so its [[eigenvalues|0BQAA2BK3Q]] are $\pm \sqrt{n}$, each with multiplicity $2^{n-1}$.
The [[Cauchy interlacing theorem|8QQPVNR80F]] then gives the induced subgraph a largest eigenvalue at least $\sqrt{n}$, which bounds its maximum degree from below.
An earlier reduction of Gotsman and Linial turns this graph statement into the bound $\deg(f) \le s(f)^2$.

Example: for $f = x_1 \vee \dots \vee x_n$, flipping any coordinate of $x = 0$ changes the value, so $s(f) = n$.
Here $\deg(f) = n$, since $1 - f = (1 - x_1) \cdots (1 - x_n)$, and indeed $n \le n^2$.

## Explanations

### L1 human

The sensitivity of a yes/no function of $n$ bits counts, at the worst input, how many single bit flips change the answer.
The degree measures how complicated the function is as a polynomial.
The theorem says that a function of high degree must be sensitive to many bits at some input.
It settled the sensitivity conjecture, a question that had been open for nearly thirty years.

### L2 human

Many measures of the complexity of a Boolean function, such as degree, block sensitivity, certificate complexity and [[decision tree|8ZVN9X9WEC]] complexity, were known to be polynomially related to each other.
Sensitivity was the one measure not known to belong to this family.
Combined with the bound $\mathrm{bs}(f) \le 2 \deg(f)^2$ of Nisan and Szegedy on block sensitivity, the theorem gives $\mathrm{bs}(f) \le 2 s(f)^4$.
So sensitivity is polynomially related to all the others.
The short spectral proof is a striking use of linear algebra in combinatorics.
