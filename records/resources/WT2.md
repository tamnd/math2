---
records:
    - id: WT2Z3PPCP8
      kind: monograph
      title: A Brief on Tensor Analysis
      creators:
        - name: James G. Simmonds
          role: author
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi:
                - 10.1007/978-1-4419-8522-4
                - 10.1007/978-1-4684-0141-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1994"
              ids:
                isbn:
                    - "9781461264248"
                    - "9781441985224"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1982"
              ids:
                isbn:
                    - "9781468401431"
                    - "9781468401417"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8522-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0141-7
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
