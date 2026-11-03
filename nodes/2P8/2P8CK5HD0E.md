---
tag: 2P8CK5HD0E
kind: example
name: Market for lemons
msc: [91B44, 91B26]
illustrates: [JREVYHFY4T]
uses: [JREVYHFY4T]
sources:
  - url: https://en.wikipedia.org/wiki/The_Market_for_Lemons
same_as:
  wikidata: Q555438
  wikipedia: The Market for Lemons
---

## Example

Used cars have a quality $q$ that is uniformly distributed on $[0, 1]$.
Each seller knows the quality of their own car and values it at $q$.
Buyers cannot see the quality, and they value a car of quality $q$ at $\frac{3}{2} q$.
There are more buyers than cars, and all cars sell at one market price $p$.

At a price $p \in (0, 1]$, exactly the sellers with $q \le p$ offer their cars, so the average quality on offer is $p/2$.
A buyer then values a car bought at random at $\frac{3}{2} \cdot \frac{p}{2} = \frac{3p}{4} < p$, so no buyer wants to pay $p$.
At a price $p > 1$ all cars are offered, the average quality is $1/2$, and buyers value a car at $3/4 < p$.
So no positive price gives trade, and in equilibrium no cars are sold.

Yet every car is worth $50\%$ more to a buyer than to its owner, so every trade would be a gain.
The outcome with no trade is not [[Pareto efficient|JREVYHFY4T]].
For example, selling a car of quality $q > 0$ at price $\frac{5}{4} q$ makes both parties better off.
This failure comes from asymmetric information, which the first of the [[fundamental theorems of welfare economics|J6KA8R1H5Z]] leaves out.

## Explanations

### L1 human

George Akerlof's 1970 paper "The Market for 'Lemons'" made this point with used cars, where a "lemon" is a bad car.
Buyers cannot tell good cars from bad ones, so they offer an average price.
At that price, owners of good cars refuse to sell, which lowers the average quality and so the price buyers will pay, and the process repeats until the market collapses.
Warranties, inspections and reputations are ways to fight this, and signalling models such as [[Spence's job market model|BH0QN3M8H0]] study a related remedy.
