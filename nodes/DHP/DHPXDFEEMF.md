---
tag: DHPXDFEEMF
kind: example
name: Pólya urn model
msc: [60C05, 60G42, 60J10]
instance_of: [0G48PYM96Q]
sources:
  - url: https://en.wikipedia.org/wiki/Pólya_urn_model
same_as:
  wikidata: Q2120628
  wikipedia: Pólya urn model
---

## Example

Let $a \ge 1$ and $b \ge 1$ be integers.
An urn holds $a$ red balls and $b$ black balls.
At each step one draws a ball uniformly at random and notes its colour.
Then one puts it back together with one more ball of the same colour.
Let $R_n$ and $B_n$ be the numbers of red and black balls after $n$ steps, so $R_n + B_n = a + b + n$.
Then $(R_n, B_n)$ is a [[Markov chain|0G48PYM96Q]], since the next draw depends only on the current contents.
From $(r, k)$ it moves to $(r + 1, k)$ with probability $r/(r + k)$ and to $(r, k + 1)$ otherwise.

The fraction $M_n = R_n / (a + b + n)$ of red balls is a [[martingale|0D0GBNDKDH]]:
$$\mathbb{E}[M_{n+1} \mid R_n, B_n] = \frac{R_n}{R_n + B_n} \cdot \frac{R_n + 1}{R_n + B_n + 1} + \frac{B_n}{R_n + B_n} \cdot \frac{R_n}{R_n + B_n + 1} = \frac{R_n}{R_n + B_n} = M_n.$$
It takes values in $[0, 1]$, so it converges almost surely, and its limit has the [[beta distribution|0EW824Z7G2]] with parameters $a$ and $b$.

## Remarks

For $a = b = 1$ the limit is uniform on $[0, 1]$, and $R_n$ is uniform on $\set{1, 2, \ldots, n + 1}$ for each $n$.
The sequence of colours drawn is [[exchangeable|4MR4YJS1ZD]]: the probability of a sequence depends only on how many red and black draws it contains.
By [[de Finetti's theorem|W19129PVKQ]], given the limit fraction $M$, the draws are independent with probability $M$ of red.
The urn shows that a random process can have a random limit: the rich get richer.

## Explanations

### L1 human

Each draw of a colour makes that colour more likely next time.
Early luck has a lasting effect, so the proportion of red settles down, but to a value that is itself random.
Starting with one red and one black ball, every final proportion between $0$ and $1$ is equally likely.
