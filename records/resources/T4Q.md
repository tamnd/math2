---
records:
    - id: T4Q8JR41WH
      kind: monograph
      title: Number Fields
      creators:
        - name: Daniel A. Marcus
          role: author
      date: "1977"
      expressions:
        - key: e1
          kind: edition
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4684-9356-6
                - 10.1007/978-3-319-90233-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9780387902791"
                    - "9781468493566"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319902326"
                    - "9783319902333"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9356-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-90233-3
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
