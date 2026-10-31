---
records:
    - id: TG433H3E5V
      kind: problem-set
      title: IMO 2014 Shortlist
      date: "2014"
      expressions:
        - key: e1
          kind: edition
          date: "2014"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: 2014-sl
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: TG490X16WC
      kind: monograph
      title: Automorphic Functions and Number Theory
      creators:
        - name: Goro Shimura
          role: author
      date: "1968"
      expressions:
        - key: e1
          kind: edition
          date: "1968"
          ids:
            doi: 10.1007/bfb0071097
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1968"
              ids:
                isbn:
                    - "9783540042242"
                    - "9783540358329"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0071097
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
