---
tag: 9ZPQYZ5NDP
kind: example
name: PageRank as an eigenvector problem
msc: ["15A18", "15B51", "68P20"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [TA8QR5HFAY]
illustrates: [HBE0MHJ2ZP]
uses: [YVNZGHHZJ5, TA8QR5HFAY, HBE0MHJ2ZP, Y9FRWY8YX4, 0R5HTV7REV]
sources:
  - url: https://en.wikipedia.org/wiki/PageRank
    locator: Algorithm
  - url: https://en.wikipedia.org/wiki/PageRank
    locator: Damping factor
  - url: https://en.wikipedia.org/wiki/PageRank
    locator: History
---

## Example

A search engine finds thousands of pages that contain your search words, and it must decide which ones to show first.
PageRank answers with one idea: a page is important when important pages link to it.
This sounds circular, but it is an eigenvector equation, and linear algebra solves it.

Take a small web of four pages, with the links $1 \to 2$, $1 \to 3$, $2 \to 3$, $3 \to 1$, $4 \to 1$ and $4 \to 3$.
Imagine a random surfer who moves from page to page along links.
The rank of a page is the long-run share of time that the surfer spends there, which is the [[steady-state vector|TA8QR5HFAY]] of a Markov chain.

1. The links form a [[directed graph|0R5HTV7REV]].
   Put $s_{ij} = 1 / d_j$ when page $j$ links to page $i$, where $d_j$ is the number of links out of page $j$, and put $s_{ij} = 0$ otherwise.
   This gives
$$S = \begin{pmatrix} 0 & 0 & 1 & 1/2 \\ 1/2 & 0 & 0 & 0 \\ 1/2 & 1 & 0 & 1/2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
   Every page has at least one link out, so every column sums to $1$, and $S$ is a [[column-stochastic matrix|YVNZGHHZJ5]].
2. Now add damping.
   With probability $\alpha = 0.85$ the surfer follows a random link, and otherwise the surfer jumps to a random page.
   With the all-ones matrix $J$, this is the Google matrix $G = \alpha S + \frac{1 - \alpha}{4} J$, which is
$$G = \frac{1}{80} \begin{pmatrix} 3 & 3 & 71 & 37 \\ 37 & 3 & 3 & 3 \\ 37 & 71 & 3 & 37 \\ 3 & 3 & 3 & 3 \end{pmatrix}.$$
3. $G$ is stochastic, because $S$ and $\frac14 J$ are stochastic and $0.85 + 0.15 = 1$.
   All entries of $G$ are at least $3/80 > 0$.
4. By the theorem on [[eigenvalues and steady state of a positive stochastic matrix|HBE0MHJ2ZP]], $G$ has exactly one steady-state vector $r$.
   Also $G^k x_0 \to r$ for every probability vector $x_0$.
5. Write $a = 0.15/4 = 0.0375$.
   Then $G r = r$ reads
$$r_1 = a + 0.85 (r_3 + \tfrac12 r_4), \quad r_2 = a + 0.425\, r_1, \quad r_3 = a + 0.85 (\tfrac12 r_1 + r_2 + \tfrac12 r_4), \quad r_4 = a,$$
   together with $r_1 + r_2 + r_3 + r_4 = 1$.
6. No page links to page $4$, so $r_4 = 0.0375$.
   Then $r_1 + r_2 + r_3 = 0.9625$, and with $r_2 = 0.0375 + 0.425\, r_1$ this gives $r_3 = 0.925 - 1.425\, r_1$.
7. Put this into the first equation.
   This gives $r_1 = 0.0375 + 0.85 (0.925 - 1.425\, r_1) + 0.425 \cdot 0.0375$, so $2.21125\, r_1 = 0.8396875$.
8. So $r_1 \approx 0.3797$, $r_2 \approx 0.1989$, $r_3 \approx 0.3839$ and $r_4 = 0.0375$.
   In exact form, $r = (107480, 56293, 108653, 10614) / 283040$.
   Check the third equation: $0.0375 + 0.85 (0.18987 + 0.19889 + 0.01875) \approx 0.3839$.
9. So page $3$ comes first, then pages $1$, $2$ and $4$.
   Page $3$ has three links in, and page $1$ has only two, but one of those comes from the important page $3$.
10. A real search engine cannot solve the equations directly, so it multiplies instead.
    From $x_0 = (\frac14, \frac14, \frac14, \frac14)$, the iterates $x_{k+1} = G x_k$ are $x_1 \approx (0.3562, 0.1438, 0.4625, 0.0375)$ and $x_2 \approx (0.4466, 0.1889, 0.3270, 0.0375)$.
    Later, $x_5 \approx (0.3828, 0.2061, 0.3736, 0.0375)$ and $x_{10} \approx (0.3809, 0.1987, 0.3829, 0.0375)$.
    After $20$ steps they agree with $r$ to four decimals.
11. The eigenvalues of $G$ are $1$, $-0.425 \pm 0.425\, i$ and $0$.
    The second largest absolute value is $0.85 \cdot \sqrt{0.5} \approx 0.60$, and the error shrinks by about this factor at each step.

## Remarks

### What the example shows

The ranking is an eigenvector: $r$ is the eigenvector of $G$ for the eigenvalue $1$, scaled so that its entries sum to $1$.
Because every entry of $G$ is positive, this eigenvector exists, is unique and has positive entries.
Repeated multiplication by $G$ finds it, and the method is [[power iteration|H4MQD841BR]] from numerical linear algebra.
The general theory is the same as in [[steady-state vectors of Markov chains|Y9FRWY8YX4]].

### What the damping does

The damping changes the answer and makes it unique.
Without damping ($\alpha = 1$), the steady state of $S$ is $(0.4, 0.2, 0.4, 0)$.
Then pages $1$ and $3$ tie, and page $4$ gets rank $0$.
With damping, every page gets at least the share $(1 - \alpha)/n$, and the tie breaks in favor of page $3$.

In general, the eigenvalues of $G$ other than $1$ are $\alpha$ times eigenvalues of $S$.
So the second eigenvalue has absolute value at most $\alpha$.
For a large web, the error of the power iteration therefore shrinks roughly like $\alpha^k$, whatever the link structure.
The value $\alpha = 0.85$ is the one usually assumed for the original algorithm.

### Watch out: pages without links out

A page without links out gives a zero column in $S$, and then $S$ is not stochastic.
The usual fix replaces that column by $\frac1n \mathbf 1$, so that the surfer jumps to a random page from there.
Without the fix, some probability is lost at every step from that page, and the iterates of $G$ tend to $0$.

### History

PageRank was developed by Page and Brin at Stanford University in 1996.

### Try it

First, take three pages with the links $1 \to 2$, $2 \to 1$, $2 \to 3$ and $3 \to 1$, and find the undamped rank.
The equations $S r = r$ are $r_1 = \tfrac12 r_2 + r_3$, $r_2 = r_1$ and $r_3 = \tfrac12 r_2$.
So $r$ is proportional to $(2, 2, 1)$, and $r = (0.4, 0.4, 0.2)$.

Second, check that this chain converges even without damping.
It has the cycles $1 \to 2 \to 1$ of length $2$ and $1 \to 2 \to 3 \to 1$ of length $3$, and every page can reach every other page.
The greatest common divisor of the cycle lengths is $1$, so $S$ is regular.

## Explanations

### L1 human

A search engine must decide which pages are important.
PageRank says that a page is important when important pages link to it.
Imagine a surfer who clicks random links and sometimes jumps to a random page.
After a long time, the share of time that the surfer spends on each page is its rank.
In the small web here, page $3$ gets about $38\%$ of the time, and page $4$, which no page links to, gets less than $4\%$.

### L2 human

To compute PageRank for $n$ pages, do these steps.

1. Make the column-stochastic link matrix $S$, with a uniform column for a page without links out.
2. Form $G = \alpha S + \frac{1 - \alpha}{n} J$ with $\alpha = 0.85$.
3. Iterate $x_{k+1} = G x_k$ from the uniform vector until the change is small.

On a real web, $J$ is never stored, because $G x = \alpha S x + \frac{1 - \alpha}{n} \mathbf 1$ for a probability vector $x$, and $S$ is sparse.
The first trap is to rank by counting links in.
Page $1$ has fewer links in than page $3$, and it still comes close, because one of its two links in comes from page $3$, the top page.
The second trap is to forget the damping, because then the steady state can be non-unique or put zero weight on many pages.

### L3 human

PageRank is the Perron vector of a positive matrix, so the Perron-Frobenius theorem gives its existence, uniqueness and positivity.
Equivalently, $r$ solves the linear system $(I - \alpha S) r = \frac{1 - \alpha}{n} \mathbf 1$, and $I - \alpha S$ is invertible because the spectral radius of $\alpha S$ is $\alpha < 1$.
So PageRank is also a Neumann series $r = \frac{1 - \alpha}{n} \sum_k \alpha^k S^k \mathbf 1$, a weighted count of walks into each page.
The same idea ranks the vertices of any directed graph, and it is related to eigenvector centrality in network science.
