---
tag: 2WPGB3N4A7
kind: proof
name: Proof of Cantor's theorem
msc: ["03E10"]
proves: 0WTEMGYV2C
sources:
  - wikipedia: en:341442@r1356713544
    locator: Cantor's theorem, section Proof
    note: adopted
    mention: wikipedia://en/341442#J939
    sections: [Proof]
---

## Proof

Cantor's argument is elegant and remarkably simple. The complete proof is presented below, with detailed explanations to follow.

By definition of cardinality, we have $\operatorname{card}(X) < \operatorname{card}(Y)$ for any two sets $X$ and $Y$ if and only if there is an [[injective function|09NWETVTNY]] but no bijective function from $X$ to $Y$. It suffices to show that there is no surjection from $X$ to $Y$. This is the heart of Cantor's theorem: there is no surjective function from any set $A$ to its power set. To establish this, it is enough to show that no function $f$ (that maps elements in $A$ to subsets of $A$) can reach every possible subset, i.e., we just need to demonstrate the existence of a subset of $A$ that is not equal to $f(x)$ for any $x \in A$. Recalling that each $f(x)$ is a subset of $A$, such a subset is given by the following construction, sometimes called the [[Cantor diagonal set|0XCH8QVDCQ]] of $f$:

$$B=\{x\in A \mid x\not\in f(x)\}.$$

This means, by definition, that for all $x\in A$, $x\in B$ if and only if $x\notin f(x)$. For all $x$ the sets $B$ and $f(x)$ cannot be equal because $B$ was constructed from elements of $A$ whose images under $f$ did not include themselves. For all $x\in A$ either $x\in f(x)$ or $x\notin f(x)$. If $x\in f(x)$ then $f(x)$ cannot equal $B$ because $x\in f(x)$ by assumption and $x\notin B$ by definition. If $x\notin f(x)$ then $f(x)$ cannot equal $B$ because $x\notin f(x)$ by assumption and $x\in B$ by the definition of $B$.

Equivalently, and slightly more formally, we have just proved that the existence of $\xi \in A$ such that $f(\xi )=B$ implies the following contradiction:

$$\begin{aligned} \xi\in B &\iff \xi\notin f(\xi) && \text{(by definition of }B\text{)}; \\ \xi \in B &\iff \xi \in f(\xi) && \text{(by assumption that }f(\xi)=B\text{)}. \\ \end{aligned}$$

Therefore, by [[reductio ad absurdum|0J0XBKG64S]], the assumption must be false. Thus there is no $\xi \in A$ such that $f(\xi )=B$ ; in other words, $B$ is not in the image of $f$ and $f$ does not map onto every element of the power set of $A$, i.e., $f$ is not surjective.

Finally, to complete the proof, we need to exhibit an injective function from $A$ to its power set. Finding such a function is trivial: just map $x$ to the singleton set $\{x\}$. The argument is now complete, and we have established the strict inequality for any set $A$ that $\operatorname{card}(A) < \operatorname{card}(\mathcal{P}(A))$.

Another way to think of the proof is that $B$, empty or non-empty, is always in the power set of $A$. For $f$ to be [[onto|01RVCMSN5N]], some element of $A$ must map to $B$. But that leads to a contradiction: no element of $B$ can map to $B$ because that would contradict the criterion of membership in $B$, thus the element mapping to $B$ must not be an element of $B$ meaning that it satisfies the criterion for membership in $B$, another contradiction. So the assumption that an element of $A$ maps to $B$ must be false; and $f$ cannot be onto.

Because of the double occurrence of $x$ in the expression "$x\in f(x)$", this is a [[diagonal argument|0XCH8QVDCQ]]. For a countable (or finite) set, the argument of the proof given above can be illustrated by constructing a table in which

1. each row is labelled by a unique $x$ from $A=\{x_1 ,x_2 , \ldots \}$, in this order. $A$ is assumed to admit a [[linear order|0316AYH1SC]] so that such table can be constructed.
1. each column of the table is labelled by a unique $y$ from the [[power set|00E0YZCERH]] of $A$; the columns are ordered by the argument to $f$, i.e. the column labels are $f(x_1),f(x_2)$, ..., in this order.
1. the intersection of each row $x$ and column $y$ records a true/false bit whether $x\in y$.

Given the order chosen for the row and column labels, the main diagonal $D$ of this table thus records whether $x\in f(x)$ for each $x\in A$. One such table will be the following:

$$\begin{array}{cccccc} & f(x_1) & f(x_2) & f(x_3) & f(x_4) & \cdots \\ \hline x_1 & {\color{red} T} & T & F & T & \cdots \\ x_2 & T & {\color{red} F} & F & F & \cdots \\ x_3 & F & F & {\color{red} T} & T & \cdots \\ x_4 & F & T & T & {\color{red} T} & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{array}$$

The set $B$ constructed in the previous paragraphs coincides with the row labels for the subset of entries on this main diagonal $D$ (which in above example, coloured red) where the table records that $x\in f(x)$ is false. Each row records the values of the indicator function of the set corresponding to the column. The indicator function of $B$ coincides with the logically negated (swap "true" and "false") entries of the main diagonal. Thus the indicator function of $B$ does not agree with any column in at least one entry. Consequently, no column represents $B$.

Despite the simplicity of the above proof, it is rather difficult for an automated theorem prover to produce it. The main difficulty lies in an automated discovery of the Cantor diagonal set. Lawrence Paulson noted in 1992 that Otter could not do it, whereas Isabelle could, albeit with a certain amount of direction in terms of tactics that might perhaps be considered cheating.
