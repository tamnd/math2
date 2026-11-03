---
tag: NQH9JRA8EX
kind: concept
name: Inventory theory
msc: [90B05, 90C39, 90B06]
specializes: [PSE3NRBXKY]
sources:
  - url: https://en.wikipedia.org/wiki/Inventory_theory
same_as:
  wikidata: Q252073
  wikipedia: Inventory theory
---

## Summary

Inventory theory is the part of [[operations research|PSE3NRBXKY]] that studies when and how much to order of a good that is stored to meet demand.
Its models weigh the fixed cost of placing an order, the cost of holding stock, and the cost of running short.
The [[economic order quantity|J0K163SEAF]] treats steady demand, and the [[newsvendor model|RMQ4JB26AT]] treats a single season of random demand.
For random demand over many periods, $(s, S)$ policies are optimal in classical models.
Many of its models are solved by [[stochastic dynamic programming|SDW79PBNWM]].

## Explanations

### L1 human

A shop sells bread and must decide how much flour to keep in the storeroom.
Ordering often costs a delivery fee each time, but ordering rarely means keeping a big pile of flour that ties up money and space.
If demand is uncertain, keeping too little risks running out and losing customers.
Inventory theory computes the order sizes and order times that balance these costs.
